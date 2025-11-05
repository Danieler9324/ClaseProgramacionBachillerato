const alumnos=[
    {nombre: "Pepe chuy" ,calificacion: 6 },
    {nombre: "Laura" ,calificacion: 7 },
    {nombre: "Neburak" ,calificacion: 8 },
    {nombre: "Damian" ,calificacion: 10 },
    {nombre: "Jose" ,calificacion: 9 }
];

const mejores= alumnos.filter(a => a.calificacion>=8)

for (let a of mejores) {
    console.log("nombre: "+a.nombre+" calificacion: "+ a.calificacion)
}