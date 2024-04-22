import FormProvider from '@/components/forms/FormProvider'
import RHFInput from '@/components/forms/RHFInput'
import RHFSelect from '@/components/forms/RHFSelect'
import RHFSlider from '@/components/forms/RHFSlider'
import RHFSubmitButton from '@/components/forms/RHFSubmitButton'
import { MultiStepLoader } from '@/components/ui/multi-step-loader'
import { useInference } from '@/hooks/inference'
import { useForm } from 'react-hook-form'
import { z } from 'zod'
import { zodResolver } from '@hookform/resolvers/zod'

const loadingStates = [
  {
    text: 'Receiving your request',
  },
  {
    text: 'Processing your request',
  },
  {
    text: 'Warming up the AI',
  },
  {
    text: 'AI is thinking',
  },
]

type TInferenceFormType = {
  manufacturer: string
  model: string
  fuel: string
  chassis: string
  sold_by: string
  gearbox: string
  year: number
  km: number
  power: number
  engine: number
}

function InferenceForm() {
  const { mutateAsync: infer } = useInference()

  const defaultValues: TInferenceFormType = {
    manufacturer: '',
    model: '',
    // @ts-ignore
    year: [2020],
    chassis: '',
    fuel: '',
    km: 0,
    power: 0,
    engine: 0,
    gearbox: '',
    sold_by: '',
  }

  const schema = z.object({
    manufacturer: z.string().min(1),
    model: z.string().min(1),
    year: z.array(z.number().int().nonnegative().min(2000, 'Year must be greater than 2000')),
    chassis: z.string().min(1),
    fuel: z.string().min(1),
    km: z.number().int().nonnegative().min(0),
    power: z.number().int().nonnegative().min(0),
    engine: z.number().int().nonnegative().min(0),
    gearbox: z.string().min(1),
    sold_by: z.string().min(1),
  })

  const form = useForm<TInferenceFormType>({
    resolver: zodResolver(schema),
    defaultValues: defaultValues,
  })

  const handleSubmit = async (data: TInferenceFormType) => {
    // Converting the form data to the right format
    const requestData = {
      ...data,
      // @ts-ignore
      year: data.year[0],
      // TODO: add real description textarea input
      description:
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec turpis nec elit tincidunt aliquam.',
    }
    // Sleep for 10 seconds to simulate the inference process TODO: Remove this line
    await new Promise((resolve) => setTimeout(resolve, 10000))
    await infer(requestData)
  }

  return form.formState.isSubmitting ? (
    <MultiStepLoader
      loadingStates={loadingStates}
      loading={form.formState.isSubmitting}
      duration={2000}
      loop={false}
    />
  ) : (
    <FormProvider form={form} onSubmit={form.handleSubmit(handleSubmit)}>
      <div className="flex flex-col gap-5">
        <div className="grid grid-cols-1 gap-5 md:grid-cols-2">
          <RHFSelect
            name="manufacturer"
            labelName="Manufacturer"
            placeholder="Choose manufacturer"
            values={['bmw', 'audi', 'mercedes']}
          />
          <RHFSelect
            name="model"
            labelName="Model"
            placeholder="Choose model"
            values={['x3', 'x4', 'x5']}
          />
        </div>
        {/*<RHFInput labelName="Year" name="year" placeholder="Enter year" type="number" disabled />*/}
        <RHFSlider labelName="Year" min={2000} max={2024} name="year" />
        <div className="grid grid-cols-1 gap-5 md:grid-cols-2">
          <RHFSelect
            name="chassis"
            labelName="Chassis"
            placeholder="Choose chassis"
            values={['suv', 'sedan']}
          />
          <RHFSelect
            name="fuel"
            labelName="Fuel"
            placeholder="Choose fuel"
            values={['gas', 'diesel', 'hibrid']}
          />
          <RHFInput labelName={'Km'} name="km" placeholder="Enter km" type="number" />
          <RHFInput labelName={'Power'} name="power" placeholder="Enter power" type="number" />
          <RHFInput
            labelName={'Engine capacity'}
            name="engine"
            placeholder="Enter engine capacity"
            type="number"
          />
          <RHFSelect
            name="gearbox"
            labelName="Gearbox"
            placeholder="Choose gearbox"
            values={['manual', 'automatic']}
          />
          <RHFSelect
            name="sold_by"
            labelName="Sold by"
            placeholder="Choose between private and dealer"
            values={['private', 'dealer']}
          />
        </div>
        <RHFSubmitButton text="Get the right price" className="mt-10 w-full" type="submit" />
      </div>
    </FormProvider>
  )
}

export default InferenceForm
