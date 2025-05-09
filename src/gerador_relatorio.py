import os
import csv

from src.coleta_sistema import get_So_name, get_cpu_percent, get_mem_total, get_disc_usage
from src.coleta_rede import get_mac_address, get_ip_address


def creat_file():
    with open('./relatorio_teste.csv', mode='w', newline='', encoding='latin-1') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        writer.writerow(['Sistema Operacional:', get_So_name()])
        writer.writerow(['Uso de CPU:', get_cpu_percent()])
        writer.writerow(['Memoria Total:', get_mem_total()])
        writer.writerow(['Memoria Usada:', get_disc_usage()])
        writer.writerow(['Endereço IP:', get_ip_address()])
        writer.writerow(['MAC da Maquina:', get_mac_address()])


def clean_report():
    path = './relatorio_teste.csv'
    if os.path.exists(path):
        os.remove(path)
        print(f"O arquivo '{path}' foi removido com sucesso!")
    else:
        print(f"O arquivo '{path}' não existe!")