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

export async function login({ email, password }: TLoginRequestModel) {
  const response = await axiosInstance.post(apiConfig.auth.login, { email, password })
  return response.data as TTokenResponseModel
}

export type TRegisterRequestModel = {
  username: string
  email: string
  password: string
}

export async function register({ username, email, password }: TRegisterRequestModel) {
  const response = await axios.post(apiConfig.auth.register, { username, email, password })
  return response.data as TTokenResponseModel
}
