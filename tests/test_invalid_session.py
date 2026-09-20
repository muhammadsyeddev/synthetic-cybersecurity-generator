
from cyber_sim.models import Application, Device, Session
from cyber_sim.organization import Organization


# Create our fictional organization.
org = Organization(name="Asterix Financial Services")

# Register a valid device and application.
device = Device(
    uid="DEV-007",
    name="Finance Laptop",
    owner_uid="USR-007",
    is_managed=True,
)

app = Application(
    uid="APP-001",
    name="Identity Provider",
    purpose="Employee authentication",
)

org.devices[device.uid] = device
org.applications[app.uid] = app

# Create a session referencing a nonexistent employee.
session = Session(
    uid="SES-003",
    user_uid="USR-999",
    device_uid="DEV-007",
    application_uid="APP-001",
)

org.sessions[session.uid] = session

# The validator must reject this session.
try:
    org.validate_sessions()

except ValueError as error:
    assert str(error) == (
        "Session SES-003 references unknown user USR-999"
    )
    print("Invalid session correctly rejected!")

else:
    raise AssertionError(
        "Validator accepted a session with an unknown user"
    )
