import { useState } from 'react'
import { uploadFile as uploadFileRequest } from '@/requests/file'

export default function useFileUploader() {
  const [fileUrl, setFileUrl] = useState<string | null>(null)
  const [isError, setIsError] = useState<boolean>(false)
  const [errorMessage, setErrorMessage] = useState<string>('')
  const [isLoading, setIsLoading] = useState<boolean>(false)

  const uploadFile = async (files: FileList) => {
    try {
      setIsLoading(true)
      const file = files[0]

      const imageUploadRes = await uploadFileRequest({ file })

      setFileUrl(imageUploadRes.url)
      setIsError(false)
      setErrorMessage('')
      setIsLoading(false)
    } catch (err: any) {
      setIsLoading(false)
      setFileUrl(null)
      setIsError(true)
      setErrorMessage('File upload failed!')
    }
  }
  return { fileUrl, upload: uploadFile, isError, errorMessage, isLoading }
}
