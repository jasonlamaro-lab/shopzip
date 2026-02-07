# ShopZip Usage Examples

This document provides practical examples of using ShopZip for various Shopify store scenarios.

## Basic Examples

### 1. Archive a Theme Directory
```bash
python shopzip.py theme ./my-shopify-theme -s my-awesome-store
```
**Output:** `output/my-awesome-store_theme.zip`

**What it includes:** All Shopify theme files (.liquid, .json, .css, .js, images)

### 2. Create a Full Store Backup
```bash
python shopzip.py backup ./store-directory -s production-store
```
**Output:** `output/production-store_full_backup_YYYYMMDD_HHMMSS.zip`

**What it includes:** All files in the directory (excluding .git, node_modules, etc.)

### 3. Archive Configuration Files
```bash
python shopzip.py config ./config -s my-store
```
**Output:** `output/my-store_config_backup.zip`

## Advanced Examples

### 4. Custom Archive with Specific Files
Only include liquid template files:
```bash
python shopzip.py custom ./theme -i "*.liquid" -s my-store -n templates-only
```

### 5. Multiple File Types
Include images and stylesheets:
```bash
python shopzip.py custom ./assets -i "*.png" "*.jpg" "*.css" -s my-store -n assets
```

### 6. Custom Output Directory
Save zips to a specific directory:
```bash
python shopzip.py theme ./theme -s my-store -o ./backups/2024
```

### 7. Named Backup
Create a backup with a specific name:
```bash
python shopzip.py backup ./store -s my-store -n "pre-migration-backup"
```

## Real-World Scenarios

### Scenario 1: Daily Theme Backup
```bash
#!/bin/bash
# daily-backup.sh
DATE=$(date +%Y-%m-%d)
python shopzip.py theme ./themes/current -s production -n "daily-backup-$DATE"
```

### Scenario 2: Pre-Deployment Archive
```bash
python shopzip.py backup ./store -s production -n "pre-deploy-$(date +%Y%m%d-%H%M)"
```

### Scenario 3: Export Liquid Templates
```bash
python shopzip.py custom ./theme -i "*.liquid" -s my-store -n liquid-templates
```

### Scenario 4: Archive All Assets
```bash
python shopzip.py custom ./theme/assets -s my-store -n all-assets
```

## Testing with Example Files

1. Set up example files:
```bash
chmod +x setup-examples.sh
./setup-examples.sh
```

2. Test theme archiving:
```bash
python shopzip.py theme examples/theme -s example-store
```

3. View the created zip:
```bash
unzip -l output/example-store_theme.zip
```

## Tips and Best Practices

1. **Use descriptive store names:** Makes it easier to identify archives
   ```bash
   python shopzip.py theme ./theme -s "acme-production"
   ```

2. **Add timestamps for backups:** Use custom names with dates
   ```bash
   python shopzip.py backup ./store -s my-store -n "backup-$(date +%Y%m%d)"
   ```

3. **Test with examples first:** Use the example files to learn the tool
   ```bash
   ./setup-examples.sh
   python shopzip.py theme examples/theme -s test
   ```

4. **Specify output directory:** Keep backups organized
   ```bash
   python shopzip.py theme ./theme -s my-store -o ./backups/monthly
   ```

5. **Use patterns wisely:** Filter exactly what you need
   ```bash
   python shopzip.py custom ./src -i "*.liquid" "*.json" -s my-store
   ```

## Common Patterns

### Shopify Theme Files
```bash
-i "*.liquid" "*.json" "*.css" "*.scss" "*.js"
```

### Images Only
```bash
-i "*.png" "*.jpg" "*.jpeg" "*.gif" "*.svg"
```

### Configuration Files
```bash
-i "*.json" "*.yml" "*.yaml" "*.config"
```

### Exclude Test Files
```bash
-e "test" "spec" "mock"
```
