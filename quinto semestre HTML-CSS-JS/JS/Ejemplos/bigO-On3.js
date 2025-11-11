function combinacionesLetras(lista){
    for (let i=0; i<lista.length;i++){
        for (let o=0; o<lista.length;o++){
            for (let k=0; k<lista.length;k++){
                console.log(lista[i],lista[o],lista[k])
            }
        }
    }
}

const letras=["A","B","C"]
combinacionesLetras(letras)