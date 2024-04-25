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
  const { isAuth } = useAuth()

  const check = useCallback(() => {
    if (isAuth) {
      router.replace(routes.dashboard.root)
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [isAuth])

  useEffect(() => {
    check()
  }, [check])

  return <>{children}</>
}
