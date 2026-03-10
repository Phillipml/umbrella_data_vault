import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { CharacterData, CharacterListed } from '../types/types'

export const apiSlice = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({ baseUrl: `${process.env.NEXT_PUBLIC_API_BASE}` }),
  endpoints: (builder) => ({
    getCharactersList: builder.query<CharacterListed[], void>({
      query: () => '/characters-list'
    }),
    getCharacterData: builder.query<CharacterData, null | string>({
      query: (name) => `/character-bio/${name}`
    })
  })
})

export const { useGetCharactersListQuery, useGetCharacterDataQuery } = apiSlice
