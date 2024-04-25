'use client'

import { useAuth } from '@/auth/context/auth'
import { getAccessToken, removeAccessToken } from '@/auth/session'
import { getCurrentUser } from '@/requests/user'
import { Loader } from 'lucide-react'
import { useState, ReactNode, useCallback, useEffect } from 'react'

export function AppFirstLogic({ children }: { children: ReactNode }) {
  const { user, setUser } = useAuth()

  const [loading, setLoading] = useState(true)

  const initialize = useCallback(async () => {
    try {
      setLoading(true)
      const accessToken = getAccessToken()

      if (accessToken) {
        try {
          const response = await getCurrentUser()
          setUser(response)
        } catch (error) {
          removeAccessToken()
          setUser(null)
        }
        setLoading(false)
      } else {
        setUser(null)
        setLoading(false)
      }
    } catch (error) {
      setUser(null)
      setLoading(false)
    }

    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  useEffect(() => {
    initialize()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  if (loading && !user) {
    return (
      <div className="flex items-center justify-center" style={{ height: 'calc(100vh - 10rem)' }}>
        <Loader className="loader-gradient h-14 w-14 text-zinc-800 md:h-24 md:w-24" />
      </div>
    )
  }
  return children
}
