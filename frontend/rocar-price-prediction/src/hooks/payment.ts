import { toast } from '@/components/ui/use-toast'
import { createCheckoutSession, TCreateCheckoutSessionRequestModel } from '@/requests/payment'
import { AxiosError } from 'axios'
import { useRouter } from 'next/navigation'
import { useMutation } from 'react-query'

export function useCreateCheckoutSession() {
  const router = useRouter()

  return useMutation(
    'createCheckoutSession',
    async (payload: TCreateCheckoutSessionRequestModel) => await createCheckoutSession(payload),
    {
      onSuccess: async ({ url }) => {
        router.push(url)
      },
      onError: (error: AxiosError) => {
        toast({
          title: error.message,
          variant: 'destructive',
        })
      },
    }
  )
}
