import { getAccessToken } from '@/auth/session'
import { BACKEND_URL, routes } from '@/config.global'
import axios from 'axios'

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

export default axiosInstance
