"""Utility to normalize framework imports in agent code."""

import re
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def normalize_agent_imports(agent_dir: str | Path) -> None:
    """Scan and fix incorrect framework imports in an agent directory.
    
    Converts 'from core.framework...' to 'from framework...'
    """
    agent_path = Path(agent_dir)
    if not agent_path.exists():
        return

    # Pattern to match 'from core.framework' or 'import core.framework'
    pattern = re.compile(r'(from|import)\s+core\.framework')

    for py_file in agent_path.rglob("*.py"):
        try:
            content = py_file.read_text(encoding="utf-8")
            if pattern.search(content):
                new_content = pattern.sub(r'\1 framework', content)
                py_file.write_text(new_content, encoding="utf-8")
                logger.info(f"Normalized imports in {py_file}")
        except Exception as e:
            logger.error(f"Failed to normalize {py_file}: {e}")
