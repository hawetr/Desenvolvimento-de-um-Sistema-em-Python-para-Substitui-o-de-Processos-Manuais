import pandas as pd


class Funcionarios:
    def __init__(self):
        self.funcionarios = {}

    def adicionar_funcionario(self, nome):
        if nome not in self.funcionarios:
            self.funcionarios[nome] = []
            print(f"Funcionário {nome} adicionado.")
        else:
            print(f"Funcionário {nome} já existe.")

    def adicionar_turno(self, nome, dia, turno):
        if nome in self.funcionarios:
            self.funcionarios[nome].append((dia, turno))
            print(f"Turno {turno} adicionado para {nome} no dia {dia}.")
        else:
            print(f"Funcionário {nome} não encontrado.")

    def exibir_escala(self):
        for funcionario, turnos in self.funcionarios.items():
            print(f"\nFuncionário: {funcionario}")
            for dia, turno in turnos:
                print(f"  Dia: {dia}, Turno: {turno}")

    def criar_planilha(self, nome_arquivo):
        dados = []
        for funcionario, turnos in self.funcionarios.items():
            for dia, turno in turnos:
                dados.append({"Funcionário": funcionario, "Dia": dia, "Turno": turno})

        df = pd.DataFrame(dados)
        df.to_excel(nome_arquivo, index=False)
        print(f"Planilha {nome_arquivo} criada com sucesso.")

    def exibir_planilha(self, nome_arquivo):
        try:
            df = pd.read_excel(nome_arquivo)
            print("\nConteúdo da planilha:")
            print(df)
        except FileNotFoundError:
            print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao abrir a planilha: {e}")


def main():
    sistema = Funcionarios()

    # Adicionando funcionários de exemplo
    funcionarios_exemplo = ["Alice", "Mariana", "Carlos", "Júlia"]
    for nome in funcionarios_exemplo:
        sistema.adicionar_funcionario(nome)

    # Adicionando turnos de exemplo
    turnos_exemplo = [
        ("Alice", "2024-11-01", "manhã"),
        ("Alice", "2024-11-02", "tarde"),
        ("Mariana", "2024-11-01", "noite"),
        ("Carlos", "2024-11-02", "manhã"),
        ("Júlia", "2024-11-01", "tarde"),
        ("Júlia", "2024-11-02", "noite")
    ]

    for nome, dia, turno in turnos_exemplo:
        sistema.adicionar_turno(nome, dia, turno)

    while True:
        print("\n1. Adicionar Funcionário")
        print("2. Adicionar Turno")
        print("3. Exibir Escala")
        print("4. Criar Planilha")
        print("5. Exibir Planilha")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do funcionário: ")
            sistema.adicionar_funcionario(nome)

        elif opcao == '2':
            nome = input("Digite o nome do funcionário: ")
            dia = input("Digite o dia (ex: 2024-11-01): ")
            turno = input("Digite o turno (ex: manhã, tarde, noite): ")
            sistema.adicionar_turno(nome, dia, turno)

        elif opcao == '3':
            sistema.exibir_escala()

        elif opcao == '4':
            nome_arquivo = input("Digite o nome do arquivo (ex: escala_funcionarios.xlsx): ")
            sistema.criar_planilha(nome_arquivo)

        elif opcao == '5':
            nome_arquivo = input("Digite o nome do arquivo para exibir (ex: escala_funcionarios.xlsx): ")
            sistema.exibir_planilha(nome_arquivo)

        elif opcao == '6':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()