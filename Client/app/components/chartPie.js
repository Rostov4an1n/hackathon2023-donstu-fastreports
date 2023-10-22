import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Filler,
    ArcElement,
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
    cutout: '65%',
};

export const labels = ['Реализовано', 'Закуплено']; // Экспортируем labels

export const data = {
    labels: labels,
    datasets: [{
        data: [323, 417],
        backgroundColor: [
            '#17C969FF',
            '#FF5050FF',
        ],
        borderRadius: 50,
    }],
};

export const dataValues = data.datasets[0].data; // Экспортируем значения из data