import unittest
from unittest import TestCase

from app import User
from app import validate_user


class TestValidate_user(TestCase):
    def test_validate_user(self):
        parms = {
            'Years': '10',
            'Balance': '6000000',
            'Rating': '700',
            'Age': 22,
            'AccountType': 'Blue'
        }
        TestUser = User(parms['Years'], parms['Balance'], parms['Rating'], parms['Age'], parms['AccountType'])
        self.assertTrue(validate_user(TestUser))

    def test_invalid_number(self):
        parms = {
            'Years': '10',
            'Balance': '6000000',
            'Rating': '700',
            'Age': 22,
            'AccountType': 'Blue'
        }

        for Parameter, ParameterValue in parms.items():
            cloneParms = parms.copy()
            if Parameter == 'AccountType':
                continue

            cloneParms[Parameter] = str(ParameterValue) + 'f'
            TestUser = User(cloneParms['Years'], cloneParms['Balance'], cloneParms['Rating'], cloneParms['Age'],
                            cloneParms['AccountType'])
            self.assertFalse(validate_user(TestUser))

            cloneParms = parms.copy()
            if Parameter == 'Balance':
                continue
            cloneParms[Parameter] = 0
            TestUser = User(cloneParms['Years'], cloneParms['Balance'], cloneParms['Rating'], cloneParms['Age'],
                            cloneParms['AccountType'])
            self.assertFalse(validate_user(TestUser))

            cloneParms = parms.copy()
            cloneParms[Parameter] = -1
            TestUser = User(cloneParms['Years'], cloneParms['Balance'], cloneParms['Rating'], cloneParms['Age'],
                            cloneParms['AccountType'])
            self.assertFalse(validate_user(TestUser))


    def test_test_invalid_AccountType(self):
        parms = {
            'Years': '10',
            'Balance': '6000000',
            'Rating': '700',
            'Age': 22,
            'AccountType': 'Blue'
        }

        TestUser = User(parms['Years'], parms['Balance'], parms['Rating'], parms['Age'], parms['AccountType'])

        for AccountType in {'red', '', '-1' 'Bluee' '$$$'}:
            TestUser.AccountType = AccountType
            self.assertFalse(validate_user(TestUser))

if __name__ == '__main__':
    unittest.main()
