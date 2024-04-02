'use client'

import { Toaster } from '@/components/ui/toaster'
import { ReactNode } from 'react'
import { QueryClient, QueryClientProvider } from 'react-query'

function GlobalProviders({ children }: { children: ReactNode }) {
  return (
    <QueryClientProvider client={new QueryClient()}>
      {children}
      <Toaster />
    </QueryClientProvider>
  )
}

export default GlobalProviders
