import { Loader } from 'lucide-react'

function Loading() {
  return (
    <div className="flex items-center justify-center" style={{ height: 'calc(100vh - 10rem)' }}>
      <Loader className="loader-gradient h-14 w-14 text-zinc-800 md:h-24 md:w-24" />
    </div>
  )
}

export default Loading
