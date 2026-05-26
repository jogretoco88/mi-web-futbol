fetch('data.json')
    .then(response => response.json())
    .then(data => {
        const contenedor = document.getElementById('resultados');
        contenedor.innerHTML = '<h2>Partidos de hoy</h2>';
        
        if (data.response && data.response.length > 0) {
            data.response.forEach(p => {
                const div = document.createElement('div');
                div.className = 'partido-card';
                
                // Determinamos el estado del partido
                let estado = p.fixture.status.short; // FT, LIVE, NS
                let marcador = `${p.goals.home || 0} - ${p.goals.away || 0}`;
                if (estado === 'NS') marcador = 'vs';

                div.innerHTML = `
                    <div class="liga">${p.league.name}</div>
                    <div class="equipos">
                        ${p.teams.home.name} <strong>${marcador}</strong> ${p.teams.away.name}
                    </div>
                    <div class="estado">Estado: ${p.fixture.status.long}</div>
                `;
                contenedor.appendChild(div);
            });
        } else {
            contenedor.innerHTML = '<p>No hay partidos registrados para hoy.</p>';
        }
    });
