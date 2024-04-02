import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import Link from 'next/link'
import { FormEvent } from 'react'

type TAuthFormProps = {
  type: 'login' | 'register'
}

function AuthForm({ type }: TAuthFormProps) {
  return (
    <div className="flex items-center justify-center py-12">
      <div className="mx-auto grid w-[350px] gap-6">
        <div className="grid gap-2 text-center">
          <h1 className="text-3xl font-bold">{type === 'login' ? 'Login' : 'Register'}</h1>
          <p className="text-balance text-muted-foreground">
            {type === 'login'
              ? 'Enter your email below to login to your account'
              : 'Enter your credentials below to register for a new account'}
          </p>
        </div>
        <div className="grid gap-4">
          {type === 'register' && (
            <div className="grid gap-2">
              <Label htmlFor="email">Username</Label>
              <Input id="username" placeholder="m" required />
            </div>
          )}
          <div className="grid gap-2">
            <Label htmlFor="email">Email</Label>
            <Input id="email" type="email" placeholder="m@example.com" required />
          </div>
          <div className="grid gap-2">
            <Label htmlFor="password">Password</Label>
            <Input id="password" type="password" required />
          </div>
          <Button type="submit" className="w-full">
            {type === 'login' ? 'Login' : 'Register'}
          </Button>
        </div>
        <div className="mt-4 text-center text-sm">
          {type === 'login' ? (
            <>
              Don&apos;t have an account?{' '}
              <Link href="/auth/register" className="underline">
                Sign up
              </Link>
            </>
          ) : (
            <Link href="/auth/login" className="underline">
              Already have an account? Sign in
            </Link>
          )}
        </div>
      </div>
    </div>
  )
}

export default AuthForm
