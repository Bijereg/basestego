from unittest import TestCase
from base64 import b64decode as orig_decode
from basestego import b64encode, b64decode


class BasestegoTestCase(TestCase):
    def test_b64encode_fast(self):
        for i in range(2**4):
            test_string = b64encode(b"bijereg", i, False)
            self.assertEqual(b"bijereg", orig_decode(test_string))

    def test_b64encode_slow(self):
        for i in range(2**4):
            test_string = b64encode(b"bijereg", i, True)
            self.assertEqual(b"bijereg", orig_decode(test_string))

    def test_b64decode(self):
        for i in range(2**4):
            test_string = b64encode(b"bijereg", i)
            self.assertEqual(b64decode(test_string), i)
