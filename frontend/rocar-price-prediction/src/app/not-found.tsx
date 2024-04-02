import MaxWidthWrapper from '@/components/max-width-wrapper'
import { buttonVariants } from '@/components/ui/button'
import { routes } from '@/config.global'
import { ArrowRight } from 'lucide-react'
import Link from 'next/link'

function NotFound() {
  return (
    <main className="flex h-[calc(100vh-56px)] flex-col items-center justify-center">
      <MaxWidthWrapper className="flex flex-col items-center justify-center">
        <h1 className="my-auto text-4xl font-bold">404 - Page Not Found</h1>
        <p className="text-lg">The page you are looking for does not exist.</p>
        <Link
          href={routes.landingpage.root}
          className={buttonVariants({
            size: 'lg',
            variant: 'link',
          })}
        >
          Go back to home <ArrowRight className="ml-2 h-5 w-5" />
        </Link>
      </MaxWidthWrapper>
    </main>
  )
}

export default NotFound
