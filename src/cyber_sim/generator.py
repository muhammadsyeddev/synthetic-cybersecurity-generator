
from cyber_sim.models import (
    Employee,
    Device,
    Application,
    Document,
    Session,
)
from cyber_sim.organization import Organization


def generate_organization() -> Organization:
    """Generate our fictional cybersecurity organization."""

    org = Organization(name="Asterix Financial Services")

    # --------------------------------------------------
    # 1. Generate employees and their corporate devices
    # --------------------------------------------------

    names = [
        "James Carter",
        "Emma Wilson",
        "Oliver Bennett",
        "Sophia Mitchell",
        "Daniel Foster",
        "Charlotte Hayes",
        "Alice Morgan",
        "Ethan Brooks",
        "Amelia Reed",
        "Noah Collins",
        "Isabella Turner",
        "Lucas Parker",
        "Mia Richardson",
        "Henry Cooper",
        "Grace Phillips",
    ]

    roles = [
        "Finance Analyst",
        "HR Specialist",
        "Software Engineer",
    ]

    for index, name in enumerate(names, start=1):
        user_uid = f"USR-{index:03d}"
        device_uid = f"DEV-{index:03d}"

        employee = Employee(
            uid=user_uid,
            name=name,
            role=roles[(index - 1) % len(roles)],
            device_uid=device_uid,
        )

        device = Device(
            uid=device_uid,
            name=f"Corporate Laptop {index:03d}",
            owner_uid=user_uid,
            is_managed=True,
        )

        org.employees[employee.uid] = employee
        org.devices[device.uid] = device

    # --------------------------------------------------
    # 2. Register applications
    # --------------------------------------------------

    applications = [
        Application(
            uid="APP-001",
            name="Identity Provider",
            purpose="Employee authentication",
        ),
        Application(
            uid="APP-002",
            name="Document Portal",
            purpose="Document storage and management",
        ),
        Application(
            uid="APP-003",
            name="Internal Web Application",
            purpose="Daily business operations",
        ),
    ]

    for application in applications:
        org.applications[application.uid] = application


    # --------------------------------------------------
    # 3. Register company documents
    # --------------------------------------------------

    documents = [
        Document(
            uid="DOC-001",
            name="financial_report.pdf",
            sensitivity="confidential",
            application_uid="APP-002",
        ),
        Document(
            uid="DOC-002",
            name="employee_handbook.pdf",
            sensitivity="internal",
            application_uid="APP-002",
        ),
        Document(
            uid="DOC-003",
            name="quarterly_revenue.xlsx",
            sensitivity="confidential",
            application_uid="APP-002",
        ),
        Document(
            uid="DOC-004",
            name="meeting_notes.docx",
            sensitivity="internal",
            application_uid="APP-002",
        ),
        Document(
            uid="DOC-005",
            name="customer_records.csv",
            sensitivity="confidential",
            application_uid="APP-002",
        ),
        Document(
            uid="DOC-006",
            name="company_policy.pdf",
            sensitivity="internal",
            application_uid="APP-002",
        ),
    ]

    for document in documents:
        org.documents[document.uid] = document

    # --------------------------------------------------
    # 4. Register Alice's legitimate session
    # --------------------------------------------------

    session = Session(
        uid="SES-001",
        user_uid="USR-007",
        device_uid="DEV-007",
        application_uid="APP-001",
    )

    org.sessions[session.uid] = session


    # --------------------------------------------------
    # 5. Register attacker device and session
    # --------------------------------------------------

    attacker_device = Device(
        uid="ATK-001",
        name="External Laptop",
        owner_uid=None,
        is_managed=False,
    )

    org.devices[attacker_device.uid] = attacker_device

    attacker_session = Session(
        uid="SES-002",
        user_uid="USR-007",
        device_uid="ATK-001",
        application_uid="APP-001",
    )

    org.sessions[attacker_session.uid] = attacker_session
    org.validate()

    return org