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

const labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']; // Метки для оси x

const datalabels = [20, 18, 16, 13, 10, 9, 12, 3, 1, 20, 18, 16]; // Данные для Dataset 1
const datalabels2 = [29, 27, 25, 22, 19, 18, 21, 22, 1, 29, 27, 25]; // Данные для Dataset 2

export const dataLine = {
    labels, // Подставляем метки для оси x
    datasets: [{
            label: false, // Название Dataset 1
            data: datalabels, // Данные для Dataset 1
            backgroundColor: '#FF6666FF', // Цвет заливки графика (красный)
            borderColor: "#FF6666FF", // Цвет границы графика (красный)
            yAxisID: 'y', // Использовать ось y
            fill: {
                target: 'origin', // Заполнить область под графиком
                above: '#FF666644', // Цвет заливки выше графика (красный с прозрачностью)
                below: '#F9000000', // Цвет заливки ниже графика (красный с прозрачностью)
            },
            borderDashOffset: 3,
        },
        {
            label: false, // Название Dataset 2
            data: datalabels2, // Данные для Dataset 2
            backgroundColor: '#42BD53FF', // Цвет заливки графика (зеленый)
            borderColor: "#42BD53FF", // Цвет границы графика (зеленый)
            yAxisID: 'y1', // Использовать ось y1
            fill: {
                target: 'origin', // Заполнить область под графиком
                above: '#42BD533D', // Цвет заливки выше графика (зеленый с прозрачностью)
                below: '#F9000000' // Цвет заливки ниже графика (красный с прозрачностью)
            }
        },
    ],
}