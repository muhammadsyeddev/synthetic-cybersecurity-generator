
from dataclasses import dataclass, field

from cyber_sim.models import (
    Employee,
    Device,
    Application,
    Document,
    Session,
)


@dataclass
class Organization:
    name: str

    employees: dict[str, Employee] = field(default_factory=dict)
    devices: dict[str, Device] = field(default_factory=dict)
    applications: dict[str, Application] = field(default_factory=dict)
    documents: dict[str, Document] = field(default_factory=dict)
    sessions: dict[str, Session] = field(default_factory=dict)


    def validate_employee_devices(self) -> None:
        for employee in self.employees.values():

            # Check whether the assigned device exists.
            if employee.device_uid not in self.devices:
                raise ValueError(
                    f"Device {employee.device_uid} does not exist"
                )

            # Retrieve the employee's device.
            device = self.devices[employee.device_uid]

            # Verify that the device belongs to this employee.
            if device.owner_uid != employee.uid:
                raise ValueError(
                    f"Device {device.uid} does not belong to {employee.uid}"
                )
    

    def validate_sessions(self) -> None:
        for session in self.sessions.values():

            # Verify that the user exists.
            if session.user_uid not in self.employees:
                raise ValueError(
                    f"Session {session.uid} references "
                    f"unknown user {session.user_uid}"
                )

            # Verify that the device exists.
            if session.device_uid not in self.devices:
                raise ValueError(
                    f"Session {session.uid} references "
                    f"unknown device {session.device_uid}"
                )

            # Verify that the application exists.
            if session.application_uid not in self.applications:
                raise ValueError(
                    f"Session {session.uid} references "
                    f"unknown application {session.application_uid}"
                )

            # Check device ownership for managed devices.
            device = self.devices[session.device_uid]

            if device.is_managed and device.owner_uid != session.user_uid:
                raise ValueError(
                    f"Managed device {device.uid} "
                    f"does not belong to {session.user_uid}"
                )


    def validate_documents(self) -> None:
        for document in self.documents.values():

            # Check whether the document's application exists.
            if document.application_uid not in self.applications:
                raise ValueError(
                    f"Document {document.uid} references "
                    f"unknown application {document.application_uid}"
                )