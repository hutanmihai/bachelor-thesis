'use client'

import { useAuth } from '@/auth/context/auth'
import { Button } from '@/components/ui/button'
import { routes } from '@/config.global'
import { useCreateCheckoutSession } from '@/hooks/payment'
import { cn } from '@/lib/utils'
import { ArrowRight, Loader } from 'lucide-react'
import { useRouter } from 'next/navigation'

type TBuyButtonProps = {
  product: 'three' | 'five' | 'ten'
}

function BuyButton({ product }: TBuyButtonProps) {
  const { user } = useAuth()
  const router = useRouter()
  const { isLoading, mutateAsync: createCheckoutSession } = useCreateCheckoutSession()

  const onClick = async () => {
    if (!user) {
      router.push(routes.auth.login)
      return
    }

    await createCheckoutSession({ price_id: product })
  }

  const productClassNamesMap = {
    three: 'text-black bg-white hover:bg-accent hover:text-accent-foreground',
    five: 'text-white bg-primary',
    ten: 'text-white bg-purple-600 hover:bg-purple-500',
  }

  return (
    <Button
      onClick={onClick}
      className={cn('w-full', productClassNamesMap[product])}
      disabled={isLoading}
    >
      Buy now{' '}
      {isLoading ? (
        <Loader className="loader-gradient ml-1.5 h-5 w-5" />
      ) : (
        <ArrowRight className="ml-1.5 h-5 w-5" />
      )}
    </Button>
  )
}

export default BuyButton
