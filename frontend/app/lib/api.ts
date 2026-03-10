import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export const apiSlice = createApi({
    reducerPath: 'api',
    baseQuery: fetchBaseQuery({ baseUrl: `${process.env.NEXT_PUBLIC_API_BASE}`}),
    endpoints: (builder) => ({
        getData: builder.query({
            query: () => '/data',
        })
    })
})

export const { useGetDataQuery } = apiSlice;