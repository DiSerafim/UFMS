document.getElementById('formulario-cadastro').addEventListener('submit', function(e) {
    e.preventDefault();

    const dados = new FormData(e.target);
    const result = {};

    dados.forEach((value, key) => { 
        if (result[key]) {
            if (!Array.isArray(result[key])) {
                result[key] = [result[key]];
            }
            result[key].push(value);
        } else {
            result[key] = value;
        }
    });

    for (const [key, value] of Object.entries(result)) {
        if (Array.isArray(value)) {
            `<p>${key}: <b>${value.join(', ')}</b></p>`;
        } else {
            `<p>${key}: <b>${value}</b></p>`;
        }
    }

    const mostraResultado = window.open('', '_blank');

    mostraResultado.document.write('<html><head><title>Resultado aqui!</title></head></html>');

    mostraResultado.document.close();
});