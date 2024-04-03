export const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL
export const STRIPE_PUBLIC_KEY = process.env.NEXT_PUBLIC_STRIPE_PUBLIC_KEY

export const apiConfig = {
  auth: {
    login: `${BACKEND_URL}/login`,
    register: `${BACKEND_URL}/register`,
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
  },
  pricing: {
    root: '/pricing',
  },
}

export const publicRoutes = [routes.landingpage.root, routes.auth.login, routes.auth.register]
export const protectedRoutes = [routes.dashboard.root]
