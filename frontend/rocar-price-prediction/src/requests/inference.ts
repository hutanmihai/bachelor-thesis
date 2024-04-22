import { apiConfig } from '@/config.global'
import axiosInstance from '@/utils/axios'

export type TInferenceRequestModel = {
  manufacturer: string
  model: string
  fuel: string
  chassis: string
  sold_by: string
  gearbox: string
  year: number
  km: number
  power: number
  engine: number
}

export type TInferenceResponseModel = {
  prediction: number
}

export async function callInference(payload: TInferenceRequestModel) {
  const response = await axiosInstance.post(apiConfig.inference, payload)
  return response.data as TInferenceResponseModel
}
