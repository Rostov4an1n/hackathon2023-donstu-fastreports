'use client';

import React from 'react';
import Link from 'next/link';
import { useQuery } from 'react-query';

export default function RegPage() {
    const { isLoading, error, data } = useQuery(
        'repoData',
        () =>
          fetch(
            'https://api.github.com/repos/tannerlinsley/react-query'
          ).then((response) => response.json())
    );
    
    if (isLoading) return <p>Загрузка...</p>;
    
    if (error) return <p>Ошибка: {error.message}</p>;

  return (
    <main className='flex flex-col h-screen w-full items-center justify-center'>
      <div className='flex flex-col h-auto p-4 w-[500px] bg-red-600 my-[69px] items-center justify-center gap-y-10'>
        <div className='w-auto h-auto bg-green-500 p-3'>
            <input id="email" className='email-input' type="text" placeholder="Enter your email" />
        </div>
        <div className='w-auto h-auto bg-green-500 p-3'>
            <input id="password" className='password-input' type="text" placeholder="Enter your password" />
        </div>
        <Link href='/'>
            <button className='w-40 h-5 rounded-md bg-green-500 p-5 flex items-center justify-center'>Register</button>
        </Link>
      </div>

      <div>
        <h1>{data.name}</h1>
        <p>{data.description}</p>
        <strong>👀 {data.subscribers_count}</strong>{' '}
        <strong>✨ {data.stargazers_count}</strong>{' '}
        <strong>🍴 {data.forks_count}</strong>
    </div>
    </main>
  );
}
