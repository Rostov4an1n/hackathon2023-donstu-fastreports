import {
    Chart as ChartJS, // Импортируем необходимые компоненты и модули из библиотеки Chart.js
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Filler,
    ArcElement,
    borderWidth,
    Segment,
} from 'chart.js';

ChartJS.register(
    ArcElement,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Filler
);

export const options2 = {
    responsive: true,
    plugins: {
        legend: {
            display: true,
            position: 'right',
        },
    },
    cutout: '65%', // Устанавливаем вырез в центре диаграммы
};


const labels = ['Продажа', 'Закупка'];

export const data2 = {
    labels,
    datasets: [{
        data: [110, 70], // Ваши данные здесь
        backgroundColor: [
            '#17C969FF',
            '#FF5050FF',
        ],
        borderRadius: 50,
    }, ],
};