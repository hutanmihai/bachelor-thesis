'use client'

import { useAuth } from '@/auth/context/auth'
import MaxWidthWrapper from '@/components/max-width-wrapper'
import MobileNav from '@/components/navbar/mobile-nav'
import UserAccountNav from '@/components/navbar/user-account-nav'
import { buttonVariants } from '@/components/ui/button'
import { routes } from '@/config.global'
import { useUser } from '@/hooks/user'
import { ArrowRight } from 'lucide-react'
import Link from 'next/link'

function Navbar() {
  const { user } = useAuth()

  return (
    <nav className="sticky inset-x-0 top-0 z-30 h-14 w-full border-b border-gray-200 bg-white/75 backdrop-blur-lg transition-all">
      <MaxWidthWrapper>
        <div className="flex h-14 items-center justify-between border-b border-zinc-200">
          <Link href={routes.landingpage.root} className="z-40 flex font-semibold">
            RoCar.
          </Link>
          <MobileNav />

          <div className="hidden items-center space-x-4 sm:flex">
            {!user ? (
              <>
                <Link
                  href={routes.pricing.root}
                  className={buttonVariants({
                    variant: 'ghost',
                    size: 'sm',
                  })}
                >
                  Pricing
                </Link>
                <Link
                  href={routes.auth.login}
                  className={buttonVariants({
                    variant: 'ghost',
                    size: 'sm',
                  })}
                >
                  Login
                </Link>
                <Link
                  href={routes.auth.register}
                  className={buttonVariants({
                    size: 'sm',
                  })}
                >
                  Get started <ArrowRight className="ml-1.5 h-5 w-5" />
                </Link>
              </>
            ) : (
              <>
                <Link
                  href={routes.pricing.root}
                  className={buttonVariants({
                    variant: 'ghost',
                    size: 'sm',
                  })}
                >
                  Pricing
                </Link>
                <Link
                  href={routes.dashboard.root}
                  className={buttonVariants({
                    variant: 'ghost',
                    size: 'sm',
                  })}
                >
                  Dashboard
                </Link>

                <UserAccountNav email={user?.email} name={user?.username} />
              </>
            )}
          </div>
        </div>
      </MaxWidthWrapper>
    </nav>
  )
}

export default Navbar
