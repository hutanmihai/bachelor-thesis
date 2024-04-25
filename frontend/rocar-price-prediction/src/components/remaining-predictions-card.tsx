'use client'

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
import { useUser } from '@/hooks/user'
import Link from 'next/link'

function RemainingPredictionsCard() {
  const { data: userData } = useUser({
    enabled: true,
  })

  return (
    <Card className="w-full border-2">
      <CardHeader>
        <CardTitle>Remaining predictions</CardTitle>
        <CardDescription>The number of predictions available for you</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="flex items-center justify-center">
          <span className="h-12 text-5xl font-bold">{userData?.predictions}</span>
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
