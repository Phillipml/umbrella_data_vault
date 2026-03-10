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
        <div className="w-15 animate-ping"><Image src="/umbrella-icon.png" alt="logo" width={180} height={32} style={{objectFit: "contain"}}/></div>
        {data?.map(i =>(
          <p>{i.name}</p>
        ))}
      
      </div>
    </div>
  );
}
