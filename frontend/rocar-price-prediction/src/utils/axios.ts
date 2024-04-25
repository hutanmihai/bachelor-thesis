import { getAccessToken } from '@/auth/session'
import { BACKEND_URL, routes } from '@/config.global'
import axios, { AxiosError, AxiosResponse } from 'axios'

const axiosInstance = axios.create({ baseURL: BACKEND_URL })

axiosInstance.interceptors.request.use(
  async (config) => {
    const token = getAccessToken()
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

axiosInstance.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    if (error.response && error.response.status === 403) {
      const currentPath = window.location.pathname
      if (currentPath !== routes.auth.login) {
        window.location.href = routes.auth.login
      }
    }
    return Promise.reject(error)
  }
)

interface CustomApiResponse<T = any> extends AxiosResponse<T> {
  data: T & { detail: string }
}

export interface CustomApiError<T = any> extends AxiosError<T> {
  response?: CustomApiResponse<T>
}

export default axiosInstance
