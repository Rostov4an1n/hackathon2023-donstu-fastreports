import Link from 'next/link'
import CategoryDairyProducts from './categoryDairyProducts'
import { BsClock, BsPersonCircle } from 'react-icons/bs'

export default function NavPanel() {
    return (
        <nav className="flex justify-center items-center w-full h-[100px]">
            <div className='flex flex-row space-x-[20px] w-auto h-auto'>
                <Link href="/reglog">
                    <div className='shadow-1 flex justify-center items-center w-[60px] h-[60px] bg-white rounded-[30px] cursor-pointer hover:bg-[#F4F4F4] duration-300'>
                        <BsPersonCircle size={44}/>
                    </div>
                </Link>
                <div className='shadow-1 flex items-center px-[40px] w-[1400px] h-[60px] rounded-[30px] bg-white'>
                    <div className='flex w-full h-[40px] overflow-hidden'>
                        <div className='swiper-x-categories flex flex-row space-x-[20px] w-max h-full'>
                            <CategoryDairyProducts/>
                        </div>
                    </div>
                </div>
                <div className='shadow-1 flex justify-center items-center w-[60px] h-[60px] bg-white rounded-[30px] cursor-pointer hover:bg-[#F4F4F4] duration-300'>
                    <BsClock size={44}/>
                </div>
            </div>
        </nav>
    )
}
