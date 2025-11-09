class Persona {
    constructor(edad,nombre, colorFavorito){
        this.edad=edad
        this.nombre=nombre
        this.colorFavorito=colorFavorito
    }
    getNombre(){
        console.log("hola mi nombre es: "+this.nombre)
    }
    setNombre(nuevoNombre){
        this.nombre=nuevoNombre
        console.log("Ahora mi nombre es: "+ nuevoNombre)
    }
}

class Policia extends Persona {
    constructor(edad,nombre,placa){
        super(edad,nombre)

        this.placa=placa
    }
    getPlaca(){
        console.log("Esta es mi placa: "+this.placa)
    }
    
    setPlaca(nuevaplaca){
        console.log("Cambie de placa ahora es: "+ nuevaplaca)
    }
    
}

const persona1=new Persona(16,"Julian","negro")
const Policia1=new Policia(30,"Homero","Comisario")

persona1.getNombre()
persona1.setNombre("lupe")

Policia1.getNombre()
Policia1.getPlaca()
Policia1.setPlaca("Sheriff")