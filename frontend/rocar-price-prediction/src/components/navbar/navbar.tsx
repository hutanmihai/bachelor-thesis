import MaxWidthWrapper from '@/components/max-width-wrapper'
import MobileNav from '@/components/navbar/mobile-nav'
import { buttonVariants } from '@/components/ui/button'
import { ArrowRight } from 'lucide-react'
import Link from 'next/link'

function Navbar() {
  return (
    <nav className="sticky inset-x-0 top-0 z-30 h-14 w-full border-b border-gray-200 bg-white/75 backdrop-blur-lg transition-all">
      <MaxWidthWrapper>
        <div className="flex h-14 items-center justify-between border-b border-zinc-200">
          <Link href="/" className="z-40 flex font-semibold">
            RoCar.
          </Link>
          <MobileNav isAuth={false} />

          <div className="hidden items-center space-x-4 sm:flex">
            <>
              <Link
                href="/pricing"
                className={buttonVariants({
                  variant: 'ghost',
                  size: 'sm',
                })}
              >
                Pricing
              </Link>
              <Link
                href="/auth/login"
                className={buttonVariants({
                  variant: 'ghost',
                  size: 'sm',
                })}
              >
                Login
              </Link>
              <Link
                href="/auth/register"
                className={buttonVariants({
                  size: 'sm',
                })}
              >
                Get started <ArrowRight className="ml-1.5 h-5 w-5" />
              </Link>
            </>
          </div>
        </div>
      </MaxWidthWrapper>
    </nav>
  )
}

export default Navbar
