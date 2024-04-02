import { Button, ButtonProps } from '@/components/ui/button'
import { useFormContext } from 'react-hook-form'
import { Loader } from 'lucide-react'

export type TRHFSubmitButtonProps = ButtonProps & {
  text: string
}

function RHFSubmitButton({
  text,
  disabled,
  variant = 'default',
  color = 'primary',
  ...other
}: TRHFSubmitButtonProps) {
  const {
    formState: { isSubmitting },
  } = useFormContext()

  return (
    <Button
      variant={variant}
      color={color}
      type="submit"
      disabled={disabled || isSubmitting}
      {...other}
    >
      {isSubmitting ? <Loader className="h-6 w-6" /> : text}
    </Button>
  )
}

export default RHFSubmitButton
