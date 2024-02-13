#!/usr/bin/python3
""" unittests for models/city.py. Defined

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        my_city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_is_public_class_attribute(self):
        my_city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_two_cities_unique_ids(self):
        my_city1 = City()
        my_city2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_two_cities_different_created_at(self):
        my_city1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_two_cities_different_updated_at(self):
        my_city1 = City()
        sleep(0.05)
        my_city2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    def test_str_representation(self):
        my_date = datetime.today()
        my_date_repr = repr(dt)
        my_city = City()
        city.id = "122456"
        my_city.created_at = cy.updated_at = dt
        my_city_str = cy.__str__()
        self.assertIn("[City] (122456)", cystr)
        self.assertIn("'id': '122456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_args_unused(self):
        my_city = City(None)
        self.assertNotIn(None, cy.__dict__.values())

    def test_instantiation_with_kwargs(self):
        my_date = datetime.today()
        my_date_iso = dt.isoformat()
        my_city = City(id="234", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(my_city.id, "234")
        self.assertEqual(my_city.created_at, dt)
        self.assertEqual(my_city.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        my_city = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        my_city.save()
        self.assertLess(first_updated_at, cy.updated_at)

    def test_two_saves(self):
        my_city = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        my_city.save()
        second_updated_at = cy.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        my_city.save()
        self.assertLess(second_updated_at, cy.updated_at)

    def test_save_with_arg(self):
        my_city = City()
        with self.assertRaises(TypeError):
            cy.save(None)

    def test_save_updates_file(self):
        my_city = City()
        my_city.save()
        _mycityid = "City." + cy.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        my_city = City()
        self.assertIn("id", cy.to_dict())
        self.assertIn("created_at", my_city.to_dict())
        self.assertIn("updated_at", my_city.to_dict())
        self.assertIn("__class__", my_city.to_dict())

    def test_to_dict_contains_added_attributes(self):
        my_city = City()
        my_city.middle_name = "Songoro88"
        my_city.my_number = 88
        self.assertEqual("Songoro", my_city.middle_name)
        self.assertIn("my_number", my_city.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        my_city = City()
        my_city_dict = cy.to_dict()
        self.assertEqual(str, type(my_city_dict["id"]))
        self.assertEqual(str, type(my_city_dict["created_at"]))
        self.assertEqual(str, type(my_city_dict["updated_at"]))

    def test_to_dict_output(self):
        my_date = datetime.today()
        my_city = City()
        my_city.id = "122456"
        my_city.created_at = my_city.updated_at = my_date
        tdict = {
            'id': '122456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(cy.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        my_city = City()
        self.assertNotEqual(my_city.to_dict(), my_city.__dict__)

    def test_to_dict_with_arg(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.to_dict(None)


if __name__ == "__main__":
    unittest.main()

