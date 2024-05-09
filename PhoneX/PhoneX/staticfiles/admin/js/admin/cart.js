function toggleCart() {
  var cart = document.getElementById('cart');
  cart.style.display = cart.style.display === 'block' ? 'none' : 'block';
}

function addToCart(id, name, price, imageUrl) {
  let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
  let item = cartItems.find(item => item.id === id);
  if (item) {
      item.quantity += 1;
  } else {
      cartItems.push({ id, name, price, imageUrl, quantity: 1 });
  }
  localStorage.setItem('cartItems', JSON.stringify(cartItems));
  updateCartUI();
}

function updateCartUI() {
  let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
  let cartList = document.getElementById('cart-items');
  cartList.innerHTML = ''; // Clear current cart items
  cartItems.forEach(item => {
      let li = document.createElement('li');
      li.textContent = `${item.name} - $${item.price} x ${item.quantity}`;
      cartList.appendChild(li);
  });
}

document.addEventListener('DOMContentLoaded', function() {
  updateCartUI();
});
