#1ESPA25 Sprint 3
#Felipe Menezes | RM:566607
#Gabriel Ardito | RM:568318
#João Sarracine | RM:567407
#João Gonzales | RM:568166

def boas_vindas()->None:
    '''Essa função tem com objetivo dar boas vindas ao usuário'''
    print('Boa Vindas')
    print(r'''  ___   __   ____  ____    ____  __    _  _  ____       
 / __) / _\ (  _ \(  __)  (  _ \(  )  / )( \/ ___)      
( (__ /    \ )   / ) _)    ) __// (_/\) \/ (\___ \      
 \___)\_/\_/(__\_)(____)  (__)  \____/\____/(____/      ''')
    print()
def aceitar_lgpd()->None:
    '''Essa função tem como objetivo mostrar os termos de lgpd para o usuário aceitar ou não'''
    print('Termos de concentimento:')
    print('Na Care Plus levamos a sério o tratamento de\n'
          'dados dos nossos usuários, por isso elaboramos\n'
          'um resumo de tudo que será requisitado no\n'
          'recurso BoostCare')
    print()
    print('Como tratamos seus dados?')
    print("""Para personalizar missões, acompanhar seu progresso e liberar
    recompensas, precisamos acessar algumas informações de saúde.
    Tudo é tratado com segurança, transparência e apenas
    para fins de bem-estar.

    O que coletamos:
    - passos, distância e calorias
    - horas de sono
    - hidratação
    - BPM e dados do smartwatch
    - informações do scan diário (pele e sinais faciais)

    Para que usamos:
    - criar missões e desafios
    - liberar pontos, troféus e recompensas
    - gerar recomendações personalizadas
    - oferecer suporte no Mind+
    - melhorar sua experiência no app

    Você decide:
    - permitir dados de atividade
    - permitir dados de sono
    - permitir BPM/smartwatch
    - participar do ranking (opt-in)
    - receber notificações
    - revogar tudo a qualquer momento

    Seus dados não são vendidos e não aparecem para outros
    usuários — apenas seu desempenho dentro
    dos desafios.

    Botões — Gerencie seus dados e permissões:
    - Ver dados coletados
    - Editar consentimentos
    - Sair do ranking
    - Alterar / Excluir dados de saúde
    - Revogar consentimento

    Seus dados estão protegidos pela LGPD.
    """)
    while True:
        escolha:str = input("Deseja aceitar os termos de LGPD? S/N:").lower()
        match escolha:
            case "s":
                print('Obrigado por aceitar os termos de LGPD!')
                print()
                break
            case "n":
                print('Termos não aceitos!')
                print()
                exit()
            case _:
                print("Escolha uma opção váida!")
                print()
                continue
id_usuario = None
def pedir_login()->None:
    '''Essa função tem como objetivo perguntar se o usuário ja é registrado ou deseja fazer login'''
    print('Bem vindo a página de login da Care Plus')
    global id_usuario
    while True:
        escolha:str = input("Caso seja sua primeira vez digite 'login', caso ja tenha conta, digite 'entrar':").lower()
        match escolha:
            case "login":
                login()
                break
            case "entrar":
                id_usuario = entrar()
                break

            case _:
                print('Digite uma opção válida!')
                continue

def login()->None:
    '''Essa função tem como objetivo realizar o login do usuário'''
    streak = '0'
    print()
    print('Login da Care Plus')
    confirmarSenha:str=''
    while True:
        try:
            nome:str = input('Digite seu nome: ')

            if not nome.replace(" ", "").isalpha():
                raise ValueError

        except ValueError:
            print("O nome deve conter apenas letras!")
            continue
        break

    while True:
        try:
            numeroCarteirinha:int = int(input('Digite o número da carteirinha: '))

        except ValueError:
            print('O número de carteirinha deve conter apenas números!')
            continue
        break

    while True:
        try:
            senha:str = input('Digite sua senha:')

            if len(senha)<8:
                print("A senha deve ter mais de 8 caracteres.")
                continue

            if senha.isalnum(): #Verifica se tem caractere especial
                print('A senha precisa ter pelo menos um caractere especial!')
                continue

        except ValueError:
            print('Erro inesperado!')
        break
    global id_usuario  # Mantem uma variavél global
    id_usuario = numeroCarteirinha
    while True:
        if senha != confirmarSenha:
            print('As senhas precisam ser identicas!')
            confirmarSenha = input('Digite a senha novamente:')
            continue
        else:
            print('Login realizado com sucesso!')

            #pergunta para as missões
            respostas = missoes_contextuais()

            #adiciona no arquivo
            with open('users.txt', 'a',encoding='utf-8')  as u:
                u.write(";".join([
                    str(numeroCarteirinha),
                    nome,
                    senha,
                    streak,
                    ",".join(map(str, respostas))
                ]) + "\n")

            #Estrutura dentro do arquivo
            #[id];[nome];[senha];[streak];[respostas]

            break
def entrar() -> bool:
    print('Para acessar sua conta digite:')

    while True:
        try:
            numeroCarteirinha = int(input('Número da carteirinha: '))
        except ValueError:
            print('O número de carteirinha deve conter apenas números!')
            continue

        senha = input('Digite sua senha: ')

        if len(senha) < 8:
            print("A senha deve ter mais de 8 caracteres.")
            continue

        if senha.isalnum():
            print('A senha precisa ter pelo menos um caractere especial!')
            continue

        # verifica no arquivo
        encontrado = False

        with open("users.txt", "a+") as f:
            f.seek(0)
            for linha in f:
                if linha.strip() == "":
                    continue

                id_, nome, senha_salva, streak, respostas = linha.strip().split(";")

                if numeroCarteirinha == int(id_) and senha == senha_salva:
                    print(f"Bem-vindo, {nome}!")
                    return int(id_)
        # se não encontrou
        print("Carteirinha ou senha incorretos!")

        opcao = input('Digite "criar" para criar conta ou Enter para tentar novamente: ').lower()

        if opcao == "criar":
            login()
            return False
    return None

def perguntar_numerico(pergunta):
    while True:
        try:
            valor = float(input(pergunta))
            return valor
        except ValueError:
            print("Digite um número válido!")

def missoes_contextuais() ->list:
    print('Agora responda algumas perguntas para melhorarmos sua experiência')
    respostas:list = []
    perguntas = [
        'Quantos dias por semana você pratica atividade física? ',
        'Quantos minutos você passa sentado por dia? ',
        'Qual a distância média que você percorre por dia (em km)? ',
        'Quantos litros de água você bebe por dia? ',
        'Quantas horas você dorme por noite? ',
        'Quantas horas por dia você passa no celular? ',
        'Quantas pausas você faz durante o dia? ',
        'Quantos copos de cafeína você consome por dia? ',
        'Quantos minutos por dia você passa ao ar livre? ',
        'Quantas refeições você faz por dia? '
    ]



    for p in perguntas:
        respostas.append(perguntar_numerico(p))
    return respostas

def definir_missoes(id_usuario) -> None:
    with open("users.txt", "r", encoding="utf-8", errors='ignore') as f:
        for linha in f:
            if linha.strip() == "":
                continue

            id_, nome, senha, streak, respostas_str = linha.strip().split(";")

            if int(id_) != id_usuario:
                continue  # ignora outros usuários

            # achou o usuário certo
            id_ = int(id_)
            streak = int(streak)
            respostas = list(map(float, respostas_str.split(",")))

            print("ID:", id_)
            print("Nome:", nome)
            print("Streak:", streak)
            print("Respostas:", respostas)

            break  # para o loop depois de achar

def menu():
    while True:
        print("\n" + "=" * 40)
        print("        CARE PLUS - MENU")
        print("=" * 40)
        print("1 - Missões Ativas")
        print("2 - Benefícios")
        print("3 - Mind+")
        print("4 - Scan Diário")
        print("5 - Conect+")
        print("6 - Notícias")
        print("7 - Meu Perfil")
        print("0 - Sair")
        print("=" * 40)

        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                print("\nAcessando Missões Ativas...\n")

            case "2":
                print("\nAcessando Benefícios...\n")

            case "3":
                print("\nAcessando Mind+...\n")

            case "4":
                print("\nAcessando Scan Diário...\n")

            case "5":
                print("\nAcessando Conect+...\n")

            case "6":
                print("\nAcessando Notícias...\n")

            case "7":
                print("\nAcessando Meu Perfil...\n")

            case "0":
                print("\nEncerrando... Até mais!")
                break

            case _:
                print("\n Opção inválida! Tente novamente.\n")

boas_vindas()
aceitar_lgpd()
pedir_login()
definir_missoes(id_usuario)
#menu()
