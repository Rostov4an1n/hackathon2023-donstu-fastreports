import { BsClock, BsPersonAdd } from 'react-icons/bs';
import Link from 'next/link';

export default function NavPanel() {
    return (
        <nav className="flex flex-row justify-center items-center w-full h-[70px]">
            <div className='w-[1480px] h-[40px] flex flex-row justify-start items-start gap-x-[20px]'>
                <Link href='/regPage'>
                    <button className='w-[60px] h-[60px] items-center flex justify-center'>
                        <BsPersonAdd size={40} className='fill-black'/>
                    </button>
                </Link>
                <div className='w-[1400px] h-[60px] bg-white shadow-md flex flex-row rounded-[30px] items-center'>
                    <div className='h-auto w-auto pr-[40px] flex flex-row'>
                        <button className='ml-[90px] h-[40px] w-[310px] rounded-[27px] font-bold text-[18px] hover:shadow-md hover:shadow-[#efdfff] transition-all duration-300'>Молочная продукция</button>
                    </div>
                    <div className='h-[40px] w-[6px] bg-[#a8a8a8] rounded-[3px] space-x-[40px]'></div>
                    <div className='h-auto w-auto pl-[40px] pr-[70px] flex flex-row'>
                        <button className='h-[40px] w-[115px] rounded-[27px] font-bold text-[18px] hover:shadow-md hover:shadow-[#efdfff] transition-all duration-300'>Молоко</button>
                    </div>
                    <div className='h-auto w-auto gap-x-[70px] flex flex-row mr-[90px]'>
                        <button className='h-[40px] w-[70px] rounded-[27px] font-bold text-[18px] hover:shadow-md hover:shadow-[#efdfff] transition-all duration-300'>Сыр</button>
                        <button className='h-[40px] w-[115px] rounded-[27px] font-bold text-[18px] hover:shadow-md hover:shadow-[#efdfff] transition-all duration-300'>Творог</button>
                        <button className='h-[40px] w-[135px] rounded-[27px] font-bold text-[18px] hover:shadow-md hover:shadow-[#efdfff] transition-all duration-300'>Йогурты</button>
                        <button className='h-[40px] w-[110px] rounded-[27px] font-bold text-[18px] hover:shadow-md hover:shadow-[#efdfff] transition-all duration-300'>Сырки</button>
                    </div>
                </div>
                <select id="countries" className="bg-gray-50 shadow-md text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-[300px] p-2.5 my-[10px]">
                    <option>Последний месяц</option>
                    <option>Последние 6 месяцев</option>
                    <option>Последний год</option>
                </select>
            </div>
        </nav>
    )
}
