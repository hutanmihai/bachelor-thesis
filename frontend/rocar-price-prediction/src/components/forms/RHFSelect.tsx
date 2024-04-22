import { FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { cn } from '@/lib/utils'
import { Asterisk } from 'lucide-react'
import * as React from 'react'
import { useFormContext } from 'react-hook-form'

type TRHFSelectProps = {
  name: string
  labelName: string
  placeholder: string
  values: string[]
  required?: boolean
  className?: string
  disabled?: boolean
}

function RHFSelect({
  name,
  labelName,
  required,
  className,
  disabled,
  placeholder,
  values,
}: TRHFSelectProps) {
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
            <Select
              onValueChange={field.onChange}
              defaultValue={field.value}
              disabled={disabled || isSubmitting}
              required={required}
            >
              <FormControl>
                <SelectTrigger className={cn(className, error ? 'ring-2 ring-destructive' : '')}>
                  <SelectValue placeholder={placeholder} />
                </SelectTrigger>
              </FormControl>
              <SelectContent>
                {values.map((value) => (
                  <SelectItem key={value} value={value}>
                    {value}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </FormControl>
          {error && (
            <FormMessage className="mb-0 mt-0.5 line-clamp-1 text-xs">{error.message}</FormMessage>
          )}
        </FormItem>
      )}
    />
  )
}

export default RHFSelect
