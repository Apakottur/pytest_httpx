import base64
import json
from pathlib import Path
from typing import Any


def read_file(file_path) -> list[dict[str, Any]]:
    file_content = Path(file_path).read_text()
    if not file_content:
        return []
    return json.loads(file_content)


def decode_content(encoded_content: str) -> bytes:
    return base64.decodebytes(encoded_content.encode())
