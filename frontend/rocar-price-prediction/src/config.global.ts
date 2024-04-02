export const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL

export const apiConfig = {
  auth: {
    login: `${BACKEND_URL}/login`,
    register: `${BACKEND_URL}/register`,
  },
}
