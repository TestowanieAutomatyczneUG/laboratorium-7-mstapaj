import string


class ValidPassword:
    def check(self, password):
        """
        # >>> c.ValidPassword()
        >>> c.check('abcDEF2@')
        True
        >>> c.check('ABC2cdef$%')
        True
        >>> c.check('abcccccccccccccccc@@@@@@cccccccsss!!!!!!!!sssssssssssssssaaaaaaaa3333333$$$$$$DEF2@')
        True
        >>> c.check('aDEF2@')
        False
        >>> c.check('abcdsDEF@')
        False
        >>> c.check('abcdDEF2a')
        False
        >>> c.check('abcdefs2@')
        False
        >>> c.check('')
        False
        >>> c.check('aaaaaabbbb')
        False
        >>> c.check('###$$$$&&***')
        False
        >>> c.check('222333115566')
        False
        >>> c.check([])
        Traceback (most recent call last):
            File "C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_3.9.2544.0_x64__qbz5n2kfra8p0\\lib\\doctest.py", line 1334, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.ValidPassword.check[11]>", line 1, in <module>
                c.check([])
            File "C:\\Users\\MTXst\\Projekty Python\\Testowanie automatyczne\\Lab07\\Zad2a\\src\\ValidPassword.py", line 123, in check
                raise TypeError('Hasło nie jest typu string')
        TypeError: Hasło nie jest typu string
        >>> c.check({})
        Traceback (most recent call last):
          File "C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_3.9.2544.0_x64__qbz5n2kfra8p0\\lib\\doctest.py", line 1334, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest __main__.ValidPassword.check[12]>", line 1, in <module>
            c.check({})
          File "C:\\Users\\MTXst\\Projekty Python\\Testowanie automatyczne\\Lab07\\Zad2a\\src\\ValidPassword.py", line 60, in check
            raise TypeError('Hasło nie jest typu string')
        TypeError: Hasło nie jest typu string
        >>> c.check(None)
        Traceback (most recent call last):
          File "C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_3.9.2544.0_x64__qbz5n2kfra8p0\\lib\\doctest.py", line 1334, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest __main__.ValidPassword.check[13]>", line 1, in <module>
            c.check(None)
          File "C:\\Users\\MTXst\\Projekty Python\\Testowanie automatyczne\\Lab07\\Zad2a\\src\\ValidPassword.py", line 60, in check
            raise TypeError('Hasło nie jest typu string')
        TypeError: Hasło nie jest typu string
        >>> c.check(True)
        Traceback (most recent call last):
          File "C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_3.9.2544.0_x64__qbz5n2kfra8p0\\lib\\doctest.py", line 1334, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest __main__.ValidPassword.check[14]>", line 1, in <module>
            c.check(True)
          File "C:\\Users\\MTXst\\Projekty Python\\Testowanie automatyczne\\Lab07\\Zad2a\\src\\ValidPassword.py", line 60, in check
            raise TypeError('Hasło nie jest typu string')
        TypeError: Hasło nie jest typu string
        >>> c.check(False)
        Traceback (most recent call last):
          File "C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_3.9.2544.0_x64__qbz5n2kfra8p0\\lib\\doctest.py", line 1334, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest __main__.ValidPassword.check[15]>", line 1, in <module>
            c.check(False)
          File "C:\\Users\\MTXst\\Projekty Python\\Testowanie automatyczne\\Lab07\\Zad2a\\src\\ValidPassword.py", line 60, in check
            raise TypeError('Hasło nie jest typu string')
        TypeError: Hasło nie jest typu string
        >>> c.check(23)
        Traceback (most recent call last):
          File "C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_3.9.2544.0_x64__qbz5n2kfra8p0\\lib\\doctest.py", line 1334, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest __main__.ValidPassword.check[16]>", line 1, in <module>
            c.check(23)
          File "C:\\Users\\MTXst\\Projekty Python\\Testowanie automatyczne\\Lab07\\Zad2a\\src\\ValidPassword.py", line 60, in check
            raise TypeError('Hasło nie jest typu string')
        TypeError: Hasło nie jest typu string
        >>> c.check(2.456)
        Traceback (most recent call last):
          File "C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_3.9.2544.0_x64__qbz5n2kfra8p0\\lib\\doctest.py", line 1334, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest __main__.ValidPassword.check[17]>", line 1, in <module>
            c.check(2.456)
          File "C:\\Users\\MTXst\\Projekty Python\\Testowanie automatyczne\\Lab07\\Zad2a\\src\\ValidPassword.py", line 60, in check
            raise TypeError('Hasło nie jest typu string')
        TypeError: Hasło nie jest typu string
        >>> c.check(-12)
        Traceback (most recent call last):
          File "C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_3.9.2544.0_x64__qbz5n2kfra8p0\\lib\\doctest.py", line 1334, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest __main__.ValidPassword.check[18]>", line 1, in <module>
            c.check(-12)
          File "C:\\Users\\MTXst\\Projekty Python\\Testowanie automatyczne\\Lab07\\Zad2a\\src\\ValidPassword.py", line 60, in check
            raise TypeError('Hasło nie jest typu string')
        TypeError: Hasło nie jest typu string
        >>> c.check(-5.123)
        Traceback (most recent call last):
          File "C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.9_3.9.2544.0_x64__qbz5n2kfra8p0\\lib\\doctest.py", line 1334, in __run
            exec(compile(example.source, filename, "single",
          File "<doctest __main__.ValidPassword.check[19]>", line 1, in <module>
            c.check(-5.123)
          File "C:\\Users\\MTXst\\Projekty Python\\Testowanie automatyczne\\Lab07\\Zad2a\\src\\ValidPassword.py", line 60, in check
            raise TypeError('Hasło nie jest typu string')
        TypeError: Hasło nie jest typu string
        """
        if isinstance(password, str):
            if len(password) < 8:
                return False
            if not any(i.isdigit() for i in password):
                return False
            if not any(i.isupper() for i in password):
                return False
            if not any(i in list(string.punctuation) for i in password):
                return False
            return True
        else:
            raise TypeError('Hasło nie jest typu string')


# if __name__ == "__main__":
#     # c = ValidPassword()
#     import doctest
#
#     # doctest.testmod()
#     doctest.testmod(extraglobs={'c': ValidPassword()})
