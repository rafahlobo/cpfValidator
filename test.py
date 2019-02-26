import unittest
import cpf

class test_validate(unittest.TestCase):
    def test_cpf_true(self):
        """ Testing cpf validation. """
        self.assertTrue(cpf.isCpfValid("146.212.130-67"))

    def test_cpf_false(self):
        """ Testing cpf validation. """
        self.assertFalse(cpf.isCpfValid("146.234.830-67"))

    def test_cnpj_true(self):
        """ Testing cnpj validation. """
        self.assertTrue(cpf.isCnpjValid("46.773.756/0001-74"))

    def test_cnpj_false(self):
        """ Testing cnpj validation. """
        self.assertFalse(cpf.isCnpjValid("46.553.736/0001-74"))

unittest.main()
