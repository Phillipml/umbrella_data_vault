'use client'
import { useGetCharacterDataQuery } from '@/app/lib/api'
import type { FetchBaseQueryError } from '@reduxjs/toolkit/query'
import Image from 'next/image'
import Link from 'next/link'
import { useParams } from 'next/navigation'

export default function CharacterDetail() {
  const params = useParams<{ param: string }>()
  const param = params?.param

  const { data, isLoading, isError, error } = useGetCharacterDataQuery(
    param ?? null
  )

  if (isLoading) {
    return (
      <div className="w-full min-h-[60vh] animate-pulse flex justify-center items-center px-4">
        <div className="relative w-28 h-28 sm:w-36 sm:h-36">
          <Image
            src="/umbrella-icon.png"
            alt="logo"
            fill
            className="object-contain"
            sizes="(max-width: 640px) 112px, 144px"
          />
        </div>
      </div>
    )
  }

  if (isError) {
    const status = (error as FetchBaseQueryError)?.status

    if (status === 404) {
      return (
        <div className="w-3/4 m-auto mt-10 text-center">
          <h2 className="font-bold">Registro indisponível</h2>
          <p>Esse personagem não consta mais na fonte oficial.</p>
          <Link href="/" className="underline">
            Voltar para lista
          </Link>
        </div>
      )
    }

    return (
      <div className="w-3/4 m-auto mt-10 text-center">
        <h2 className="font-bold">Falha temporária</h2>
        <p>
          Não foi possível consultar a fonte oficial agora. Tente novamente.
        </p>
      </div>
    )
  }

  const imageSrc = data?.img ? data.img : '/umbrella-icon.png'

  return (
    <div className="w-3/4 m-auto mb-2 flex flex-wrap justify-center items-center lg:w-10/12">
      <div className="relative w-md mr-4 h-100 overflow-hidden rounded-xl">
        {data?.img ? (
          <Image
            src={data.img}
            alt="logo"
            fill
            className="object-cover"
            sizes="100vw"
          />
        ) : (
          <Image
            src={'/umbrella-icon.png'}
            alt="logo"
            fill
            className="object-contain"
            sizes="100vw"
          />
        )}
      </div>
      <div className="w-full lg:w-1/2 mt-12 lg:mt-0 h-100 flex flex-col gap-4 border-t-2 border-l-2 border-alternative pl-4 pt-4">
        <ul>
          <li>Nome: {data?.name ?? '-'}</li>
          <li>Ano de Nascimento: {data?.birth ?? '-'}</li>
          <li>Tipo Sanguíneo: {data?.bloodType ?? '-'}</li>
          <li>Altura: {data?.height ?? '-'}</li>
          <li>Peso: {data?.weight ?? '-'}</li>
        </ul>
        <h2 className="font-bold">Dados coletados:</h2>
        <p className="overflow-y-auto">
          {data?.bio ?? 'Sem biografia disponível.'}
        </p>
      </div>
    </div>
  )
}
