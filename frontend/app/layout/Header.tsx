import Image from 'next/image'
import Link from 'next/link'

export default function Header() {
  return (
    <header className="m-auto w-full bg-background border-b-2 border-alternative flex justify-center p-4 fixed z-50">
      <Link href="/">
        <Image
          src="/umbrella-full-logo.png"
          alt="logo"
          width={180}
          height={32}
          style={{ objectFit: 'contain' }}
        />
      </Link>
    </header>
  )
}
