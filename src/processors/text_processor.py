#!/bin/bash
# 自動創建所有必要的文件和目錄

# 創建目錄結構
mkdir -p src/processors src/collectors src/api src/utils src/database

# 創建 __init__.py 文件
touch src/__init__.py
touch src/processors/__init__.py
touch src/collectors/__init__.py
touch src/api/__init__.py
touch src/utils/__init__.py
touch src/database/__init__.py

echo "項目結構創建完成！"
