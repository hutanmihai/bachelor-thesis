/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [{ hostname: 'https://thesis-s3.s3.amazonaws.com/', pathname: '*' }],
  },
}

export default nextConfig
