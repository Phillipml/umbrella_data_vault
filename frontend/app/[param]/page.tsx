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
    <div className="w-11/12 max-w-[1200px] m-auto flex flex-col lg:flex-row justify-center items-start gap-4">
      <div className="relative w-full lg:w-3/5 h-88 sm:h-112 lg:h-148 overflow-hidden rounded-xl">
        <Image
          src={imageSrc}
          alt={data?.name ?? 'personagem'}
          fill
          className="object-contain"
          sizes="(max-width: 1024px) 100vw, 60vw"
        />
      </div>

      <div className="w-full lg:w-2/5 lg:h-148 flex flex-col gap-4 border-t-2 lg:border-t-0 lg:border-l-2 border-alternative pl-0 pt-4 lg:pl-4 lg:pt-0">
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
