document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/products?top=true')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('product-container');
            data.forEach(product => {
                const productDiv = document.createElement('div');
                productDiv.className = 'about-box';
                productDiv.innerHTML = `
                    <div class="box-img">
                        <img src="${product.image}" alt="">
                    </div>
                    <h3>${product.name}</h3>
                    <h2>${product.price} $</h2>
                `;
                container.appendChild(productDiv);
            });
        });
});


document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/products')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('shop-container');
            data.forEach(product => {
                const productDiv = document.createElement('div');
                productDiv.className = 'shop-box';
                productDiv.innerHTML = `
                    <div class="shop-img">
                        <img src="${product.image}" alt="">
                    </div>
                    <h2>${product.name}</h2>
                    <h3>${product.price} $</h3>
                    <i class="fas fa-shopping-cart"></i>
                `;
                container.appendChild(productDiv);
            });
        })
});
