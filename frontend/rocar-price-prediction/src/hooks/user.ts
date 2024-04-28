import { getCurrentUser } from '@/requests/user'
import { useQuery } from 'react-query'

type TUseUserProps = {
  enabled?: boolean
}

export function useUser({ enabled = true }: TUseUserProps = {}) {
  return useQuery('getCurrentUser', async () => await getCurrentUser(), {
    enabled,
  })
}
