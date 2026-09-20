
from dataclasses import dataclass


@dataclass(frozen=True)
class Employee:
    uid: str
    name: str
    role: str
    device_uid: str
