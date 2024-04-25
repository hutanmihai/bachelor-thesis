import { getCurrentUser } from '@/requests/user'

export function saveAccessToken({ token }: { token: string }) {
  localStorage.setItem('accessToken', token)
}

export function getAccessToken() {
  return localStorage.getItem('accessToken')
}

export function removeAccessToken() {
  localStorage.removeItem('accessToken')
}

export async function checkIsValidSession() {
  try {
    const token = getAccessToken()
    if (!token) return false
    const user = await getCurrentUser()
    return !!user
  } catch (error) {
    return false
  }
}
