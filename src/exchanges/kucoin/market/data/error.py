from __future__ import annotations

from dataclasses import dataclass

@dataclass
class ErrorMessage:
    code: int
    message: str

    @classmethod
    def from_api(cls, data) -> ErrorMessage:
        return cls(
            code=data.error_code,
            message=data.error_message,
        )