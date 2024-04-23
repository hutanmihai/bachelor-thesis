import { routes } from '@/config.global'
import { getCurrentUser } from '@/requests/user'
import { useRouter } from 'next/navigation'
import { useQuery } from 'react-query'

type TUseUserProps = {
  enabled: boolean
}

export function useUser({ enabled }: TUseUserProps) {
  const router = useRouter()

  return useQuery('getCurrentUser', async () => await getCurrentUser(), {
    onError: () => {
      router.push(routes.auth.login)
    },
    enabled,
  })
}
