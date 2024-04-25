import { getCurrentUser } from '@/requests/user'
import { useQuery } from 'react-query'

type TUseUserProps = {
  enabled: boolean
}

export function useUser({ enabled }: TUseUserProps) {
  return useQuery('getCurrentUser', async () => await getCurrentUser(), {
    enabled,
  })
}
