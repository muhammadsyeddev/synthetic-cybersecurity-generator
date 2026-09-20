
from cyber_sim.models import Employee, Device
from cyber_sim.organization import Organization


# Create a fictional organization.
org = Organization(name="Asterix Financial Services")

# Alice is assigned device DEV-007.
employee = Employee(
    uid="USR-007",
    name="Alice Morgan",
    role="Finance Analyst",
    device_uid="DEV-007",
)

# Deliberately assign the device to a different employee.
device = Device(
    uid="DEV-007",
    name="Finance Laptop",
    owner_uid="USR-005",
    is_managed=True,
)

# Register both entities.
org.employees[employee.uid] = employee
org.devices[device.uid] = device


# Verify that validation rejects the incorrect relationship.
try:
    org.validate_employee_devices()

except ValueError as error:
    print(f"Expected validation error: {error}")
    print("Invalid relationship correctly rejected!")

else:
    raise AssertionError(
        "Validator failed to detect an invalid relationship"
    )
