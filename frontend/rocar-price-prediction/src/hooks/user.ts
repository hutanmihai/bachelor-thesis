import { getCurrentUser } from '@/requests/user'
import { useQuery } from 'react-query'

export function useUser() {
  return useQuery('getCurrentUser', async () => await getCurrentUser())
}
