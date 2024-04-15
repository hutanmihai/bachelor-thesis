'use client'

import { AuthGuard } from '@/auth/guard'
import { ReactNode } from 'react'

type TDashboardLayoutProps = {
  children: ReactNode
}

function DashboardLayout({ children }: TDashboardLayoutProps) {
  return <AuthGuard>{children}</AuthGuard>
}

export default DashboardLayout
