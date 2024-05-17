import re


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    match = re.match(pattern, email)

    if match:
        if email.count('@') == 1 and email.count('.') == 1:
            return True
    return False

emails = [
    'example@email.com',
    'username@example.com',
    'johndoe123@example.org',
    'example.com',
    'user@examplecom',
    '@example.org',
    'john.doe@example.com',
    'info@company.co.uk',
    'user_name123@example.org',
    'john.doe@examplecom',
    'user@example.co.uk',
    'example.org@user',
    'john.doe@example.com',
    'user123@example.co.uk',
]

for email in emails:
    print(validate_email(email))
