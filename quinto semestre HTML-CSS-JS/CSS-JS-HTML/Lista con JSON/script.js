const lista = document.getElementById("lista");
const todos = document.getElementById("todos");
const maE = document.getElementById("maE");
const meE = document.getElementById("meE");
const apro = document.getElementById("aprobados");
const repro = document.getElementById("reprobados");
const hombres = document.getElementById("hombres");
const mujeres = document.getElementById("mujeres");
const limpiar = document.getElementById("limpiar");
const buscar = document.getElementById("buscar")

let alumnos = [];

fetch("lista.json")
    .then(res => res.json())
    .then(data => {
        alumnos = data;
        console.log("JSON cargado:", alumnos);
    })
    .catch(err => console.error("Error al cargar JSON:", err));

function mostrar(datos) {
    lista.value = datos.map(a =>
        a.Nombre + " " + a.Apellidos + " | CURP: " + a.Curp + " | Edad: " + a.Edad +" | Promedio: "+ a.Promedio +" | Genero: "+ a.Genero).join("\n");
}

todos.onclick = () => mostrar(alumnos);

maE.onclick = () => {
    const filtro = alumnos.filter (e => e.Edad >= 18);
    mostrar(filtro)
}

meE.onclick = () => {
    const filtro = alumnos.filter (e => e.Edad < 18)
    mostrar(filtro)
}

apro.onclick = () => {
    const filtro = alumnos.filter(p => p.Promedio > 5)
    mostrar(filtro)
}

repro.onclick = () => {
    const filtro = alumnos.filter(p => p.Promedio <= 5)
    mostrar(filtro)
}

hombres.onclick = () => {
    const filtro = alumnos.filter(g => g.Genero == "H")
    mostrar(filtro)
}

mujeres.onclick = () => {
    const filtro = alumnos.filter(g => g.Genero == "M")
    mostrar(filtro)
}

limpiar.onclick = () => {
    lista.value = ""
}

buscar.addEventListener("input", () => {
    const texto = buscar.value.toLowerCase()

    const filtrar = alumnos.filter(a => a.Nombre.toLowerCase().includes(texto))
    mostrar(filtrar)
})