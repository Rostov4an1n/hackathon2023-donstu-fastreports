'use client';
import React from 'react';
import { Bar, Line } from 'react-chartjs-2';
import { optionsLine, dataLine } from './components/chartLine';

export default function Home() {
  return (
    <main className="h-screen w-screen flex justify-center bg-[#EEF1F8FF]">
      <div className='w-[80%] h-screen mx-26 my-16 '>
        <div className='w-[550px] h-[320px] pt-8 pb-[20px] rounded-[27px] bg-white shadow-md'>
          <h4 className='font-bold text-[20px] ml-6'>Сводка закупок/реализации</h4>
          <div className='flex items-center ml-6'>
            <div className="flex items-center ml-1">
              <div className="w-2 h-2 bg-[#FF6666FF] rounded-[50%] mr-2"></div>
              <p className='text-[#989898] text-[12px]'>Закуплено</p>
            </div>
            <div className="flex items-center ml-6">
              <div className="w-2 h-2 bg-[#42BD53FF] rounded-[50%] mr-2"></div>
              <p className='text-[#989898] text-[12px]'>Реализовано</p>
            </div>
          </div>
          <div className='w-full h-[210px] ml-10'>
            <Line options={optionsLine} data={dataLine}/>
          </div>
        </div>
      </div>
    </main>
  );
}
