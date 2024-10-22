'use client'

import { removeAccessToken, saveAccessToken } from '@/auth/session'
import { toast } from '@/components/ui/use-toast'
import { routes } from '@/config.global'
import { useUser } from '@/hooks/user'
import { TLoginRequestModel, TRegisterRequestModel } from '@/requests/auth'
import { TUser } from '@/types/user.types'
import { useRouter } from 'next/navigation'
import { createContext, useContext, useState, useCallback, ReactNode } from 'react'

import { useLogin, useRegister } from '@/hooks/auth'

type AuthContextType = {
  isLoading: boolean
  user: TUser | null
  setUser: (user: TUser | null) => void
  login: (payload: TLoginRequestModel) => Promise<void>
  register: (payload: TRegisterRequestModel) => Promise<void>
  logout: () => Promise<void>
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [isLoading, setIsLoading] = useState<boolean>(false)
  const [user, setUser] = useState<TUser | null>(null)
  const { refetch: refetchUser } = useUser({ enabled: false })
  const router = useRouter()

  const { mutateAsync: loginMutation } = useLogin()
  const { mutateAsync: registerMutation } = useRegister()

  const login = useCallback(
    async (payload: TLoginRequestModel) => {
      setIsLoading(true)
      await loginMutation(payload, {
        onSuccess: async (token) => {
          try {
            saveAccessToken(token)
            const { data: user } = await refetchUser()
            if (!user) {
              throw new Error('Failed to fetch user')
            }
            setUser(user)
            router.push(routes.dashboard.root)
          } catch (error) {
            removeAccessToken()
            setUser(null)
          }
        },
        onError: () => {
          removeAccessToken()
          setUser(null)
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
            const { data: user } = await refetchUser()
            if (!user) {
              throw new Error('Failed to fetch user')
            }
            setUser(user)
            router.push(routes.dashboard.root)
          } catch (error) {
            removeAccessToken()
            setUser(null)
          }
        },
        onError: () => {
          removeAccessToken()
          setUser(null)
        },
      })
      setIsLoading(false)
    },
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [registerMutation]
  )

  const logout = useCallback(async () => {
    removeAccessToken()
    setUser(null)
    router.push(routes.auth.login)
    toast({
      title: 'Logged out successfully',
    })
  }, [router])

  const value = { user, setUser, isLoading, login, register, logout }

  return <AuthContext.Provider value={value}> {children} </AuthContext.Provider>
}

export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}
