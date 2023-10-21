'use client';
import React from 'react';
import { Bar, Line } from 'react-chartjs-2';
import { optionsBar, dataBar } from './components/chartSales';
import { optionsLine, dataLine } from './components/chartLine';

export default function Home() {
  return (
    <main className="h-screen w-screen flex justify-center bg-[#EEF1F8FF]">
      <div className='w-[80%] h-screen mx-26 my-16 '>
        <div className='w-1/3 h-[200px] flex justify-center items-center'>
          <Line options={optionsLine} data={dataLine}/>
        </div>
      </div>
    </main>
  );
}
