from uuid import UUID

import stripe
from fastapi import APIRouter, Depends, Header, HTTPException, Request, status
from src.apis.utils.utils import generate_api_error_response, generate_error_responses
from src.auth.auth_bearer import auth_required
from src.schemas.payment_schema import CreateCheckoutSessionRequestSchema, CreateCheckoutSessionResponseSchema
from src.services.errors import UserNotFound
from src.services.user_srv import UserSrv
from src.settings import settings

stripe.api_key = settings.stripe_secret_key
stripe.api_version = settings.stripe_api_version

router = APIRouter(tags=["payment"])

PRODUCTS = {settings.stripe_price_id_ten: 10, settings.stripe_price_id_five: 5, settings.stripe_price_id_three: 3}


@router.post(
    "/create-checkout-session",
    summary="Create checkout session",
    status_code=status.HTTP_200_OK,
    response_description="Checkout session created succesfully",
    responses=generate_error_responses(status.HTTP_403_FORBIDDEN),
    response_model=CreateCheckoutSessionResponseSchema,
)
async def create_checkout_session(
    create_checkout_schema: CreateCheckoutSessionRequestSchema, request: Request, user_id: UUID = Depends(auth_required)
):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price": create_checkout_schema.price_id,
                    "quantity": 1,
                },
            ],
            mode="payment",
            client_reference_id=str(user_id),
            metadata={"user_id": str(user_id), "price_id": create_checkout_schema.price_id},
            success_url=request.headers.get("referer") + "dashboard",
            cancel_url=request.headers.get("referer") + "pricing",
        )
        return CreateCheckoutSessionResponseSchema(url=session.url)
    except Exception as e:
        print(e)
        return generate_api_error_response(status.HTTP_500_INTERNAL_SERVER_ERROR, "An unexpected error has occured")


@router.post("/webhook", status_code=status.HTTP_200_OK, summary="Stripe webhook", response_model=None)
async def webhook_stripe(
    request: Request,
    stripe_signature=Header(None),
    user_srv: UserSrv = Depends(UserSrv),
):
    webhook_secret = settings.stripe_webhook_secret
    raw_body = await request.body()

    try:
        event = stripe.Webhook.construct_event(
            payload=raw_body,
            sig_header=stripe_signature,
            secret=webhook_secret,
        )
    except Exception as e:
        raise HTTPException(422, detail=str(e))

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        user_id = session["client_reference_id"]
        product_id = session["metadata"]["price_id"]
        try:
            await user_srv.update_user_predictions(user_id, PRODUCTS[product_id])
        except UserNotFound:
            raise HTTPException(404, detail="User not found")

    return status.HTTP_200_OK
