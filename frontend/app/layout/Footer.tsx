export default function Footer() {
  return (
    <footer className="border-t-2 border-text p-2 w-full bg-background ">
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
  )
}
