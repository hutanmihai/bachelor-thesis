'use client'

import { useAuth } from '@/auth/context/auth'
import { buttonVariants } from '@/components/ui/button'
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'
import { routes } from '@/config.global'
import Link from 'next/link'

function RemainingPredictionsCard() {
  const { user } = useAuth()

  return (
    <Card className="w-full border-2">
      <CardHeader>
        <CardTitle>Remaining predictions</CardTitle>
        <CardDescription>The number of predictions available for you</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="flex items-center justify-center">
          <span className="text-5xl font-bold">{user?.predictions}</span>
        </div>
      </CardContent>
      <CardFooter>
        <Link
          href={routes.pricing.root}
          className={buttonVariants({
            variant: 'ghost',
            className: 'w-full',
          })}
        >
          You can always buy more
        </Link>
      </CardFooter>
    </Card>
  )
}

export default RemainingPredictionsCard
