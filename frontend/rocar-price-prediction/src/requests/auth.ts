import { apiConfig } from '@/config.global'
import axiosInstance from '@/utils/axios'
import axios from 'axios'

export type TLoginRequestModel = {
  email: string
  password: string
}

export async function login({ email, password }: TLoginRequestModel) {
  const response = await axiosInstance.post(apiConfig.auth.login, { email, password })
  return response.data
}

export type TRegisterRequestModel = {
  username: string
  email: string
  password: string
}

export function register({ username, email, password }: TRegisterRequestModel) {
  return axios.post(apiConfig.auth.register, { username, email, password })
}
