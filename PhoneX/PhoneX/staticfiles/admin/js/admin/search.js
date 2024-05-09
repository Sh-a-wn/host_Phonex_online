function searchProducts(searchTerm) {
    const allProducts = getProductsData(); // Get product data from your source
    const filteredProducts = allProducts.filter(product => 
      product.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      product.description.toLowerCase().includes(searchTerm.toLowerCase())
    );
  
    // Update product list UI with filtered products
    updateProductList(filteredProducts);
  }
  
  // Add event listener to search input field
  const searchInput = document.getElementById("searchInput");
  searchInput.addEventListener("keyup", () => searchProducts(searchInput.value));
  