const personas = [
    {nombre:"Pepe", edad:24 , ciudad:"Monterrey"},
    {nombre:"Juan", edad:18 , ciudad:"Veracruz"},
    {nombre:"Mari", edad:26 , ciudad:"Aguascalientes"},
]

for (let ps of personas) {
    console.log(ps.nombre+" tiene "+ps.edad+" años y actualmente vive en la ciudad de "+ps.ciudad)
}