function confirmacion() {
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var telefono = document.getElementById("telefono").value;
    var email = document.getElementById("email").value;
    var comentario= document.getElementById("comentario").value;

    
    
    alert('Estos son los datos ingresados: '+ nombre + apellido + telefono + email+ comentario  );
}

var imagenes = [
    './static/images/santa-rosa-tastil.jpg',
    './static/images/seclanta.jpg', 
    './static/images/cachi3.jpg', 
    './static/images/campo_quijano.jpg'
];
var indice = 0;

function cambiarImagen() {
    var imagen = document.getElementById('imagenes-varias');
    indice++;
    if (indice >= imagenes.length) {
        indice = 0;
    }
    imagen.src = imagenes[indice];
}



function api(){ // Falta terminar!!!
    const fechaActual = new Date(); // Para obtener la hora, y buscar la temperatura segun la hora actual
    tempCont=document.querySelector('#temp_api')
    fetch('https://api.open-meteo.com/v1/forecast?latitude=-24.79&longitude=-65.41&hourly=temperature_2m')
    .then(res =>res.json())
    .then(data=>{
        const temperature = data.hourly.temperature_2m[0].value;
        document.getElementById('temp_api').textContent = temperature;
    })
}



fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales') 
        .then(response => response.json())
        .then(data => {
            const dolarOficial = data.find(item => item.casa.nombre === 'Dolar Oficial');
            const dolarBlue = data.find(item => item.casa.nombre === 'Dolar Blue');

            document.getElementById('moneda1').textContent = dolarOficial.casa.compra;
            document.getElementById('moneda2').textContent = dolarBlue.casa.compra;
        });