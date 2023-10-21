'use client';

import React from 'react';
import { Line } from 'react-chartjs-2';
import { optionsLine, dataLine } from './components/chartLine';

export default function Home() {
  return (
    <main className='flex flex-col h-screen w-full items-center'>
      <div id='topContainer' className='flex flex-row h-[200px] w-[1540px] bg-red-600 mt-[69px] gap-x-[30px]'>
        <div className='w-[430px] h-[200px] bg-blue-500'>

        </div>
        <div className='w-[620px] h-[200px] bg-blue-500'>

        </div>
        <div className='w-[430px] h-[200px] bg-blue-500'>

        </div>
      </div>

      <div id='middleContainer' className='flex flex-row h-[300px] w-[1540px] bg-red-600 my-[30px] gap-x-[30px]'>
        <div className='w-[755px] h-[300px] bg-blue-500'>

        </div>
        <div className='w-[755px] h-[300px] bg-blue-500'>

        </div>
      </div>
      <div id='bottomContainer' className='flex flex-row h-[280px] w-[1540px] bg-red-600 my-[30px]'>

      </div>
    </main>
  );
}
