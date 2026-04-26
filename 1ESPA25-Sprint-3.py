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

def definir_missoes(id_usuario) -> list:
    with open("users.txt", "r", encoding="utf-8", errors='ignore') as f:
        for linha in f:
            if linha.strip() == "":
                continue

            id_, nome, senha, streak, respostas_str = linha.strip().split(";")

            if int(id_) != id_usuario:
                continue

            respostas = list(map(float, respostas_str.split(",")))

            dias_atividade = respostas[0]
            tempo_sentado = respostas[1]
            distancia = respostas[2]
            agua = respostas[3]
            sono = respostas[4]
            celular = respostas[5]
            pausas = respostas[6]
            cafeina = respostas[7]
            ar_livre = respostas[8]
            refeicoes = respostas[9]

            missoes = []

            # atividade física
            if dias_atividade == 0:
                missoes.append("Comece com 1 dia de atividade física essa semana")
            elif dias_atividade <= 2:
                missoes.append("Aumente para 3 dias de atividade física")
            else:
                missoes.append("Mantenha sua rotina ativa e faça 1 atividade hoje")

            # tempo sentado
            if tempo_sentado > 600:
                missoes.append("Levante-se e caminhe por 5 minutos agora")
            elif tempo_sentado > 300:
                missoes.append("Faça uma pausa para alongamento")
            else:
                missoes.append("Ótimo! Continue se movimentando ao longo do dia")

            # distância
            if distancia < 1:
                missoes.append("Caminhe pelo menos 1 km hoje")
            elif distancia < 3:
                missoes.append("Tente aumentar sua caminhada para 3 km")
            else:
                missoes.append("Excelente! Continue com seu nível de movimento")

            # água
            if agua < 1:
                missoes.append("Beba pelo menos 1 litro de água hoje")
            elif agua < 2:
                missoes.append("Tente atingir 2 litros de água hoje")
            else:
                missoes.append("Ótimo! Continue se hidratando bem")

            # sono
            if sono < 5:
                missoes.append("Durma pelo menos 6 horas hoje")
            elif sono < 7:
                missoes.append("Tente melhorar seu sono para 7-8 horas")
            else:
                missoes.append("Excelente! Continue com um bom descanso")

            # celular
            if celular > 8:
                missoes.append("Reduza 1 hora de uso do celular hoje")
            elif celular > 5:
                missoes.append("Tente diminuir o tempo de tela")
            else:
                missoes.append("Ótimo controle de tempo de tela!")

            # pausas
            if pausas == 0:
                missoes.append("Faça pelo menos 2 pausas hoje")
            elif pausas < 3:
                missoes.append("Aumente para 3 pausas ao longo do dia")
            else:
                missoes.append("Ótimo! Continue fazendo pausas regulares")

            # cafeína
            if cafeina > 5:
                missoes.append("Reduza o consumo de cafeína hoje")
            elif cafeina > 2:
                missoes.append("Tente diminuir um pouco a cafeína")
            else:
                missoes.append("Bom controle no consumo de cafeína")

            # ar livre
            if ar_livre < 10:
                missoes.append("Passe pelo menos 10 minutos ao ar livre hoje")
            elif ar_livre < 30:
                missoes.append("Tente ficar 30 minutos ao ar livre")
            else:
                missoes.append("Ótimo! Continue aproveitando o tempo externo")

            # refeições
            if refeicoes < 3:
                missoes.append("Faça pelo menos 3 refeições hoje")
            elif refeicoes <= 4:
                missoes.append("Tente manter uma alimentação equilibrada")
            else:
                missoes.append("Cuidado com excessos, mantenha equilíbrio")

            break  # para o loop depois de achar
    return missoes

def menu(missoes_escolhidas,contador,id_usuario):
    while True:
        print("\n" + "=" * 40)
        print("        CARE PLUS - MENU")
        print("=" * 40)
        print("1 - Missões Ativas")
        print("2 - Benefícios")
        print("3 - Mind+")
        print("4 - Seu Streak")
        print("5 - Conect+")
        print("6 - Notícias")
        print("7 - Meu Perfil")
        print("0 - Sair")
        print("=" * 40)

        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                print("\nMissões ativas\n")
                contador = mostrar_missoes(missoes_escolhidas, contador)

            case "2":
                print("\nAcessando Benefícios...\n")

            case "3":
                print("\nAcessando Mind+...\n")

            case "4":
                print("\nAcessando Seu Streak...\n")
                atualizar_streak_arquivo(id_usuario,contador)

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

def gerar_missoes(missoes):
    import random

    missoes_escolhidas = random.sample(missoes, min(2, len(missoes)))

    with open('missoesgenericas.txt', 'r') as m:
        missoes_genericas = [linha.strip() for linha in m.readlines()]

    missoes_escolhidas += random.sample(missoes_genericas, 1)

    return missoes_escolhidas

contador = 0
def mostrar_missoes(missoes_escolhidas,contador):

    print("\n" + "=" * 40)
    print("        MISSÕES ATIVAS")
    print("=" * 40)

    for i, m in enumerate(missoes_escolhidas, 1): #enumerate pega o indice e o valor de uma lista
        print(f"{i} - {m}")

    print("=" * 40)

    try:
        escolha = int(input('Digite o número da missão que você realizou (0 para nenhuma): '))
    except ValueError:
        print("Entrada inválida!")
        return contador

    if escolha == 0:
        return contador

    if 1 <= escolha <= len(missoes_escolhidas):
        removida = missoes_escolhidas.pop(escolha - 1)
        print(f"Missão concluída: {removida}")
        contador += 1
    else:
        print("Número inválido!")
    return contador

def atualizar_streak_arquivo(id_usuario, contador):
    if contador < 3:
        print("Você ainda não completou 3 missões.")
        return

    linhas = []

    with open("users.txt", "r", encoding="utf-8") as f:
        for linha in f:
            if linha.strip() == "":
                continue

            partes = linha.strip().split(";")

            id_, nome, senha, streak, respostas = partes

            if int(id_) == id_usuario:
                streak = str(int(streak) + 1)
                print(f"Streak atualizado! Novo streak: {streak}")

            nova_linha = ";".join([id_, nome, senha, streak, respostas])
            linhas.append(nova_linha)

    # reescreve o arquivo inteiro
    with open("users.txt", "w", encoding="utf-8") as f:
        for l in linhas:
            f.write(l + "\n")


boas_vindas()
aceitar_lgpd()
pedir_login()
missoes = definir_missoes(id_usuario)
missoes_escolhidas = gerar_missoes(missoes)
menu(missoes_escolhidas,contador,id_usuario)
