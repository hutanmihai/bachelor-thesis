import AuthForm from '@/components/auth/auth-form'
import Image from 'next/image'

function Register() {
  return (
    <main className="h-[calc(100vh-56px)] w-full lg:grid lg:min-h-[600px] lg:grid-cols-2 xl:min-h-[800px]">
      <AuthForm type="register" />
      <div className="hidden bg-muted lg:block">
        <Image
          src="/auth/side-image.webp"
          alt="Image"
          width="1024"
          height="1024"
          quality="100"
          className="h-full w-full object-cover dark:brightness-[0.3]"
        />
      </div>
    </main>
  )
}

export default Register
