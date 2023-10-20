import Link from 'next/link'

export default function NavPanel() {
    return (
        <nav className="flex flex-row justify-center items-center w-full h-[70px] bg-slate-300">
            <div className='flex flex-row items-center space-x-[20px] w-auto h-auto'>
                <Link href='/'>
                    <button className='bg-purple-700 rounded-md p-3'>Main Page</button>
                </Link>
                <Link href='/TestPage'>
                    <button className='bg-purple-700 rounded-md p-3'>Test Page</button>
                </Link>
            </div>
        </nav>
    )
}
