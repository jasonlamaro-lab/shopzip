# ShopZip - Shopify Store Zip Folder Creator

A simple and efficient Python tool to create organized zip archives for your Shopify store files, themes, and configurations.

## Features

- 🎨 **Theme Archiving**: Create zip files of Shopify themes with proper file filtering
- 📦 **Full Backups**: Generate complete backups of your store directories
- ⚙️ **Config Backups**: Archive configuration files separately
- 🎯 **Custom Archives**: Create custom zip files with include/exclude patterns
- 🚀 **Easy CLI**: Simple command-line interface for quick operations
- 📁 **Smart Filtering**: Automatically excludes common files like `.git`, `node_modules`, etc.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/jasonlamaro-lab/shopzip.git
cd shopzip
```

2. Install dependencies (optional, only if you need additional features):
```bash
pip install -r requirements.txt
```

## Usage

### Quick Start

Make the script executable:
```bash
chmod +x shopzip.py
```

### Command Syntax

```bash
python shopzip.py <command> <source> [options]
```

### Commands

#### 1. Create Theme Zip
Archive a Shopify theme directory with automatic filtering for theme files (`.liquid`, `.json`, `.css`, `.js`, images, etc.):

```bash
python shopzip.py theme ./my-theme -s my-store-name
```

#### 2. Create Configuration Backup
Archive configuration files:

```bash
python shopzip.py config ./config-files -s my-store-name
```

#### 3. Create Full Store Backup
Create a complete backup of your store directory:

```bash
python shopzip.py backup ./store-directory -s my-store-name
```

#### 4. Create Custom Archive
Create a custom zip with specific include/exclude patterns:

```bash
python shopzip.py custom ./source-dir -n custom-archive -s my-store-name
```

With include patterns:
```bash
python shopzip.py custom ./source-dir -i "*.liquid" "*.json" -s my-store-name
```

With exclude patterns:
```bash
python shopzip.py custom ./source-dir -e "test" "temp" -s my-store-name
```

### Options

- `-s, --store-name`: Name of the Shopify store (default: `shopify-store`)
- `-o, --output-dir`: Output directory for zip files (default: `output`)
- `-n, --name`: Custom name for the zip file (without `.zip` extension)
- `-i, --include`: Patterns to include (space-separated)
- `-e, --exclude`: Additional patterns to exclude (space-separated)

## Examples

### Example 1: Archive a Theme
```bash
python shopzip.py theme ./my-shopify-theme -s "awesome-store"
```
Output: `output/awesome-store_theme.zip`

### Example 2: Create Full Backup with Custom Name
```bash
python shopzip.py backup ./store-data -s "my-shop" -n "backup-2024-01-15"
```
Output: `output/backup-2024-01-15.zip`

### Example 3: Custom Archive with Specific Files
```bash
python shopzip.py custom ./assets -i "*.png" "*.jpg" "*.svg" -s "my-shop" -n "images"
```
Output: `output/images.zip`

## Project Structure

```
shopzip/
├── shopzip.py           # Main script
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── .gitignore          # Git ignore patterns
└── output/             # Output directory (created automatically)
    └── *.zip           # Generated zip files
```

## How It Works

1. **Input**: You provide a source directory and choose a command type
2. **Processing**: ShopZip walks through the directory, applying filters based on the command
3. **Archiving**: Files are compressed into a ZIP archive with proper structure
4. **Output**: The zip file is saved to the output directory with a descriptive name

## Automatic Exclusions

ShopZip automatically excludes common files and directories that shouldn't be in archives:
- `.git` - Git repository data
- `__pycache__` - Python cache files
- `node_modules` - Node.js dependencies
- `.DS_Store` - macOS system files
- `Thumbs.db` - Windows system files

## Use Cases

- **Theme Development**: Easily package themes for deployment or sharing
- **Version Control**: Create timestamped backups of your store files
- **Migration**: Prepare store data for migration to another platform
- **Collaboration**: Share store components with team members
- **Archiving**: Keep organized backups of different store versions

## Requirements

- Python 3.6 or higher
- No external dependencies required for core functionality

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Made with ❤️ for Shopify store management**