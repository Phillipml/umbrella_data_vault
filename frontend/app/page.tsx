'use client'
import Image from "next/image";
import { useGetCharactersListQuery } from "./lib/api";

export default function Home() {
  const {data}=useGetCharactersListQuery()
  return (
    <div className="min-h-screen">
      <div className="max-w-[1400px] m-auto">
        <div className="m-auto w-100vw border-b-2 border-alternative flex justify-center p-4">
        <Image src="/umbrella-full-logo.png" alt="logo" width={180} height={32} style={{objectFit: "contain"}}/>
        </div>
        <div className="w-3/4 m-auto mt-6 text-center lg:w-1/2"><h2>Umbrella Corporation — Arquivos restritos</h2> <p className="uppercase italic text-sm">&quot;our business is life itself&quot;</p></div>
        <div className="w-3/4 m-auto mt-6 lg:w-1/2"><p className="text-sm">Você está visualizando registros internos obtidos pela Umbrella Corporation sobre indivíduos envolvidos, 
          direta ou indiretamente, em incidentes biológicos e eventos de interesse da organização.<br />
          Os perfis abaixo contêm dados coletados ao longo de diferentes operações, incluindo sobreviventes, 
          agentes governamentais, pesquisadores e outras entidades consideradas relevantes.<br />
          Algumas informações podem estar incompletas ou classificadas.</p></div>
        <div className="w-2/3 h-60 m-auto flex flex-wrap justify-center gap-2 overflow-y-scroll mt-10 mb-10 scrollbar-custom ">
        {data?.map(i =>(
          <button key={i.param} className="w-80 mb-2 border-b border-alternative rounded-2xl cursor-pointer hover:shadow-md hover:shadow-alternative hover:text-shadow-lg/30 hover:text-shadow-alternative">{i.name}</button>
        ))}
        </div>
      </div>
    </div>
  );
}
