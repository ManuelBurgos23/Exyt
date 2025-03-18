
const API_URL = "http://127.0.0.1:8000";

document.getElementById("usuarioForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    

    console.log(fecha_nac);

    let usuario = {
        nombre: document.getElementById("nombre").value,
        apellidos: document.getElementById("apellidos").value,
        email: document.getElementById("email").value,
        fecha_nac:  document.getElementById("fecha_nac").value,
        dni: document.getElementById("dni").value
    };
    console.log("JSON enviado:", JSON.stringify(usuario, null, 2));
    try{
        let response = await fetch(`${API_URL}/registrar`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(usuario)
        });

        let data = await response.json();
        
        if(!response.ok) {
            throw new Error(data.message);
        }

        alert("Usuario creado correctamente");
        getUsuarios();
    } catch(error) {
        alert(error);
        console.log(error);
    }
   
});

async function getUsuarios() {
    try {
        let response = await fetch(`${API_URL}/usuarios`);
        let data = await response.json();
        console.log(data);
        if (!response.ok) {
            throw new Error(data.message);
        }

        let tabla = document.getElementById("usuariosTabla");
        tabla.innerHTML = "";

        if (data.usuarios && Array.isArray(data.usuarios)) {
            data.usuarios.forEach(usuario => {
                let fila = `<tr>
                    <td>${usuario.nombre}</td>
                    <td>${usuario.apellidos}</td>
                    <td>${usuario.email}</td>
                    <td>${usuario.fecha_nac}</td>
                    <td>${usuario.dni}</td>
                </tr>`;
                tabla.innerHTML += fila;
            });
        } else {
            console.error("La respuesta no contiene la propiedad 'usuarios' o no es un array.");
        }
    } catch (error) {
        alert(error);
        console.log(error);
    }
}

