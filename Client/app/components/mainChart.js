import {
    Chart as ChartJS,
    LinearScale,
    CategoryScale,
    BarElement,
    PointElement,
    LineElement,
    Tooltip,
} from 'chart.js';

ChartJS.register(
    LinearScale,
    CategoryScale,
    BarElement,
    PointElement,
    LineElement,
    Tooltip
);

export const options4 = {
    scales: {
        x: {
            beginAtZero: true,
            display: false, // Отображать ось
            position: 'none', // Не показывать значения оси
        },
    },
}

const labels = ['Янв', 'Фев', 'Март', 'Май', 'Июнь', 'Июль', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'];

export const data4 = {
    labels,
    datasets: [{
            type: 'line',
            borderColor: '#FF5050FF',
            borderWidth: 2,
            fill: true,
            data: [25, 40, 12, 80, 60, 95, 10, 50, 70, 90, 35, 5],
        },
        {
            type: 'bar',
            backgroundColor: '#8E34FFFF',
            data: [70, 85, 60, 98, 75, 90, 40, 80, 95, 99, 45, 20],
            borderColor: 'white',
            borderWidth: 2,
        },
        {
            type: 'bar',
            backgroundColor: '#17C969FF',
            data: [30, 45, 20, 80, 60, 95, 10, 50, 70, 90, 25, 5],
        },
    ],
};