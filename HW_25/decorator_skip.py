def skip_if(condition, reason=''):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                if reason:
                    print(reason)
                return
            return func(*args, **kwargs)
        return wrapper
    return decorator


@skip_if(True, 'Skipped because of JIRA-123 bug')
def test_two_plus_two():
    assert 2 + 2 == 5

test_two_plus_two()


@skip_if(condition=False, reason='Skipped because of JIRA-123 bug')
def test_two_minus_two():
    assert 2 - 2 == 5

test_two_minus_two()
