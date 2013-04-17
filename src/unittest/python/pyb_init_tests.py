import unittest
from mockito import when, verify, any as any_value, unstub

import pyb_init
from pyb_init import entry_point

class PybInitTests(unittest.TestCase):
    
    def tearDown(self):
        unstub()

    
    def test_should_invoke_docopt_with_version_and_docstring(self):
        when(pyb_init).docopt(doc=any_value(), version=any_value()).thenReturn({})
        
        entry_point()

        verify(pyb_init).docopt(doc=pyb_init.__doc__, version='${version}')

