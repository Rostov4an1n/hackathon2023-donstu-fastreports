import { BsClock } from 'react-icons/bs';
import Link from 'next/link';

export default function NavPanel() {
    return (
        <nav className="flex flex-row justify-center items-center w-full h-[100px]">
            <div className='w-[1480px] h-[60px] bg-red-500 flex flex-row justify-start items-start gap-x-[20px]'>
                <div className='w-[1400px] h-[60px] bg-blue-500 flex flex-row rounded-[30px] items-center'>
                    <div className='h-auto w-auto pr-[40px] flex flex-row'>
                        <button className='ml-[90px] h-[40px] w-[310px] bg-green-500'>Молочная продукция</button>
                    </div>
                    <div className='h-[40px] w-[6px] bg-[#EEF1F8] rounded-[3px] space-x-[40px]'></div>
                    <div className='h-auto w-auto pl-[40px] pr-[70px] flex flex-row'>
                        <button className='h-[40px] w-[115px] bg-green-500'>Молоко</button>
                    </div>
                    <div className='h-auto w-auto gap-x-[70px] flex flex-row'>
                        <button className='h-[40px] w-[70px] bg-green-500'>Сыр</button>
                        <button className='h-[40px] w-[115px] bg-green-500'>Творог</button>
                        <button className='h-[40px] w-[135px] bg-green-500'>Йогурты</button>
                        <button className='h-[40px] w-[110px] bg-green-500'>Сырки</button>
                        <Link href='/regPage'>
                            <button className='h-[40px] w-[110px] bg-green-500'>Регистрация</button>
                        </Link>
                    </div>
                </div>
                <div className='w-[60px] h-[60px] bg-blue-500 rounded-full items-center flex justify-center'>
                    <BsClock size={44} className='fill-black'/>
                </div>
            </div>
        </nav>
    )
}
