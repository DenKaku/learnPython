import sys, os
print ("----------", sys.path)
crruntePath = os.path.dirname( __file__ )
sys.path.append( crruntePath + "/")

from .main import parse
import unittest

class TestParse( unittest.TestCase ):

    def setUp ( self ):

        self.parse = parse()

    def test_parse( self ):
        expect = INPUT
        actual = self.parse ( OUTPUT )
        self.assertEqual( expect, actual)

INPUT = {
    "test": [
        {
            "test1": 123,
            "test2": "abc"
        }
    ]
}

OUTPUT = {
    "Test": [
        {
            "test1": 123,
            "test2": "abc"
        }
    ]
}

if __name__ == "__main__":
    unittest.main()