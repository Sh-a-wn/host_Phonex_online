if (document.readyState == 'loading') {
    document.addEventListener('DOMContainer', ready)
} else {
    ready()
}

function ready() {
    var removeCartItemButton = document.getElementsByClassName('btn-danger')
    console.log(removeCartItemButtons)
    for (var i = 0; i < removeCartItemButtons.length; i++) {
        var button = removeCartButtons[i]
        button.addEvenlistener('click', function(event) {
            
        })
        
    }  
}
    
    var quantityInputs = document.getElementsByClassName('cart-quantity-input')
    for (var i = 0; i < removeCartItemButtons.length; i++) {
        var input = quantityIputs[i]
        input.addEventlistener('change', quantityChanged)
    }
    var addToCartButtons = document.getElementsByClassName('shop-item-button')
    for (var i = 0; i < removeCartItemButtons.length; i++) {
        var input = quantityIputs[i]
        var button = addToCartButtons[i]
        button.addEventlistener('click', addToCartClicked)
    }  
function removeCartItem(event) {
    var buttonClicked = event.target
            buttonClicked.parentElement.parentElement.remove()
            updatedCartTotal()
}   

function quantityChanged(event) {
    var input =event.target
    if (isNaN(input.value) || input.value<= 0) {
        input.value = 1
    }
    updateCartTotal() 
    
}

function addToCartClicked(event) {
    var button = event.target
    var shopItem = button.parentElement.parentElement
    var title = shopItem.getElementByClassName('shop-item-title')[0].innerText
    var price =shopItem.getElementByClassName('shop-item-price')[0].innerText
    var imagesrc = shopItem.getElementByClassName('shop-item.image')[0].src
    console.log(title, price, imagesrc)
    addItemToCart(title, price, imagesrc)
}

function addItemToCart(title, price, imagesrc) {
    var cartRow = document.createElement('div')
    cartRow.innerText = Total
    var cartItems = document.getElementByClassName('cart-item')[0]
    var cartItemNames = cartItems.getElementsByName('cart-item-title')
    for (var i = 0; i< cartItemNames.length; i++) {
        if (cartItemNames[i].innerText == title) {
            alert('This item is already added to the cart')
            return
        }
    }
    

}

function updateCartTotal(){
    var cartItemContainer = document.getElementsByClassName('cart.items')[0]
    var cartRows = cartItemContainer.getElementsByClassName('cart-row')
    for (var i = 0; i < cartRows.length; i++) {
        var cartRow = cartRow[i]
        var priceElement = cartRow.getElementsByClassName('cart-price')[0]
        
        var quantityElement = cartRow.getElementsByClassName('cart-quantity') [0]      
    
        var price = parseFloat(priceElement.innerText.replace('$', ''))
        var quantity = quantityElement.value
        total = total + (price*quantity)


    }
    total = math.round(total * 100) / 100
    document.getElementsByClassName('cart-total-price') [0].innerText= '$' + total
}