'use client';

import { useState } from "react";
import { useMutation } from 'react-query';
import { useRouter } from "next/navigation";


export default function RegPage() {
    const mutation = useMutation((formData) => {
        return axios.post('http://testsite', formData);
    });

    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
    });

    const router = useRouter();

    const handleFormSubmit = async (e) => {
        
        e.preventDefault();
        mutation.mutate(formData);

        // Если авторизация успешна, перенаправляем пользователя на главную страницу
        if (mutation.isSuccess) {
            router.push('/'); // Перенаправление на главную страницу
        }
    };

    return(
        <main className='flex flex-col h-screen w-screen items-center justify-center'>
            <div className='w-[700px] h-[700px] bg-white rounded-[30px] shadow-md justify-center items-center flex flex-col'>
                <h1 className="font-bold text-[50px]">
                    Авторизация
                </h1>
                <form onSubmit={handleFormSubmit} className="mt-[60px]">
                    <div className="mb-5 flex justify-center items-center flex-col">
                        <label className="block text-[30px] font-semibold" htmlFor="username">
                        Имя пользователя:
                        </label>
                        <input
                        id="username"
                        className='username-input border-2 border-[#EEF1F8] p-4 rounded-[30px]'
                        type="text"
                        placeholder="Введите имя пользователя"
                        value={formData.username}
                        onChange={(e) => setFormData({ ...formData, username: e.target.value })}
                        />
                    </div>
                    <div className="mb-5 flex justify-center items-center flex-col">
                        <label className="block text-[30px] font-semibold" htmlFor="username">
                        Email:
                        </label>
                        <input
                        id="email"
                        className='email-input border-2 border-[#EEF1F8] p-4 rounded-[30px]'
                        type="text"
                        placeholder="Введите email"
                        value={formData.email}
                        onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                        />
                    </div>
                    <div className="mb-5 flex justify-center items-center flex-col">
                        <label className="block text-[30px] font-semibold" htmlFor="password">
                        Пароль:
                        </label>
                        <input
                        id="password"
                        className='password-input border-2 border-[#EEF1F8] p-4 rounded-[30px]'
                        type="password"
                        placeholder="Введите пароль"
                        value={formData.password}
                        onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                        />
                    </div>
                    <button
                        type="submit"
                        className="w-full bg-[#aba0f8] text-white font-semibold rounded-[30px] py-2"
                    >
                        Войти
                    </button>
                </form>
            </div>
        </main>
    )
}