const display = document.querySelector('input[name="display"]');
const botones = document.querySelectorAll("button");

document.getElementById("backspace").addEventListener("click", () => {
    display.value=display.value.slice(0,-1)
})

botones.forEach(boton => {
    boton.addEventListener("click", () => {
        const valor = boton.textContent;

        if (valor === "⌫") return
        if (valor === "C") {
            display.value = "";
        } else if (valor === "=") {

            let expresion = display.value
            const parentesisAbiertos = (expresion.match(/√\(/g) || []).length
            const parentesisCerrados = (expresion.match(/\)/g) || []).length
            const faltan = parentesisAbiertos - parentesisCerrados

            expresion += ")".repeat(faltan) 

            expresion = expresion.replace(/√\(/g, "Math.sqrt(").replace(/\^/g, "**").replace(/x/g, "*").replace(/÷/g, "/").replace(/%/g, "/100")
                display.value = eval(expresion)
        } else if (valor === "√") 
            {
                display.value += "√(";
        } else {
            display.value += valor; 
        }
    });
});