import curses
from curses import wrapper
import re

#definições de configurações da tela.
def ci(tela):
    tela.clear()
    curses.curs_set(1)
    curses.echo()
#criação de uma função para formatar coordenadas abaixo inferirores a 10
def transfStr(a):
    if (a < 10) :
        return "0" + str(a)
    else : 
        return str(a)
#função que digita a frase que indica a atual posição da turtle
def coord(dx,dy):
    frase = "x,y = (" + dx + "," + dy + ")"
    return frase
#função que cria a janela de movimentação da turtle
def criacaoJanela(alturaJanela,largura,posicaox,posicaoy):
    janela = curses.newwin(alturaJanela,largura,posicaox,posicaoy)
    janela.box()
    janela.refresh()
#elementos a serem utilizados no jogo de forma direta.
def elementosJogo(turtle,teclamov,modo):
    return (turtle,teclamov,modo)    
#função para limpar a tela
def limpeza(a):
            a.erase()
            a.refresh()  
#função que origina o jogo
def main(tela):

    #configurações iniciais
    ci(tela)
    #Declaração das variaveis relacionadas as janelas e pads
    altura,largura = tela.getmaxyx()
    margemInferior = 3 
    margemSuperior = 3
    distanciaDigitaocao = 1
    nomeComandos = "Direção :"

    #Valores das coordenadas iniciais da tataruga
    x = (largura-2)//2  
    y = (altura-margemInferior-margemSuperior)//2
    
    #Texto das coordenadas
    dx = transfStr(x)
    dy = transfStr(y)
    coordenadas = coord(dx,dy)
    vazio = "              "     
    #Estabelecimento das medidas das janelas e pads
   
    alturajanela = altura-margemInferior-margemSuperior
    larguracoord = len(coordenadas)+3

    
    posicaoxComandos = len(nomeComandos) + distanciaDigitaocao
    larguraComando = largura-larguracoord-posicaoxComandos-2

    #Elementos do jogo
    turtle,teclamov,modo = elementosJogo("@","*",1)

    #Criação da janela de movimentação do personagem
    janela = curses.newwin(alturajanela,largura,margemSuperior,0)
    janela.box()
    janela.refresh()

    #Criação do pad para as coordenadas
    padcoord = curses.newpad(3,larguracoord)
    padcoord.box()
    padcoord.addstr(1,1,coordenadas)
    padcoord.refresh(0,0,altura-margemInferior,largura-larguracoord,altura-1,largura-1)

    #Criação dos pads para o comando
    padcom = curses.newpad(margemInferior,largura-larguracoord-1)
    padcom.addstr(1,1,nomeComandos)
    padcom.box()
    padcom.refresh(0, 0, altura-margemInferior , 0 , altura-1 , largura-larguracoord-1)


    #Criação pad tamanho
    xTamanho = transfStr(largura-2)
    yTamanho = transfStr(alturajanela)
    tamanho = coord(xTamanho,yTamanho)
    padtamanho = curses.newpad(3,len(tamanho)+2)
    padtamanho.box()
    padtamanho.addstr(1,1,tamanho)
    padtamanho.refresh(0,0,0,0,3,largura-1)
    
    #pad modo
    padmodo = curses.newpad(3,10)
    padmodo.box()
    padmodo.refresh(0,0,0,largura-10,3,largura-1)

    #Criação do espaço para digitação dos comandos
    comandos = curses.newwin(1,larguraComando,altura-2,posicaoxComandos)

    while True: 
        #atualização do modo
        padmodo.addstr(1,1,f"Modo: {modo}")
        padmodo.refresh(0,0,0,largura-10,3,largura-1)

        #atualização das coordenadas
        dx = transfStr(x)
        dy = transfStr(y)

        #impressão das coordenadas do turtle
        coordenadas = coord(dx,dy)
        padcoord.addstr(1,1,coordenadas)
        padcoord.refresh(0,0,altura-3,largura-larguracoord,altura-1,largura-1)    
        if(x < 100):        
            padcoord.addstr(1,1,vazio)
            coordenadas = coord(dx,dy)
            padcoord.addstr(1,1,coordenadas)
            padcoord.refresh(0,0,altura-3,largura-larguracoord,altura-1,largura-1)  
        if(y < 100):
            padcoord.addstr(1,1,vazio)
            coordenadas = coord(dx,dy)
            padcoord.addstr(1,1,coordenadas)
            padcoord.refresh(0,0,altura-3,largura-larguracoord,altura-1,largura-1)  

        #impressão do turtle
        janela.addstr(y,x,turtle)
        janela.refresh()
        
        limpeza(comandos)
        
        #Função que irá printar a atual localização em y,x
        def movimento():
            janela.addstr(y,x,teclamov)

        #Input
        entrada = comandos.getstr(0, 0)

        #exceção caso o jogador queira voltar ao menu
        if entrada.decode('utf-8') == 'sair':
             janela.clear()
             wrapper(inicio)

        #Divisão do input     
        dados = re.match(r'^(\S+)\s+(\d+)$', entrada.decode('utf-8'))
        
        #Análise do input 
        if entrada.decode('utf-8') == 'apagar':
            janela.clear()
            janela.box()
            janela.addstr(y,x,turtle)
            janela.refresh()

        elif dados:
            direcao = dados.group(1)
            numeroPassos = int(dados.group(2))

        #Movimentação baseada na direção e numero de passos
            if (direcao == "l" or direcao == "leste" ):
                for i in range(0,numeroPassos):    
                    movimento()
                    x+= 1
                    if(x == largura-1):
                        x = 1
            elif(direcao == "o" or direcao == "oeste"):
                for i in range(0,numeroPassos):                
                    movimento()
                    x-= 1
                    if(x == 0):
                        x = largura-2

            elif(direcao == "s" or direcao == "sul" ):
                for i in range(0,numeroPassos):
                    movimento()
                    y+= 1
                    if(y == altura-7):
                        y = 1

            elif(direcao == "n" or direcao == "norte"):
                for i in range(0,numeroPassos):                
                    movimento()
                    y-= 1
                    if (y == 0):
                        y = altura-8

            elif(direcao == "ne" or direcao == "nordeste" ):
                for i in range(0,numeroPassos):
                    movimento()
                    y-= 1
                    x+= 1
                    if (y == 0 ):
                        y = altura-8  
                    if(x == largura-1):
                        x = 1

            elif(direcao == "no" or direcao == "noroeste"):
                for i in range(0,numeroPassos):
                    movimento()
                    y-= 1
                    x-= 1
                    if (y == 0 ):
                        y = altura-8  
                    if(x == 0):
                        x = largura-2

            elif(direcao == "se" or direcao == "sudeste" ):
                for i in range(0,numeroPassos):
                    movimento()
                    y+= 1
                    x+= 1
                    if (y == altura-7 ):
                        y = 1  
                    if(x == largura-1):
                        x = 1

            elif(direcao == "so" or direcao == "sudoeste"):
                for i in range(0,numeroPassos):
                    movimento()
                    y+= 1
                    x-= 1
                    if (y == altura-7 ):
                        y = 1  
                    if(x == 0):
                        x = largura-2   

            #alteração do modo
            elif(direcao == "modo"):
                if (numeroPassos == 1):
                    modo = 1
                    turtle ="@"
                elif(numeroPassos == 2):
                    modo = 2
                    turtle = "#"
                if (modo == 1):
                    teclamov = "*"
                elif(modo == 2):
                    teclamov = " " 
#comando para fazer o fractal baseado no tamanho dado pelo número de passos. 
            elif(direcao == "fractal" or direcao == "fra"):
                for i in range(0,numeroPassos):
                    movimento()
                    y-= 1
                    x+= 1
                    if (y == 0 ):
                        y = altura-8  
                    if(x == largura-1):
                        x = 1
                for i in range(0,numeroPassos):
                    movimento()
                    y+= 1
                    x+= 1
                    if (y == altura-7 ):
                        y = 1  
                    if(x == largura-1):
                        x = 1
                for i in range(0,2*numeroPassos):
                    movimento()
                    x-= 1
                for i in range(0,numeroPassos):
                    movimento()
                    y+= 1
                    x-= 1
                    if (y == altura-7 ):
                        y = 1  
                    if(x == 0):
                        x = largura-2  
                for i in range(0,2*numeroPassos):
                    movimento()
                    x+= 1
                    if(x == largura-1):
                        x = 1
                for i in range(0,numeroPassos):
                    movimento()
                    x-= 1
                    y-= 1
                    if (y == 0 ):
                        y = altura-8  
                    if(x == 0):
                        x = largura-2
                for i in range(0,numeroPassos):
                    movimento()
                    x+= 1
                    y+= 1
                    if (y == altura-7 ):
                        y = 1  
                    if(x == largura-1):
                        x = 1                        
                for i in range(0,numeroPassos):
                    movimento()
                    x+=1
                    y-=1
                    if (y == 0 ):
                        y = altura-8  
                    if(x == largura-1):
                        x = 1
                for i in range(0,numeroPassos):
                    movimento()
                    x+=1
                    y+=1
                    if (y == altura-7 ):
                        y = 1  
                    if(x == largura-1):
                        x = 1
                for i in range(0,2*numeroPassos):
                    movimento()
                    x-= 1 
                    if(x == 0):
                        x = largura-2
        #Comando para fazer um quadrado
            elif(direcao == "quadrado" or direcao == "quad"):
                for i in range(0,numeroPassos):
                    movimento()
                    y-= 1
                    if (y == 0):
                        y = altura-8
                for i in range(0,2*numeroPassos):
                    movimento()
                    x+= 1
                    if(x == largura-1):
                        x = 1
                for i in range(0,numeroPassos):
                    movimento()
                    y+=1
                    if(y == altura-7):
                        y = 1
                for i in range(0,2*numeroPassos):
                    movimento()
                    x-=1
                    if(x == 0):
                        x = largura-2
        #Comando para fazer um triângulo
            elif(direcao == "triangulo" or direcao =="tri"):
                for i in range(0,numeroPassos):
                    movimento()
                    x+=1
                    y-=1
                    if (y == 0 ):
                            y = altura-8  
                    if(x == largura-1):
                            x = 1
                for i in range(0,numeroPassos):
                    movimento()
                    x+=1
                    y+=1
                    if (y == altura-7 ):
                        y = 1  
                    if(x == largura-1):
                        x = 1
                for i in range(0,2*numeroPassos):
                    movimento()
                    x-=1
                    if(x == 0):
                        x = largura-2
        #comando para fazer um hexagono
            elif(direcao == "hexagono" or direcao == "hexa"):
                for i in range(0,2*numeroPassos):
                    movimento()
                    x+= 1
                    if(x == largura-1):
                        x = 1
                for i in range(0,numeroPassos):
                    movimento()
                    x+=1
                    y+=1
                    if (y == altura-7 ):
                        y = 1  
                    if(x == largura-1):
                        x = 1
                for i in range(0,numeroPassos):
                    movimento()
                    x-=1
                    y+=1
                    if (y == altura-7 ):
                        y = 1  
                    if(x == 0):
                        x = largura-2  
                for i in range(0,2*numeroPassos):
                    movimento()
                    x-=1
                    if(x == 0):
                        x = largura-2
                for i in range(0,numeroPassos):
                    movimento()
                    x-=1
                    y-=1
                    if (y == 0 ):
                            y = altura-8  
                    if(x == 0):
                            x = largura-2
                for i in range(0,numeroPassos):
                    movimento()
                    x+=1
                    y-=1
                    if (y == 0 ):
                            y = altura-8  
                    if(x == largura-1):
                            x = 1         
        #comando para desenhar uma estrelar
            elif(direcao == "estrela" or direcao == "star"):
                for i in range(0,numeroPassos):
                    movimento()    
                    x+=1
                    y-=1
                    if (y == 0 ):
                        y = altura-8  
                    if(x == largura-1):
                        x = 1
                for i in range(0,numeroPassos):
                    movimento()
                    x+=1
                    y+=1   
                    if (y == altura-7 ):
                        y = 1  
                    if(x == largura-1):
                        x = 1 
                for i in range(0,(numeroPassos*2)):
                    movimento()
                    x+=1
                    if(x == largura-1):
                        x = 1
                for i in range(0,numeroPassos):
                    movimento()
                    x-=1
                    y+=1
                    if (y == altura-7 ):
                        y = 1  
                    if(x == 0):
                        x = largura-2   
                for i in range(0,numeroPassos):
                    movimento()
                    x+=1
                    y+=1
                    if (y == altura-7 ):
                        y = 1  
                    if(x == largura-1):
                        x = 1
                for i in range(0,(numeroPassos*2)):
                    movimento()
                    x-=1
                    if(x == 0):
                        x = largura-2
                for i in range(0,numeroPassos):
                    movimento()
                    x-=1
                    y+=1
                    if (y == altura-7 ):
                        y = 1  
                    if(x == 0):
                        x = largura-2   
                for i in range(0,numeroPassos):
                    movimento()
                    x-=1
                    y-=1
                    if (y == 0 ):
                        y = altura-8  
                    if(x == 0):
                        x = largura-2
                for i in range(0,(numeroPassos*2)):
                    movimento()
                    x-=1
                    if(x == 0):
                        x = largura-2
                for i in range(0,numeroPassos):
                    movimento()
                    x+=1
                    y-=1
                    if (y == 0 ):
                        y = altura-8  
                    if(x == largura-1):
                        x = 1
                for i in range(0,numeroPassos):
                    movimento()
                    x-=1
                    y-=1
                    if (y == 0 ):
                        y = altura-8  
                    if(x == 0):
                        x = largura-2
                for i in range(0,(numeroPassos*2)):
                    movimento()
                    x+=1
                    if(x == largura-1):
                        x = 1

                    
        #É impresso "ERROR" na tela de comandos caso o que o usuário tenha digitado não corresponda a nenhuma outra entrada admitida pelo jogo
            else:
                limpeza(comandos)
                comandos.addstr(0,0,"ERROR")
                comandos.refresh()
                comandos.getch() 
            
        else :
            limpeza(comandos)
            comandos.addstr(0,0,"ERROR")
            comandos.refresh()
            comandos.getch()

#definições da tela de menu
def ciMenu(tela):
    curses.curs_set(0)
    curses.cbreak() 
    tela.clear()
#função criada para escrever na tela as instruções
def escreveinstru(janmenu,largura,divisaoDois,instrucoesprincipais,exemplo,casomodo,explicacaomodo1,explicacaomodo2,norte,sul,leste,oeste,nordeste,noroeste,sudeste,sudoeste,matriz,atual,altura,modosair,apagar):
     janmenu.clear()
     janmenu.box()
     janmenu.addstr((altura//18), (largura//2)-(divisaoDois(instrucoesprincipais)), instrucoesprincipais)
     janmenu.addstr((altura//18 * 2),(largura//2)-(divisaoDois(exemplo)), exemplo)
     janmenu.addstr((altura//18 * 3), (largura//2)-(divisaoDois(casomodo)), casomodo)
     janmenu.addstr((altura//18 * 4),(largura//2)-(divisaoDois(explicacaomodo1)),explicacaomodo1)
     janmenu.addstr((altura//18 * 5),(largura//2)-(divisaoDois(explicacaomodo2)),explicacaomodo2)
     janmenu.addstr((altura//18 * 6), (largura//2)-(divisaoDois(modosair)), modosair)
     janmenu.addstr((altura//18 * 7), (largura//2)-(divisaoDois(apagar)), apagar)
     janmenu.addstr((altura//18 * 8), (largura//2)-(divisaoDois(norte)), norte)
     janmenu.addstr((altura//18 * 9), (largura//2)-(divisaoDois(sul)), sul)
     janmenu.addstr((altura//18 * 10), (largura//2)-(divisaoDois(leste)), leste)
     janmenu.addstr((altura//18 * 11), (largura//2)-(divisaoDois(oeste)), oeste)
     janmenu.addstr((altura//18 * 12), (largura//2)-(divisaoDois(nordeste)), nordeste)
     janmenu.addstr((altura//18 * 13), (largura//2)-(divisaoDois(noroeste)), noroeste)
     janmenu.addstr((altura//18 * 14), (largura//2)-(divisaoDois(sudeste)), sudeste)
     janmenu.addstr((altura//18 * 15), (largura//2)-(divisaoDois(sudoeste)), sudoeste)
     janmenu.addstr((altura//18 * 16), (largura//2)-(divisaoDois(matriz)), matriz)
     janmenu.addstr((altura//18 * 17), (largura//2)-(divisaoDois(atual)), atual)
     
#função criada para escrever na tela os créditos
def escrevecreditos(janmenu,altura,largura,divisaoDois,final,peri,bruno,guilherme,ivo):
     janmenu.clear()
     janmenu.box()
     janmenu.addstr((altura//8), (largura//2)-(divisaoDois(final)), final)
     janmenu.addstr((altura//8 *2), (largura//2)-(divisaoDois(peri)), (peri))
     janmenu.addstr((altura//8 *3), (largura//2)-(divisaoDois(bruno)), bruno)
     janmenu.addstr((altura//8 *4), (largura//2)-(divisaoDois(guilherme)), guilherme)
     janmenu.addstr((altura//8 *5), (largura//2)-(divisaoDois(ivo)), ivo)
     janmenu.refresh    
#criação da função do menu
def inicio(menu):
    #Função para não aparecer o cursor
    ciMenu(menu)
    #Declaração de tamanhos
    altura, largura = menu.getmaxyx()
    #criação da janela menu
    janmenu = curses.newwin(altura, largura, 0, 0)
    janmenu.box()
    janmenu.refresh()
    janmenu.keypad(True)
    #função de tamanho
    def divisaoDois(c):
        return len(c)//2
    
    #criação tela "PRESSIONE QUALQUER TECLA"
    inicio = "PRESSIONE QUALQUER TECLA"
    janmenu.clear()
    janmenu.box()
    janmenu.addstr(altura//2, (largura//2)-(divisaoDois(inicio)), inicio)
    janmenu.refresh()
    janmenu.getch()
    
    #variáveis a serem usadas no menu
    jogo = True
    opcao = 0
    matriz = "TAMANHO DA MATRIZ EXIBIDO NA PARTE SUPERIOR"
    atual ="ATUAL POSIÇÃO EXIBIDA NA PARTE INFERIOR"
    final = "LOGO TURTLE POR:"
    logo = "LOGO TURTLE"
    jogar = "JOGAR"
    instrucoes = "INSTRUÇÕES"
    creditos = "CRÉDITOS"
    explicacaomodo1 = "modo 1 (@) - modo de desenho"
    explicacaomodo2 = "modo 2 (#) - modo de borracha"
    sair = "SAIR"
    instrucoesprincipais = "PRIMEIRO COLOQUE A DIREÇÃO E DEPOIS A DISTÂNCIA"
    exemplo = "EXEMPLO: 'n 20'"
    casomodo = "DIGITE 'modo 1' E 'modo 2' PARA TROCAR O MODO"
    norte = "NORTE = n"
    sul = "SUL = s"
    leste = "LESTE = l"
    oeste = "OESTE = o"
    nordeste = "NORDESTE = ne"
    noroeste = "NOROESTE = no"
    sudeste = "SUDESTE = se"
    sudoeste = "SUDOESTE = so"
    peri =  "PERI L. MACEDO"
    bruno = "BRUNO C. P. L. FILHO"
    guilherme = "GUILHERME V. R. SILVA"
    ivo = "IVO L. S. NETO"
    apagar = "PARA APAGAR TODA A TELA DIGITE 'apagar'"
    modosair = "DIGITE 'sair' PARA VOLTAR PARA O MENU"
    
    #função da tela de menu inicial
    while jogo == True:
        #função que cria a tela após a tela de pressione alguma tecla
        def mainmenu(janmenu):
            janmenu.clear()
            janmenu.box()
            janmenu.addstr((altura//4), (largura//2)-(divisaoDois(logo)), logo,)
            janmenu.addstr(((altura//2)-1), ((largura//2)-2)-(divisaoDois(jogar)), ("->"+jogar))
            janmenu.addstr(((altura//2)), (largura//2)-(divisaoDois(instrucoes)), instrucoes)
            janmenu.addstr(((altura//2)+1), (largura//2)-(divisaoDois(creditos)), creditos)
            janmenu.addstr(((altura//2)+2), (largura//2)-(divisaoDois(sair)), sair)
            janmenu.refresh()
        mainmenu(janmenu)

        #função para movimentar a seta, tendo como base a variável 'opcao' que será alterada conforme o input das setinhas, caso seja usada a setinha para baixo o valor de opcao aumenta
        #caso seja usada a setinha para cima o valor de opcao diminui, e caso seja pressionado enter é feita uma análise para realizar um comando baseado no valor de opcao. 
        def menumov(opcao):
            if opcao % 4 == 0:
                        janmenu.addstr((altura//4), (largura//2)-(divisaoDois(logo)), logo)
                        janmenu.addstr(((altura//2)-1), ((largura//2)-2)-(divisaoDois(jogar)), ("->"+jogar))
                        janmenu.addstr(((altura//2)), (largura//2)-(divisaoDois(instrucoes)), instrucoes)
                        janmenu.addstr(((altura//2)+1), (largura//2)-(divisaoDois(creditos)), creditos)
                        janmenu.addstr(((altura//2)+2), (largura//2)-(divisaoDois(sair)), sair)
                        janmenu.refresh()
            elif opcao % 4 == 1:
                        janmenu.addstr((altura//4), (largura//2)-(divisaoDois(logo)), logo,)
                        janmenu.addstr(((altura//2)-1), (largura//2)-(divisaoDois(jogar)), (jogar))
                        janmenu.addstr(((altura//2)), ((largura//2)-2)-(divisaoDois(instrucoes)), ('->'+instrucoes))
                        janmenu.addstr(((altura//2)+1), (largura//2)-(divisaoDois(creditos)), creditos)
                        janmenu.addstr(((altura//2)+2), (largura//2)-(divisaoDois(sair)), sair)
                        janmenu.refresh()
            elif opcao %4 == 2:
                        janmenu.addstr((altura//4), (largura//2)-(divisaoDois(logo)), logo,)
                        janmenu.addstr((((altura//2)-1)), (largura//2)-(divisaoDois(jogar)), (jogar))   
                        janmenu.addstr(((altura//2)), (largura//2)-(divisaoDois(instrucoes)), instrucoes)
                        janmenu.addstr(((altura//2)+1), ((largura//2)-2)-(divisaoDois(creditos)),("->" + creditos))
                        janmenu.addstr(((altura//2)+2), (largura//2)-(divisaoDois(sair)), sair) 
                        janmenu.refresh()               
            elif opcao % 4 == 3:
                        janmenu.addstr((altura//4), (largura//2)-(divisaoDois(logo)), logo,)
                        janmenu.addstr(((altura//2)-1), (largura//2)-(divisaoDois(jogar)), (jogar))
                        janmenu.addstr(((altura//2)), (largura//2)-(divisaoDois(instrucoes)), instrucoes)
                        janmenu.addstr(((altura//2)+1), (largura//2)-(divisaoDois(creditos)), creditos)
                        janmenu.addstr(((altura//2)+2), ((largura//2)-2)-(divisaoDois(sair)), ("->" +sair))
                        janmenu.refresh()

        #código que recebe entradas das setinhas, do W, do S e do enter.
        while True:
            key = janmenu.getkey()
            if key == 'KEY_DOWN' or key == "s":
                opcao+=1
                janmenu.clear()
                janmenu.box()
                menumov(opcao)
            elif key == "KEY_UP" or key == "w":
                opcao-=1
                janmenu.clear()
                janmenu.box()
                menumov(opcao)
            elif key == "\n":

            #Comando do "jogar"
                if opcao % 4 == 0:
                #Nestas linhas abaixo é feita uma limpeza da tela para a execução da função do jogo
                    janmenu.clear()
                    wrapper(main)

                #Comando das instruções
                elif opcao % 4 == 1:
                #Uso da função para escrever na tela as instruções
                    escreveinstru(janmenu,largura,divisaoDois,instrucoesprincipais,exemplo,casomodo,explicacaomodo1,explicacaomodo2,norte,sul,leste,oeste,nordeste,noroeste,sudeste,sudoeste,matriz,atual,altura,modosair,apagar)
                    opcao = 0
                    janmenu.getch()
                    break
                #Comando dos créditos
                elif opcao %4 == 2:
                #Uso da função para escrever na tela os créditos
                    escrevecreditos(janmenu,altura,largura,divisaoDois,final,peri,bruno,guilherme,ivo)
                    opcao = 0
                    janmenu.getch()
                    break
                #Comando do "sair"
                elif opcao % 4 == 3:
                    quit()
wrapper(inicio)