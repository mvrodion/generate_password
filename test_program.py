try:
    import password
except ImportError:
    raise AssertionError('Модуль `password` не обнаружен.')

EXPECTED_FUNC_NAME = 'generate_password'

def test_generate_password_exists():
    assert hasattr(password, EXPECTED_FUNC_NAME), (
        f'Функция `{EXPECTED_FUNC_NAME}` не обнаружена в модуле `password`')

def test_generate_password_run_without_exceptions():
    try:
        password.generate_password()
    except Exception as error:
        raise AssertionError(
            f'При запуске функции `{EXPECTED_FUNC_NAME}` возникло '
            f'исключение: {type(error).__name__}: {error}`'
        )
