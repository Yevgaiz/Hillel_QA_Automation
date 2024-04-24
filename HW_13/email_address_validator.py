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