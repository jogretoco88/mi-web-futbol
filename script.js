fetch('data.json')
    .then(response => response.json())
    .then(data => {
        const contenedor = document.getElementById('resultados');
        contenedor.innerHTML = JSON.stringify(data, null, 2); // Esto mostrará los datos crudos para empezar
    });
