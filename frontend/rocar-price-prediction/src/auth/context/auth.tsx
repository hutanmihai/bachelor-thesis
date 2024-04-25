'use client'

import {
  checkIsValidSession,
  getAccessToken,
  removeAccessToken,
  saveAccessToken,
} from '@/auth/session'
import { toast } from '@/components/ui/use-toast'
import { routes } from '@/config.global'
import { useUser } from '@/hooks/user'
import { TLoginRequestModel, TRegisterRequestModel } from '@/requests/auth'
import { TUser } from '@/types/user.types'
import { useRouter } from 'next/navigation'
import { createContext, useContext, useState, useCallback, ReactNode, useEffect } from 'react'

import { useLogin, useRegister } from '@/hooks/auth'

type AuthContextType = {
  isAuth: boolean
  user: TUser | null
  isLoading: boolean
  login: (payload: TLoginRequestModel) => Promise<void>
  register: (payload: TRegisterRequestModel) => Promise<void>
  logout: () => Promise<void>
  setIsAuth: (isAuth: boolean) => void
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [isLoading, setIsLoading] = useState<boolean>(false)
  const [isAuth, setIsAuth] = useState<boolean>(false)
  const [user, setUser] = useState<TUser | null>(null)
  const { data: userData } = useUser({
    enabled: isAuth,
  })
  const router = useRouter()

  const { mutateAsync: loginMutation } = useLogin()
  const { mutateAsync: registerMutation } = useRegister()

  useEffect(() => {
    const validateSession = async () => {
      const isValidSession = await checkIsValidSession()
      setIsAuth(isValidSession)
    }

    validateSession()
  }, [])

  useEffect(() => {
    if (userData) {
      setUser(userData)
    } else {
      setUser(null)
    }
  }, [userData])

  const login = useCallback(
    async (payload: TLoginRequestModel) => {
      setIsLoading(true)
      await loginMutation(payload, {
        onSuccess: async (token) => {
          try {
            saveAccessToken(token)
            setIsAuth(true)
            router.push(routes.dashboard.root)
          } catch (error) {
            removeAccessToken()
            setIsAuth(false)
          }
        },
        onError: () => {
          removeAccessToken()
          setIsAuth(false)
        },
      })
      setIsLoading(false)
    },
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [loginMutation]
  )

  const register = useCallback(
    async (payload: TRegisterRequestModel) => {
      setIsLoading(true)
      await registerMutation(payload, {
        onSuccess: async (token) => {
          try {
            saveAccessToken(token)
            setIsAuth(true)
            router.push(routes.dashboard.root)
          } catch (error) {
            removeAccessToken()
            setIsAuth(false)
          }
        },
        onError: () => {
          removeAccessToken()
          setIsAuth(false)
        },
      })
      setIsLoading(false)
    },
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [registerMutation]
  )

  const logout = useCallback(async () => {
    removeAccessToken()
    setIsAuth(false)
    router.push(routes.auth.login)
    toast({
      title: 'Logged out successfully',
    })
  }, [router])

  const value = { isAuth, user, isLoading, login, register, logout, setIsAuth }

  return <AuthContext.Provider value={value}> {children} </AuthContext.Provider>
}

export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}
