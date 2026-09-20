# OCSF 1.9 Event Mapping

## Authentication Event

Class UID: 3002

Purpose:
Represent legitimate and attacker authentication activity.

### Important Fields

- class_uid: Authentication event class.
- activity_id: Authentication action.
- type_uid: class_uid \* 100 + activity_id.
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

## File Hosting Activity

Class UID: 6006
Category UID: 6
Category: Application Activity

Purpose:
Represent document operations performed through the
company's fictional Document Portal.

### Selected Activities

- 9: Preview
- 14: Open
- 2: Download

### Important Fields

- actor: The actor performing the file operation.
- file: The file being accessed.
- src_endpoint: The device initiating the operation.

### Scenario Mapping

Normal employee activity:

- An employee previews or opens a financial report.
- The event references the employee's account and device.

Incident activity:

- The attacker downloads confidential financial reports.
- The actor references the compromised account USR-007.
- The source endpoint references attacker device ATK-001.

### Validation Note

The selected activities and class-specific required
attributes are based on OCSF 1.9.

We will verify nested object requirements, inherited
attributes, and session-correlation details before
implementing the event serializer.

## HTTP Activity

Class UID: 4002
Category UID: 4
Category: Network Activity

Purpose:
Represent normal web requests and observable HTTP
traffic associated with the cybersecurity incident.

### Selected Activities

- 3: GET
- 6: POST

### Important Fields

- http_request: Details of the HTTP request.
- http_request.http_method: HTTP method.
- http_request.url: Requested URL.
- http_response: Details of the HTTP response.
- http_response.code: HTTP response status code.
- src_endpoint: Source of the network activity.
- dst_endpoint: Destination of the network activity.

### Scenario Mapping

Normal activity:

- Employees request pages from the internal web application.
- Employees access the document portal through HTTP requests.

Incident activity:

- The attacker accesses the document portal.
- A monitored organizational service sends sensitive
  data to a fictional external destination.

### Validation Note

OCSF 1.9 requires at least one of http_request
or http_response for HTTP Activity.

Our generator will include both when the simulated
telemetry provides request and response information.

We will verify inherited attributes, nested object
requirements, and endpoint relationships before
implementing the HTTP event serializer.
