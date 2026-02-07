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
  const productImagesContainer = document.querySelector('.product-images');
  if (productImagesContainer) {
    const mainImage = productImagesContainer.querySelector('img:first-child');
    const thumbnails = productImagesContainer.querySelectorAll('img[style*="cursor"]');
    
    thumbnails.forEach((thumb, index) => {
      thumb.addEventListener('click', function() {
        if (mainImage && this.src !== mainImage.src) {
          mainImage.src = this.src;
          mainImage.alt = this.alt;
        }
      });
    });
  }

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
