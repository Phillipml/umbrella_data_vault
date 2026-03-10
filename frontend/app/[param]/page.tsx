"use client"
import { useGetCharacterDataQuery } from "@/app/lib/api"
import { useParams } from "next/navigation"

export default function CharacterDetail() {
    
    const params = useParams<{param: string}>();
    const param = params?.param
    const {data,isLoading, isError} = useGetCharacterDataQuery(param)
    
  return (
    <div>
      {data?.name}
    </div>
  )
}
