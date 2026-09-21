
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Employee:
    uid: str
    name: str
    role: str
    device_uid: str


@dataclass(frozen=True)
class Device:
    uid: str
    name: str
    owner_uid: str | None
    is_managed: bool



@dataclass(frozen=True)
class Application:
    uid: str
    name: str
    purpose: str



@dataclass(frozen=True)
class Document:
    uid: str
    name: str
    sensitivity: str
    application_uid: str



@dataclass(frozen=True)
class Session:
    uid: str
    user_uid: str
    device_uid: str
    application_uid: str


@dataclass(frozen=True)
class SimulationEvent:
    uid: str
    timestamp: datetime
    event_type: str
    action: str
    user_uid: str | None = None
    source_uid: str | None = None
    application_uid: str | None = None
    session_uid: str | None = None
    document_uid: str | None = None
    correlation_uid: str | None = None