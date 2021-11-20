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
