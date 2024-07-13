 // Función para obtener la hora actual
 function getCurrentTime() {
    const now = new Date();
    const day = now.toLocaleDateString('en-US', { weekday: 'long' });
    const date = now.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });
    const time = now.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit' });
    return `${day}, ${date}, ${time}`;
}

// Función para actualizar la hora actual cada segundo
function updateTime() {
    const currentTimeElement = document.getElementById('current-time');
    if (currentTimeElement) {
        currentTimeElement.textContent = getCurrentTime();
    }
}

// Llamar a la función updateTime inicialmente
updateTime();

// Actualizar la hora cada segundo
setInterval(updateTime, 1000);



// Función para generar una fecha aleatoria dentro del rango especificado para una noticia específica
function generateRandomDate(newsId) {
    // Verificamos si ya existe una fecha almacenada en el localStorage para esta noticia
    var storedDate = localStorage.getItem('randomDate_' + newsId);
    if (storedDate) {
        return storedDate;
    }

    // Obtenemos la fecha actual
    var currentDate = new Date();

    // Definimos el rango de años para la fecha aleatoria (hasta 4 años atrás)
    var minYear = currentDate.getFullYear() - 4;
    var maxYear = currentDate.getFullYear();

    // Generamos un año aleatorio dentro del rango especificado
    var randomYear = Math.floor(Math.random() * (maxYear - minYear + 1)) + minYear;

    // Generamos una fecha aleatoria dentro del año aleatorio
    var randomDate = new Date(
        randomYear,
        Math.floor(Math.random() * 12), // Mes aleatorio
        Math.floor(Math.random() * 28) + 1 // Día aleatorio (del 1 al 28 para simplificar)
    );

    // Formateamos la fecha aleatoria en el formato deseado (Ene 01, 2045)
    var months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'];
    var formattedDate = months[randomDate.getMonth()] + ' ' + randomDate.getDate() + ', ' + randomDate.getFullYear();

    // Almacenamos la fecha aleatoria en el localStorage para esta noticia
    localStorage.setItem('randomDate_' + newsId, formattedDate);

    return formattedDate;
}

// Mostramos la fecha aleatoria para cada noticia
var randomDateElements = document.querySelectorAll('.random-date');
randomDateElements.forEach(function(element) {
    var newsId = element.getAttribute('data-news-id');
    element.textContent = generateRandomDate(newsId);
});