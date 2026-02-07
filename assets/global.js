/**
 * ShopZip Theme - Global JavaScript
 */

document.addEventListener('DOMContentLoaded', function() {
  // Mobile menu toggle (if needed in the future)
  console.log('ShopZip Theme Loaded');

  // Add to cart feedback
  const forms = document.querySelectorAll('form[action*="/cart/add"]');
  forms.forEach(form => {
    form.addEventListener('submit', function(e) {
      const button = form.querySelector('button[type="submit"]');
      if (button) {
        const originalText = button.textContent;
        button.textContent = 'Adding...';
        button.disabled = true;
        
        setTimeout(() => {
          button.textContent = originalText;
          button.disabled = false;
        }, 1000);
      }
    });
  });

  // Product image gallery
  const thumbnails = document.querySelectorAll('.product-images img[style*="cursor"]');
  const mainImage = document.querySelector('.product-images img:first-child');
  
  thumbnails.forEach(thumb => {
    thumb.addEventListener('click', function() {
      if (mainImage) {
        const tempSrc = mainImage.src;
        mainImage.src = this.src;
        this.src = tempSrc;
      }
    });
  });

  // Cart quantity updates
  const quantityInputs = document.querySelectorAll('input[name="updates[]"]');
  quantityInputs.forEach(input => {
    input.addEventListener('change', function() {
      if (this.value < 0) {
        this.value = 0;
      }
    });
  });
});
