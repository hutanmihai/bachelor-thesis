import { apiConfig } from '@/config.global'
import axiosInstance from '@/utils/axios'

export type TFileUploadRequest = {
  file: any
}

export type TFileUploadResponse = {
  url: string
}

export const uploadFile = async ({ file }: TFileUploadRequest) => {
  const formData = new FormData()
  formData.append('file', file)

  const response = await axiosInstance.post(apiConfig.entry.upload, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  })

  return response.data as TFileUploadResponse
}
