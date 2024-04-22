import { FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { Slider } from '@/components/ui/slider'
import { cn } from '@/lib/utils'
import { SliderProps } from '@radix-ui/react-slider'
import { Asterisk } from 'lucide-react'
import * as React from 'react'
import { useFormContext } from 'react-hook-form'

type TRHFSliderProps = SliderProps & {
  name: string
  labelName: string
  required?: boolean
  className?: string
  disabled?: boolean
}

function RHFSlider({ name, labelName, required, disabled, ...other }: TRHFSliderProps) {
  const {
    control,
    formState: { isSubmitting },
  } = useFormContext()

  return (
    <FormField
      control={control}
      name={name}
      render={({ field, fieldState: { error } }) => (
        <FormItem>
          <div className="mb-1 flex items-center justify-start">
            <FormLabel>
              {labelName} - {field.value}
            </FormLabel>
            {required && <Asterisk className="mb-2 h-4 w-4 text-destructive" />}
          </div>
          <FormControl>
            <Slider
              defaultValue={[field.value]}
              onValueChange={field.onChange}
              disabled={disabled || isSubmitting}
              {...other}
            />
          </FormControl>
          {error && (
            <FormMessage className="mb-0 mt-0.5 line-clamp-1 text-xs">{error.message}</FormMessage>
          )}
        </FormItem>
      )}
    />
  )
}

export default RHFSlider
