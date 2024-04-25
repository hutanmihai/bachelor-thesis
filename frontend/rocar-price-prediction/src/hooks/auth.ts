import { toast, useToast } from '@/components/ui/use-toast'
import { login, register, TLoginRequestModel, TRegisterRequestModel } from '@/requests/auth'
import { CustomApiError } from '@/utils/axios'
import { useMutation } from 'react-query'

export function useLogin() {
  const { toast } = useToast()

  return useMutation('login', async (payload: TLoginRequestModel) => await login(payload), {
    onSuccess: async () => {
      toast({
        title: 'Login successful',
      })
    },
    onError: (error: CustomApiError) => {
      toast({
        title: error.response?.data?.detail,
        variant: 'destructive',
      })
    },
  })
}

export function useRegister() {
  return useMutation(
    'register',
    async (payload: TRegisterRequestModel) => await register(payload),
    {
      onSuccess: async () => {
        toast({
          title: 'Registration successful',
        })
      },
      onError: (error: CustomApiError) => {
        toast({
          title: error.response?.data.detail,
          variant: 'destructive',
        })
      },
    }
  )
}
