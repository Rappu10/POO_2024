document.addEventListener('DOMContentLoaded', () => {
    let cart = [];

    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', () => {
            const productElement = button.closest('.product');
            if (productElement) {
                const productId = productElement.getAttribute('data-id');
                const productName = productElement.querySelector('h3').innerText;
                cart.push({ id: productId, name: productName });
                updateCart();
                alert(`Producto ${productName} agregado al carrito!`);
            } else {
                console.error('No se encontró el elemento del producto.');
            }
        });
    });

    function updateCart() {
        const cartCount = document.getElementById('cart-count');
        const cartItems = document.getElementById('cart-items');
        cartCount.textContent = cart.length;
        cartItems.innerHTML = '';
        cart.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item.name;
            cartItems.appendChild(li);
        });
    }
});