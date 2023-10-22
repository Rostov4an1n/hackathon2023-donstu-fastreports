'use client';

import { Inter } from 'next/font/google';
import './globals.css';
import { ReactQueryProvider } from './reactQueruProvider';
import NavPanel from './components/navPanel';
import { usePathname } from 'next/navigation';
import { metadata } from './metadata';

const inter = Inter({ subsets: ['latin'] });

export default function RootLayout({ children }) {
  const currentPage = usePathname();

  return (
    <ReactQueryProvider>
      <html lang="en">
      <title>{metadata.title}</title>
      <meta name="description" content={metadata.description} />
        <body className={inter.className}>
          {currentPage === '/' && <NavPanel />}
          {children}
        </body>
      </html>
    </ReactQueryProvider>
  );
}