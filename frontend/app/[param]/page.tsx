'use client'
import { useGetCharacterDataQuery } from '@/app/lib/api'
import Image from 'next/image'
import { useParams } from 'next/navigation'

export default function CharacterDetail() {
  const params = useParams<{ param: string }>()
  const param = params?.param
  const { data, isLoading, isError } = useGetCharacterDataQuery(param)
  if (isError) {
    return 'Erro ao buscar dados'
  }
  if (isLoading) {
    return (
      <div className="absolute -translate-1/2 top-1/2 left-1/2 animate-pulse flex justify-center items-center mt-12 w-2/3 h-70 m-auto">
        <div className="relative w-100 h-100">
          <Image src="/umbrella-icon.png" alt="logo" loading="lazy" fill />
        </div>
      </div>
    )
  }
  return (
    <div className="w-3/4 m-auto h-148 flex flex-wrap justify-center items-center lg:w-10/12">
      <div className="relative w-3xl mr-4 h-148 overflow-hidden rounded-xl">
        <Image
          src={`${data?.img}` || '/umbrella-icon.png'}
          alt="logo"
          fill
          className="object-cover"
          sizes="100vw"
        />
      </div>
      <div className="w-1/2 sm:mt-4 h-full flex flex-col gap-4 border-t-2 border-l-2 border-alternative pl-4 pt-4">
        <ul>
          <li>Nome: {data?.name}</li>
          <li>Ano de Nascimento: {data?.birth}</li>
          <li>Tipo Sanguíneo: {data?.bloodType}</li>
          <li>Altura: {data?.height}</li>
          <li>Peso: {data?.weight}</li>
        </ul>
        <h2 className="font-bold">Dados coletados:</h2>
        <p className="overflow-y-scroll">{data?.bio}</p>
      </div>
    </div>
  )
}
