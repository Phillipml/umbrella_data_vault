import Image from "next/image";

export default function Home() {
  return (
    <div className="min-h-screen">
      <div className="max-w-[1400px] m-auto">
        <div className="m-auto w-100vw border-b-2 border-alternative flex justify-center p-4">
        <Image src="/umbrella-full-logo.png" alt="logo" width={180} height={32} style={{objectFit: "contain"}}/>
        </div>
        <div className="w-15 animate-ping"><Image src="/umbrella-icon.png" alt="logo" width={180} height={32} style={{objectFit: "contain"}}/></div>
      
      </div>
    </div>
  );
}
