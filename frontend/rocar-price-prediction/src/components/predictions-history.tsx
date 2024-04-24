'use client'

import Chip from '@/components/chip'
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from '@/components/ui/alert-dialog'
import { BentoGrid, BentoGridItem } from '@/components/ui/bento-grid'
import { buttonVariants } from '@/components/ui/button'
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover'
import { useDeleteEntry, useEntries } from '@/hooks/entry'
import { Trash2 } from 'lucide-react'

const Skeleton = () => (
  <div className="flex h-full min-h-[6rem] w-full flex-1 rounded-xl bg-gradient-to-br from-neutral-200 to-neutral-100 dark:from-neutral-900 dark:to-neutral-800"></div>
)

function PredictionsHistory() {
  const { data } = useEntries()
  const { mutateAsync: deleteEntry } = useDeleteEntry()

  const handleDelete = async (id: string) => {
    await deleteEntry(id)
  }

  return (
    <BentoGrid className="w-full">
      {data?.entries.map((entry, i) => (
        <BentoGridItem
          key={i}
          title={`${entry.manufacturer} ${entry.model} ${entry.year} - ${entry.prediction} €`}
          description={
            <div className="flex flex-col gap-4">
              <div className="flex flex-wrap gap-2.5">
                <Chip text={entry.fuel} />
                <Chip text={entry.km.toString() + ' km'} />
                <Chip text={entry.power.toString() + ' hp'} />
                <Chip text={entry.engine.toString() + ' cm3'} />
                <Chip text={entry.gearbox} />
                <Chip text={entry.sold_by} />
                <Chip text={entry.chassis} />
              </div>
              <div className="flex items-center justify-between">
                <Popover>
                  <PopoverTrigger
                    className={buttonVariants({
                      variant: 'secondary',
                      size: 'sm',
                      className: 'text-xs',
                    })}
                  >
                    Read description
                  </PopoverTrigger>
                  <PopoverContent className="max-w-xl">{entry.description}</PopoverContent>
                </Popover>
                <AlertDialog>
                  <AlertDialogTrigger>
                    <Trash2 color="#ef4444" size={20} className="cursor-pointer rounded-full" />
                  </AlertDialogTrigger>
                  <AlertDialogContent>
                    <AlertDialogHeader>
                      <AlertDialogTitle>
                        Are you sure you want to delete this entry?
                      </AlertDialogTitle>
                      <AlertDialogDescription>
                        This action cannot be undone. This will permanently delete the entry.
                      </AlertDialogDescription>
                    </AlertDialogHeader>
                    <AlertDialogFooter>
                      <AlertDialogCancel>Cancel</AlertDialogCancel>
                      <AlertDialogAction
                        className="bg-destructive hover:bg-destructive"
                        onClick={() => handleDelete(entry.id)}
                      >
                        Delete
                      </AlertDialogAction>
                    </AlertDialogFooter>
                  </AlertDialogContent>
                </AlertDialog>
              </div>
            </div>
          }
          header={
            entry.image_url ? (
              // eslint-disable-next-line @next/next/no-img-element
              <img
                src={entry.image_url}
                alt={entry.manufacturer + entry.model}
                className="flex h-full min-h-[6rem] w-full flex-1 rounded-xl"
              />
            ) : (
              <Skeleton />
            )
          }
          className={i === 3 || i === 6 ? 'md:col-span-2' : ''}
        />
      ))}
    </BentoGrid>
  )
}

export default PredictionsHistory
