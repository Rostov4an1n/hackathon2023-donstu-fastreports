'use client';

import React from 'react'; // Make sure to import React
import { Bar } from 'react-chartjs-2';
import { options, data } from './components/chartSales';

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className='w-[588px] h-[304px] flex justify-center items-center'>
        <Bar options={options} data={data} />
      </div>
      <div className='w-[588px] h-[304px] flex justify-center items-center'>
        <Bar options={options} data={data} />
      </div>
    </main>
  );
}
