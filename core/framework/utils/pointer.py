"""Pointer Pattern implementation for handling large data results in memory/context."""

import json
import uuid
import logging
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__)

SPILLOVER_DIR = Path.home() / ".hive" / "spillover"
MAX_LITERAL_SIZE = 30 * 1024  # 30KB

def handle_large_result(result: Any, run_id: str = "unknown") -> Any:
    """If result is too large, save to disk and return a pointer.
    
    Args:
        result: The result to process (string or dict)
        run_id: ID for the current run
        
    Returns:
        The original result or a pointer dict.
    """
    if not result:
        return result

    # Convert to string to check size
    if isinstance(result, (dict, list)):
        serialized = json.dumps(result, indent=2)
    else:
        serialized = str(result)

    if len(serialized.encode('utf-8')) <= MAX_LITERAL_SIZE:
        return result

    # It's large, use pointer
    if not SPILLOVER_DIR.exists():
        SPILLOVER_DIR.mkdir(parents=True, exist_ok=True)

    file_id = f"{run_id}_{uuid.uuid4().hex[:8]}.json"
    file_path = SPILLOVER_DIR / file_id
    
    pointer = {
        "__pointer__": True,
        "type": "file_ref",
        "path": str(file_path),
        "size_bytes": len(serialized.encode('utf-8')),
        "summary": serialized[:200] + "...",
        "timestamp": datetime.now().isoformat()
    }

    try:
        file_path.write_text(serialized, encoding="utf-8")
        logger.info(f"Large result saved to pointer: {file_id} ({pointer['size_bytes']} bytes)")
        return pointer
    except Exception as e:
        logger.error(f"Failed to save large result: {e}")
        return result # Fallback to literal if save fails
