import unittest

from pyb_init.configuration import ConfigurationLoader

class ConfigurationTests(unittest.TestCase):

    def test_should_return_empty_configuration_when_no_parameters_passed(self):
      actual_configuration = ConfigurationLoader().load_configuration()
      self.assertEqual(actual_configuration, {})

