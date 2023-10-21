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
    Math
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

export const options = {
    responsive: true,
    plugins: {
        legend: {
            display: true,
            position: 'right',
        },
    },
    cutout: '65%', // Устанавливаем вырез в центре диаграммы
};




export const data = {

    labels: ['Реализовано', 'Закуплено'],
    datasets: [{
        data: [30, 50], // Ваши данные здесь
        backgroundColor: [
            '#17C969FF',
            '#FF5050FF',
        ],
        borderRadius: 50,
    }, ],

};