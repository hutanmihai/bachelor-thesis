import { apiConfig } from '@/config.global'
import { TEntry } from '@/types/entry.types'
import axiosInstance from '@/utils/axios'

export type TEntryResponseModel = {
  entries: TEntry[]
}

export async function listEntries() {
  const response = await axiosInstance.get(apiConfig.entry.list)
  return response.data as TEntryResponseModel
}

export async function deleteEntry(id: string) {
  await axiosInstance.delete(apiConfig.entry.delete(id))
}
