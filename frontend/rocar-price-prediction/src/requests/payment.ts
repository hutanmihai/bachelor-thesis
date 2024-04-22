import { apiConfig } from '@/config.global'
import axiosInstance from '@/utils/axios'

export type TCreateCheckoutSessionRequestModel = {
  price_id: string
}

export type TCreateCheckoutSessionResponseModel = {
  url: string
}

export async function createCheckoutSession(payload: TCreateCheckoutSessionRequestModel) {
  const response = await axiosInstance.post(apiConfig.stripe.createCheckoutSession, payload)
  return response.data as TCreateCheckoutSessionResponseModel
}
