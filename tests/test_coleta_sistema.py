import unittest
import platform

from src.coleta_sistema import get_So_name, get_cpu_percent, get_mem_total, get_disc_usage


class Test_coleta_sistema(unittest.TestCase):

    def test_get_So_name(self):
        So_nome = get_So_name()
        message = "O retorno de get_so_name() não é uma string"

        self.assertIsInstance(So_nome, str, message)

    def test_get_cpu_percent(self):
        cpu_percent = get_cpu_percent()
        message_type = "O retorno de get_cpu_percent() não é um float"
        message_range = "O valor de uso da CPU está fora do intervalo 0–100"

        self.assertIsInstance(cpu_percent, float, message_type)
        self.assertGreaterEqual(cpu_percent, 0.0, message_range)
        self.assertLessEqual(cpu_percent, 100.0, message_range)

    def test_get_mem_total(self):
        mem_total = get_mem_total()
        message = "o retorno da get_mem_total() não é um inteiro"

        self.assertIsInstance(mem_total, int, message)

    def test_get_disc_usage(self):
        disc_usage = get_disc_usage()
        message = "o retorno da get_disc_usage() não é um dicionario"

        self.assertIsInstance(disc_usage, dict, message)


if __name__ == '__main__':
    unittest.main()
