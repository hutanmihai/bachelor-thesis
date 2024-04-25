import { toast } from '@/components/ui/use-toast'
import { callInference, TInferenceRequestModel } from '@/requests/inference'
import { CustomApiError } from '@/utils/axios'
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
      onError: (error: CustomApiError) => {
        toast({
          title: error.response?.data.detail,
          variant: 'destructive',
        })
      },
    }
  )
}
