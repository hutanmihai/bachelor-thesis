import { Button, ButtonProps } from '@/components/ui/button'
import { useFormContext } from 'react-hook-form'

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
      // TODO: Add Spinner icon
      // endIcon={isSubmitting ? <Spinner /> : null}
      disabled={disabled || isSubmitting}
      {...other}
    >
      {text}
    </Button>
  )
}

export default RHFSubmitButton
