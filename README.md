# Blackjack Game

Um jogo simples de **Blackjack** implementado em Python, com funcionalidades de **depósito**, **retirada** e **gestão de chips**. O jogo simula transações de dinheiro virtual, com autenticação de usuários, e oferece uma experiência de cassino interativa.

## Funcionalidades

- **Cadastro e login de usuários**: Permite criar contas e fazer login para salvar o progresso do jogo.
- **Gestão de chips**: Realize depósitos e retiradas de chips antes de começar o jogo.
- **Jogo de Blackjack**: Jogue o tradicional Blackjack contra o dealer.
- **Registro de transações**: Todas as ações financeiras são registradas e salvas em arquivos JSON.
- **Armazenamento persistente**: Dados de usuários e transações são salvos em arquivos JSON, garantindo que o progresso seja mantido.

## Estrutura do Projeto

O projeto é dividido nas seguintes partes:

- **Controller**: Lógica do jogo, transações e autenticação de usuários.
- **Model**: Representação dos dados de transações e usuários.
- **View**: Interface do usuário que exibe mensagens e interage com o usuário via terminal.
- **Utils**: Funções auxiliares, como a validação de entradas do usuário.

## Requisitos

- Python 3.6 ou superior
- Biblioteca padrão do Python (não há dependências externas)

## Instalação

Clone o repositório para a sua máquina:

```bash
git clone https://github.com/seu-usuario/blackjack-game.git
cd blackjack-game
```

Não é necessário instalar dependências externas para este projeto.

## Como Rodar

Para rodar o projeto, basta executar o arquivo principal. Execute no terminal:

```bash
python main.py
```

Isso iniciará o jogo e pedirá para você realizar o login ou criar uma nova conta, e então você poderá jogar o Blackjack.

## Fluxo do Jogo

1. **Cadastro/Login**: O usuário é solicitado a criar uma conta ou fazer login.
2. **Depósito/Retirada**: O usuário pode depositar dinheiro para jogar ou retirar qualquer valor antes de jogar (desde que esteja disponível em sua conta).
3. **Jogo de Blackjack**: O jogo de Blackjack é jogado com o objetivo de atingir o maior valor possível sem ultrapassar 21 pontos.
4. **Final do Jogo**: Após a partida, o saldo do jogador é atualizado e o usuário pode optar por jogar novamente ou sair.

## Exemplo de Uso

### Cadastro de novo usuário

1. Escolha a opção de **registrar** e forneça um nome de usuário e senha.

### Realizar Depósito

1. Antes de jogar, o jogador pode realizar um depósito de chips, que serão adicionados ao seu saldo.

### Jogo de Blackjack

1. Escolha entre **Hit** (pedir uma carta) ou **Stand** (manter as cartas atuais).
2. O objetivo é chegar o mais próximo possível de 21 sem ultrapassar esse valor.

### Finalização da Partida

Após o fim da partida, o saldo é atualizado e o jogador pode continuar jogando ou sair.

