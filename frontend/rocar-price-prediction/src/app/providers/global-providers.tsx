'use client'

import { AppFirstLogic } from '@/auth/context/app-first-logic'
import { AuthProvider } from '@/auth/context/auth'
import { Toaster } from '@/components/ui/toaster'
import { ReactNode } from 'react'
import { QueryClient, QueryClientProvider } from 'react-query'

function GlobalProviders({ children }: { children: ReactNode }) {
  return (
    <QueryClientProvider client={new QueryClient()}>
      <AuthProvider>
        <AppFirstLogic>{children}</AppFirstLogic>
        <Toaster />
      </AuthProvider>
    </QueryClientProvider>
  )
}

export default GlobalProviders
