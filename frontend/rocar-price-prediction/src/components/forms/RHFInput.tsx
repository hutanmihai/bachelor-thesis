import { FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form'
import { Input, InputProps } from '@/components/ui/input'
import { cn } from '@/lib/utils'
import { Asterisk } from 'lucide-react'
import * as React from 'react'
import { useFormContext } from 'react-hook-form'

type TRHFInputProps = InputProps & {
  name: string
  labelName: string
  required?: boolean
}

function RHFInput({
  name,
  labelName,
  required,
  className,
  type,
  disabled,
  ...other
}: TRHFInputProps) {
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
            <Input
              {...field}
              type={type}
              value={type === 'number' && field.value === 0 ? '' : field.value}
              onChange={(event) => {
                if (type === 'number') {
                  field.onChange(Number(event.target.value))
                } else {
                  field.onChange(event.target.value)
                }
              }}
              disabled={disabled || isSubmitting}
              className={cn(className, error ? 'ring-2 ring-destructive' : '')}
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

export default RHFInput
