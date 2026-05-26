fetch('data.json')
    .then(response => response.json())
    .then(data => {
        const contenedor = document.getElementById('resultados');
        contenedor.innerHTML = '<h2>Partidos de hoy</h2>';
        
        if (data.response && data.response.length > 0) {
            data.response.forEach(p => {
                const div = document.createElement('div');
                div.className = 'partido-card';
                div.innerHTML = `
                    <p>${p.league.name}</p>
                    <strong>${p.teams.home.name} ${p.goals.home || 0} - ${p.goals.away || 0} ${p.teams.away.name}</strong>
                    <small>Estado: ${p.fixture.status.short}</small>
                `;
                contenedor.appendChild(div);
            });
        } else {
            contenedor.innerHTML = '<p>No hay partidos programados para hoy.</p>';
        }
    });
