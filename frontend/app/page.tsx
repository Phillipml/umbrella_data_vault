'use client'

import List from './layout/List'

export default function Home() {
  return (
    <>
      <div className="max-w-[1400px] m-auto">
        <div className="w-3/4 m-auto mt-6 text-center lg:w-1/2">
          <h2>Umbrella Corporation — Arquivos restritos</h2>{' '}
          <p className="uppercase italic text-sm">
            &quot;our business is life itself&quot;
          </p>
        </div>
        <div className="w-3/4 m-auto mt-6 lg:w-full">
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
        <List />
      </div>
    </>
  )
}
