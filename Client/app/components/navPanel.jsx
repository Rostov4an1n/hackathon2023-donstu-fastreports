import { BsClock } from 'react-icons/bs';

export default function NavPanel() {
    return (
        <nav className="flex flex-row justify-center items-center w-full h-[70px]">
            <div className='w-[1480px] h-[40px] flex flex-row justify-start items-start gap-x-[20px]'>
                <div className='w-[1400px] h-[60px] bg-white shadow-md flex flex-row rounded-[30px] items-center'>
                    <div className='h-auto w-auto pr-[40px] flex flex-row'>
                        <button className='ml-[90px] h-[40px] w-[310px] rounded-[27px] font-bold text-[14px]'>Молочная продукция</button>
                    </div>
                    <div className='h-[40px] w-[6px] bg-[#a8a8a8] rounded-[3px] space-x-[40px]'></div>
                    <div className='h-auto w-auto pl-[40px] pr-[70px] flex flex-row'>
                        <button className='h-[40px] w-[115px] rounded-[27px] font-bold text-[14px]'>Молоко</button>
                    </div>
                    <div className='h-auto w-auto gap-x-[70px] flex flex-row'>
                        <button className='h-[40px] w-[70px] rounded-[27px] font-bold text-[14px]'>Сыр</button>
                        <button className='h-[40px] w-[115px] rounded-[27px] font-bold text-[14px]'>Творог</button>
                        <button className='h-[40px] w-[135px] rounded-[27px] font-bold text-[14px]'>Йогурты</button>
                        <button className='h-[40px] w-[110px] rounded-[27px] font-bold text-[14px]'>Сырки</button>
                    </div>
                </div>
                <div className='w-[60px] h-[60px] items-center flex justify-center'>
                    <BsClock size={40} className='fill-black'/>
                </div>
            </div>
        </nav>
    )
}
