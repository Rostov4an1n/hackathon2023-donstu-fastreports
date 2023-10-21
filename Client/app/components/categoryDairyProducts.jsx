import Link from 'next/link'

export default function CategoryDairyProducts() {
    return (
        <div className='categories flex items-center space-x-[20px] w-max h-full'>
            <div className='p-[3px] w-[12px] h-full bg-[#D9D9D9] rounded-[6px]'>
                <div className='w-full h-full bg-white rounded-[3px]'></div>
            </div>
            <h1 className='button-text-1 whitespace-nowrap'>Молочная продукция</h1>
            <div className='w-[6px] h-[34px] bg-[#D9D9D9] rounded-[3px]'></div>
            <button className='button-text-1'>Молоко</button>
            <button className='button-text-1'>Сыр</button>
            <button className='button-text-1'>Творог</button>
            <button className='button-text-1'>Йогурты</button>
            <button className='button-text-1'>Сырки</button>
        </div>
    )
}