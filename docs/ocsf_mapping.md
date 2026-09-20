
# OCSF 1.9 Event Mapping

## Authentication Event

Class UID: 3002

Purpose:
Represent legitimate and attacker authentication activity.

### Important Fields

- class_uid: Authentication event class.
- activity_id: Authentication action.
- type_uid: class_uid * 100 + activity_id.
- time: UTC Unix timestamp in milliseconds.
- user.uid: Account being authenticated.
- src_endpoint.uid: Device initiating authentication.
- session.uid: Authentication session identifier.
- status_id: Authentication outcome.
- metadata.version: OCSF schema version.

### Scenario Mapping

Legitimate login:
- User: USR-007
- Device: DEV-007
- Session: SES-001

Attacker login:
- User: USR-007
- Device: ATK-001
- Session: SES-002

Both logins use the same account but different
devices and sessions.

### Validation Note

This document is an initial field mapping.
We will verify all required fields, object
constraints, and enum values against OCSF 1.9
before implementing the serializer.
