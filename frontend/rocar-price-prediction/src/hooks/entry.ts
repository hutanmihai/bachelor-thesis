import { toast } from '@/components/ui/use-toast'
import { deleteEntry, listEntries } from '@/requests/entry'
import { CustomApiError } from '@/utils/axios'
import { useMutation, useQuery, useQueryClient } from 'react-query'

export function useEntries() {
  return useQuery('entries', async () => await listEntries(), {
    onError: (error: CustomApiError) => {
      toast({
        title: error.response?.data.detail,
        variant: 'destructive',
      })
    },
  })
}

export function useDeleteEntry() {
  const queryClient = useQueryClient()

  return useMutation('deleteEntry', async (id: string) => await deleteEntry(id), {
    onSuccess: async () => {
      await queryClient.invalidateQueries('entries')
      toast({
        title: 'Entry deleted successfully!',
      })
    },
    onError: (error: CustomApiError) => {
      toast({
        title: error.response?.data.detail,
        variant: 'destructive',
      })
    },
  })
}
