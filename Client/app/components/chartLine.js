import {
    Chart as ChartJS, // Импортируем необходимые компоненты и модули из библиотеки Chart.js
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Filler
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Filler);
// Регистрируем необходимые компоненты в Chart.js

export const optionsLine = { // Настройки для графика Line Chart
    responsive: true, // График будет адаптивным к размеру контейнера
    interaction: {
        mode: 'index', // Режим взаимодействия при наведении
        intersect: false, // Необходимо, чтобы подсветка не пересекалась
    },
    stacked: false, // График не будет складываться (не применимо к Line Chart)
    plugins: {
        legend: { // отображение маркеров
            display: false, // Не отображать заголовок
            text: 'Граффик доходов/расходов', // Заголовок графика
        },
    },
    scales: { // Настройки осей
        y: {
            type: 'linear', // Тип оси - линейная
            display: true, // Отображать ось
            position: 'none', // Не показывать значения оси
            grid: {
                borderDash: [3, 3],
            }
        },
        x: {
            type: 'category', // Предполагая, что это категориальная ось x
            display: true,
            grid: {
                drawOnChartArea: false, // Не рисовать сетку на графике
            },
        },
        y1: {
            type: 'linear', // Тип оси - линейная
            display: true, // Отображать ось
            position: 'none', // Не показывать значения оси
            grid: {
                drawOnChartArea: false, // Не рисовать сетку на графике
            },
        },
    },
    elements: {
        line: {
            tension: 0.5, // Натяжение линии графика (плавность)
        },
    },
};