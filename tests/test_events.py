
import unittest
from datetime import datetime, timezone

from cyber_sim.generator import generate_organization
from cyber_sim.events import generate_login_event, generate_document_event


class TestAuthenticationEvents(unittest.TestCase):

    def setUp(self):
        """Create a fresh organization before each test."""
        self.org = generate_organization()

    def test_legitimate_login(self):
        event = generate_login_event(
            org=self.org,
            event_uid="EVT-000001",
            session_uid="SES-001",
            timestamp=datetime(
                2026, 9, 18, 9, 0, tzinfo=timezone.utc
            ),
        )

        self.assertEqual(event.event_type, "authentication")
        self.assertEqual(event.action, "logon")
        self.assertEqual(event.user_uid, "USR-007")
        self.assertEqual(event.source_uid, "DEV-007")
        self.assertEqual(event.session_uid, "SES-001")

    def test_attacker_login(self):
        event = generate_login_event(
            org=self.org,
            event_uid="EVT-000002",
            session_uid="SES-002",
            timestamp=datetime(
                2026, 9, 18, 10, 15, tzinfo=timezone.utc
            ),
        )

        self.assertEqual(event.event_type, "authentication")
        self.assertEqual(event.action, "logon")
        self.assertEqual(event.user_uid, "USR-007")
        self.assertEqual(event.source_uid, "ATK-001")
        self.assertEqual(event.session_uid, "SES-002")
    


    def test_document_access(self):
        """Verify that document access uses existing entities."""

        event = generate_document_event(
            org=self.org,
            event_uid="EVT-000003",
            session_uid="SES-001",
            document_uid="DOC-001",
            timestamp=datetime(
                2026, 9, 18, 9, 10, tzinfo=timezone.utc
            ),
        )

        # Verify the event type and action.
        self.assertEqual(event.event_type, "file_activity")
        self.assertEqual(event.action, "open")

        # Verify entity relationships.
        self.assertEqual(event.user_uid, "USR-007")
        self.assertEqual(event.source_uid, "DEV-007")
        self.assertEqual(event.application_uid, "APP-002")
        self.assertEqual(event.session_uid, "SES-001")
        self.assertEqual(event.document_uid, "DOC-001")
    

    def test_document_download(self):
        """Verify that an attacker can generate a download event."""

        event = generate_document_event(
            org=self.org,
            event_uid="EVT-000004",
            session_uid="SES-002",
            document_uid="DOC-001",
            timestamp=datetime(
                2026, 9, 18, 10, 22, tzinfo=timezone.utc
            ),
            action="download",
        )

        self.assertEqual(event.action, "download")
        self.assertEqual(event.user_uid, "USR-007")
        self.assertEqual(event.source_uid, "ATK-001")
        self.assertEqual(event.session_uid, "SES-002")
        self.assertEqual(event.document_uid, "DOC-001")

    def test_invalid_document_action(self):
        """Verify that unsupported document actions are rejected."""

        with self.assertRaises(ValueError):
            generate_document_event(
                org=self.org,
                event_uid="EVT-000005",
                session_uid="SES-001",
                document_uid="DOC-001",
                timestamp=datetime(
                    2026, 9, 18, 9, 30, tzinfo=timezone.utc
                ),
                action="delete",
            )


if __name__ == "__main__":
    unittest.main()
