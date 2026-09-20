
from cyber_sim.models import Employee, Device, Application, Document, Session
from cyber_sim.organization import Organization


# Step 1: Create our fictional organization.
org = Organization(name="Asterix Financial Services")


# Step 2: Create an employee.
employee = Employee(
    uid="USR-007",
    name="Alice Morgan",
    role="Finance Analyst",
    device_uid="DEV-007",
)


# Step 3: Register the employee.
org.employees[employee.uid] = employee


# Step 4: Retrieve the employee by ID.
retrieved_employee = org.employees["USR-007"]


# Step 5: Verify the result.
assert retrieved_employee == employee

print(retrieved_employee)
print(f"Total employees: {len(org.employees)}")


# Create Alice's corporate laptop.
device = Device(
    uid="DEV-007",
    name="Finance Laptop",
    owner_uid="USR-007",
    is_managed=True,
)

# Register the device in our organization.
org.devices[device.uid] = device

# Retrieve the registered device.
registered_device = org.devices["DEV-007"]

# Validate the employee-device relationship.
assert employee.device_uid == registered_device.uid
assert registered_device.owner_uid == employee.uid

print("Device registered successfully!")
print(f"Total devices: {len(org.devices)}")


# Create our fictional applications.
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

# Register each application in the organization.
for app in applications:
    org.applications[app.uid] = app

# Verify the applications were registered.
assert len(org.applications) == 3

print(f"Total applications: {len(org.applications)}")
print(org.applications["APP-002"])



# Create a sensitive financial document.
document = Document(
    uid="DOC-001",
    name="financial_report.pdf",
    sensitivity="confidential",
    application_uid="APP-002",
)

# Register the document.
org.documents[document.uid] = document

# Retrieve the registered document.
registered_document = org.documents["DOC-001"]

# Verify that its application exists.
assert registered_document.application_uid in org.applications

# Verify that the document belongs to the Document Portal.
assert org.applications[registered_document.application_uid].name == "Document Portal"

print("Document registered successfully!")
print(f"Total documents: {len(org.documents)}")



# Create the legitimate employee's authentication session.
session = Session(
    uid="SES-001",
    user_uid="USR-007",
    device_uid="DEV-007",
    application_uid="APP-001",
)

# Register the session.
org.sessions[session.uid] = session

# Retrieve the registered session.
registered_session = org.sessions["SES-001"]

# Verify that all referenced entities exist.
assert registered_session.user_uid in org.employees
assert registered_session.device_uid in org.devices
assert registered_session.application_uid in org.applications

# Verify that the employee owns the device.
assert (
    org.devices[registered_session.device_uid].owner_uid
    == registered_session.user_uid
)

print("Authentication session registered successfully!")
print(f"Total sessions: {len(org.sessions)}")


# Create the attacker's external laptop.
attacker_device = Device(
    uid="ATK-001",
    name="External Laptop",
    owner_uid=None,
    is_managed=False,
)

# Register the device.
org.devices[attacker_device.uid] = attacker_device

# Retrieve the registered device.
registered_attacker_device = org.devices["ATK-001"]

# Validate the attacker's device.
assert registered_attacker_device.owner_uid is None
assert registered_attacker_device.is_managed is False

# Verify that both devices exist.
assert len(org.devices) == 2

print("Attacker device registered successfully!")
print(f"Total devices: {len(org.devices)}")


# Create the attacker's authentication session.
attacker_session = Session(
    uid="SES-002",
    user_uid="USR-007",
    device_uid="ATK-001",
    application_uid="APP-001",
)

# Register the session.
org.sessions[attacker_session.uid] = attacker_session

# Verify that all referenced entities exist.
assert attacker_session.user_uid in org.employees
assert attacker_session.device_uid in org.devices
assert attacker_session.application_uid in org.applications

# Verify that both sessions use the same account.
assert attacker_session.user_uid == session.user_uid

# Verify that the devices and sessions are different.
assert attacker_session.device_uid != session.device_uid
assert attacker_session.uid != session.uid

# Verify that the attacker's device is unmanaged.
assert org.devices[attacker_session.device_uid].is_managed is False

print("Attacker session registered successfully!")
print(f"Total sessions: {len(org.sessions)}")

org.validate_employee_devices()
print("Employee-device validation passed!")

org.validate_sessions()
print("Session validation passed!")

org.validate_documents()
print("Document validation passed!")