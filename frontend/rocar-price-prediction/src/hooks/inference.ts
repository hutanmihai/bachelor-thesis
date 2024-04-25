import { toast } from '@/components/ui/use-toast'
import { callInference, TInferenceRequestModel } from '@/requests/inference'
import { CustomApiError } from '@/utils/axios'
import { useMutation, useQueryClient } from 'react-query'

export function useInference() {
  const queryClient = useQueryClient()

  return useMutation(
    'inference',
    async (payload: TInferenceRequestModel) => await callInference(payload),
    {
      onSuccess: async ({ prediction }) => {
        toast({
          title: `Prediction: ${prediction}`,
        })
        await queryClient.invalidateQueries('getCurrentUser')
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
