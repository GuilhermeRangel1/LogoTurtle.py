# Logo Turtle

Este é um projeto de interface de linha de comando em Python desenvolvido com a biblioteca `curses`. O "Logo Turtle" simula uma interface gráfica em modo texto, permitindo desenhar ou apagar linhas em uma matriz por meio de comandos específicos. O usuário pode controlar a "tartaruga" para mover-se em diferentes direções e distâncias.

## Funcionalidades

- **Modo de desenho**: permite que o usuário desenhe com o símbolo `@`.
- **Modo de borracha**: permite que o usuário apague com o símbolo `#`.
- **Comandos de movimento**: mova a tartaruga em oito direções (norte, sul, leste, oeste, nordeste, noroeste, sudeste, sudoeste).
- **Limpeza da tela**: apague todos os desenhos feitos na matriz.
- **Navegação entre menus**: selecione entre diferentes opções, como JOGAR, INSTRUÇÕES e CRÉDITOS.

## Menu Principal

- **TAMANHO DA MATRIZ**: Exibido na parte superior.
- **POSIÇÃO ATUAL**: Exibida na parte inferior.
- **LOGO TURTLE**: Título do projeto.
- **JOGAR**: Inicia o modo de desenho.
- **INSTRUÇÕES**: Mostra as instruções do jogo.
- **CRÉDITOS**: Exibe os créditos do projeto.
- **SAIR**: Fecha o programa.

## Instruções de Jogo

1. **Mudar de Modo**: Digite `modo 1` para o modo de desenho ou `modo 2` para o modo de borracha.
2. **Comandos de Movimento**:
    - **Norte**: `n`
    - **Sul**: `s`
    - **Leste**: `l`
    - **Oeste**: `o`
    - **Nordeste**: `ne`
    - **Noroeste**: `no`
    - **Sudeste**: `se`
    - **Sudoeste**: `so`
3. **Definir a Distância**: Após especificar a direção, insira a distância a ser percorrida. Exemplo: `n 20` para mover 20 unidades para o norte.
4. **Limpar a Tela**: Digite `apagar` para limpar toda a matriz.
5. **Sair para o Menu Principal**: Digite `sair` a qualquer momento para retornar ao menu.

## Exemplos de Uso

```text
n 10      # Move para o norte por 10 unidades
se 5      # Move para o sudeste por 5 unidades
modo 1    # Ativa o modo de desenho (@)
modo 2    # Ativa o modo de borracha (#)
apagar    # Limpa toda a tela
sair      # Retorna ao menu principal
```
# Pré-requisitos

1. Instalar o Python:
   - Baixe e instale o Python a partir do site oficial: https://www.python.org/downloads/
   - Certifique-se de marcar a opção "Add Python to PATH" durante a instalação.

2. Instalar o Curses no Windows:
   - O `curses` não está disponível nativamente no Windows. Para usar o `curses`, instale a biblioteca `windows-curses`:
     pip install windows-curses

# Passos para Executar o Projeto

1. Baixar o Código:
   - Clone ou baixe o repositório contendo o código do projeto.

2. Abrir o Prompt de Comando:
   - No Windows, pressione `Win + R`, digite `cmd` e pressione `Enter`.

3. Navegar até o Diretório do Projeto:
   cd caminho\para\o\diretorio\do\projeto

4. Executar o Programa:
   python jogo.py
