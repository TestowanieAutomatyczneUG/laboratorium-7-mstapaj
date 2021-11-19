class isPangram:
    def check(self,word):
        """
        # >>> c = isPangram()
        >>> c.check('abcsdfs')
        False
        >>> c.check('abcdefghijklmnopqrstuvwxyz')
        True
        >>> c.check('jklwxyamnopqrbcdevfstughiz')
        True
        >>> c.check('abcdefghi  jklmnopqrst  uvwxy z')
        True
        >>> c.check('abcefghi  jklmnopqrst  uvxy z')
        False
        >>> c.check('abcde//*fghijk+-lmno.pqrstu+++vwx,,yz')
        True
        >>> c.check('acde//*fghijk+-lmno.pqrtu+++vwx,,yz')
        False
        >>> c.check('abc445defghi25jklmno4654pqrst14uvwxy77z4')
        True
        >>> c.check('ac445defghi25jklmno4654pqst14uvwxy77z4')
        False
        >>> c.check('3212')
        False
        >>> c.check(25)
        Traceback (most recent call last):
            File "C:\\Python310\\lib\\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.isPangram.check[10]>", line 1, in <module>
                c.check(25)
            File "c:\\Users\\mstapaj\\github-classroom\\TestowanieAutomatyczneUG\\laboratorium-7-mstapaj\\Zad1\\src\isPangram.py", line 38, in check
                raise Exception("Podane dane nie są stringiem")
        Exception: Podane dane nie są stringiem
        >>> c.check(-15)
        Traceback (most recent call last):
            File "C:\\Python310\\lib\\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.isPangram.check[11]>", line 1, in <module>
                c.check(-15)
            File "c:\\Users\\mstapaj\\github-classroom\\TestowanieAutomatyczneUG\\laboratorium-7-mstapaj\\Zad1\\src\\m.py", line 61, in check
                raise Exception("Podane dane nie są stringiem")
        Exception: Podane dane nie są stringiem
        >>> c.check(2.35)
        Traceback (most recent call last):
            File "C:\\Python310\\lib\\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.isPangram.check[12]>", line 1, in <module>
                c.check(2.35)
            File "c:\\Users\\mstapaj\\github-classroom\\TestowanieAutomatyczneUG\\laboratorium-7-mstapaj\\Zad1\\src\\m.py", line 61, in check
                raise Exception("Podane dane nie są stringiem")
        Exception: Podane dane nie są stringiem
        >>> c.check(-4.315)
        Traceback (most recent call last):
            File "C:\\Python310\\lib\\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.isPangram.check[13]>", line 1, in <module>
                c.check(-4.315)
            File "c:\\Users\\mstapaj\\github-classroom\\TestowanieAutomatyczneUG\\laboratorium-7-mstapaj\\Zad1\\src\\isPangram.py", line 117, in check
                raise Exception("Podane dane nie są stringiem")
        Exception: Podane dane nie są stringiem
        >>> c.check([])
        Traceback (most recent call last):
            File "C:\\Python310\\lib\\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.isPangram.check[14]>", line 1, in <module>
                c.check([])
            File "c:\\Users\\mstapaj\\github-classroom\\TestowanieAutomatyczneUG\\laboratorium-7-mstapaj\\Zad1\\src\\m.py", line 61, in check
                raise Exception("Podane dane nie są stringiem")
        Exception: Podane dane nie są stringiem
        >>> c.check({})
        Traceback (most recent call last):
            File "C:\\Python310\\lib\\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.isPangram.check[15]>", line 1, in <module>
                c.check({})
            File "c:\\Users\\mstapaj\\github-classroom\\TestowanieAutomatyczneUG\\laboratorium-7-mstapaj\\Zad1\\src\\m.py", line 61, in check
                raise Exception("Podane dane nie są stringiem")
        Exception: Podane dane nie są stringiem
        >>> c.check(None)
        Traceback (most recent call last):
            File "C:\\Python310\\lib\\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.isPangram.check[16]>", line 1, in <module>
                c.check(None)
            File "c:\\Users\\mstapaj\\github-classroom\\TestowanieAutomatyczneUG\\laboratorium-7-mstapaj\\Zad1\\src\\m.py", line 61, in check
                raise Exception("Podane dane nie są stringiem")
        Exception: Podane dane nie są stringiem
        >>> c.check(True)
        Traceback (most recent call last):
            File "C:\\Python310\\lib\\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.isPangram.check[17]>", line 1, in <module>
                c.check(True)
            File "c:\\Users\\mstapaj\\github-classroom\\TestowanieAutomatyczneUG\\laboratorium-7-mstapaj\\Zad1\\src\\m.py", line 61, in check
                raise Exception("Podane dane nie są stringiem")
        Exception: Podane dane nie są stringiem
        >>> c.check(False)
        Traceback (most recent call last):
            File "C:\\Python310\\lib\\doctest.py", line 1336, in __run
                exec(compile(example.source, filename, "single",
            File "<doctest __main__.isPangram.check[18]>", line 1, in <module>
                c.check(False)
            File "c:\\Users\\mstapaj\\github-classroom\\TestowanieAutomatyczneUG\\laboratorium-7-mstapaj\\Zad1\\src\\isPangram.py", line 61, in check
                raise Exception("Podane dane nie są stringiem")
        Exception: Podane dane nie są stringiem
        """
        if isinstance(word,str):
            tab = []
            for i in word:
                if i not in tab and i != " " and i in 'abcdefghijklmnopqrstuvwxyz':
                    tab.append(i)
            if len(tab) > 25:
                return True
            else:
                return False
        else:
            raise Exception("Podane dane nie są stringiem")



if __name__ == "__main__":
    # c = isPangram()
    # print(c.check('abc'))
    import doctest
    # doctest.testmod()
    doctest.testmod(extraglobs={'c': isPangram()})