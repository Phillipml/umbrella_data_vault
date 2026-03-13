import Image from 'next/image'
import { useGetCharactersListQuery } from '../lib/api'
import { useMemo, useState } from 'react'
import Search from './Search'

export default function List() {
  const { data, isError, isLoading } = useGetCharactersListQuery()

  const [searchTerm, setSearchTerm] = useState('')
  const filteredList = useMemo(() => {
    if (!data) return []
    if (!searchTerm.trim()) return data
    const term = searchTerm.toLowerCase().trim()
    return data.filter((i) => i.name.toLowerCase().includes(term))
  }, [data, searchTerm])
  const isSearch = searchTerm == ''
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
    <>
      <Search value={searchTerm} onChange={setSearchTerm} />
      <div className="w-2/4 h-100 m-auto flex flex-wrap justify-center gap-x-12 gap-y-4 overflow-y-scroll mt-10 mb-10 scrollbar-custom lg:w-full">
        {isSearch
          ? data?.map((i) => (
              <a
                key={i.param}
                href={`/${i.param}`}
                className="w-80 mb-2 border-b border-alternative rounded-2xl text-center cursor-pointer hover:shadow-md hover:shadow-alternative hover:text-shadow-lg/30 hover:text-shadow-alternative"
              >
                {i.name}
              </a>
            ))
          : filteredList?.map((i) => (
              <a
                key={i.param}
                href={`/${i.param}`}
                className="w-80 h-6 mb-2 border-b border-alternative rounded-2xl text-center cursor-pointer hover:shadow-md hover:shadow-alternative hover:text-shadow-lg/30 hover:text-shadow-alternative"
              >
                {i.name}
              </a>
            ))}
      </div>
    </>
  )
}
