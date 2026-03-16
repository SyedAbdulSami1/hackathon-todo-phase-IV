/** @type {import('next').NextConfig} */
const nextConfig = {
    distDir: '../.next',
    images: {
        domains: ['api.dicebear.com', 'yt3.googleusercontent.com'],
    },
    trailingSlash: false,
    eslint: {
        ignoreDuringBuilds: true,
    },
    typescript: {
        ignoreBuildErrors: true,
    },
}

module.exports = nextConfig