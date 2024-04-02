import { Input, InputProps } from '@/components/ui/input'
import { cn } from '@/lib/utils'
import * as React from 'react'
import { Controller, useFormContext } from 'react-hook-form'

type TRHFInputProps = InputProps & {
  name: string
}

function RHFInput({ name, className, type, disabled, ...other }: TRHFInputProps) {
  const {
    control,
    formState: { isSubmitting },
  } = useFormContext()

  return (
    <Controller
      name={name}
      control={control}
      render={({ field, fieldState: { error } }) => (
        <div>
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
          {error && (
            <span className="mb-0 mt-0.5 line-clamp-1 text-xs text-destructive">
              {error.message}
            </span>
          )}
        </div>
      )}
    />
  )
}

export default RHFInput
