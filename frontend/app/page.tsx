'use client'
import Image from 'next/image'
import { useGetCharactersListQuery } from './lib/api'

export default function Home() {
  const { data, isError, isLoading } = useGetCharactersListQuery()
  const listHandle = () => {
    if (isError) {
      return 'Erro ao carregar Lista'
    }
    if (isLoading) {
      return (
        <div className="animate-spin flex justify-center items-center mt-12 w-2/3 h-70 m-auto">
          <Image
            src="/umbrella-icon.png"
            alt="logo"
            width={56}
            height={56}
            loading="lazy"
            style={{ objectFit: 'contain' }}
          />
        </div>
      )
    }
    return (
      <div className="w-2/4 h-100 m-auto flex flex-wrap justify-center gap-x-12 gap-y-4 overflow-y-scroll mt-10 mb-10 scrollbar-custom ">
        {' '}
        {data?.map((i) => (
          <button
            key={i.param}
            className="w-80 mb-2 border-b border-alternative rounded-2xl cursor-pointer hover:shadow-md hover:shadow-alternative hover:text-shadow-lg/30 hover:text-shadow-alternative"
          >
            {i.name}
          </button>
        ))}
      </div>
    )
  }
  return (
    <div className="min-h-screen flex flex-col">
      <div className="m-auto w-full border-b-2 border-alternative flex justify-center p-4">
        <Image
          src="/umbrella-full-logo.png"
          alt="logo"
          width={180}
          height={32}
          style={{ objectFit: 'contain' }}
        />
      </div>
      <div className="max-w-[1400px] m-auto flex-1">
        <div className="w-3/4 m-auto mt-6 text-center lg:w-1/2">
          <h2>Umbrella Corporation — Arquivos restritos</h2>{' '}
          <p className="uppercase italic text-sm">
            &quot;our business is life itself&quot;
          </p>
        </div>
        <div className="w-3/4 m-auto mt-6 lg:w-1/2">
          <p className="text-sm">
            Você está visualizando registros internos obtidos pela Umbrella
            Corporation sobre indivíduos envolvidos, direta ou indiretamente, em
            incidentes biológicos e eventos de interesse da organização.
            <br />
            Os perfis abaixo contêm dados coletados ao longo de diferentes
            operações, incluindo sobreviventes, agentes governamentais,
            pesquisadores e outras entidades consideradas relevantes.
            <br />
            Algumas informações podem estar incompletas ou classificadas.
          </p>
        </div>
        {listHandle()}
      </div>
      <footer className="border-t-2 border-text p-2 w-full mt-auto">
        <p className="text-center">
          Projeto criado por{' '}
          <a
            href="https://www.linkedin.com/in/phillip-menezes-desenvolvedor/"
            target="_blank"
            className="text-sm border-b border-alternative hover:text-alternative"
          >
            Phillip Menezes
          </a>
        </p>
        <p className="text-center">
          Conteúdos extraídos de{' '}
          <a
            href="https://www.residentevildatabase.com/"
            target="_blank"
            className="text-sm border-b border-alternative hover:text-alternative"
          >
            Resident Evil Database
          </a>
        </p>
        <p className="text-center">
          Siga{' '}
          <a
            href="https://www.youtube.com/@monidatabase"
            target="_blank"
            className="text-sm border-b border-alternative hover:text-alternative"
          >
            Moni | Database
          </a>
        </p>
      </footer>
    </div>
  )
}
