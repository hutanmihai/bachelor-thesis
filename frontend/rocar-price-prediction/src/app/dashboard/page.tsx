'use client'

import InferenceForm from '@/components/inference-form'
import MaxWidthWrapper from '@/components/max-width-wrapper'
import PredictionsHistory from '@/components/predictions-history'
import { Button, buttonVariants } from '@/components/ui/button'
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
import { useState } from 'react'

function Dashboard() {
  const [isHistoryVisible, setIsHistoryVisible] = useState(true)

  return (
    <MaxWidthWrapper>
      <div className="mt-10 flex w-full flex-col gap-10 md:flex-row">
        <Button className="w-full" onClick={() => setIsHistoryVisible((prev) => !prev)}>
          {isHistoryVisible ? 'Make a new prediction' : 'Show history'}
        </Button>
        <Card className="w-full border-2">
          <CardHeader>
            <CardTitle>Remaining predictions</CardTitle>
            <CardDescription>The number of predictions available for you</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex items-center justify-center">
              <span className="text-5xl font-bold">5</span>
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
      </div>
      <div className="mt-10">{isHistoryVisible ? <PredictionsHistory /> : <InferenceForm />}</div>
    </MaxWidthWrapper>
  )
}

export default Dashboard
