'use client'

import { useAuth } from '@/auth/context/auth'
import { routes } from '@/config.global'
import { useRouter } from 'next/navigation'
import { useEffect, useCallback, ReactNode } from 'react'

type GuestGuardProps = {
  children: ReactNode
}

export default function GuestGuard({ children }: GuestGuardProps) {
  const router = useRouter()
  const { user, isAuth } = useAuth()

  const check = useCallback(() => {
    if (user) {
      router.replace(routes.dashboard.root)
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  useEffect(() => {
    check()
  }, [check, isAuth, router])

  return <>{children}</>
}
