import { UseFormReturn, FieldValues } from 'react-hook-form'
import { ReactNode } from 'react'
import { Form } from '@/components/ui/form'

type TFormProviderProps<T extends FieldValues> = {
  children: ReactNode
  form: UseFormReturn<T>
  onSubmit?: VoidFunction
}

function FormProvider<T extends object>({ children, onSubmit, form }: TFormProviderProps<T>) {
  return (
    <Form {...form}>
      <form onSubmit={onSubmit} noValidate>
        {children}
      </form>
    </Form>
  )
}

export default FormProvider
