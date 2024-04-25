import { Loader } from 'lucide-react'

function Loading() {
  return (
    <div className="flex items-center justify-center" style={{ height: 'calc(100vh - 10rem)' }}>
      <Loader className="loader-gradient h-32 w-32 text-zinc-800 md:h-48 md:w-48" />
    </div>
  )
}

export default Loading
