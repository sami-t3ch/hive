"""Hive-Boot V2.0: Pre-flight Advanced Validation (Protocol Zeta)."""

import os
import sys
import urllib.request
import subprocess
import json
from pathlib import Path

# --- CONFIGURATION ---
HIVE_ROOT = Path.home() / ".hive"
CORE_URL = "http://localhost:8000/api/health"
TOOLS_URL = "http://localhost:4001/health"

def log(step, msg, status="INFO"):
    icons = {"OK": "✓", "ERR": "✗", "WARN": "!", "INFO": "i"}
    print(f"[{step}] {msg:.<45} [{icons.get(status, ' ')}]")

def check_docker():
    """Verify Docker engine and containers status."""
    try:
        res = subprocess.run(["docker", "ps", "--format", "json"], capture_output=True, text=True)
        if res.returncode != 0:
            log("1/5", "Docker Engine", "ERR")
            return False
        
        containers = res.stdout.strip().split("\n")
        active = [c for c in containers if "hive-main" in c]
        if not active:
            log("1/5", "Docker Hive Containers (Not Running)", "WARN")
        else:
            log("1/5", f"Docker Engine ({len(active)} hive containers)", "OK")
    except Exception:
        log("1/5", "Docker Engine (Not Found)", "ERR")
        return False
    return True

def check_env():
    """Validate .env keys and format."""
    env_path = Path(".env")
    if not env_path.exists():
        log("2/5", ".env file missing", "ERR")
        return False
    
    with open(env_path) as f:
        content = f.read()
        keys = ["GROQ_API_KEY", "ANTHROPIC_API_KEY", "HIVE_CREDENTIAL_KEY"]
        missing = [k for k in keys if k not in content or "tu_clave" in content]
        
    if missing:
        log("2/5", f"Keys: {', '.join(missing)}", "ERR")
        return False
    log("2/5", "Environment Credentials", "OK")
    return True

def check_connectivity():
    """Check services and parse JSON health reports."""
    all_ok = True
    try:
        with urllib.request.urlopen(CORE_URL, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            if data.get("status") == "ok":
                log("3/5", f"Backend Core (Sessions: {data.get('sessions', 0)})", "OK")
            else:
                log("3/5", "Backend Core (Unhealthy)", "ERR")
                all_ok = False
    except Exception:
        log("3/5", "Backend Core (OFFLINE)", "ERR")
        all_ok = False

    try:
        with urllib.request.urlopen(TOOLS_URL, timeout=5) as resp:
            if resp.status == 200:
                log("4/5", "Tools Server (MCP)", "OK")
            else:
                log("4/5", "Tools Server (Status Error)", "ERR")
                all_ok = False
    except Exception:
        log("4/5", "Tools Server (OFFLINE)", "ERR")
        all_ok = False
    return all_ok

def check_shared_memory():
    """Verify the Hive persistent storage layer."""
    if not HIVE_ROOT.exists():
        try:
            HIVE_ROOT.mkdir(parents=True, exist_ok=True)
            log("5/5", "Shared Memory (Created)", "OK")
        except Exception:
            log("5/5", "Shared Memory (Access Denied)", "ERR")
            return False
    else:
        # Check writability
        test_file = HIVE_ROOT / ".boot_check"
        try:
            test_file.write_text("zeta_check")
            test_file.unlink()
            log("5/5", "Shared Memory (Writable)", "OK")
        except Exception:
            log("5/5", "Shared Memory (Read-Only)", "ERR")
            return False
    return True

def main():
    print("\n" + "="*60)
    print(" HIVE-BOOT V2.0: PROTOCOLO DE LISTEZA ZETA ".center(60, "█"))
    print("="*60)
    
    results = [
        check_docker(),
        check_env(),
        check_connectivity(),
        check_shared_memory()
    ]
    
    print("-" * 60)
    if all(results):
        print(" [READY] EL ENJAMBRE ESTÁ SINCRONIZADO Y LISTO ".center(60))
    else:
        print(" [SYSTEM ERROR] REVISA LOS COMPONENTES FALLIDOS ".center(60))
    print("-" * 60 + "\n")

if __name__ == "__main__":
    main()
