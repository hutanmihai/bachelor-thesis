import { toast } from '@/components/ui/use-toast'
import { callInference, TInferenceRequestModel } from '@/requests/inference'
import { AxiosError } from 'axios'
import { useMutation } from 'react-query'

export function useInference() {
  return useMutation(
    'inference',
    async (payload: TInferenceRequestModel) => await callInference(payload),
    {
      onSuccess: async ({ prediction }) => {
        toast({
          title: `Prediction: ${prediction}`,
        })
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
