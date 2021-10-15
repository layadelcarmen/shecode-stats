import json

import unittest

from datastats.datastats import DataStats

class TestStats(unittest.TestCase):

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

    def test_stats(self):

        ds = DataStats()
        ds_result = json.loads(ds.stats(self.test_data, 20, 20000))
        self.assertDictEqual(ds_result, self.vr_data)


    def test__stats(self):
        
        ds = DataStats()
        self.assertDictEqual(ds._stats(self.test_data, 20, 20000), self.vr_data)

    
    def test__avg_age(self):

        ds = DataStats()
        assert ds._avg_age(self.test_data) == 56


    def test__avg_salary(self):

        ds = DataStats()
        assert ds._avg_salary(self.test_data) == 57933


    def test__yearly_avg_increase(self):

        ds = DataStats()
        assert ds._yearly_avg_increase(self.test_data,20, 20000) == 1053  
        
        
    def test__max_salary(self):

        ds = DataStats()
        assert ds._max_salary(self.test_data) == self.vr_data['max_salary']


        


        
