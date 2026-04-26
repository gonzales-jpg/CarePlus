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

def pedir_login()->None:
    '''Essa função tem como objetivo perguntar se o usuário ja é registrado ou deseja fazer login'''
    print('Bem vindo a página de login da Care Plus')
    while True:
        escolha:str = input("Caso seja sua primeira vez digite 'login', caso ja tenha conta, digite 'entrar':").lower()
        match escolha:
            case "login":
                login()
                break
            case "entrar":
                entrar()
                break
            case _:
                print('Digite uma opção válida!')
                continue

def login()->None:
    '''Essa função tem como objetivo realizar o login do usuário'''
    print()
    print('Login da Care Plus')
    confirmarSenha:str=''
    users = {}
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

    while True:
        if senha != confirmarSenha:
            print('As senhas precisam ser identicas!')
            confirmarSenha = input('Digite a senha novamente:')
            continue
        else:
            print('Login realizado com sucesso!')
            #adiciona no arquivo
            with open('users.txt', 'a') as u:
                u.write(";".join([str(numeroCarteirinha), nome, senha]) + "\n")
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

                id_, nome, senha_salva = linha.strip().split(";")

                if numeroCarteirinha == int(id_) and senha == senha_salva:
                    print(f"Bem-vindo, {nome}!")
                    return True

        # se não encontrou
        print("Carteirinha ou senha incorretos!")

        opcao = input('Digite "criar" para criar conta ou Enter para tentar novamente: ').lower()

        if opcao == "criar":
            login()
            return False

def perguntar_numerico(pergunta):
    while True:
        try:
            valor = float(input(pergunta))
            return valor
        except ValueError:
            print("Digite um número válido!")


def missoes_contextuais():
    print('Agora responda algumas perguntas para melhorarmos sua experiência')

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

    respostas = []

    for p in perguntas:
        respostas.append(perguntar_numerico(p))

    print(respostas)
''''boas_vindas()
aceitar_lgpd()
pedir_login()'''
missoes_contextuais()
