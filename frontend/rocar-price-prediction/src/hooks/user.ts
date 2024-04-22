import { toast } from '@/components/ui/use-toast'
import { routes } from '@/config.global'
import { getCurrentUser } from '@/requests/user'
import { AxiosError } from 'axios'
import { useQuery } from 'react-query'

export function useUser() {
  return useQuery('getCurrentUser', async () => await getCurrentUser(), {
    onError: (error: AxiosError) => {
      toast({
        title: error.message,
        variant: 'destructive',
      })
    },
  })
}
