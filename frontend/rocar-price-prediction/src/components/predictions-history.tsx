import Chip from '@/components/chip'
import { BentoGrid, BentoGridItem } from '@/components/ui/bento-grid'

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
    header: <Skeleton />,
  },
]

function PredictionsHistory() {
  return (
    <BentoGrid className="w-full">
      {items.map((item, i) => (
        <BentoGridItem
          key={i}
          title={`${item.manufacturer} ${item.model} ${item.year} - ${item.prediction} €`}
          description={
            <div className="flex flex-wrap gap-2.5">
              <Chip text={item.fuel} />
              <Chip text={item.km.toString() + ' km'} />
              <Chip text={item.power.toString() + ' hp'} />
              <Chip text={item.engine.toString() + ' cm3'} />
              <Chip text={item.gearbox} />
              <Chip text={item.sold_by} />
              <Chip text={item.chassis} />
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
