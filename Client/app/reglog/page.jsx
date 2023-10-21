import Link from 'next/link';

export default function reglog() {
  return (
    <div className='flex justify-center items-center w-full h-screen'>
        <div className='container-box-reg'>
            <div className='text-[40px] text-[#333333] flex justify-center items-center w-auto h-[50px] mt-[50px]'>Создай аккаунт</div>
            <div className='flex justify-center items-center w-[380px] h-[60px] mt-[60px] rounded-[15px] bg-[#F4F4F4]'>
                <input id="email" className='text-[20px] text-[#333333] text-center w-[350px] h-[30px] bg-transparent' type="text" placeholder="Enter your email"/>
            </div>
            <div className='flex justify-center items-center w-[380px] h-[60px] mt-[20px] rounded-[15px] bg-[#F4F4F4]'>
                <input id="password" className='text-[20px] text-[#333333] text-center w-[350px] h-[30px] bg-transparent' type="text" placeholder="Enter your password"/>
            </div>
            <Link href="/home">
                <button className='submit'>Начнем</button>
            </Link>
        </div>
    </div>    
  );
}