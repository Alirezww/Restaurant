from constanst import SUPERVISOR_CREDENTIAL


def check_credential(user_credential):
    if len(user_credential) > 2:
        check_username = bool(SUPERVISOR_CREDENTIAL[0]['username'] == user_credential[1])
        check_password = bool(SUPERVISOR_CREDENTIAL[0]['password'] == user_credential[2])
        return check_password, check_username
    return False