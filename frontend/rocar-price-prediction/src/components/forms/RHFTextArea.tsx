import { FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form'
import { Textarea, TextareaProps } from '@/components/ui/textarea'
import { cn } from '@/lib/utils'
import { Asterisk } from 'lucide-react'
import * as React from 'react'
import { useFormContext } from 'react-hook-form'

type TRHFTextArea = TextareaProps & {
  name: string
  labelName: string
  required?: boolean
  disabled?: boolean
  className?: string
}

function RHFTextArea({ name, labelName, required, disabled, className, ...other }: TRHFTextArea) {
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
            <FormLabel>{labelName}</FormLabel>
            {required && <Asterisk className="mb-2 h-4 w-4 text-destructive" />}
          </div>
          <FormControl>
            <Textarea
              placeholder="Paste the ad description here..."
              disabled={disabled || isSubmitting}
              className={cn(
                className,
                error ? 'resize-none ring-2 ring-destructive' : 'resize-none'
              )}
              {...field}
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

export default RHFTextArea
