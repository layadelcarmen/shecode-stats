import json

import unittest

from datastats.datastats import DataStats

class TestStats(unittest.TestCase):

    def test_json(self):
        test_data = [
            {
                "id": 1,
                "name": "Laura",
                "surname": "Wagner",
                "age": 58,
                "salary": "€36000"
            },
            {
                "id": 2,
                "name": "Mike",
                "surname": "Schneider",
                "age": 45,
                "salary": "€57300"
            },
            {
                "id": 3,
                "name": "Bern",
                "surname": "Hellebrand",
                "age": 65,
                "salary": "€80500"
            }
        ]

        vr_data = {
                'avg_age': 56,
                'avg_salary': 57933,
                'avg_yearly_increase': 1053,
                'max_salary': [{
                    "id": 3,
                    "name": "Bern",
                    "surname": "Hellebrand",
                    "age": 65,
                    "salary": "€80500"
                }],
                'min_salary': [{
                    "id": 1,
                    "name": "Laura",
                    "surname": "Wagner",
                    "age": 58,
                    "salary": "€36000"
                }]
            }

        ds = DataStats()

        ds_result = json.loads(ds.stats(test_data, 20, 20000))
        self.assertDictEqual(ds_result, vr_data)


        
