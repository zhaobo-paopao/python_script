# create_simple_structure.ps1 - 精简企业级目录结构
Write-Host "📁 创建精简企业级目录结构..." -ForegroundColor Cyan

# 1. 核心业务模块
$modules = @("core", "api", "models", "utils", "config")
foreach ($module in $modules) {
    $dir = "src\$module"
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Force -Path $dir
        Write-Host "✅ 创建: src\$module" -ForegroundColor Green
    }
}

# 2. 创建 __init__.py 文件
$init_files = @(
    "src\__init__.py",
    "src\core\__init__.py",
    "src\api\__init__.py", 
    "src\models\__init__.py",
    "src\utils\__init__.py",
    "src\config\__init__.py"
)

foreach ($file in $init_files) {
    if (-not (Test-Path $file)) {
        New-Item -ItemType File -Force -Path $file
        Write-Host "📄 创建: $file" -ForegroundColor Yellow
    }
}

# 3. 创建核心业务文件（可选，有模板）
$core_files = @(
    "src\core\main.py",
    "src\api\routes.py",
    "src\config\settings.py",
    "src\utils\helpers.py"
)

foreach ($file in $core_files) {
    if (-not (Test-Path $file)) {
        # 创建带基础模板的文件
        $template = @'
"""模块说明"""

def main():
    """主函数"""
    return "Hello from module"

if __name__ == "__main__":
    print(main())
'@
        [System.IO.File]::WriteAllText("$PWD\$file", $template, [System.Text.Encoding]::UTF8)
        Write-Host "📄 创建(带模板): $file" -ForegroundColor Yellow
    }
}

# 4. 测试目录
$test_dirs = @("tests", "tests\unit", "tests\integration")
foreach ($dir in $test_dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Force -Path $dir
        Write-Host "✅ 创建: $dir" -ForegroundColor Green
    }
}

# 5. 测试文件
$test_files = @("tests\__init__.py", "tests\conftest.py", "tests\test_core.py")
foreach ($file in $test_files) {
    if (-not (Test-Path $file)) {
        New-Item -ItemType File -Force -Path $file
        Write-Host "📄 创建: $file" -ForegroundColor Yellow
    }
}

# 6. 必要的配置文件（只创建最必要的）
$config_files = @{
    ".env.example" = "# 环境变量示例`nDEBUG=true`nDATABASE_URL=sqlite:///app.db"
    "requirements.txt" = "# 生产依赖"
    "requirements-dev.txt" = "# 开发依赖`nruff`nblack`npytest"
}

foreach ($file in $config_files.Keys) {
    if (-not (Test-Path $file)) {
        [System.IO.File]::WriteAllText("$PWD\$file", $config_files[$file], [System.Text.Encoding]::UTF8)
        Write-Host "📄 创建: $file" -ForegroundColor Cyan
    }
}

# 7. 文档和脚本目录（可选）
@("docs", "scripts") | ForEach-Object {
    if (-not (Test-Path $_)) {
        New-Item -ItemType Directory -Force -Path $_
        Write-Host "✅ 创建: $_" -ForegroundColor Green
    }
}

Write-Host "`n🎉 精简企业级目录结构创建完成！" -ForegroundColor Green
Write-Host "`n📁 生成结构：" -ForegroundColor Cyan
Write-Host "  src/" -ForegroundColor Cyan
Write-Host "  ├── core/        # 核心业务逻辑" -ForegroundColor White
Write-Host "  ├── api/         # API接口" -ForegroundColor White
Write-Host "  ├── models/      # 数据模型" -ForegroundColor White
Write-Host "  ├── utils/       # 工具函数" -ForegroundColor White
Write-Host "  └── config/      # 配置管理" -ForegroundColor White
Write-Host "  tests/" -ForegroundColor Cyan
Write-Host "  ├── unit/        # 单元测试" -ForegroundColor White
Write-Host "  └── integration/ # 集成测试" -ForegroundColor White
Write-Host "  docs/           # 文档" -ForegroundColor Cyan
Write-Host "  scripts/        # 脚本" -ForegroundColor Cyan
Write-Host "`n📄 创建的文件：" -ForegroundColor Cyan
Write-Host "  .env.example    # 环境变量模板" -ForegroundColor White
Write-Host "  requirements*.txt # 依赖文件" -ForegroundColor White
Write-Host "  src/*/__init__.py # Python包文件" -ForegroundColor White
Write-Host "  src/core/main.py  # 主程序入口" -ForegroundColor White
Write-Host "`n🚀 下一步：uv venv 创建虚拟环境" -ForegroundColor Yellow