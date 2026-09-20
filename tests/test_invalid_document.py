
from cyber_sim.models import Document
from cyber_sim.organization import Organization


# Create an organization with no registered applications.
org = Organization(name="Asterix Financial Services")

# Create a document referencing a nonexistent application.
document = Document(
    uid="DOC-001",
    name="financial_report.pdf",
    sensitivity="confidential",
    application_uid="APP-999",
)

# Register the document.
org.documents[document.uid] = document


# Verify that the validator rejects the invalid reference.
try:
    org.validate_documents()

except ValueError as error:
    assert str(error) == (
        "Document DOC-001 references unknown application APP-999"
    )
    print("Invalid document correctly rejected!")

else:
    raise AssertionError(
        "Validator accepted a document with an unknown application"
    )
