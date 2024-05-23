'use client'

import ExtraOptions from '@/components/extra-options'
import FormProvider from '@/components/forms/FormProvider'
import RHFInput from '@/components/forms/RHFInput'
import RHFSelect from '@/components/forms/RHFSelect'
import RHFSubmitButton from '@/components/forms/RHFSubmitButton'
import RHFTextArea from '@/components/forms/RHFTextArea'
import Dropzone from '@/components/ui/dropzone'
import { FormLabel } from '@/components/ui/form'
import { MultiStepLoader } from '@/components/ui/multi-step-loader'
import { toast } from '@/components/ui/use-toast'
import { routes } from '@/config.global'
import {
  chassisTypes,
  fuelTypes,
  gearboxTypes,
  getAllManufacturers,
  getModelsForManufacturer,
  soldByTypes,
} from '@/constants'
import useFileUploader from '@/hooks/file-upload'
import { useInference } from '@/hooks/inference'
import { Asterisk } from 'lucide-react'
import { useRouter } from 'next/navigation'
import { useEffect, useState } from 'react'
import * as React from 'react'
import { useForm } from 'react-hook-form'
import { z } from 'zod'
import { zodResolver } from '@hookform/resolvers/zod'

const loadingStates = [
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
  description: string
  image_url: string
  audio_and_technology?: string[]
  confort_and_extra_options?: string[]
  electronics_and_assistance_systems?: string[]
  performance?: string[]
  safety?: string[]
}

function InferenceForm() {
  const { isError, errorMessage, upload, fileUrl } = useFileUploader()
  const { mutateAsync: infer } = useInference()
  const [modelValues, setModelValues] = useState<string[]>([])
  const router = useRouter()

  const defaultValues = {
    manufacturer: '',
    model: '',
    year: 2024,
    chassis: '',
    fuel: '',
    km: 0,
    power: 0,
    engine: 0,
    gearbox: '',
    sold_by: '',
    description: '',
    image_url: '',
    audio_and_technology: [],
    comfort_and_optional_equipment: [],
    electronics_and_assistance_systems: [],
    performance: [],
    safety: [],
  }

  const schema = z.object({
    manufacturer: z.string().min(1),
    model: z.string().min(1),
    year: z
      .number()
      .int()
      .nonnegative()
      .min(2000, 'Year must be greater than 2000')
      .max(2024, 'Year must be less than 2024'),
    chassis: z.string().min(1),
    fuel: z.string().min(1),
    km: z.number().int().nonnegative().min(0),
    power: z.number().int().nonnegative().min(0),
    engine: z.number().int().nonnegative().min(0),
    gearbox: z.string().min(1),
    sold_by: z.string().min(1),
    description: z.string().min(1),
    image_url: z.string().min(1).url(),
    audio_and_technology: z.array(z.string()).optional(),
    comfort_and_optional_equipment: z.array(z.string()).optional(),
    electronics_and_assistance_systems: z.array(z.string()).optional(),
    performance: z.array(z.string()).optional(),
    safety: z.array(z.string()).optional(),
  })

  const form = useForm<z.infer<typeof schema>>({
    resolver: zodResolver(schema),
    defaultValues: defaultValues,
  })

  useEffect(() => {
    if (fileUrl) {
      form.setValue('image_url', fileUrl, { shouldValidate: true, shouldDirty: true })
    }
  }, [fileUrl, form])

  useEffect(() => {
    if (isError) {
      form.setError('image_url', {
        type: 'manual',
        message: errorMessage,
      })
      toast({
        title: 'Error',
        description: errorMessage,
        variant: 'destructive',
      })
    }
  }, [isError, errorMessage, form])

  useEffect(() => {
    const subscription = form.watch((value, { name, type }) => {
      if (name === 'manufacturer') {
        setModelValues(() => getModelsForManufacturer(value.manufacturer))
      }
    })
    return () => subscription.unsubscribe()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [form.watch])

  const handleDrop = async (files: FileList | null) => {
    if (!files) return
    await upload(files)
  }

  const handleSubmit = async (data: TInferenceFormType) => {
    await new Promise((resolve) => setTimeout(resolve, 1500))
    await infer(data)
    router.push(routes.dashboard.root)
    form.reset(defaultValues)
  }

  return form.formState.isSubmitting ? (
    <MultiStepLoader
      loadingStates={loadingStates}
      loading={form.formState.isSubmitting}
      duration={500}
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
            values={getAllManufacturers()}
            required
          />
          <RHFSelect
            name="model"
            labelName="Model"
            placeholder="Choose model"
            values={modelValues}
            disabled={!form.watch('manufacturer')}
            required
          />
          <RHFInput labelName="Year" name="year" placeholder="Enter year" type="number" required />
          <RHFSelect
            name="fuel"
            labelName="Fuel"
            placeholder="Choose fuel"
            required
            values={fuelTypes}
          />
        </div>
        <RHFTextArea labelName="Description" name="description" required />
        <div className="grid grid-cols-1 gap-5 md:grid-cols-2">
          <RHFSelect
            name="chassis"
            labelName="Chassis"
            placeholder="Choose chassis"
            required
            values={chassisTypes}
          />
          <RHFInput labelName="Km" name="km" placeholder="Enter km" type="number" required />
          <RHFInput
            labelName="Power"
            name="power"
            placeholder="Enter power"
            type="number"
            required
          />
          <RHFInput
            labelName="Engine capacity"
            name="engine"
            placeholder="Enter engine capacity"
            type="number"
            required
          />
          <RHFSelect
            name="gearbox"
            labelName="Gearbox"
            placeholder="Choose gearbox"
            required
            values={gearboxTypes}
          />
          <RHFSelect
            name="sold_by"
            labelName="Sold by"
            placeholder="Choose between private and dealer"
            required
            values={soldByTypes}
          />
        </div>
        <div>
          <div className="mb-1 flex items-center justify-start">
            <FormLabel>Image</FormLabel>
            <Asterisk className="mb-2 h-4 w-4 text-destructive" />
          </div>
          <Dropzone
            dropMessage="Image is required"
            handleOnDrop={(files) => handleDrop(files)}
            accept="image/*"
            imageUrl={form.watch('image_url')}
          />
        </div>
        <div>
          <ExtraOptions />
        </div>
        <RHFSubmitButton text="Get the right price" className="mt-10 w-full" type="submit" />
      </div>
    </FormProvider>
  )
}

export default InferenceForm
