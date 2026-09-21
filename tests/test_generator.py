
import unittest

from cyber_sim.generator import generate_organization


class TestOrganizationGenerator(unittest.TestCase):

    def test_generate_organization(self):
        # Generate our fictional organization.
        org = generate_organization()

        # Verify the number of generated entities.
        self.assertEqual(len(org.employees), 15)
        self.assertEqual(len(org.devices), 16)
        self.assertEqual(len(org.applications), 3)
        self.assertEqual(len(org.documents), 1)
        self.assertEqual(len(org.sessions), 2)

        # Verify the compromised employee account.
        alice = org.employees["USR-007"]
        self.assertEqual(alice.name, "Alice Morgan")
        self.assertEqual(alice.device_uid, "DEV-007")

        # Verify the attacker session.
        attacker_session = org.sessions["SES-002"]

        self.assertEqual(attacker_session.user_uid, "USR-007")
        self.assertEqual(attacker_session.device_uid, "ATK-001")

        # Validate all organization relationships.
        org.validate()


if __name__ == "__main__":
    unittest.main()
