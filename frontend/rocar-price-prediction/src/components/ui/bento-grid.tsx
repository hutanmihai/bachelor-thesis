import { cn } from '@/lib/utils'
import { ReactNode } from 'react'

export const BentoGrid = ({
  className,
  children,
}: {
  className?: string
  children?: ReactNode
}) => {
  return (
    <div className={cn('mx-auto grid max-w-7xl grid-cols-1 gap-4 md:grid-cols-3 ', className)}>
      {children}
    </div>
  )
}

export const BentoGridItem = ({
  className,
  title,
  description,
  header,
  icon,
}: {
  className?: string
  title?: string | ReactNode
  description?: string | ReactNode
  header?: ReactNode
  icon?: ReactNode
}) => {
  return (
    <div
      className={cn(
        'group/bento row-span-1 flex flex-col justify-between space-y-4 rounded-xl border border-transparent bg-white p-4 shadow-input transition duration-200 hover:shadow-xl',
        className
      )}
    >
      {header}
      <div>
        {icon}
        <div className="mb-2 mt-2 font-sans font-bold text-zinc-900 ">{title}</div>
        <div className="font-sans text-xs font-normal text-zinc-900">{description}</div>
      </div>
    </div>
  )
}
