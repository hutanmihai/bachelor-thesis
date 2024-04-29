import { FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form'
import { Switch } from '@/components/ui/switch'
import { cn } from '@/lib/utils'
import { SwitchProps } from '@radix-ui/react-switch'
import { Asterisk } from 'lucide-react'
import * as React from 'react'
import { useFormContext } from 'react-hook-form'

type TRHFSwitchProps = SwitchProps & {
  name: string
  labelName: string
  required?: boolean
  disabled?: boolean
}

function RHFSwitch({ name, labelName, required, disabled, className, ...other }: TRHFSwitchProps) {
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
          <FormControl>
            <div className="flex items-center justify-start gap-2.5">
              <Switch
                {...field}
                value={field.value}
                onChange={field.onChange}
                disabled={disabled || isSubmitting}
                className={cn(className, error ? 'ring-2 ring-destructive' : '')}
                {...other}
              />
              <div className="mb-1 flex items-center justify-start">
                <FormLabel>{labelName}</FormLabel>
                {required && <Asterisk className="mb-2 h-4 w-4 text-destructive" />}
              </div>
            </div>
          </FormControl>
          {error && (
            <FormMessage className="mb-0 mt-0.5 line-clamp-1 text-xs">{error.message}</FormMessage>
          )}
        </FormItem>
      )}
    />
  )
}

export default RHFSwitch
