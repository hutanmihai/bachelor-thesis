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
import { Button } from '@/components/ui/button'
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover'
import { Trash2 } from 'lucide-react'
import { useState } from 'react'

const Skeleton = () => (
  <div className="flex h-full min-h-[6rem] w-full flex-1 rounded-xl bg-gradient-to-br from-neutral-200 to-neutral-100 dark:from-neutral-900 dark:to-neutral-800"></div>
)

const items = [
  {
    manufacturer: 'BMW',
    model: 'X5',
    year: '2021',
    fuel: 'diesel',
    km: 100000,
    power: 200,
    engine: 2000,
    gearbox: 'automatic',
    sold_by: 'dealer',
    chassis: 'suv',
    prediction: 50000,
    description:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies.',
    header: <Skeleton />,
  },
  {
    manufacturer: 'BMW',
    model: 'X5',
    year: '2021',
    fuel: 'diesel',
    km: 100000,
    power: 200,
    engine: 2000,
    gearbox: 'automatic',
    sold_by: 'dealer',
    chassis: 'suv',
    prediction: 50000,
    description:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies.',
    header: <Skeleton />,
  },
  {
    manufacturer: 'BMW',
    model: 'X5',
    year: '2021',
    fuel: 'diesel',
    km: 100000,
    power: 200,
    engine: 2000,
    gearbox: 'automatic',
    sold_by: 'dealer',
    chassis: 'suv',
    prediction: 50000,
    description:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies.',
    header: <Skeleton />,
  },
  {
    manufacturer: 'BMW',
    model: 'X5',
    year: '2021',
    fuel: 'diesel',
    km: 100000,
    power: 200,
    engine: 2000,
    gearbox: 'automatic',
    sold_by: 'dealer',
    chassis: 'suv',
    prediction: 50000,
    description:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies.',
    header: <Skeleton />,
  },
  {
    manufacturer: 'BMW',
    model: 'X5',
    year: '2021',
    fuel: 'diesel',
    km: 100000,
    power: 200,
    engine: 2000,
    gearbox: 'automatic',
    sold_by: 'dealer',
    chassis: 'suv',
    prediction: 50000,
    description:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies.',
    header: <Skeleton />,
  },
  {
    manufacturer: 'BMW',
    model: 'X5',
    year: '2021',
    fuel: 'diesel',
    km: 100000,
    power: 200,
    engine: 2000,
    gearbox: 'automatic',
    sold_by: 'dealer',
    chassis: 'suv',
    prediction: 50000,
    description:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies.',
    header: <Skeleton />,
  },
  {
    manufacturer: 'BMW',
    model: 'X5',
    year: '2021',
    fuel: 'diesel',
    km: 100000,
    power: 200,
    engine: 2000,
    gearbox: 'automatic',
    sold_by: 'dealer',
    chassis: 'suv',
    prediction: 50000,
    description:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies. Nullam nec purus nec libero tincidunt ultricies.',
    header: <Skeleton />,
  },
]

function PredictionsHistory() {
  const handleDelete = () => {
    alert('Deleted')
  }

  return (
    <BentoGrid className="w-full">
      {items.map((item, i) => (
        <BentoGridItem
          key={i}
          title={`${item.manufacturer} ${item.model} ${item.year} - ${item.prediction} €`}
          description={
            <div className="flex flex-col gap-4">
              <div className="flex flex-wrap gap-2.5">
                <Chip text={item.fuel} />
                <Chip text={item.km.toString() + ' km'} />
                <Chip text={item.power.toString() + ' hp'} />
                <Chip text={item.engine.toString() + ' cm3'} />
                <Chip text={item.gearbox} />
                <Chip text={item.sold_by} />
                <Chip text={item.chassis} />
              </div>
              <div className="flex items-center justify-between">
                <Popover>
                  <PopoverTrigger>
                    <Button variant="secondary" size="sm">
                      Read description
                    </Button>
                  </PopoverTrigger>
                  <PopoverContent className="max-w-xl">{item.description}</PopoverContent>
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
                        onClick={handleDelete}
                      >
                        Delete
                      </AlertDialogAction>
                    </AlertDialogFooter>
                  </AlertDialogContent>
                </AlertDialog>
              </div>
            </div>
          }
          header={item.header}
          className={i === 3 || i === 6 ? 'md:col-span-2' : ''}
        />
      ))}
    </BentoGrid>
  )
}

export default PredictionsHistory
