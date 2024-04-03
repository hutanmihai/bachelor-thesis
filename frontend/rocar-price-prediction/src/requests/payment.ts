import axiosInstance from '@/utils/axios'

export type TCreateCheckoutSessionRequestModel = {
  price_id: string
}

export type TCreateCheckoutSessionResponseModel = {
  url: string
}

export async function createCheckoutSession(payload: TCreateCheckoutSessionRequestModel) {
  const response = await axiosInstance.post('/create-checkout-session', payload)
  return response.data as TCreateCheckoutSessionResponseModel
}
