'use client';

import React from 'react'; // Make sure to import React
import { Bar, Line } from 'react-chartjs-2';
import { optionsBar, dataBar } from './components/chartSales';
import { optionsLine, dataLine } from './components/chartLine';

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className='w-[588px] h-[304px] flex justify-center items-center'>
        <Bar options={optionsBar} data={dataBar} />
      </div>
      <div className='w-[588px] h-[304px] flex justify-center items-center'>
        <Line options={optionsLine} data={dataLine} />
      </div>
    </main>
  );
}
