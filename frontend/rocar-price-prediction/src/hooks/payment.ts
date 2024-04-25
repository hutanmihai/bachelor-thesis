import { toast } from '@/components/ui/use-toast'
import { createCheckoutSession, TCreateCheckoutSessionRequestModel } from '@/requests/payment'
import { CustomApiError } from '@/utils/axios'
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
      onError: (error: CustomApiError) => {
        toast({
          title: error.response?.data.detail,
          variant: 'destructive',
        })
      },
    }
  )
}
