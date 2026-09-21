
import unittest
from datetime import datetime, timezone

from cyber_sim.generator import generate_organization
from cyber_sim.events import generate_login_event


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


if __name__ == "__main__":
    unittest.main()
