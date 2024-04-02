'use client'

import { useAuth } from '@/auth/context/auth'
import FormProvider from '@/components/forms/FormProvider'
import RHFInput from '@/components/forms/RHFInput'
import RHFSubmitButton from '@/components/forms/RHFSubmitButton'
import { Label } from '@/components/ui/label'
import { routes } from '@/config.global'
import { zodResolver } from '@hookform/resolvers/zod'
import Link from 'next/link'
import { useForm } from 'react-hook-form'
import { z } from 'zod'

type TAuthFormProps = {
  type: 'login' | 'register'
}

function AuthForm({ type }: TAuthFormProps) {
  const { login, register } = useAuth()

  const defaultValues =
    type === 'login'
      ? { email: '', password: '' }
      : {
          email: '',
          password: '',
          username: '',
        }

  type TLoginFormType = {
    email: string
    password: string
  }

  type TRegisterFormType = {
    email: string
    password: string
    username: string
  }

  type TAuthFormType = TLoginFormType | TRegisterFormType

  const schema = z.object({
    email: z.string().email(),
    password: z.string().min(8),
    username: type === 'register' ? z.string().min(3) : z.string().optional(),
  })

  const methods = useForm<TAuthFormType>({
    resolver: zodResolver(schema),
    defaultValues: defaultValues,
  })

  const handleSubmit = async (data: TAuthFormType) => {
    if (type === 'login') {
      await login(data)
    } else {
      // @ts-ignore
      await register(data)
    }
  }

  return (
    <FormProvider methods={methods} onSubmit={methods.handleSubmit(handleSubmit)}>
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
              <RHFInput
                name="username"
                id="username"
                placeholder="m"
                labelName="Username"
                required
              />
            </div>
          )}
          <div className="grid gap-2">
            <RHFInput
              name="email"
              id="email"
              type="email"
              placeholder="m@example.com"
              labelName="Email"
              required
            />
          </div>
          <div className="grid gap-2">
            <RHFInput name="password" id="password" type="password" labelName="Password" required />
          </div>
          <RHFSubmitButton
            type="submit"
            className="w-full"
            text={type === 'login' ? 'Login' : 'Register'}
          />
        </div>
        <div className="mt-4 text-center text-sm">
          {type === 'login' ? (
            <>
              Don&apos;t have an account?{' '}
              <Link href={routes.auth.register} className="underline">
                Sign up
              </Link>
            </>
          ) : (
            <Link href={routes.auth.login} className="underline">
              Already have an account? Sign in
            </Link>
          )}
        </div>
      </div>
    </FormProvider>
  )
}

export default AuthForm
