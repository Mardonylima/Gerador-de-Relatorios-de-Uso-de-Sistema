from src.gerador_relatorio import creat_file, clean_report

def main():

    while True:
        print("Sistema Gerador De Relatório:")
        print("1 - Gerar Relatório")
        print("2 - Mostrar Prévia do Conteúdo")
        print("3 - Apagar Relatório")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            creat_file()
            print("Relatório criado\n")

        elif opcao == '2':
            print("A inplementar\n")

        elif opcao == "3":
            clean_report()
            print("Apagando...")
            print("Relatório apagado.\n")

        elif opcao == "4":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção invalida, tente novamente.\n")

if __name__ == "__main__":
    main()