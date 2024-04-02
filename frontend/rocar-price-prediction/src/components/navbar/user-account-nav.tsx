import LogoutButton from '@/components/auth/logout-button'
import { Avatar, AvatarFallback } from '@/components/ui/avatar'
import { Button } from '@/components/ui/button'
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
import { routes } from '@/config.global'
import Image from 'next/image'
import Link from 'next/link'
import { Gem, User } from 'lucide-react'

interface UserAccountNavProps {
  email: string | undefined
  name: string
}

function UserAccountNav({ email, name }: UserAccountNavProps) {
  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild className="overflow-visible">
        <Button className="aspect-square h-8 w-8 rounded-full bg-primary">
          <Avatar className="mb-1 flex items-center justify-center">
            <User className="h-5 w-5" />
          </Avatar>
        </Button>
      </DropdownMenuTrigger>

      <DropdownMenuContent className="bg-white" align="end">
        <div className="flex items-center justify-start gap-2 p-2">
          <div className="flex flex-col space-y-0.5 leading-none">
            {name && <p className="text-sm font-medium text-black">{name}</p>}
            {email && <p className="w-[200px] truncate text-xs text-zinc-700">{email}</p>}
          </div>
        </div>

        <DropdownMenuSeparator />

        <DropdownMenuItem asChild>
          <Link href={routes.dashboard.root} className="cursor-pointer">
            Dashboard
          </Link>
        </DropdownMenuItem>

        {/*<DropdownMenuItem asChild>*/}
        {/*  {subscriptionPlan?.isSubscribed ? (*/}
        {/*    <Link href="/dashboard/billing">Manage Subscription</Link>*/}
        {/*  ) : (*/}
        {/*    <Link href={routes.dashboard.root}>*/}
        {/*      Upgrade <Gem className="ml-1.5 h-4 w-4 text-blue-600" />*/}
        {/*    </Link>*/}
        {/*  )}*/}
        {/*</DropdownMenuItem>*/}

        <DropdownMenuSeparator />

        <DropdownMenuItem className="cursor-pointer">
          <LogoutButton />
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}

export default UserAccountNav
