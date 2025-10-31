const palabras = ["zapato","perpendicular","circulo","camion","comida","tren","persona","hola","gudbay"]

let larga = palabras[0]

for (let palabra of palabras) {
    if (palabra.length >larga.length) {
        larga = palabra
    }
}

console.log("La palabra mas larga es: ", larga)