import { Inter } from 'next/font/google'
import './globals.css'
import NavPanel from './components/navPanel'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Fast Reports',
  description: 'Hackathon app',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <NavPanel />
        {children}
      </body>
    </html>
  )
}
