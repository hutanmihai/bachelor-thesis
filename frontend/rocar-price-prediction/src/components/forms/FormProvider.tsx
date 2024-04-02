import { UseFormReturn, FormProvider as Form, FieldValues } from 'react-hook-form'
import { ReactNode } from 'react'

type TFormProviderProps<T extends FieldValues> = {
  children: ReactNode
  methods: UseFormReturn<T>
  onSubmit?: VoidFunction
}

function FormProvider<T extends object>({ children, onSubmit, methods }: TFormProviderProps<T>) {
  return (
    <Form {...methods}>
      <form onSubmit={onSubmit} noValidate>
        {children}
      </form>
    </Form>
  )
}

export default FormProvider
