export const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL

export const apiConfig = {
  auth: {
    login: `${BACKEND_URL}/login`,
    register: `${BACKEND_URL}/register`,
  },
  inference: `${BACKEND_URL}/inference`,
  stripe: {
    createCheckoutSession: `${BACKEND_URL}/create-checkout-session`,
  },
  user: {
    me: `${BACKEND_URL}/user/me`,
  },
  entry: {
    list: `${BACKEND_URL}/entry/all`,
    delete: (id: string) => `${BACKEND_URL}/entry/${id}`,
    upload: `${BACKEND_URL}/upload`,
  },
}

export const routes = {
  landingpage: {
    root: '/',
  },
  auth: {
    login: '/auth/login',
    register: '/auth/register',
  },
  dashboard: {
    root: '/dashboard',
    newPrediction: '/dashboard/new-prediction',
  },
  pricing: {
    root: '/pricing',
  },
}
