fetch('data.json')
    .then(response => response.json())
    .then(data => {
        const contenedor = document.getElementById('resultados');
        // Esto imprime el JSON completo en la pantalla para que veamos cómo se llama cada cosa
        contenedor.innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
        console.log(data); // También lo puedes ver en la consola (F12)
    })
    .catch(error => {
        document.getElementById('resultados').innerHTML = "Error al leer data.json: " + error;
    });
