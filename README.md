# ShopZip - Shopify Theme

A modern, clean, and responsive Shopify theme designed for e-commerce stores.

## Features

- **Responsive Design**: Mobile-first approach with clean, modern aesthetics
- **Product Showcase**: Beautiful product grids with hover effects
- **Cart Management**: Full-featured shopping cart with quantity updates
- **Customizable Colors**: Theme editor support for color customization
- **Fast Loading**: Optimized images and minimal JavaScript
- **SEO Friendly**: Proper meta tags and semantic HTML

## Theme Structure

```
shopzip/
├── assets/           # Static files (CSS, JS, images)
│   └── global.js    # Main JavaScript file
├── config/          # Theme configuration
│   ├── settings_schema.json  # Theme settings definition
│   └── settings_data.json    # Default theme settings
├── layout/          # Layout templates
│   └── theme.liquid          # Main theme layout
├── locales/         # Translation files
│   └── en.default.json       # English translations
├── sections/        # Reusable sections
├── snippets/        # Reusable code snippets
│   └── meta-tags.liquid      # SEO meta tags
└── templates/       # Page templates
    ├── index.liquid          # Homepage
    ├── product.liquid        # Product page
    ├── collection.liquid     # Collection page
    ├── cart.liquid           # Shopping cart
    ├── page.liquid           # Static pages
    └── 404.liquid            # Error page
```

## Installation

1. **Download Theme**: Clone or download this repository
2. **Compress Files**: Create a ZIP file of all theme files
3. **Upload to Shopify**:
   - Go to your Shopify Admin
   - Navigate to Online Store > Themes
   - Click "Upload theme"
   - Select the ZIP file
   - Click "Upload"

## Customization

### Theme Settings

Access theme customization through:
1. Shopify Admin > Online Store > Themes
2. Click "Customize" on the ShopZip theme
3. Modify settings in the theme editor:
   - Colors (Primary, Secondary, Text, Background)
   - Typography (Header and Body fonts)
   - Layout (Page width)
   - Product Grid settings

### Code Customization

- **Styles**: Modify inline styles in `layout/theme.liquid` or add custom CSS
- **JavaScript**: Edit `assets/global.js` for custom interactions
- **Templates**: Customize page layouts in the `templates/` directory
- **Snippets**: Create reusable components in `snippets/`

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

This theme is open source and available for use in your Shopify store.

## Support

For issues or questions, please visit: https://github.com/jasonlamaro-lab/shopzip/issues