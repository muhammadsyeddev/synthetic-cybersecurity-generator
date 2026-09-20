
import json
from pathlib import Path

# Load our example authentication event.
event = json.loads(
    Path("docs/examples/authentication.json").read_text()
)

# Check some OCSF classification rules.
assert event["class_uid"] == 3002
assert event["category_uid"] == 3
assert event["activity_id"] == 1

assert event["type_uid"] == (
    event["class_uid"] * 100 + event["activity_id"]
)

assert isinstance(event["time"], int)
assert event["metadata"]["version"] == "1.9.0"
assert "service" in event or "dst_endpoint" in event

# Check relationships defined in our scenario.
assert event["user"]["uid"] == "USR-007"
assert event["src_endpoint"]["uid"] == "ATK-001"
assert event["session"]["uid"] == "SES-002"

print("Basic authentication checks passed")
