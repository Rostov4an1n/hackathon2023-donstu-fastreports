import { Inter } from 'next/font/google'
import './globals.css'
import { ReactQueryProvider } from './reactQueruProvider'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Fast Reports',
  description: 'Hackathon app for Fast Reports',
}

export default function RootLayout({ children }) {
  return (
    <ReactQueryProvider>
      <html lang="en">
        <body className={inter.className}>
          {children}
        </body>
      </html>
    </ReactQueryProvider>
  )
}
