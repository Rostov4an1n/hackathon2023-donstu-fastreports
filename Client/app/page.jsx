'use client';
import React from 'react';
import Image from 'next/image';
import { Line, Doughnut } from 'react-chartjs-2';
import { optionsLine, dataLine } from './components/chartLine';
import { optionsLine2, dataLine2 } from './components/chartLine2'
import {data, options} from './components/chartPie';
import {data2, options2} from './components/ChartPie2';


export default function Home() {
  
  return (
    <main className='flex flex-col h-screen w-screen items-center'>
      <div id='topContainer' className='flex flex-row h-[200px] w-[1540px] mt-[69px] gap-x-[30px]'>
        <div className=' flex w-[430px] h-[200px] bg-white shadow-md rounded-[27px] items-center'>
          <div className='absolute ml-4 mb-[140px]'><h1 className='text-[18px] font-bold'>Кол-во</h1></div>
          <div className='flex items-center w-auto ml-3'>

            <div className='h-auto'>
              <div className="flex items-center ml-1">
                <div className="w-2 h-2 bg-[#FF6666FF] rounded-[50%] mr-2"></div>
                <p className='text-black font-bold text-[13px]'>Закуплено</p>
              </div>
              <div className='flex justify-center'>
                <h2 className='font-bold text-[26px]'>250</h2>
              </div>
            </div>

            <div className='h-auto'>
              <div className="flex items-center ml-6">
                <div className="w-2 h-2 bg-[#42BD53FF] rounded-[50%] mr-2"></div>
                <p className='text-black font-bold text-[13px]'>Реализовано</p>
              </div>
              <div className='flex justify-center ml-5'>
                <h2 className='font-bold text-[26px]'>250</h2>
              </div>
            </div>
          </div>
          
          <div className='w-[130px] h-[130px] ml-3'>
            <Doughnut data={data} options={options} />
          </div>

        </div>


        <div className='w-[620px] h-[200px] flex justify-center bg-white shadow-md rounded-[27px]'>
          <div className='w-full h-auto '>
            <div className='w-full h-auto flex mt-10 ml-[90px]'>
                
                {/* img */}
              <div className='w-[60px] h-[60px] rounded-[15px]'>
                <Image
                  src="/milk.png"
                  width={70}
                  height={70}
                />
              </div>

              {/* layer */}
              <div className='h-auto ml-[10px]'>
                <h1 className='font-semibold text-[18px]'>Молочная продукция</h1>
                <div className='w-full bg-black h-[1px] rounded-[10px]'></div>
                <h1 className='font-semibold text-[18px]'>Молоко</h1>
              </div>

            </div>
            <div className='mt-6'>
              <div className='flex'>
                <h1 className='font-bold text-[18px] ml-[59px]'>Спрос</h1>
                <h1 className='font-bold text-[18px] mr-8 ml-auto'>70%</h1>
              </div>
              <div className='flex justify-center mt-2'>
                <div className='bg-white shadow-md h-[10px] w-[80%] rounded-[10px]'>
                  <div className='bg-[#8E34FF] bar shadow-md h-full rounded-[10px]'></div>
                </div>
              </div>
            </div>

          </div>
        </div>

        <div className=' flex w-[430px] h-[200px] bg-white shadow-md rounded-[27px] items-center'>
        <div className='absolute ml-4 mb-[140px]'><h1 className='text-[18px] font-bold'>Цена</h1></div>
          <div className='flex items-center w-auto ml-3'>

            <div className='h-auto'>
              <div className="flex items-center ml-1">
                <div className="w-2 h-2 bg-[#FF6666FF] rounded-[50%] mr-2"></div>
                <p className='text-black font-bold text-[13px]'>Закупка</p>
              </div>
              <div className='flex justify-center'>
                <h2 className='font-bold text-[26px]'>250</h2>
              </div>
            </div>

            <div className='h-auto'>
              <div className="flex items-center ml-6">
                <div className="w-2 h-2 bg-[#42BD53FF] rounded-[50%] mr-2"></div>
                <p className='text-black font-bold text-[13px]'>Продажа</p>
              </div>
              <div className='flex justify-center ml-5'>
                <h2 className='font-bold text-[26px]'>250</h2>
              </div>
            </div>
          </div>
          
          <div className='w-[130px] h-[130px] ml-8'>
            <Doughnut data={data2} options={options2} />
          </div>

        </div>
      </div>

      <div id='middleContainer' className='flex flex-row h-[300px] w-[1540px] my-[30px] justify-center gap-x-[30px]'>
        <div className='w-auto h-[300px]'>

          <div className='w-auto h-auto pt-8 pb-[20px] rounded-[27px] bg-white px-[30px] shadow-md'>
            
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


        <div className='w-auto h-[300px]'>
          <div className='w-auto h-auto pt-8 pb-[20px] rounded-[27px] bg-white px-[30px] shadow-md'>
           
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
              <Line options={optionsLine2} data={dataLine2}/>
            </div>

          </div>
        </div>
      </div>
      <div id='bottomContainer' className='flex flex-row h-[280px] w-[1540px] '>

      </div>
    </main>
  );
}
