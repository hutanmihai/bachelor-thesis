'use client'

import { useAuth } from '@/auth/context/auth'
import { Button } from '@/components/ui/button'
import { LogOut } from 'lucide-react'

function LogoutButton() {
  const { logout } = useAuth()
  return (
    <Button variant="destructive" onClick={logout} className="w-full font-semibold">
      Logout <LogOut className="ml-2 h-5 w-5" />
    </Button>
  )
}

export default LogoutButton
