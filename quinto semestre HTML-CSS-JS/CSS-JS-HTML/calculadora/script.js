const display = document.querySelector('input[name="display"]');
const botones = document.querySelectorAll("button");

document.getElementById("backspace").addEventListener("click", () => {
    if (display.disabled) return;
    display.value = display.value.slice(0, -1);
    operacionReal = operacionReal.slice(0, -1);
})

let operacionReal = "";
let ans = 0;

botones.forEach(boton => {
    boton.addEventListener("click", () => {
        const valor = boton.textContent;

        if (display.value === "Infinity" || display.disabled) {
            if (valor === "C") {
                display.value = "";
                operacionReal = "";
                display.disabled = false;
            }
            return;
        }
        
        if (valor === "⌫") return;
        
        if (valor === "C") {
            display.value = "";
            operacionReal = "";
            display.disabled = false;
        } else if (valor === "=") {
            let expresion = operacionReal;

            expresion = expresion.replace(/[\+\-\*\/]+$/, "");
            
            const parentesisAbiertos = (expresion.match(/Math\.sqrt\(/g) || []).length;
            const parentesisCerrados = (expresion.match(/\)/g) || []).length;
            const faltan = parentesisAbiertos - parentesisCerrados;

            expresion += ")".repeat(faltan);
            
            try {
                const resultado = eval(expresion);
                display.value = resultado;
                ans = resultado;
                operacionReal = String(resultado);
                
                if (resultado === Infinity || resultado === -Infinity) {
                    display.disabled = true;
                }
            } catch (error) {
                display.value = "Error";
                display.disabled = true;
            }

        } else if (valor === "√") {
            display.value += "√(";
            operacionReal += "Math.sqrt(";
        } else if (valor === "x10ˣ") {
            display.value += "x10^";
            operacionReal += "*10**";
        } else if (valor === "Ans") {
            display.value += ans;
            operacionReal += ans;
        } else if (valor === "^") {
            display.value += "^";
            operacionReal += "**";
        } else if (valor === "x") {
            display.value += "x";
            operacionReal += "*";
        } else if (valor === "÷") {
            display.value += "÷";
            operacionReal += "/";
        } else if (valor === "%") {
            display.value += "%";
            operacionReal += "/100 *";
        } else {
            display.value += valor;
            operacionReal += valor;
        }
    });
});