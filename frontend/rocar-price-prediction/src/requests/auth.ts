import { apiConfig } from '@/config.global'
import axiosInstance from '@/utils/axios'
import axios from 'axios'

export type TTokenResponseModel = {
  token: string
}

export type TLoginRequestModel = {
  email: string
  password: string
}

export async function login(payload: TLoginRequestModel) {
  const response = await axiosInstance.post(apiConfig.auth.login, payload)
  return response.data as TTokenResponseModel
}

export type TRegisterRequestModel = {
  username: string
  email: string
  password: string
}

export async function register(payload: TRegisterRequestModel) {
  const response = await axios.post(apiConfig.auth.register, payload)
  return response.data as TTokenResponseModel
}
