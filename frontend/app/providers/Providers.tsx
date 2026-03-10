'use client'
import { ApiProvider } from '@reduxjs/toolkit/query/react'
import { ReactNode } from 'react'
import { apiSlice } from '../lib/api'

export function Providers({ children }: { children: ReactNode }) {
  return <ApiProvider api={apiSlice}>{children}</ApiProvider>
}
