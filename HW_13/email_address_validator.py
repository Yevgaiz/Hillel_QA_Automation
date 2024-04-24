emails = [
    "johnsnow@example.com",
    "email123@test.com",
    "someone@example.co.uk",  # '.' twice
    "alice.bob@example",  # '.' before '@'
    "john.doe@example",  # Missing top-level domain
    "john.doeexample.com",  # Missing '@'
    "john@doe@example.com",  # Multiple '@'
    "@example.com",  # Starts with '@'
    "john.doe@example.",  # Ends with '.'
]

for email in emails:
    if ('@' not in email or '.' not in email or email.index('.') < email.index('@')
            or email.count('@') != 1 or email.count('.') != 1 or email.startswith('@') or email.endswith('.')):
        is_valid = False
    else:
        is_valid = True
        for char in email:
            if char != '@' and char != '.' and not char.isalnum():
                is_valid = False
                break

    print(email, "#", is_valid)