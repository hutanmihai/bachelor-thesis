'use client'

import { removeAccessToken, saveAccessToken } from '@/auth/session'
import { protectedRoutes, routes } from '@/config.global'
import { TLoginRequestModel, TRegisterRequestModel } from '@/requests/auth'
import { usePathname, useRouter } from 'next/navigation'
import { createContext, useContext, useState, useEffect, useCallback, ReactNode } from 'react'

import { useLogin, useRegister } from '@/hooks/auth'

type AuthContextType = {
  isAuth: boolean
  isLoading: boolean
  login: (payload: TLoginRequestModel) => Promise<void>
  register: (payload: TRegisterRequestModel) => Promise<void>
  logout: () => Promise<void>
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [isLoading, setIsLoading] = useState<boolean>(false)
  const [isAuth, setIsAuth] = useState<boolean>(false)
  const router = useRouter()
  const pathname = usePathname()

  const { mutateAsync: loginMutation } = useLogin()
  const { mutateAsync: registerMutation } = useRegister()

  useEffect(() => {
    if (!isAuth && protectedRoutes.includes(pathname)) {
      router.replace(routes.auth.login)
    }
  }, [isAuth, pathname, router])

  const login = useCallback(
    async (payload: TLoginRequestModel) => {
      setIsLoading(true)
      await loginMutation(payload, {
        onSuccess: async (token) => {
          try {
            saveAccessToken(token)
            setIsAuth(true)
            // TODO: Redirect to dashboard
            router.push(routes.landingpage.root)
          } catch (error) {
            removeAccessToken()
            setIsAuth(false)
          }
        },
        onError: () => {
          setIsAuth(false)
        },
      })
      setIsLoading(false)
    },
    [loginMutation, router]
  )

  const register = useCallback(
    async (payload: TRegisterRequestModel) => {
      setIsLoading(true)
      await registerMutation(payload, {
        onSuccess: async (token) => {
          try {
            saveAccessToken(token)
            setIsAuth(true)
            // TODO: Redirect to dashboard
            router.push(routes.landingpage.root)
          } catch (error) {
            removeAccessToken()
            setIsAuth(false)
          }
        },
        onError: () => {
          setIsAuth(false)
        },
      })
      setIsLoading(false)
    },
    [registerMutation, router]
  )

  const logout = useCallback(async () => {
    removeAccessToken()
    setIsAuth(false)
  }, [])

  const value = { isAuth, isLoading, login, register, logout }

  return <AuthContext.Provider value={value}> {children} </AuthContext.Provider>
}

export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}
