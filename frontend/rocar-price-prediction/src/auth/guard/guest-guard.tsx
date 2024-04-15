"use client"

import { getAccessToken } from '@/auth/session'
import { routes } from '@/config.global'
import { useRouter } from 'next/navigation'
import { useEffect, useCallback, ReactNode } from 'react'

type GuestGuardProps = {
  children: ReactNode
}

export default function GuestGuard({ children }: GuestGuardProps) {
  const router = useRouter()

  const check = useCallback(() => {
    const token = getAccessToken()
    if (token) {
      router.replace(routes.dashboard.root)
    }
  }, [router])

  useEffect(() => {
    check()
  }, [check])

  return <>{children}</>
}
