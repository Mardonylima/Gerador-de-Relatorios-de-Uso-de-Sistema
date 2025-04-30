# Gerador de Relatórios de Uso de Sistema

Um projeto desenvolvido em Python com foco em práticas reais de automação, coleta de dados do sistema e geração de relatórios. Este sistema coleta informações do computador local e gera relatórios detalhados sobre o sistema operacional, hardware e rede, com exportação em formato `.txt` ou `.csv`.

---

## Objetivos do Projeto

Este projeto faz parte do meu roadmap de estudos em Python e infraestrutura, e tem como objetivo:

- Praticar a coleta de dados do sistema usando bibliotecas especializadas.
- Aplicar princípios de programação modular e limpa.
- Desenvolver habilidades com manipulação de arquivos.
- Gerar relatórios automatizados com informações reais do sistema.
- Simular um projeto técnico com organização e documentação profissional.

---

## Funcionalidades

- Coleta de informações do sistema operacional (SO, versão, arquitetura).
- Coleta de informações da CPU, memória RAM e disco.
- Coleta de informações da rede (endereço IP, MAC, etc.).
- Geração de relatórios nos formatos `.txt` ou `.csv`.
- Estrutura de código modular.
- Interface de execução via terminal (CLI).

---

## Tecnologias Utilizadas

- **Python 3.x**
- **psutil** – Monitoramento de recursos do sistema.
- **platform** – Detecção de informações sobre o sistema operacional.
- **socket** – Coleta de dados da rede.
- **csv** – Escrita de relatórios em formato tabular.
- **Boas práticas** – Organização modular, tipagem, comentários e estrutura de diretórios.

---

## Estrutura do Projeto

```
relatorio_sistema/
├── main.py               # Ponto de entrada do programa (interface CLI)
├── coleta_sistema.py     # Funções para coletar dados do sistema operacional e hardware
├── coleta_rede.py        # Funções para coletar dados de rede
├── gerador_relatorio.py  # Geração dos arquivos de relatório (.txt ou .csv)
└── tests/
    ├── test_coleta_sistema.py
    └── test_gerador_relatorio.py
```

---

## Como Executar o Projeto

Clone o repositório:

```bash
git clone https://github.com/Mardonylima/Relatorio-de-Uso-do-Sistema.git
cd Relatorio-de-Uso-do-Sistema
```

Instale as dependências (se necessário):

```bash
pip install psutil
```

Execute o programa:

```bash
python main.py --formato txt
python main.py --formato csv
```

---

## Próximos Passos

- Adicionar geração de relatório em JSON.
- Implementar menu com `argparse` ou `typer`.
- Criar sistema de logs.
- Permitir agendamento automático de geração de relatórios.

---

## Autor

Desenvolvido por **Mardony**  
Projeto educacional e pessoal para prática de Python e infraestrutura.
