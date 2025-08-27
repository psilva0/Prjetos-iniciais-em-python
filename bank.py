import json
import hashlib
import os


def gerar_hash(senha):
    senha_bytes = senha.encode('utf-8')
    hash_obj = hashlib.sha256(senha_bytes)
    return hash_obj.hexdigest()


arquivo_dos_dados_login = 'dados_usuario.json'
login_confirmado = False

print('Bem-vindo ao banco \033[1;91mBRADESCO\033[0m')
print('Siga as instruções a seguir.')

while True:
    try:
        cad = int(input('Você já tem cadastro? (1 para SIM, 2 para NÃO): '))
        if cad in [1, 2]:
            break
        else:
            print('Opção inválida. Por favor, digite 1 ou 2.')
    except ValueError:
        print('Entrada inválida. Por favor, digite um número.')

if cad == 1:
    if not os.path.exists(arquivo_dos_dados_login):
        print('Nenhum cadastro foi encontrado. Por favor, reinicie e crie um cadastro.')
    else:
        with open(arquivo_dos_dados_login, 'r', encoding='utf-8') as f:
            dados_salvos = json.load(f)

        login = input('Digite seu login: ').strip()
        senha = input('Digite sua senha: ').strip()
        hash_senha_digitada = gerar_hash(senha)

        if login == dados_salvos['login'] and hash_senha_digitada == dados_salvos['hash_senha']:
            nome_completo = dados_salvos.get('nome', login)
            print(f"\033[1;92mLogin bem-sucedido! Bem-vindo(a), {nome_completo}!\033[0m")
            login_confirmado = True
        else:
            print("\033[1;91mLogin ou senha incorretos.\033[0m")

elif cad == 2:
    while True:
        nome = input('Digite seu nome completo: ').strip()
        log1 = input('Crie seu login: ').strip()
        senh1 = input('Crie sua senha: ')
        CPFl = input('Digite seu CPF sem pontos ou traços: ')
        print('=' * 5, 'CONFIRMAÇÃO DE INFORMAÇÕES', '=' * 5)
        print(f'\nNome: {nome}\nLogin: {log1}\nCPF: {CPFl}\nSenha: {"*" * len(senh1)}')

        conf = input('Digite 1 para confirmar ou 2 para voltar: ')
        if conf == '1':
            hash_da_senha = gerar_hash(senh1)
            dados_para_salvar = {'nome': nome, 'login': log1, 'cpf': CPFl, 'hash_senha': hash_da_senha}
            with open(arquivo_dos_dados_login, 'w', encoding='utf-8') as f:
                json.dump(dados_para_salvar, f, indent=4)
            print("\n\033[1;92mCadastro realizado com sucesso!\033[0m")
            print("Por favor, reinicie o programa para fazer o login.")
            break
        elif conf == '2':
            print("\nOk, vamos tentar novamente.\n")
        else:
            print("\nOpção inválida. Por favor, tente novamente.\n")

if login_confirmado:
    arquivo_financeiro = "{}_financas.json".format(login)

    try:
        with open(arquivo_financeiro, 'r', encoding='utf-8') as f:
            transacoes = json.load(f)
    except FileNotFoundError:
        transacoes = []

    while True:
        print('\n*** Meu Gestor de Finanças Pessoais ***')
        print('[1] Adicionar Receita \n[2] Adicionar Despesa \n[3] Ver Resumo de Transações \n[4] Ver Saldo Atual \n[5] Sair e Salvar')
        opc = input('Digite uma opção: ')

        if opc == '1':
            try:
                valor = float(input("Digite o valor da receita: R$ ").strip())
                descricao = input("Digite a descrição da receita (ex: Salário): ").strip()
                transacoes.append({'tipo': 'receita', 'valor': valor, 'descricao': descricao})
                print('\033[1;92mReceita adicionada com sucesso!\033[0m')
            except ValueError:
                print("\033[1;91mErro: Por favor, digite um valor numérico válido.\033[0m")

        elif opc == '2':
            try:
                valor = float(input("Digite o valor da despesa: R$ ").strip())
                descricao = input("Digite a descrição da despesa (ex: Aluguel): ").strip()
                transacoes.append({'tipo': 'despesa', 'valor': valor, 'descricao': descricao})
                print('\033[1;92mDespesa adicionada com sucesso!\033[0m')
            except ValueError:
                print("\033[1;91mErro: Por favor, digite um valor numérico válido.\033[0m")

        elif opc == '3':
            print("\n--- Resumo de Transações ---")
            if not transacoes:
                print("Nenhuma transação registrada.")
            for transacao in transacoes:
                if transacao['tipo'] == 'receita':
                    print(f"[+] Receita: R$ {transacao['valor']:.2f} - {transacao['descricao']}")
                else:
                    print(f"[-] Despesa: R$ {transacao['valor']:.2f} - {transacao['descricao']}")

        elif opc == '4':
            total_receitas = sum(t['valor'] for t in transacoes if t['tipo'] == 'receita')
            total_despesas = sum(t['valor'] for t in transacoes if t['tipo'] == 'despesa')
            saldo = total_receitas - total_despesas
            print(f"\n--- Saldo Atual ---")
            print("Total de Receitas: R$ {}".format(total_receitas))
            print("Total de Despesas: R$ {}".format(total_despesas))
            print("Saldo Final: R$ {}".format(saldo))

        elif opc == '5':
            with open(arquivo_financeiro, 'w', encoding='utf-8') as f:
                json.dump(transacoes, f, indent=4)
            print("\nDados financeiros salvos com sucesso. Até logo!")
            break

        else:
            print("\033[1;91mOpção inválida. Por favor, tente novamente.\033[0m")