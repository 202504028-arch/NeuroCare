// ---------------------------------------------------
// ROMPECABEZAS - NeuroCare
// tablero de 3x3 (9 piezas). Se arma tocando 2 piezas
// para intercambiarlas de lugar.
// ---------------------------------------------------

const TAMANO = 3; // 3x3 = 9 piezas
const TOTAL_PIEZAS = TAMANO * TAMANO;

let intercambios = 0;
let orden = [];        // orden[posicion] = pieza original que esta ahi
let piezaElegida = null;
let piezasCorrectas = 0;
let segundos = 0;
let cronometro = null;
let juegoIniciado = false;
let imagenActual = "";

const seleccionPaisaje = document.getElementById("seleccionPaisaje");
const tablero = document.getElementById("tableroRompecabezas");
const instrucciones = document.getElementById("instrucciones");
const elPiezas = document.getElementById("piezasCorrectas");
const elTiempo = document.getElementById("tiempo");
const mensajeVictoria = document.getElementById("mensajeVictoria");
const resumenVictoria = document.getElementById("resumenVictoria");

// ---------------------------------------------------
// Seleccion de imagen
// ---------------------------------------------------
document.querySelectorAll(".opcionPaisaje").forEach((img) => {
    img.addEventListener("click", () => {
        document.querySelectorAll(".opcionPaisaje").forEach((i) => i.classList.remove("seleccionada"));
        img.classList.add("seleccionada");
        imagenActual = img.dataset.src;

        seleccionPaisaje.style.display = "none";
        tablero.classList.add("activo");
        instrucciones.classList.add("activo");

        iniciarJuego();
    });
});

// ---------------------------------------------------
// Iniciar / reiniciar juego
// ---------------------------------------------------
function iniciarJuego() {
    if (!imagenActual) return; // todavia no eligio imagen

    orden = mezclar([...Array(TOTAL_PIEZAS).keys()]);
    piezaElegida = null;
    piezasCorrectas = 0;
    segundos = 0;
    juegoIniciado = false;

    elPiezas.textContent = `0/${TOTAL_PIEZAS}`;
    elTiempo.textContent = "00:00";
    mensajeVictoria.classList.remove("activo");
    clearInterval(cronometro);

    dibujarTablero();
    contarCorrectas();
}

function mezclar(array) {
    const copia = [...array];
    for (let i = copia.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [copia[i], copia[j]] = [copia[j], copia[i]];
    }
    // si por azar quedo ya resuelto, volvemos a mezclar
    const resuelto = copia.every((valor, indice) => valor === indice);
    return resuelto ? mezclar(array) : copia;
}

// ---------------------------------------------------
// Dibujar el tablero
// ---------------------------------------------------
function dibujarTablero() {
    tablero.innerHTML = "";

    orden.forEach((piezaOriginal, posicion) => {
        const div = document.createElement("div");
        div.classList.add("pieza");
        div.dataset.posicion = posicion;

        const fila = Math.floor(piezaOriginal / TAMANO);
        const col = piezaOriginal % TAMANO;
        const posX = (col / (TAMANO - 1)) * 100;
        const posY = (fila / (TAMANO - 1)) * 100;

        div.style.backgroundImage = `url(${imagenActual})`;
        div.style.backgroundPosition = `${posX}% ${posY}%`;

        div.addEventListener("click", () => elegirPieza(div));
        tablero.appendChild(div);
    });
}

// ---------------------------------------------------
// Elegir / intercambiar piezas
// ---------------------------------------------------
function elegirPieza(div) {
    if (!juegoIniciado) {
        juegoIniciado = true;
        iniciarCronometro();
    }

    const posicion = Number(div.dataset.posicion);

    if (piezaElegida === null) {
        piezaElegida = posicion;
        div.classList.add("elegida");
        return;
    }

    if (piezaElegida === posicion) {
        // toco la misma pieza dos veces: deselecciona
        div.classList.remove("elegida");
        piezaElegida = null;
        return;
    }

    // intercambiar las dos piezas en el arreglo "orden"
    [orden[piezaElegida], orden[posicion]] = [orden[posicion], orden[piezaElegida]];
    intercambios++;  
    piezaElegida = null;
    dibujarTablero();
    contarCorrectas();
}

// ---------------------------------------------------
// Contar piezas en su lugar correcto
// ---------------------------------------------------
function contarCorrectas() {
    piezasCorrectas = 0;
    const divs = tablero.querySelectorAll(".pieza");

    orden.forEach((piezaOriginal, posicion) => {
        const esCorrecta = piezaOriginal === posicion;
        if (esCorrecta) {
            piezasCorrectas++;
            divs[posicion].classList.add("correcta");
        }
    });

    elPiezas.textContent = `${piezasCorrectas}/${TOTAL_PIEZAS}`;

    if (piezasCorrectas === TOTAL_PIEZAS) {
        terminarJuego();
    }
}

// ---------------------------------------------------
// Cronometro
// ---------------------------------------------------
function iniciarCronometro() {
    cronometro = setInterval(() => {
        segundos++;
        const min = String(Math.floor(segundos / 60)).padStart(2, "0");
        const seg = String(segundos % 60).padStart(2, "0");
        elTiempo.textContent = `${min}:${seg}`;
    }, 1000);
}

// ---------------------------------------------------
// Terminar juego (gano)
// ---------------------------------------------------
function terminarJuego() {
    clearInterval(cronometro);
    resumenVictoria.textContent = `Tiempo: ${elTiempo.textContent}`;
    mensajeVictoria.classList.add("activo");

    // aqui despues se conecta con la base de datos para guardar
    // el resultado en historialActividad (tiempo, fecha, paciente)
    // guardar el resultado real en la base de datos
    fetch("/guardar-resultado", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            idActividad: 2,   // 2 = Rompecabezas
            intentos: intercambios,
            tiempo: segundos
        })
    });
}

// ---------------------------------------------------
// Botones
// ---------------------------------------------------
document.getElementById("btnReiniciar").addEventListener("click", () => {
    // vuelve a mostrar el selector de imagen
    tablero.classList.remove("activo");
    instrucciones.classList.remove("activo");
    mensajeVictoria.classList.remove("activo");
    seleccionPaisaje.style.display = "block";
    clearInterval(cronometro);
    imagenActual = "";
    document.querySelectorAll(".opcionPaisaje").forEach((i) => i.classList.remove("seleccionada"));
});

document.getElementById("btnJugarOtraVez").addEventListener("click", () => {
    document.getElementById("btnReiniciar").click();
});