import RemainingPredictionsCard from '@/components/remaining-predictions-card'
import { buttonVariants } from '@/components/ui/button'
import { routes } from '@/config.global'
import { cn } from '@/lib/utils'
import { PlusIcon } from 'lucide-react'
import Link from 'next/link'

type TDashboardHeaderProps = {
  linkHref: string
  linkText: string
  title: string
}

function DashboardHeader({ title, linkHref, linkText }: TDashboardHeaderProps) {
  return (
    <>
      <RemainingPredictionsCard />
      <div className="mb-10 mt-12 flex w-full flex-row items-center justify-between gap-10 md:flex-row">
        <h1>
          <span className="text-xl font-bold md:text-2xl">{title}</span>
        </h1>
        <Link
          href={linkHref}
          className={cn(
            buttonVariants({
              size: 'sm',
            }),
            'w-fit'
          )}
        >
          {linkText}
          {linkHref === routes.dashboard.newPrediction && <PlusIcon className="ml-1.5 h-5 w-5" />}
        </Link>
      </div>
    </>
  )
}

export default DashboardHeader
