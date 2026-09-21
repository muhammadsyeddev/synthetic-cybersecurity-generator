
from datetime import datetime, timezone

from cyber_sim.models import SimulationEvent
from cyber_sim.organization import Organization


def generate_login_event(
    org: Organization,
    event_uid: str,
    session_uid: str,
    timestamp: datetime,
) -> SimulationEvent:
    """Create a login event from an existing session."""

    # Find the session in our organization.
    session = org.sessions[session_uid]

    # Create an event using the session's existing relationships.
    event = SimulationEvent(
        uid=event_uid,
        timestamp=timestamp,
        event_type="authentication",
        action="logon",
        user_uid=session.user_uid,
        source_uid=session.device_uid,
        application_uid=session.application_uid,
        session_uid=session.uid,
    )

    return event



def generate_document_event(
    org: Organization,
    event_uid: str,
    session_uid: str,
    document_uid: str,
    timestamp: datetime,
    action: str = "open",
) -> SimulationEvent:
    """Generate a document access or download event."""

    allowed_actions = {"open", "download"}

    if action not in allowed_actions:
        raise ValueError(
            f"Unsupported document action: {action}"
        )

    session = org.sessions[session_uid]
    document = org.documents[document_uid]

    return SimulationEvent(
        uid=event_uid,
        timestamp=timestamp,
        event_type="file_activity",
        action=action,
        user_uid=session.user_uid,
        source_uid=session.device_uid,
        application_uid=document.application_uid,
        session_uid=session.uid,
        document_uid=document.uid,
    )

