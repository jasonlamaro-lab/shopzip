#!/usr/bin/env python3
"""
ShopZip - Create zip folders for Shopify stores

This tool helps you create organized zip archives of your Shopify store files,
including themes, assets, and configurations.
"""

import os
import zipfile
import argparse
from datetime import datetime
from pathlib import Path


class ShopZip:
    """Main class for creating zip archives of Shopify store content."""
    
    def __init__(self, store_name="shopify-store", output_dir="output"):
        """
        Initialize ShopZip.
        
        Args:
            store_name: Name of the Shopify store
            output_dir: Directory where zip files will be saved
        """
        self.store_name = store_name
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
    def create_zip(self, source_dir, zip_name=None, include_patterns=None, exclude_patterns=None):
        """
        Create a zip file from a source directory.
        
        Args:
            source_dir: Path to the directory to zip
            zip_name: Name of the output zip file (without .zip extension)
            include_patterns: List of patterns to include (e.g., ['*.liquid', '*.json'])
            exclude_patterns: List of patterns to exclude (e.g., ['node_modules', '.git'])
            
        Returns:
            Path to the created zip file
        """
        source_path = Path(source_dir)
        
        if not source_path.exists():
            raise ValueError(f"Source directory does not exist: {source_dir}")
        
        # Generate zip file name
        if zip_name is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            zip_name = f"{self.store_name}_{timestamp}"
        
        zip_path = self.output_dir / f"{zip_name}.zip"
        
        # Default exclude patterns for common files to skip
        default_excludes = {'.git', '__pycache__', 'node_modules', '.DS_Store', 'Thumbs.db'}
        if exclude_patterns:
            default_excludes.update(exclude_patterns)
        
        print(f"Creating zip archive: {zip_path}")
        print(f"Source directory: {source_path}")
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            file_count = 0
            
            for root, dirs, files in os.walk(source_path):
                # Filter directories to exclude
                dirs[:] = [d for d in dirs if d not in default_excludes]
                
                for file in files:
                    # Skip excluded patterns
                    if any(pattern in file for pattern in default_excludes):
                        continue
                    
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(source_path)
                    
                    # Apply include patterns if specified
                    if include_patterns:
                        if not any(file_path.match(pattern) for pattern in include_patterns):
                            continue
                    
                    zipf.write(file_path, arcname)
                    file_count += 1
            
            print(f"Added {file_count} files to archive")
        
        print(f"✓ Successfully created: {zip_path}")
        print(f"  Size: {zip_path.stat().st_size / 1024:.2f} KB")
        
        return zip_path
    
    def create_shopify_theme_zip(self, theme_dir):
        """
        Create a zip file specifically for Shopify theme structure.
        
        Args:
            theme_dir: Path to the Shopify theme directory
            
        Returns:
            Path to the created zip file
        """
        print("Creating Shopify theme zip...")
        
        # Shopify theme specific patterns
        include_patterns = ['*.liquid', '*.json', '*.css', '*.scss', '*.js', 
                          '*.png', '*.jpg', '*.jpeg', '*.gif', '*.svg', '*.ico']
        
        return self.create_zip(
            theme_dir, 
            zip_name=f"{self.store_name}_theme",
            include_patterns=include_patterns
        )
    
    def create_config_backup_zip(self, config_dir):
        """
        Create a zip file for Shopify configuration files.
        
        Args:
            config_dir: Path to the configuration directory
            
        Returns:
            Path to the created zip file
        """
        print("Creating configuration backup zip...")
        
        return self.create_zip(
            config_dir,
            zip_name=f"{self.store_name}_config_backup"
        )
    
    def create_store_backup(self, store_dir):
        """
        Create a complete backup zip of the entire store directory.
        
        Args:
            store_dir: Path to the store directory
            
        Returns:
            Path to the created zip file
        """
        print("Creating complete store backup...")
        
        return self.create_zip(
            store_dir,
            zip_name=f"{self.store_name}_full_backup"
        )


def main():
    """Command-line interface for ShopZip."""
    parser = argparse.ArgumentParser(
        description='Create zip folders for Shopify store content',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create a zip from a theme directory
  python shopzip.py theme ./my-theme -s my-store
  
  # Create a full backup of a store directory
  python shopzip.py backup ./store-files -s my-store
  
  # Create a custom zip with specific name
  python shopzip.py custom ./source-dir -n custom-archive -s my-store
        """
    )
    
    parser.add_argument(
        'command',
        choices=['theme', 'config', 'backup', 'custom'],
        help='Type of zip to create'
    )
    
    parser.add_argument(
        'source',
        help='Source directory to zip'
    )
    
    parser.add_argument(
        '-s', '--store-name',
        default='shopify-store',
        help='Name of the Shopify store (default: shopify-store)'
    )
    
    parser.add_argument(
        '-o', '--output-dir',
        default='output',
        help='Output directory for zip files (default: output)'
    )
    
    parser.add_argument(
        '-n', '--name',
        help='Custom name for the zip file (without .zip extension)'
    )
    
    parser.add_argument(
        '-i', '--include',
        nargs='+',
        help='Patterns to include (e.g., *.liquid *.json)'
    )
    
    parser.add_argument(
        '-e', '--exclude',
        nargs='+',
        help='Additional patterns to exclude'
    )
    
    args = parser.parse_args()
    
    # Create ShopZip instance
    shopzip = ShopZip(store_name=args.store_name, output_dir=args.output_dir)
    
    try:
        # Execute the appropriate command
        if args.command == 'theme':
            zip_path = shopzip.create_shopify_theme_zip(args.source)
        elif args.command == 'config':
            zip_path = shopzip.create_config_backup_zip(args.source)
        elif args.command == 'backup':
            zip_path = shopzip.create_store_backup(args.source)
        elif args.command == 'custom':
            zip_path = shopzip.create_zip(
                args.source,
                zip_name=args.name,
                include_patterns=args.include,
                exclude_patterns=args.exclude
            )
        
        print(f"\n✓ Success! Zip file created at: {zip_path}")
        return 0
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return 1


if __name__ == '__main__':
    exit(main())
