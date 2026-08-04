// ---------------------------------------------------
// AVISOS - NeuroCare
// los avisos ahora vienen de MySQL (avisosIniciales,
// inyectado por Flask/Jinja en el HTML)
// ---------------------------------------------------

let avisos = avisosIniciales;

const listaAvisos = document.getElementById("listaAvisos");
const sinAvisos = document.getElementById("sinAvisos");

const modalAviso = document.getElementById("modalAviso");
const inputTitulo = document.getElementById("inputTitulo");
const inputHora = document.getElementById("inputHora");

// ---------------------------------------------------
// Dibujar la lista de avisos en pantalla
// ---------------------------------------------------
function dibujarAvisos() {
    listaAvisos.innerHTML = "";

    if (avisos.length === 0) {
        sinAvisos.classList.add("activo");
        return;
    }
    sinAvisos.classList.remove("activo");

    const ordenados = [...avisos].sort((a, b) => a.hora.localeCompare(b.hora));

    ordenados.forEach((aviso) => {
        const tarjeta = document.createElement("div");
        tarjeta.classList.add("tarjetaAviso");
        if (aviso.completado) tarjeta.classList.add("completado");

        tarjeta.innerHTML = `
            <div class="icono">
                <img src="/static/img/icono_campanaa.png" alt="">
            </div>
            <div class="informacion">
                <div class="titulo">
                    <h2>${aviso.titulo}</h2>
                </div>
                <div class="horaTipo">
                    <p>${aviso.hora}</p>
                </div>
            </div>
            <div class="botonCompletado ${aviso.completado ? "marcado" : ""}">
                ${aviso.completado ? "&#10003;" : ""}
            </div>
        `;

        const boton = tarjeta.querySelector(".botonCompletado");
        boton.addEventListener("click", () => alternarCompletado(aviso.id));

        listaAvisos.appendChild(tarjeta);
    });
}

// ---------------------------------------------------
// Marcar / desmarcar un aviso como completado (ahora real)
// ---------------------------------------------------
function alternarCompletado(id) {
    fetch(`/completar-aviso/${id}`, { method: "POST" })
        .then((respuesta) => respuesta.json())
        .then((datos) => {
            const aviso = avisos.find((a) => a.id === id);
            aviso.completado = datos.nuevoEstado === "Completado";
            dibujarAvisos();
        });
}

// ---------------------------------------------------
// Abrir / cerrar el modal de agregar aviso
// ---------------------------------------------------
function abrirModal() {
    inputTitulo.value = "";
    inputHora.value = "";
    modalAviso.classList.add("activo");
    inputTitulo.focus();
}

function cerrarModal() {
    modalAviso.classList.remove("activo");
}

document.getElementById("botonAgregar").addEventListener("click", abrirModal);
document.getElementById("btnCancelarAviso").addEventListener("click", cerrarModal);

modalAviso.addEventListener("click", (evento) => {
    if (evento.target === modalAviso) cerrarModal();
});

// ---------------------------------------------------
// Guardar un aviso nuevo (ahora real, en MySQL)
// ---------------------------------------------------
document.getElementById("btnGuardarAviso").addEventListener("click", () => {
    const titulo = inputTitulo.value.trim();
    const hora = inputHora.value;

    if (titulo === "" || hora === "") {
        alert("Por favor llena el título y la hora.");
        return;
    }

    fetch("/guardar-aviso", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ titulo: titulo, hora: hora })
    })
        .then((respuesta) => respuesta.json())
        .then((datos) => {
            avisos.push({
                id: datos.id,
                titulo: titulo,
                hora: hora,
                completado: false
            });

            cerrarModal();
            dibujarAvisos();
        });
});

// ---------------------------------------------------
// Primer dibujo al cargar la pagina
// ---------------------------------------------------
dibujarAvisos();