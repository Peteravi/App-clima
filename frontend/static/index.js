// Manejo del formulario para obtener el clima
document.getElementById('weatherForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar el envío del formulario

    // Obtener el valor del campo de entrada de la ciudad
    var city = document.getElementById('cityInput').value;

    // Realizar una solicitud AJAX al servidor para obtener el clima
    fetch('/weather?city=' + city)
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            // Manejar la respuesta del servidor y mostrarla en la página
            if (data.error) {
                // Si hay un error, mostrar el mensaje de error
                document.getElementById('weatherInfo').innerHTML = '<div class="alert alert-danger" role="alert">' + data.error + '</div>';
            } else {
                // Si se obtienen datos exitosamente, mostrar la información del clima
                var weatherInfo = 'Clima en ' + city + ': ' + data.main.temp + '°C';
                document.getElementById('weatherInfo').innerHTML = '<div class="alert alert-success" role="alert">' + weatherInfo + '</div>';
            }
        })
        .catch(function(error) {
            // Manejar cualquier error que ocurra durante la solicitud
            console.error('Error:', error);
            document.getElementById('weatherInfo').innerHTML = '<div class="alert alert-danger" role="alert">Error al obtener el clima</div>';
        });
});
