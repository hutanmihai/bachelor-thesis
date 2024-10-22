'use client'

import { useAuth } from '@/auth/context/auth'
import { routes } from '@/config.global'
import { useRouter } from 'next/navigation'
import { useState, useEffect, useCallback, ReactNode } from 'react'

type AuthGuardProps = {
  children: ReactNode
}

export default function AuthGuard({ children }: AuthGuardProps) {
  const router = useRouter()
  const { user } = useAuth()

  const [checked, setChecked] = useState(false)

  const check = useCallback(() => {
    if (!user) {
      router.replace(routes.auth.login)
    } else {
      setChecked(true)
    }

    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  useEffect(() => {
    check()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  if (!checked) {
    return null
  }

  return <>{children}</>
}
