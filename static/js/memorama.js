// ---------------------------------------------------
// MEMORAMA - NeuroCare
// ---------------------------------------------------

// simbolos para las 8 parejas (puedes cambiarlos por imagenes despues)
const simbolos = ["🌸", "🐦", "☀️", "🍎", "⭐", "🌙", "🍀", "🎈"];

let cartas = [];
let primeraCarta = null;
let segundaCarta = null;
let bloqueado = false;

let intentos = 0;
let parejasEncontradas = 0;
let segundos = 0;
let cronometro = null;
let juegoIniciado = false;

const tablero = document.getElementById("tablero");
const elIntentos = document.getElementById("intentos");
const elParejas = document.getElementById("parejas");
const elTiempo = document.getElementById("tiempo");
const mensajeVictoria = document.getElementById("mensajeVictoria");
const resumenVictoria = document.getElementById("resumenVictoria");

// ---------------------------------------------------
// Iniciar / reiniciar juego
// ---------------------------------------------------
function iniciarJuego() {
    // reiniciar variables
    cartas = [...simbolos, ...simbolos]; // 8 simbolos x2 = 16 cartas
    cartas = mezclar(cartas);

    primeraCarta = null;
    segundaCarta = null;
    bloqueado = false;
    intentos = 0;
    parejasEncontradas = 0;
    segundos = 0;
    juegoIniciado = false;

    elIntentos.textContent = "0";
    elParejas.textContent = "0/8";
    elTiempo.textContent = "00:00";
    mensajeVictoria.classList.remove("activo");

    clearInterval(cronometro);

    // limpiar y crear el tablero
    tablero.innerHTML = "";
    cartas.forEach((simbolo, index) => {
        const carta = document.createElement("div");
        carta.classList.add("carta");
        carta.dataset.simbolo = simbolo;
        carta.dataset.index = index;
        carta.addEventListener("click", () => voltearCarta(carta));
        tablero.appendChild(carta);
    });
}

// mezcla un array (Fisher-Yates)
function mezclar(array) {
    const copia = [...array];
    for (let i = copia.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [copia[i], copia[j]] = [copia[j], copia[i]];
    }
    return copia;
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
// Voltear carta
// ---------------------------------------------------
function voltearCarta(carta) {
    if (bloqueado) return;
    if (carta === primeraCarta) return;
    if (carta.classList.contains("encontrada")) return;

    // arranca el cronometro en el primer clic
    if (!juegoIniciado) {
        juegoIniciado = true;
        iniciarCronometro();
    }

    carta.classList.add("volteada");
    carta.textContent = carta.dataset.simbolo;

    if (!primeraCarta) {
        primeraCarta = carta;
        return;
    }

    segundaCarta = carta;
    bloqueado = true;
    intentos++;
    elIntentos.textContent = intentos;

    revisarPareja();
}

// ---------------------------------------------------
// Revisar si las 2 cartas volteadas son pareja
// ---------------------------------------------------
function revisarPareja() {
    const esPareja = primeraCarta.dataset.simbolo === segundaCarta.dataset.simbolo;

    if (esPareja) {
        primeraCarta.classList.add("encontrada");
        segundaCarta.classList.add("encontrada");
        parejasEncontradas++;
        elParejas.textContent = `${parejasEncontradas}/8`;

        resetearSeleccion();

        if (parejasEncontradas === 8) {
            terminarJuego();
        }
    } else {
        // espera un momento para que el paciente vea las 2 cartas antes de voltearlas
        setTimeout(() => {
            primeraCarta.classList.remove("volteada");
            segundaCarta.classList.remove("volteada");
            primeraCarta.textContent = "";
            segundaCarta.textContent = "";
            resetearSeleccion();
        }, 900);
    }
}

function resetearSeleccion() {
    primeraCarta = null;
    segundaCarta = null;
    bloqueado = false;
}

// ---------------------------------------------------
// Terminar juego (gano)
// ---------------------------------------------------
function terminarJuego() {
    clearInterval(cronometro);
    resumenVictoria.textContent = `Tiempo: ${elTiempo.textContent} · Intentos: ${intentos}`;
    mensajeVictoria.classList.add("activo");

    // aqui despues se conecta con la base de datos para guardar
    // el resultado en historialActividad (tiempo, intentos, fecha, paciente)
    // guardar el resultado real en la base de datos
    fetch("/guardar-resultado", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            idActividad: 1,   // 1 = Memorama
            intentos: intentos,
            tiempo: segundos
        })
    });
}


// ---------------------------------------------------
// Botones
// ---------------------------------------------------
document.getElementById("btnReiniciar").addEventListener("click", iniciarJuego);
document.getElementById("btnJugarOtraVez").addEventListener("click", iniciarJuego);

// arrancar el juego al cargar la pagina
iniciarJuego();