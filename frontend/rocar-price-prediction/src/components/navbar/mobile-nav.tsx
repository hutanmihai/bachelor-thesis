'use client'

import { useAuth } from '@/auth/context/auth'
import LogoutButton from '@/components/auth/logout-button'
import { Button } from '@/components/ui/button'
import { routes } from '@/config.global'
import { ArrowRight, LogOut, Menu } from 'lucide-react'
import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { useEffect, useState } from 'react'

const MobileNav = () => {
  const pathname = usePathname()
  const { isAuth, logout } = useAuth()
  const [isOpen, setIsOpen] = useState<boolean>(false)
  const toggleOpen = () => setIsOpen((prev) => !prev)

  useEffect(() => {
    if (isOpen) toggleOpen()
  }, [pathname])

  const closeOnCurrent = (href: string) => {
    if (pathname === href) {
      toggleOpen()
    }
  }

  return (
    <div className="sm:hidden">
      <Menu onClick={toggleOpen} className="relative z-50 h-5 w-5 text-zinc-700" />

      {isOpen ? (
        <div className="fixed inset-0 z-0 w-full animate-in fade-in-20 slide-in-from-top-5">
          <ul className="absolute grid w-full gap-3 border-b border-zinc-200 bg-white px-10 pb-8 pt-20 shadow-xl">
            {!isAuth ? (
              <>
                <li>
                  <Link
                    onClick={() => closeOnCurrent(routes.auth.register)}
                    className="flex w-full items-center font-semibold text-primary"
                    href={routes.auth.register}
                  >
                    Get started
                    <ArrowRight className="ml-2 h-5 w-5" />
                  </Link>
                </li>
                <li className="my-3 h-px w-full bg-gray-300" />
                <li>
                  <Link
                    onClick={() => closeOnCurrent(routes.auth.login)}
                    className="flex w-full items-center font-semibold"
                    href={routes.auth.login}
                  >
                    Login
                  </Link>
                </li>
                <li className="my-3 h-px w-full bg-gray-300" />
                <li>
                  <Link
                    onClick={() => closeOnCurrent(routes.pricing.root)}
                    className="flex w-full items-center font-semibold"
                    href={routes.pricing.root}
                  >
                    Pricing
                  </Link>
                </li>
              </>
            ) : (
              <>
                <li>
                  <Link
                    onClick={() => closeOnCurrent(routes.pricing.root)}
                    className="flex w-full items-center font-semibold"
                    href={routes.pricing.root}
                  >
                    Pricing
                  </Link>
                </li>
                <li className="my-3 h-px w-full bg-gray-300" />
                <li>
                  <Link
                    onClick={() => closeOnCurrent(routes.dashboard.root)}
                    className="flex w-full items-center font-semibold"
                    href={routes.dashboard.root}
                  >
                    Dashboard
                  </Link>
                </li>
                <li className="my-3 h-px w-full bg-gray-300" />
                <li>
                  <LogoutButton />
                </li>
              </>
            )}
          </ul>
        </div>
      ) : null}
    </div>
  )
}

export default MobileNav
