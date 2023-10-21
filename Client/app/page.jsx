'use client';

import React from 'react';
import { Line } from 'react-chartjs-2';
import { optionsLine, dataLine } from './components/chartLine';

export default function Home() {
  return (
    <main className='flex flex-col h-screen w-screen items-center'>
      <div id='topContainer' className='flex flex-row h-[200px] w-[1540px] mt-[69px] gap-x-[30px]'>
        <div className='w-[430px] h-[200px] bg-white shadow-md rounded-[27px]'>

        </div>
        <div className='w-[620px] h-[200px] bg-white shadow-md rounded-[27px]'>

        </div>
        <div className='w-[430px] h-[200px] bg-white shadow-md rounded-[27px]'>

        </div>
      </div>

      <div id='middleContainer' className='flex flex-row h-[300px] w-[1540px] my-[30px] gap-x-[30px]'>
        <div className='w-[755px] h-[300px]'>
          <div className='w-auto h-auto pt-8 pb-[20px] rounded-[27px] bg-white shadow-md'>
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


        <div className='w-[755px] h-[300px]'>
          <div className='w-auto h-auto pt-8 pb-[20px] rounded-[27px] bg-white shadow-md'>
            <h4 className='font-bold text-[20px] ml-6'>Стоимость закупки/реализации</h4>
            <div className='flex items-center ml-6'>
              <div className="flex items-center ml-1">
                <div className="w-2 h-2 bg-[#FF6666FF] rounded-[50%] mr-2"></div>
                <p className='text-[#989898] text-[12px]'>Закупка</p>
              </div>
              <div className="flex items-center ml-6">
                <div className="w-2 h-2 bg-[#42BD53FF] rounded-[50%] mr-2"></div>
                <p className='text-[#989898] text-[12px]'>Реализации</p>
              </div>
            </div>
            <div className='w-full h-[210px] ml-10'>
              <Line options={optionsLine} data={dataLine}/>
            </div>
          </div>
        </div>
      </div>
      <div id='bottomContainer' className='flex flex-row h-[280px] w-[1540px] bg-red-600 '>

      </div>
    </main>
  );
}
