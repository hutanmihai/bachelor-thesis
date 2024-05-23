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
  description: string
  image_url: string
  audio_and_technology?: string[]
  confort_and_extra_options?: string[]
  electronics_and_assistance_systems?: string[]
  performance?: string[]
  safety?: string[]
}

export type TInferenceResponseModel = {
  prediction: number
}

export async function callInference(payload: TInferenceRequestModel) {
  const response = await axiosInstance.post(apiConfig.inference, payload)
  return response.data as TInferenceResponseModel
}
