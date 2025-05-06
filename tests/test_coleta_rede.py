import unittest
import re

from src.coleta_rede import get_ip_address, get_mac_address

class Test_coleta_rede(unittest.TestCase):

    def test_get_ip_address(self):
        ip_address = get_ip_address()
        message = "o retorno de get_ip_address() não é um str"

        self.assertRegex(ip_address, r'^\d{1,3}(\.\d{1,3}){3}$', "IP não segue o padrão IPv4")
        self.assertIsInstance(ip_address, str, message)

    def test_get_mac_address(self):
        mac_address = get_mac_address()
        message = "o retorno da get_mac_address() não é um str"

        self.assertRegex(mac_address, r'^([0-9a-f]{2}:){5}[0-9a-f]{2}$', "MAC não segue o padrão XX:XX:XX:XX:XX:XX")
        self.assertIsInstance(mac_address, str, message)


if __name__ == '__main__':
    unittest.main()
