import unittest
import os

from src.gerador_relatorio import creat_file, clean_report

class Test_gerador_relatorio(unittest.TestCase):

    def setUp(self):
        self.nome_arquivo = './relatorio_teste.csv'
        creat_file()

    def tearDown(self):
        clean_report()  # função que remove relatórios criados pelo sistema

    def test_existence_of_the_file(self):
        """Verifica se o arquivo foi realmente criado."""
        self.assertTrue(os.path.exists(self.nome_arquivo), "O arquivo não foi criado.")

    def test_creat_file_extension(self):
        """Verifica se a extensão do arquivo está correta (.txt ou .csv)."""
        extensao = os.path.splitext(self.nome_arquivo)[1]
        self.assertIn(extensao, ['.txt', '.csv'], "A extensão do arquivo é inválida.")

    def test_type_of_content(self):
        """Verifica se o conteúdo é uma string formatada (não vazio)."""
        with open(self.nome_arquivo, 'r', encoding='latin-1') as f:
            conteudo = f.read()
        self.assertIsInstance(conteudo, str, "O conteúdo do arquivo não é uma string.")
        self.assertGreater(len(conteudo.strip()), 0, "O conteúdo do arquivo está vazio.")

    def test_expected_content(self):
        """Verifica se o conteúdo esperado está presente (Sistema, IP, etc)."""
        with open(self.nome_arquivo, 'r', encoding='latin-1') as f:
            conteudo = f.read()
        self.assertIn("Sistema Operacional", conteudo, "Informação de sistema ausente.")
        self.assertIn("Endereço IP", conteudo, "Informação de IP ausente.")
        self.assertIn("Uso de CPU", conteudo, "Informação de CPU ausente.")


if __name__ == '__main__':
    unittest.main()