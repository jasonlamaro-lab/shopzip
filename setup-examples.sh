#!/bin/bash
# Setup script for ShopZip

echo "Setting up ShopZip..."

# Create example directories for testing
mkdir -p examples/theme/assets
mkdir -p examples/theme/config
mkdir -p examples/theme/layout
mkdir -p examples/theme/sections
mkdir -p examples/theme/snippets
mkdir -p examples/theme/templates

# Create example theme files
cat > examples/theme/config/settings_schema.json << 'EOF'
[
  {
    "name": "theme_info",
    "theme_name": "Example Theme",
    "theme_version": "1.0.0",
    "theme_author": "ShopZip",
    "theme_documentation_url": "https://example.com",
    "theme_support_url": "https://example.com/support"
  }
]
EOF

cat > examples/theme/layout/theme.liquid << 'EOF'
<!doctype html>
<html>
<head>
  <title>{{ page_title }}</title>
  {{ content_for_header }}
</head>
<body>
  {{ content_for_layout }}
</body>
</html>
EOF

cat > examples/theme/sections/header.liquid << 'EOF'
<header>
  <h1>{{ shop.name }}</h1>
  {{ section.settings.header_text }}
</header>

{% schema %}
{
  "name": "Header",
  "settings": [
    {
      "type": "text",
      "id": "header_text",
      "label": "Header Text",
      "default": "Welcome"
    }
  ]
}
{% endschema %}
EOF

cat > examples/theme/snippets/product-card.liquid << 'EOF'
<div class="product-card">
  <h3>{{ product.title }}</h3>
  <p>{{ product.price | money }}</p>
</div>
EOF

cat > examples/theme/templates/index.liquid << 'EOF'
{% section 'header' %}
<main>
  <h2>Welcome to our store!</h2>
</main>
EOF

cat > examples/theme/assets/style.css << 'EOF'
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

.product-card {
  border: 1px solid #ccc;
  padding: 15px;
  margin: 10px;
}
EOF

cat > examples/theme/assets/script.js << 'EOF'
console.log('Theme loaded');

document.addEventListener('DOMContentLoaded', function() {
  console.log('DOM ready');
});
EOF

# Create a dummy image file
echo "Dummy image content" > examples/theme/assets/logo.png

echo "✓ Example theme directory created at: examples/theme"
echo ""
echo "You can now test ShopZip with:"
echo "  python shopzip.py theme examples/theme -s example-store"
echo ""
echo "Setup complete!"
