import { apiConfig } from '@/config.global'
import { TUser } from '@/types/user.types'
import axiosInstance from '@/utils/axios'

export async function getCurrentUser() {
  const response = await axiosInstance.get(apiConfig.user.me)
  return response.data as TUser
}
