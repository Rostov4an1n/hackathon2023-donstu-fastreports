import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

export const optionsLine = {
    responsive: true,
    interaction: {
        mode: 'index',
        intersect: false,
    },
    stacked: false,
    plugins: {
        title: {
            display: false,
            text: 'Chart.js Line Chart - Multi Axis',
        },
    },
    scales: {
        y: {
            type: 'linear',
            display: true,
            position: 'none',
        },
        y1: {
            type: 'linear',
            display: true,
            position: 'none',
            grid: {
                drawOnChartArea: false,
            },
        },
    },
    elements: {
        line: {
            fill: true,
            backgroundColor: 'rgba(255, 0, 0, 0.5)',
            tension: 0.4,
        },
    },
};

const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];

const datalabels = [20, 18, 16, 13, 10, 9, 12, 3, 1];
const datalabels2 = [23, 21, 19, 16, 13, 12, 15, 6, 4];

export const dataLine = {
    labels,
    datasets: [{
            label: 'Dataset 1',
            data: datalabels,
            borderColor: '#40BE53FF',
            backgroundColor: 'rgba(64, 190, 83, 0.5)',
            yAxisID: 'y',
        },
        {
            label: 'Dataset 2',
            data: datalabels2,
            borderColor: 'rgb(53, 162, 235)',
            backgroundColor: 'rgba(53, 162, 235, 0.5)',
            yAxisID: 'y1',
        },
    ],
};