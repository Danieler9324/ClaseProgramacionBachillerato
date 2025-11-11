function combinaciones(lista) {
    for (let i=0; i<lista.length; i++){
        for (let j=0; j<lista.length; j++){
            console.log(lista[i], lista[j])
        }
    }
}

const numeros=[1,2,3,4,5,6,7,8,9,10]
combinaciones(numeros)