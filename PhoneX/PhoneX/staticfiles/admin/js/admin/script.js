let cartItems = [];
let cartTotal = 0;

function addToCart(itemName, itemPrice) {
    cartItems.push({ name: itemName, price: itemPrice });
    cartTotal += itemPrice;

    // Update cart display
    updateCartDisplay();
}

function updateCartDisplay() {
    const cartItemsElement = document.getElementById('cart-items');
    const cartTotalElement = document.getElementById('cart-total');

    // Clear previous items
    cartItemsElement.innerHTML = '';

    // Add new items
    cartItems.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} - $${item.price}`;
        cartItemsElement.appendChild(li);
    });

    // Update total
    cartTotalElement.textContent = cartTotal;
}