const Api = async() => {
    try{
        const res = await fetch(`http://127.0.0.1:5000/productos`)
        const data = await res.json() 

        let nombre = ''
        let imagenes = ''
        data.Productos.forEach(element => {
            nombre = nombre + `<h4>${element.name}</h4>`
            imagenes = imagenes + `<img src=${element.url_image} alt=${element.url_image}  width="400px" height="400px" />`

            document.getElementById('card').innerHTML = nombre
            document.getElementById('card').innerHTML = imagenes
            /*console.log(element.name)*/
        });
        
    

        /*
        const prod = info.map((produc) => {
            return `<p>nombre: ${produc[2].name}</p>
            <p>id: ${produc[2].id}</p>
            <p>categoria: ${produc[2].category}</p>
            <img src=${produc[2].url_image} alt=${produc[2].name}/>
            <p>Precio: ${produc[2].price}</p>
            `
        })
        root.innerHTML = prod
        console.log(prod)*/
    }catch(error){
        console.log(error)
    }  
}
Api()
