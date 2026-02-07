# Installation Guide for ShopZip Theme

## Quick Start

Follow these steps to install the ShopZip theme on your Shopify store:

### Step 1: Create Theme Package

The theme files are already structured correctly in this repository. To create a ZIP file:

```bash
# From the repository root, create a ZIP excluding git files
zip -r shopzip-theme.zip . -x '*.git*' -x 'INSTALLATION.md'
```

Or download the repository as a ZIP from GitHub and use it directly.

### Step 2: Upload to Shopify

1. **Login to Shopify Admin**
   - Go to your Shopify store admin panel
   - Navigate to: **Online Store** → **Themes**

2. **Upload Theme**
   - Scroll down to the "Theme library" section
   - Click **Add theme** → **Upload zip file**
   - Select your `shopzip-theme.zip` file
   - Wait for the upload to complete

3. **Preview Theme**
   - Once uploaded, you'll see "ShopZip Theme" in your theme library
   - Click **Actions** → **Preview** to see how it looks with your store data

4. **Publish Theme**
   - If you're happy with the preview, click **Actions** → **Publish**
   - Your store will now use the ShopZip theme!

## Customization

### Using the Theme Editor

1. Go to **Online Store** → **Themes**
2. Find "ShopZip Theme" and click **Customize**
3. Use the theme editor to modify:
   - **Colors**: Primary, secondary, text, and background colors
   - **Typography**: Header and body fonts
   - **Layout**: Page width and product grid settings

### Advanced Customization

To modify the theme code directly:

1. From the Themes page, click **Actions** → **Edit code**
2. Navigate through the file structure:
   - `layout/theme.liquid` - Main layout file
   - `templates/` - Page templates
   - `assets/global.js` - JavaScript functionality
   - `config/settings_schema.json` - Theme settings

## Theme Features

### Homepage (index.liquid)
- Hero section with call-to-action
- Featured products grid
- About section

### Product Pages (product.liquid)
- Large product image with thumbnails
- Variant selector
- Add to cart functionality
- Product description

### Collection Pages (collection.liquid)
- Responsive product grid
- Pagination support
- Collection title and description

### Shopping Cart (cart.liquid)
- Item list with images
- Quantity management
- Subtotal calculation
- Update and checkout buttons

## Browser Compatibility

The theme is tested and works on:
- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## Troubleshooting

### Theme Won't Upload
- Ensure the ZIP file contains the theme files at the root level (not in a subfolder)
- Check that all required files are present: `layout/theme.liquid`, `templates/index.liquid`, etc.

### Products Not Displaying
- Make sure you have products added to your Shopify store
- Check that products are assigned to collections
- For the homepage featured products, create a collection with handle "frontpage"

### Customization Not Saving
- Wait a few seconds after making changes in the theme editor
- Click "Save" in the top-right corner
- Clear your browser cache if changes don't appear

## Support

For issues or questions:
- Create an issue: https://github.com/jasonlamaro-lab/shopzip/issues
- Check Shopify's theme documentation: https://shopify.dev/docs/themes

## Next Steps

After installation, consider:
1. Adding your logo and favicon in theme settings
2. Customizing colors to match your brand
3. Creating collections and adding products
4. Setting up navigation menus
5. Adding pages (About, Contact, etc.)

Enjoy your new ShopZip theme! 🎉
