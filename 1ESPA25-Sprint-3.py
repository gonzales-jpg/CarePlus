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
    trofeus = '0'
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
                    trofeus,
                    ",".join(map(str, respostas))
                ]) + "\n")

            #Estrutura dentro do arquivo
            #[id];[nome];[senha];[streak];[trofeus],[respostas]

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

        with open("users.txt", "a+", encoding='utf-8') as f:
            f.seek(0)
            for linha in f:
                if linha.strip() == "":
                    continue

                id_, nome, senha_salva, streak,trofeus, respostas = linha.strip().split(";")

                if numeroCarteirinha == int(id_) and senha == senha_salva:
                    print(f"Bem-vindo, {nome}!")
                    return int(id_)
        # se não encontrou
        print("Carteirinha ou senha incorretos!")

        opcao = input('Digite "criar" para criar conta ou Enter para tentar novamente: ').lower()

        if opcao == "criar":
            login()
            return id_usuario

        elif opcao == "":
            continue  # tenta novamente

        else:
            print("Opção inválida! Digite apenas 'criar' ou pressione Enter.")
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
    missoes = []

    with open("users.txt", "r", encoding="utf-8", errors='ignore') as f:
        for linha in f:
            if linha.strip() == "":
                continue

            id_, nome, senha, streak,trofeus, respostas_str = linha.strip().split(";")

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


            # atividade física
            if dias_atividade == 0:
                missoes.append("Comece com 1 dia de atividade física essa semana | 50 troféus")
            elif dias_atividade <= 2:
                missoes.append("Aumente para 3 dias de atividade física | 40 troféus")
            else:
                missoes.append("Mantenha sua rotina ativa e faça 1 atividade hoje | 30 troféus")

            # tempo sentado
            if tempo_sentado > 600:
                missoes.append("Levante-se e caminhe por 5 minutos agora | 40 troféus")
            elif tempo_sentado > 300:
                missoes.append("Faça uma pausa para alongamento | 30 troféus")
            else:
                missoes.append("Ótimo! Continue se movimentando ao longo do dia | 20 troféus")

            # distância
            if distancia < 1:
                missoes.append("Caminhe pelo menos 1 km hoje | 40 troféus")
            elif distancia < 3:
                missoes.append("Tente aumentar sua caminhada para 3 km | 30 troféus")
            else:
                missoes.append("Excelente! Continue com seu nível de movimento | 20 troféus")

            # água
            if agua < 1:
                missoes.append("Beba pelo menos 1 litro de água hoje | 40 troféus")
            elif agua < 2:
                missoes.append("Tente atingir 2 litros de água hoje | 30 troféus")
            else:
                missoes.append("Ótimo! Continue se hidratando bem | 20 troféus")

            # sono
            if sono < 5:
                missoes.append("Durma pelo menos 6 horas hoje | 50 troféus")
            elif sono < 7:
                missoes.append("Tente melhorar seu sono para 7-8 horas | 40 troféus")
            else:
                missoes.append("Excelente! Continue com um bom descanso | 20 troféus")

            # celular
            if celular > 8:
                missoes.append("Reduza 1 hora de uso do celular hoje | 50 troféus")
            elif celular > 5:
                missoes.append("Tente diminuir o tempo de tela | 40 troféus")
            else:
                missoes.append("Ótimo controle de tempo de tela! | 20 troféus")

            # pausas
            if pausas == 0:
                missoes.append("Faça pelo menos 2 pausas hoje | 40 troféus")
            elif pausas < 3:
                missoes.append("Aumente para 3 pausas ao longo do dia | 30 troféus")
            else:
                missoes.append("Ótimo! Continue fazendo pausas regulares | 20 troféus")

            # cafeína
            if cafeina > 5:
                missoes.append("Reduza o consumo de cafeína hoje | 40 troféus")
            elif cafeina > 2:
                missoes.append("Tente diminuir um pouco a cafeína | 30 troféus")
            else:
                missoes.append("Bom controle no consumo de cafeína | 20 troféus")

            # ar livre
            if ar_livre < 10:
                missoes.append("Passe pelo menos 10 minutos ao ar livre hoje | 40 troféus")
            elif ar_livre < 30:
                missoes.append("Tente ficar 30 minutos ao ar livre | 30 troféus")
            else:
                missoes.append("Ótimo! Continue aproveitando o tempo externo | 20 troféus")

            # refeições
            if refeicoes < 3:
                missoes.append("Faça pelo menos 3 refeições hoje | 40 troféus")
            elif refeicoes <= 4:
                missoes.append("Tente manter uma alimentação equilibrada | 30 troféus")
            else:
                missoes.append("Cuidado com excessos, mantenha equilíbrio | 20 troféus")

            break  # para o loop depois de achar
    return missoes
def menu(missoes_escolhidas,contador,id_usuario,trofeus_usuario):
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
                contador, trofeus_usuario, missoes_escolhidas = mostrar_missoes(
                    missoes_escolhidas,
                    contador,
                    id_usuario,
                    trofeus_usuario,
                    missoes
                )

            case "2":
                print("\nAcessando Benefícios...\n")
                trofeus_usuario = beneficios_menu(trofeus_usuario)

            case "3":
                print("\nAcessando Mind+...\n")
                mind_plus()

            case "4":
                print("\nAcessando Seu Streak...\n")
                atualizar_streak_arquivo(id_usuario,contador)

            case "5":
                print("\nAcessando Conect+...\n")
                connect_plus()

            case "6":
                print("\nAcessando Notícias...\n")
                noticias()

            case "7":
                print("\nAcessando Meu Perfil...\n")
                perfil(id_usuario)
            case "0":
                print("\nEncerrando... Até mais!")
                break

            case _:
                print("\n Opção inválida! Tente novamente.\n")

def gerar_missoes(missoes):
    import random

    missoes_escolhidas = random.sample(missoes, min(2, len(missoes)))

    with open('missoesgenericas.txt', 'r',encoding='utf-8') as m:
        missoes_genericas = [linha.strip() for linha in m.readlines()]

    missoes_escolhidas += random.sample(missoes_genericas, 1)

    return missoes_escolhidas

contador = 0

def mostrar_missoes(missoes_escolhidas, contador, id_usuario, trofeus_usuario, todas_missoes):
    if len(missoes_escolhidas) == 0:
        print("\nVocê não possui mais missões ativas.")

        escolha = input("Deseja gerar novas missões? (s/n): ").lower()

        if escolha == "s":
            missoes_escolhidas = gerar_missoes(todas_missoes)
            contador = 0

        else:
            return contador, trofeus_usuario, missoes_escolhidas

    print("\n" + "=" * 40)
    print("        MISSÕES ATIVAS")
    print("=" * 40)

    for i, m in enumerate(missoes_escolhidas, 1):
        print(f"{i} - {m}")

    print("=" * 40)

    try:
        escolha = int(input('Digite o número da missão que você realizou (0 para nenhuma): '))
    except ValueError:
        print("Entrada inválida!")
        return contador, trofeus_usuario, missoes_escolhidas

    if escolha == 0:
        return contador, trofeus_usuario, missoes_escolhidas

    if 1 <= escolha <= len(missoes_escolhidas):
        removida = missoes_escolhidas.pop(escolha - 1)

        trofeus_ganhos = int(removida.split("|")[1].split()[0])

        print(f"Missão concluída: {removida}")
        print(f"Você ganhou {trofeus_ganhos} troféus!")

        atualizar_trofeus_arquivo(id_usuario, trofeus_ganhos)
        trofeus_usuario = pegar_trofeus(id_usuario)

        contador += 1

    else:
        print("Número inválido!")

    return contador, trofeus_usuario, missoes_escolhidas

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

            id_, nome, senha, streak,trofeus, respostas = partes

            if int(id_) == id_usuario:
                streak = str(int(streak) + 1)
                print(f"Streak atualizado! Novo streak: {streak}")

            nova_linha = ";".join([id_, nome, senha, streak,trofeus, respostas])
            linhas.append(nova_linha)

    # reescreve o arquivo inteiro
    with open("users.txt", "w", encoding="utf-8") as f:
        for l in linhas:
            f.write(l + "\n")

def mind_plus():
    print("\n" + "=" * 40)
    print("           MIND+")
    print("=" * 40)
    print("Pedir ajuda não é sinal de fraqueza,")
    print("é a coragem de escolher cuidar de si.")
    print("=" * 40)

    while True:
        print()
        print('1. Quando procurar um psicólogo?')
        print('   Atento a sinais de alteração da saúde mental')
        print()
        print('2. Crise de ansiedade?')
        print('   Técnica 5-4-3-2-1')
        print()
        print('3. Não está se sentindo bem?')
        print('   Centro de Valorização da Vida')
        print()
        print('4. Reduzir tensão?')
        print('   Método simples de relaxamento')
        print()
        print('5. Pronto atendimento')
        print()
        print('0. Voltar')

        escolha = input('Digite o número da opção: ')

        match escolha:
            case "1":
                print("\nQuando procurar um psicólogo:")
                print("- Quando você sente tristeza constante ou desânimo")
                print("- Dificuldade para lidar com emoções")
                print("- Ansiedade frequente ou crises")
                print("- Problemas de sono ou concentração")
                print("- Sensação de estar sobrecarregado")
                print("Procurar ajuda é um passo importante para o bem-estar.\n")

            case "2":
                print("\nTécnica 5-4-3-2-1 para ansiedade:")
                print("Observe ao seu redor e identifique:")
                print("5 coisas que você pode ver")
                print("4 coisas que pode tocar")
                print("3 coisas que pode ouvir")
                print("2 coisas que pode cheirar")
                print("1 coisa que pode saborear")
                print("Isso ajuda a trazer sua atenção para o presente.\n")

            case "3":
                print("\nCentro de Valorização da Vida (CVV):")
                print("Você pode ligar gratuitamente para o número 188")
                print("Atendimento 24 horas por dia, todos os dias")
                print("Também disponível via chat no site oficial")
                print("Você não está sozinho.\n")

            case "4":
                print("\nMétodo de 2 minutos para reduzir tensão:")
                print("1. Pare o que estiver fazendo")
                print("2. Inspire profundamente pelo nariz por 4 segundos")
                print("3. Segure o ar por 4 segundos")
                print("4. Solte lentamente pela boca por 6 segundos")
                print("5. Repita por 2 minutos")
                print("Isso ajuda a desacelerar o corpo e a mente.\n")

            case "5":
                print("\nPronto atendimento:")
                print("Sua solicitação foi registrada.")
                print("Você será contatado em breve por um profissional.\n")

            case "0":
                break

            case _:
                print('Digite um número válido')

def connect_plus():
    '''Essa função tem como objetivo mostrar o menu da conectividade do sistema com relogios inteligentes'''
    print("\n" + "=" * 40)
    print("          CONNECT+")
    print("=" * 40)
    print("Integre seu dispositivo inteligente")
    print("e acompanhe seus dados em tempo real.")
    print("-" * 40)
    print("Dispositivos compatíveis:")
    print("- Smartwatch")
    print("- Pulseiras fitness")
    print("- Aplicativos de saúde")
    print("-" * 40)
    print("Sincronize passos, batimentos, sono")
    print("e outras informações automaticamente.")
    print("=" * 40)

def noticias():
    '''Essa função tem como objetivo de mostrar as noticias'''
    print("\n" + "=" * 40)
    print("            NOTÍCIAS")
    print("=" * 40)

    print("1. Saúde mental ganha destaque em 2026")
    print("Cresce a busca por apoio psicológico e bem-estar emocional.")
    print("-" * 40)

    print("2. Uso de smartwatches aumenta no Brasil")
    print("Dispositivos ajudam no monitoramento de saúde diária.")
    print("-" * 40)

    print("3. Pequenos hábitos melhoram qualidade de vida")
    print("Especialistas reforçam a importância de rotina saudável.")
    print("-" * 40)

    print("Fique atento às novidades e cuide da sua saúde.")
    print("=" * 40)

def atualizar_trofeus_arquivo(id_usuario, trofeus_ganhos):
    linhas = []

    with open("users.txt", "r", encoding="utf-8") as f:
        for linha in f:
            if linha.strip() == "":
                continue

            id_, nome, senha, streak, trofeus, respostas = linha.strip().split(";")

            if int(id_) == id_usuario:
                novo_total = int(trofeus) + trofeus_ganhos
                trofeus = str(novo_total)
                print(f"Total de troféus agora: {trofeus}")

            nova_linha = ";".join([id_, nome, senha, streak, trofeus, respostas])
            linhas.append(nova_linha)

    with open("users.txt", "w", encoding="utf-8") as f:
        for l in linhas:
            f.write(l + "\n")

def beneficios_menu(trofeus_usuario):
    beneficios = [
        "Desconto de 20% em corridas da Uber | 300 troféus",
        "1 mês grátis de Spotify Premium | 400 troféus",
        "Barrinha de proteína da Growth Supplements | 150 troféus",
        "Desconto de 30% em consulta na Dr. Consulta | 500 troféus",
        "Cupom de R$20 no iFood | 350 troféus",
        "Shake proteico da Max Titanium | 200 troféus",
        "Desconto de 25% em academia Smart Fit | 600 troféus",
        "Garrafa térmica esportiva | 250 troféus",
        "Desconto de R$15 em corrida 99 | 300 troféus",
        "Plano mensal da Headspace (meditação) | 450 troféus",
        "Kit de snacks saudáveis (barra + nuts) | 300 troféus",
        "Desconto de 20% na Decathlon | 400 troféus",
        "Fone esportivo Bluetooth | 700 troféus",
        "Voucher de R$30 em farmácia Drogasil | 500 troféus",
        "Desconto de 25% em massagem relaxante | 600 troféus",
        "Suplemento multivitamínico (1 mês) | 350 troféus",
        "Desconto de 20% em nutricionista | 550 troféus",
        "Camiseta esportiva dry-fit | 450 troféus",
        "Voucher de R$25 na Amazon | 600 troféus",
        "Plano básico do Gympass (1 semana) | 700 troféus"
    ]

    while True:
        print("\n" + "=" * 40)
        print("          BENEFÍCIOS")
        print("=" * 40)
        print(f"Seus troféus: {trofeus_usuario}")
        print("-" * 40)

        for i, b in enumerate(beneficios, 1):
            print(f"{i} - {b}")

        print("=" * 40)
        print("0 - Voltar")

        try:
            escolha = int(input("Escolha um benefício para resgatar: "))

        except ValueError:
            print("Entrada inválida!")
            continue

        if escolha == 0:
            break

        if 1 <= escolha <= len(beneficios):
            beneficio = beneficios[escolha - 1]

            # extrai custo
            custo = int(beneficio.split("|")[1].split()[0])

            if trofeus_usuario >= custo:
                trofeus_usuario -= custo

                remover_trofeus_arquivo(id_usuario, custo)
                removido = beneficios.pop(escolha - 1)

                print("\nBenefício resgatado com sucesso!")
                print(removido)
                print(f"Troféus restantes: {trofeus_usuario}")
            else:
                print("\nTroféus insuficientes!")
        else:
            print("Opção inválida!")

    return trofeus_usuario

def pegar_trofeus(id_usuario):
    with open("users.txt", "r", encoding="utf-8") as f:
        for linha in f:
            if linha.strip() == "":
                continue

            id_, nome, senha, streak, trofeus, respostas = linha.strip().split(";")

            if int(id_) == id_usuario:
                return int(trofeus)

    return 0
def perfil(id_usuario):
    '''Essa função tem como objetivo mostrar os dados do perfil'''
    with open("users.txt", "r", encoding="utf-8") as f:
        for linha in f:
            if linha.strip() == "":
                continue

            id_, nome, senha, streak, trofeus, respostas = linha.strip().split(";")

            if int(id_) == id_usuario:
                print("\n" + "=" * 40)
                print("          MEU PERFIL")
                print("=" * 40)
                print(f"Nome: {nome}")
                print(f"Carteirinha: {id_}")
                print(f"Senha: {senha}")
                print(f"Streak: {streak} dias")
                print(f"Troféus: {trofeus}")
                print("=" * 40)

                return int(trofeus)

def remover_trofeus_arquivo(id_usuario, trofeus_gastos):
    linhas = []

    with open("users.txt", "r", encoding="utf-8") as f:
        for linha in f:
            if linha.strip() == "":
                continue

            id_, nome, senha, streak, trofeus, respostas = linha.strip().split(";")

            if int(id_) == id_usuario:
                novo_total = int(trofeus) - trofeus_gastos
                trofeus = str(novo_total)

            nova_linha = ";".join([id_, nome, senha, streak, trofeus, respostas])
            linhas.append(nova_linha)

    with open("users.txt", "w", encoding="utf-8") as f:
        for l in linhas:
            f.write(l + "\n")


boas_vindas()
aceitar_lgpd()
pedir_login()
trofeus_usuario = pegar_trofeus(id_usuario)
missoes = definir_missoes(id_usuario)
missoes_escolhidas = gerar_missoes(missoes)
menu(missoes_escolhidas,contador,id_usuario,trofeus_usuario)


