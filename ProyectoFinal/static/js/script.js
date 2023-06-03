const divi = document.querySelector(".datos");
var div_votar = document.querySelector(".votacion");
var boton_agregar = document.querySelector("#agregar");
var boton = document.querySelector("#boton_votar");
var boton_terminar = document.querySelector("#boton_terminar_votacion");
var nombre_votante = document.querySelector("#nombre");
var selector = document.querySelector("select"); 
var opciones = document.querySelectorAll("option");
var arreglo = [];
var arreglo_cantidad = [];
var verdad = 0;

for (let index = 1; index < opciones.length; index++) {
    arreglo_cantidad.push(0);
    //console.log(opciones[index].value);
}

function ventanaEmergente() {
    div_votar.style.display = "block";
}

function cambiar() {
   for (let index = 0; index < arreglo_cantidad.length; index++) {
    if(selector.value == opciones[index + 1].value) {
        window.alert("Votaste por el sabor " + selector.value);
        arreglo_cantidad[index] = arreglo_cantidad[index] + 1;
        var p = document.createElement("p");
        var pTexto = document.createTextNode(nombre_votante.value);
        p.appendChild(pTexto);
        divi.appendChild(p);

        p = document.createElement("p");
        pTexto = document.createTextNode(selector.value);
        p.appendChild(pTexto);
        divi.appendChild(p);

        div_votar.style.display = "none";
        selector.value = "";
        nombre_votante.value = "";
    }
        //window.alert(index);
   }

   
    for (let index = 0; index < arreglo_cantidad.length; index++) {
         console.log(arreglo_cantidad[index]);
    
    }

   
   
}

function calcularGanador() {
    /*
        for (var i = 0; i < arreglo.length; i++) {
        if(arreglo[i] == "Fresas con crema") {
            votos_fresa += 1;
        }

        if(arreglo[i] == "Mamey") {
            votos_mamey += 1;
        }

        if(arreglo[i] == "Vainilla") {
            votos_vainilla += 1;
        }

        if(arreglo[i] == "Cajetoso") {
            votos_cajetoso += 1;
        }
    }
    */

    for (let index = 0; index < arreglo_cantidad.length; index++) {
        verdad = 0;
        for (let i = 0 ; i < arreglo_cantidad.length; i++) {
            if(arreglo_cantidad[index] >= arreglo_cantidad[i]){
                verdad += 1;
            }
            
        }

        if (verdad == arreglo_cantidad.length) {
            window.alert("Ganó el sabor " + opciones[index+1].value);
            break;
        }
        
    }

}

boton.onclick = cambiar;

boton_terminar.onclick = calcularGanador;

boton_agregar.onclick = ventanaEmergente;