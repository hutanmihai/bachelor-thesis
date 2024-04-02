'use client'

import { useAuth } from '@/auth/context/auth'
import { Button, buttonVariants } from '@/components/ui/button'
import { routes } from '@/config.global'
import { cn } from '@/lib/utils'
import { ArrowRight } from 'lucide-react'
import Link from 'next/link'

type TBuyButtonProps = {
  product: 'three' | 'five' | 'ten'
}

function BuyButton({ product }: TBuyButtonProps) {
  const { isAuth } = useAuth()

  const productClassNamesMap = {
    three: 'text-black bg-white hover:bg-accent hover:text-accent-foreground',
    five: 'text-white bg-primary',
    ten: 'text-white bg-purple-600 hover:bg-purple-500',
  }

  return (
    <Link
      href={isAuth ? routes.dashboard.root : routes.auth.login}
      className={buttonVariants({
        className: cn('w-full', productClassNamesMap[product]),
      })}
    >
      Buy now <ArrowRight className="ml-1.5 h-5 w-5" />
    </Link>
  )
}

export default BuyButton
