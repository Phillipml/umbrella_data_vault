import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'www.residentevildatabase.com'
      }
    ]
  }
}

export default nextConfig
