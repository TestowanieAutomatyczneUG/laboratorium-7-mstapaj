import string


class ValidPassword:
    def check(self, password):
        if len(password) < 8:
            return False
        elif password.islower():
           return False
        elif password.isalpha():
            return False


