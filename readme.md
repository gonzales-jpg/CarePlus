# Care Plus - Sistema de Bem-Estar

## Descrição

O Care Plus é um sistema em Python voltado para promoção de saúde e bem-estar dos usuários. Ele utiliza dados informados pelo próprio usuário para gerar missões personalizadas, incentivar hábitos saudáveis e oferecer recompensas por meio de um sistema de troféus.

O projeto simula funcionalidades de um aplicativo de saúde, incluindo login, acompanhamento de atividades, desafios diários, recompensas e suporte ao bem-estar mental.

---

## Funcionalidades

### Cadastro e Login

* Criação de conta com validação de dados
* Autenticação de usuário via número da carteirinha e senha
* Armazenamento de dados em arquivo local

### LGPD

* Exibição de termos de consentimento
* Aceitação obrigatória para uso do sistema
* Explicação sobre coleta e uso de dados

### Missões Personalizadas

* Coleta de dados de hábitos do usuário
* Geração de missões baseadas no estilo de vida
* Sistema de recompensas com troféus

### Sistema de Troféus

* Acúmulo de troféus ao completar missões
* Resgate de benefícios
* Atualização persistente em arquivo

### Streak

* Contagem de dias consecutivos completando missões
* Atualização automática após completar 3 missões

### Módulos do Sistema

#### 1. Missões

* Visualização de missões ativas
* Conclusão de missões
* Geração de novas missões

#### 2. Benefícios

* Loja de recompensas
* Troca de troféus por benefícios

#### 3. Mind+

* Conteúdo de apoio à saúde mental
* Técnicas de ansiedade
* Informações sobre ajuda psicológica

#### 4. Connect+

* Integração simulada com dispositivos inteligentes
* Monitoramento de dados de saúde

#### 5. Notícias

* Informações sobre saúde e bem-estar

#### 6. Perfil

* Visualização de dados do usuário
* Informações de progresso

---

## Estrutura do Projeto

```
.
├── 1ESPA25-Sprint-3.py
├── users.txt
├── missoesgenericas.txt
```

### Arquivos

* **1ESPA25-Sprint-3.py**
  Código principal do sistema 

* **users.txt**
  Armazena dados dos usuários no formato:

  ```
  id;nome;senha;streak;trofeus;respostas
  ```

* **missoesgenericas.txt**
  Lista de missões genéricas utilizadas no sistema

---

## Como Executar

### Pré-requisitos

* Python 3 instalado

### Passos

1. Clone ou baixe o projeto
2. Certifique-se de que os arquivos `users.txt` e `missoesgenericas.txt` existem
3. Execute o programa:

```bash
python 1ESPA25-Sprint-3.py
```

---

## Fluxo do Sistema

1. Exibe mensagem de boas-vindas
2. Solicita aceite dos termos LGPD
3. Realiza login ou cadastro
4. Coleta dados do usuário
5. Gera missões personalizadas
6. Exibe menu principal com opções:

   * Missões
   * Benefícios
   * Mind+
   * Streak
   * Connect+
   * Notícias
   * Perfil

---

## Tecnologias Utilizadas

* Python 3
* Manipulação de arquivos (I/O)
* Estruturas de controle (if, while, match-case)
* Listas e manipulação de strings

---

## Lógica de Personalização

O sistema coleta dados como:

* Atividade física
* Tempo sedentário
* Consumo de água
* Sono
* Uso de celular
* Alimentação

Com base nisso, define missões específicas para melhorar hábitos do usuário.

---

## Sistema de Armazenamento

Os dados são armazenados localmente em arquivos `.txt`, sem uso de banco de dados.

### Vantagens:

* Simplicidade
* Fácil implementação

### Limitações:

* Escalabilidade limitada
* Sem criptografia de dados

---

## Possíveis Melhorias

* Implementação de banco de dados (SQLite, PostgreSQL)
* Interface gráfica (Tkinter ou Web)
* Integração real com APIs de saúde
* Sistema de autenticação mais seguro (hash de senha)
* Dashboard com gráficos de progresso
* Notificações automáticas

---

## Autores

* Felipe Menezes
* Gabriel Ardito
* João Sarracine
* João Gonzales

---

## Observações

Este projeto é acadêmico e tem como objetivo demonstrar conceitos de programação, lógica e estruturação de sistemas voltados para experiência do usuário e bem-estar.

---

## Licença

Uso educacional.
