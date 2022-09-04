const items = document.getElementById("items");
const cardItem = document.getElementById("cardItem");

const fetchData = async () => {
  try {
    const res = await fetch(`http://127.0.0.1:5000/productos`);
    const data = await res.json();

    data.Productos.forEach((element) => {
      const div = document.createElement("div");
      div.classList.add("card");

      div.style.width = "24rem";
      div.style.borderRadius = ".8rem";
      div.innerHTML = `
                <div class="card-body " >
                <img  class="card-img-top img-productos" src=${element.url_image} alt=${element.url_image}  width="346px" height="465px" />
                    <h3 class="card-title text-center">${element.name}</h3>
                    <div class="precio">
                        <span class="fs-3 text-danger" class="card-text">$${element.price.toFixed(2)}</span>
                        <button class="btn btn-dark col-9 mx-auto fs-3">Comprar</button>
                    </div>
                </div>
            `;
      items.appendChild(div);
    });

    //<p>${element.discount}</p>
    //${element.category}</p>
  } catch (error) {
    console.log(error);
  }
};
fetchData();
