fetch('data.json')
    .then(response => response.json())
    .then(data => {
        const contenedor = document.getElementById('resultados');
        contenedor.innerHTML = ''; // Limpiamos "Cargando..."

        // Suponiendo que la API devuelve los partidos en data.response
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
    });
