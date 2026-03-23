import os
import sys
import shutil
import subprocess
from pathlib import Path

def check_dependencies():
    print("🔍 Verificando dependencias...")
    deps = ["uv", "git"]
    for dep in deps:
        if shutil.which(dep):
            print(f"  ✅ {dep} encontrado.")
        else:
            print(f"  ❌ {dep} NO encontrado. Por favor, instálalo.")

def check_env_vars():
    print("\n🔑 Verificando variables de entorno...")
    keys = ["ANTHROPIC_API_KEY", "OPENAI_API_KEY"]
    for key in keys:
        if os.getenv(key):
            print(f"  ✅ {key} está configurada.")
        else:
            print(f"  ⚠️ {key} NO está configurada. Algunos agentes podrían fallar.")

def check_framework():
    print("\n🐝 Verificando integridad del Framework...")
    core_path = Path("core/framework")
    if core_path.exists():
        print("  ✅ Estructura del Core detectada.")
    else:
        print("  ❌ No se encuentra la carpeta 'core/framework'. ¿Estás en la raíz del repo?")

def run_health_check():
    print("========================================")
    print("   HIVE STABILITY DEPLOYER (BETA)       ")
    print("========================================")
    check_dependencies()
    check_env_vars()
    check_framework()
    print("\n🚀 Estado del sistema: Listo (Simulado)")
    print("========================================")

if __name__ == "__main__":
    run_health_check()
