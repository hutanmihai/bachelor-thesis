'use client'

import { useAuth } from '@/auth/context/auth'
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
import { cn } from '@/lib/utils'
import { PlusIcon } from 'lucide-react'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import { useState } from 'react'

function NewPrediction() {
  const { user } = useAuth()
  const router = useRouter()

  return (
    <MaxWidthWrapper className="mb-10 mt-10">
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
      <div className="mb-10 flex w-full flex-col gap-10 md:flex-row">
        <div className="mt-10 flex w-full flex-col justify-between gap-10 md:flex-row">
          <h1>
            <span className="text-2xl font-bold">Create new prediction</span>
          </h1>
          <Link
            href={routes.dashboard.root}
            className={cn(
              buttonVariants({
                size: 'sm',
              }),
              'w-fit'
            )}
          >
            See predictions history
          </Link>
        </div>
      </div>
      <InferenceForm />
    </MaxWidthWrapper>
  )
}

export default NewPrediction
