import re

def extract_uuid(text):
    """
    extracts UUId in the pattern: 8-4-4-4-12 hexadecimal(0-9a-f) chars
    """
    uuid_pattern = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    uuid_list = re.findall(uuid_pattern, text)
    return uuid_list

#test
text = "123e4567-e89b-12d3-a456-426614174000, 550e8400-e29b-41d4-a716-446655440000. Our system generated the following UUIDs for the new records: 9b2e4d3f-5b6c-4f89-9876-123456789abc, 8a9e1b2c-3d4e-5f6a-7b8c-9d0e1f2a3b4c. Additionally, we encountered these UUIDs during the test phase: abcdefab-cdef-1234-5678-abcdefabcdef, fedcba98-7654-3210-fedc-ba9876543210. Another set of UUIDs was created for the user profiles: a1b2c3d4-e5f6-7890-abcd-ef1234567890, b1c2d3e4-f5a6-7890-bcde-1f234567890a. The following UUIDs are used for transaction logs: c1d2e3f4-a5b6-7890-cdef-1234567890ab, d1e2f3a4-b5c6-7890-def1-234567890abc. For auditing purposes, these UUIDs were recorded: e1f2a3b4-c5d6-7890-f123-4567890abcd1, f1a2b3c4-d5e6-7890-1234-567890abcde2. We also generated UUIDs for the API keys: 3c4d5e6f-a7b8-9012-cdef-234567890abc, 4d5e6f7a-b8c9-0123-def1-34567890abcd."
uuids = extract_uuid(text)
print(uuids)
