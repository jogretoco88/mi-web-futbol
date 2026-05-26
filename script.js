fetch('data.json')
    .then(response => response.json())
    .then(data => {
        const contenedor = document.getElementById('resultados');
        contenedor.innerHTML = ''; // Limpiamos errores previos
        
        // Verificamos si hay partidos en la lista
        if (data.response && data.response.length > 0) {
            data.response.forEach(partido => {
                const div = document.createElement('div');
                div.className = 'partido-card';
                div.innerHTML = `
                    <span class="equipo">${partido.teams.home.name}</span>
                    <span class="marcador">${partido.goals.home} - ${partido.goals.away}</span>
                    <span class="equipo">${partido.teams.away.name}</span>
                `;
                contenedor.appendChild(div);
            });
        } else {
            contenedor.innerHTML = '<p>No hay partidos en vivo en este momento.</p>';
        }
    })
    .catch(error => {
        console.error("Error al cargar datos:", error);
    });
