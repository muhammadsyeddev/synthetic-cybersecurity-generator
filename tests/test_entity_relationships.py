
from cyber_sim.models import Employee, Device


# Create our fictional employee.
employee = Employee(
    uid="USR-007",
    name="Alice Morgan",
    role="Finance Analyst",
    device_uid="DEV-007",
)

# Create the employee's corporate laptop.
device = Device(
    uid="DEV-007",
    name="Finance Laptop",
    owner_uid="USR-007",
    is_managed=True,
)


# Validate the relationship.
assert employee.device_uid == device.uid
assert device.owner_uid == employee.uid
assert device.is_managed is True

print("Employee-device relationship is valid!")
