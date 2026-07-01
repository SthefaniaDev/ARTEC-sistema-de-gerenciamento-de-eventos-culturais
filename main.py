"""
Script principal do sistema ARTEC.
Implementa um menu interativo via terminal com persistência em memória.
"""

from usuarios import Participante, Jurado


def exibir_menu_principal():
    print("\n" + "=" * 55)
    print("=== SISTEMA ARTEC - AMOSTRA COMPETITIVA DE ARTES ===")
    print("=" * 55)
    print("1. Acessar como Participante")
    print("2. Acessar como Jurado")
    print("3. Acessar como Organizador (Admin)")
    print("0. Sair do Sistema")
    print("=" * 55)


def menu_participante(participante, todos_trabalhos):
    while True:
        print(f"\n--- PAINEL DO PARTICIPANTE: {participante.nome.upper()} ---")
        print("1. Inscrever novo trabalho")
        print("2. Listar meus trabalhos inscritos (Acompanhamento)")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nCategorias válidas: pintura, fotografia, musica")
            categoria = input("Digite a categoria do trabalho: ")
            titulo = input("Digite o título da obra: ")

            try:
                novo_trabalho = participante.inscrever_trabalho(categoria, titulo)
                todos_trabalhos.append(novo_trabalho)

                print(
                    f">>> SUCESSO! Trabalho '{titulo}' inscrito "
                    f"na categoria '{categoria}'."
                )

            except Exception as e:
                print(f">>> ERRO AO INSCREVER: {e}")

        elif opcao == "2":
            if not participante.trabalhos_inscritos:
                print(">>> Você ainda não possui trabalhos inscritos.")
            else:
                print("\n--- SEUS TRABALHOS ---")
                for trabalho in participante.trabalhos_inscritos:
                    print(trabalho)

        elif opcao == "0":
            break

        else:
            print(">>> Opção inválida!")


def menu_jurado(jurado, todos_trabalhos):
    while True:
        print(f"\n--- PAINEL DO JURADO: {jurado.nome.upper()} ---")
        print("1. Listar trabalhos aguardando avaliação (Avaliação às cegas)")
        print("2. Avaliar um trabalho")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        disponiveis = [
            trabalho
            for trabalho in todos_trabalhos
            if trabalho.status == "Inscrito"
            and trabalho not in jurado.trabalhos_avaliados
        ]

        if opcao == "1":
            if not disponiveis:
                print(">>> Nenhum trabalho aguardando sua avaliação no momento.")
            else:
                print("\n--- TRABALHOS AGUARDANDO AVALIAÇÃO ---")

                for i, trabalho in enumerate(disponiveis):
                    print(
                        f"[{i}] Título: '{trabalho.titulo}' | "
                        f"Nível Exigido: {trabalho.calcular_nivel_avaliacao()} | "
                        f"Autor: (OCULTO)"
                    )

        elif opcao == "2":
            if not disponiveis:
                print(">>> Nenhum trabalho disponível para avaliação.")
                continue

            print("\n--- TRABALHOS DISPONÍVEIS PARA AVALIAÇÃO ---")

            for i, trabalho in enumerate(disponiveis):
                print(f"[{i}] Título: '{trabalho.titulo}' | Autor: (OCULTO)")

            escolha = input(
                "\nDigite o NÚMERO correspondente ao trabalho que deseja avaliar: "
            )

            try:
                idx = int(escolha)
                trabalho_escolhido = disponiveis[idx]

                nota = input("Digite a nota atribuída (0 a 10): ")
                comentario = input("Deixe um comentário sobre a obra: ")

                jurado.avaliar_trabalho(trabalho_escolhido, nota, comentario)

                print(">>> AVALIAÇÃO REGISTRADA COM SUCESSO!")

            except (ValueError, IndexError):
                print(">>> ERRO: Número de seleção inválido.")

            except Exception as e:
                print(f">>> ERRO AO AVALIAR: {e}")

        elif opcao == "0":
            break

        else:
            print(">>> Opção inválida!")
def menu_organizador(todos_trabalhos):
    while True:
        print("\n--- PAINEL DO ORGANIZADOR ---")
        print("1. Listar TODOS os trabalhos do sistema (Visão Geral)")
        print("2. Alterar status de um trabalho")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            if not todos_trabalhos:
                print(">>> Nenhum trabalho cadastrado no sistema ainda.")
            else:
                print("\n--- TODOS OS TRABALHOS ---")

                for i, trabalho in enumerate(todos_trabalhos):
                    print(f"[{i}] {trabalho}")

        elif opcao == "2":
            if not todos_trabalhos:
                print(">>> Nenhum trabalho cadastrado para alterar status.")
                continue

            print("\n--- ALTERAR STATUS DE TRABALHO ---")

            for i, trabalho in enumerate(todos_trabalhos):
                print(
                    f"[{i}] Obra: '{trabalho.titulo}' | "
                    f"Status atual: {trabalho.status}"
                )

            escolha = input("\nDigite o NÚMERO do trabalho para alterar o status: ")

            try:
                idx = int(escolha)
                trabalho = todos_trabalhos[idx]

                novo_status = input(
                    "Digite o novo status, por exemplo: Desclassificado ou Premiado: "
                )

                trabalho.alterar_status(novo_status)

                print(
                    f">>> SUCESSO! Status da obra '{trabalho.titulo}' "
                    f"atualizado para '{novo_status}'."
                )

            except (ValueError, IndexError):
                print(">>> ERRO: Seleção inválida.")

        elif opcao == "0":
            break

        else:
            print(">>> Opção inválida!")


def executar_sistema():
    todos_trabalhos = []
    usuarios_cadastrados = {}

    while True:
        exibir_menu_principal()

        opcao = input("Selecione o perfil para entrar: ")

        if opcao == "0":
            print("\nEncerrando o sistema ARTEC... Até a próxima amostra!")
            break

        elif opcao in ["1", "2"]:
            print("\n--- AUTENTICAÇÃO ---")

            matricula = input("Digite sua matrícula: ")

            if matricula not in usuarios_cadastrados:
                nome = input("Usuário não encontrado. Digite seu nome para cadastro: ")

                try:
                    if opcao == "1":
                        usuarios_cadastrados[matricula] = Participante(matricula, nome)

                    elif opcao == "2":
                        usuarios_cadastrados[matricula] = Jurado(matricula, nome)

                    print(f">>> Usuário '{nome}' cadastrado com sucesso!")

                except Exception as e:
                    print(f">>> ERRO NO CADASTRO: {e}")
                    continue

            usuario = usuarios_cadastrados[matricula]

            if opcao == "1" and isinstance(usuario, Participante):
                menu_participante(usuario, todos_trabalhos)

            elif opcao == "2" and isinstance(usuario, Jurado):
                menu_jurado(usuario, todos_trabalhos)

            else:
                print(
                    "\n>>> ERRO: Essa matrícula já está registrada "
                    "com outro perfil de acesso!"
                )

        elif opcao == "3":
            menu_organizador(todos_trabalhos)

        else:
            print(">>> Opção inválida. Tente novamente.")


if __name__ == "__main__":
    executar_sistema()