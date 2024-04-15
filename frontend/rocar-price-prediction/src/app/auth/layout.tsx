"use client"

import { GuestGuard } from '@/auth/guard'
import { ReactNode } from 'react'

type TDashboardLayoutProps = {
  children: ReactNode
}

function DashboardLayout({ children }: TDashboardLayoutProps) {
  return <GuestGuard>{children}</GuestGuard>
}

export default DashboardLayout
