from unittest import TestCase
from base64 import b64decode
from basestego import base64enc_inserted, base64dec_inserted


# TODO: Make more tests
class BasestegoTestCase(TestCase):
    def test_base64enc_inserted(self):
        for i in range(2**4):
            test_string = base64enc_inserted(b'bijereg', i)
            self.assertEqual(b'bijereg', b64decode(test_string))

    def test_base64dec_inserted(self):
        for i in range(2**4):
            test_string = base64enc_inserted(b'bijereg', i)
            self.assertEqual(int(base64dec_inserted(test_string), 2), i)
