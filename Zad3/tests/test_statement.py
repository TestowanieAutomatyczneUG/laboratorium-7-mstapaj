import unittest
from src.statement import Statements


class test_statement(unittest.TestCase):

    def setUp(self):
        self.temp = Statements()

    def test_statement(self):
        self.assertEqual(
            "Statement for BigCo\n Hamlet: $650.00 (55 seats)\n As You Like It: $580.00 (35 seats)\n Othello: "
            "$500.00 (40 seats)\nAmount owed is $1,730.00\nYou earned 47 credits\n", self.temp.statement({
                "customer": "BigCo",
                "performances": [
                    {
                        "playID": "hamlet",
                        "audience": 55
                    },
                    {
                        "playID": "as-like",
                        "audience": 35
                    },
                    {
                        "playID": "othello",
                        "audience": 40
                    }
                ]
            }, {
                "hamlet": {"name": "Hamlet", "type": "tragedy"},
                "as-like": {"name": "As You Like It", "type": "comedy"},
                "othello": {"name": "Othello", "type": "tragedy"}
            }))

    def test_statement_2(self):
        self.assertEqual(
            "Statement for BigCo\n Hamlet: $400.00 (30 seats)\nAmount owed is $400.00\nYou earned 0 credits\n",
            self.temp.statement({
                "customer": "BigCo",
                "performances": [
                    {
                        "playID": "hamlet",
                        "audience": 30
                    }
                ]
            }, {
                "hamlet": {"name": "Hamlet", "type": "tragedy"}
            }))

    def test_statement_3(self):
        self.assertEqual(
            "Statement for BigCo\n As You Like It: $620.00 (40 seats)\n Othello: $900.00 (80 seats)\nAmount owed is "
            "$1,520.00\nYou earned 68 credits\n", self.temp.statement({
                "customer": "BigCo",
                "performances": [
                    {
                        "playID": "as-like",
                        "audience": 40
                    },
                    {
                        "playID": "othello",
                        "audience": 80
                    }
                ]
            }, {
                "as-like": {"name": "As You Like It", "type": "comedy"},
                "othello": {"name": "Othello", "type": "tragedy"}
            }))

    def test_statement_value_error(self):
        self.assertRaises(ValueError, self.temp.statement, {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 55
                },
                {
                    "playID": "as-like",
                    "audience": 35
                },
                {
                    "playID": "othello",
                    "audience": 40
                }
            ]
        }, {
                              "hamlet": {"name": "Hamlet", "type": "action"},
                              "as-like": {"name": "As You Like It", "type": "comedy"},
                              "othello": {"name": "Othello", "type": "tragedy"}
                          })

    def test_statement_value_error_2(self):
        self.assertRaises(ValueError, self.temp.statement, {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 55
                },
            ]
        }, {
                              "hamlet": {"name": "Hamlet", "type": "horroe"}
                          })

    def test_statement_string_invoice(self):
        self.assertRaises(TypeError, self.temp.statement, 'abc', {
            "hamlet": {"name": "Hamlet", "type": "tragedy"}
        })

    def test_statement_string_plays(self):
        self.assertRaises(TypeError, self.temp.statement, {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 30
                }
            ]
        }, 'abc')

    def test_statement_string(self):
        self.assertRaises(TypeError, self.temp.statement, 'cba', 'abc')

    def test_statement_float_invoice(self):
        self.assertRaises(TypeError, self.temp.statement, 3.14, {
            "hamlet": {"name": "Hamlet", "type": "tragedy"}
        })

    def test_statement_float_plays(self):
        self.assertRaises(TypeError, self.temp.statement, {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 30
                }
            ]
        }, 3.14)

    def test_statement_float(self):
        self.assertRaises(TypeError, self.temp.statement, 3.14, 2.56)

    def test_statement_negative_float_invoice(self):
        self.assertRaises(TypeError, self.temp.statement, -3.14, {
            "hamlet": {"name": "Hamlet", "type": "tragedy"}
        })

    def test_statement_negative_float_plays(self):
        self.assertRaises(TypeError, self.temp.statement, {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 30
                }
            ]
        }, -3.14)

    def test_statement_negative_float(self):
        self.assertRaises(TypeError, self.temp.statement, -3.14, -2.56)

    def test_statement_negative_int_invoice(self):
        self.assertRaises(TypeError, self.temp.statement, -3, {
            "hamlet": {"name": "Hamlet", "type": "tragedy"}
        })

    def test_statement_negative_int_plays(self):
        self.assertRaises(TypeError, self.temp.statement, {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 30
                }
            ]
        }, -3)

    def test_statement_negative_int(self):
        self.assertRaises(TypeError, self.temp.statement, -3.14, -2)

    def test_statement_none_invoice(self):
        self.assertRaises(TypeError, self.temp.statement, None, {
            "hamlet": {"name": "Hamlet", "type": "tragedy"}
        })

    def test_statement_none_plays(self):
        self.assertRaises(TypeError, self.temp.statement, {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 30
                }
            ]
        }, None)

    def test_statement_none(self):
        self.assertRaises(TypeError, self.temp.statement, None, None)

    def test_statement_object_invoice(self):
        self.assertRaises(KeyError, self.temp.statement, {}, {
            "hamlet": {"name": "Hamlet", "type": "tragedy"}
        })

    def test_statement_object_plays(self):
        self.assertRaises(KeyError, self.temp.statement, {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 30
                }
            ]
        }, {})

    def test_statement_object(self):
        self.assertRaises(KeyError, self.temp.statement, {}, {})

    def test_statement_array_invoice(self):
        self.assertRaises(TypeError, self.temp.statement, [], {
            "hamlet": {"name": "Hamlet", "type": "tragedy"}
        })

    def test_statement_array_plays(self):
        self.assertRaises(TypeError, self.temp.statement, {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 30
                }
            ]
        }, [])

    def test_statement_array(self):
        self.assertRaises(TypeError, self.temp.statement, [], [])

    def test_statement_true_invoice(self):
        self.assertRaises(TypeError, self.temp.statement, True, {
            "hamlet": {"name": "Hamlet", "type": "tragedy"}
        })

    def test_statement_true_plays(self):
        self.assertRaises(TypeError, self.temp.statement, {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 30
                }
            ]
        }, True)

    def test_statement_true(self):
        self.assertRaises(TypeError, self.temp.statement, True, True)

    def test_statement_false_invoice(self):
        self.assertRaises(TypeError, self.temp.statement, False, {
            "hamlet": {"name": "Hamlet", "type": "tragedy"}
        })

    def test_statement_false_plays(self):
        self.assertRaises(TypeError, self.temp.statement, {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 30
                }
            ]
        }, False)

    def test_statement_false(self):
        self.assertRaises(TypeError, self.temp.statement, False, False)
