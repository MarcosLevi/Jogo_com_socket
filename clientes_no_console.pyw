import pygame
import sys

sys.path.append("Codigo_Aux/")
import time
import math
import random
import socket

from funcoes_aux import*
from send_receive_socket_cliente import*


IP = "127.0.0.1"
PORT = 1234

jogador_atual="GREEN"
my_username = ""



Chat=[]

minhas_pecas = ""
#RED ou GREEN
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Funcionou até aqui")
    


####tabuleiro=[[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
####           [-1, -1, -1, -1, -1, -1, -1,  2, -1, -1, -1, -1, -1, -1, -1],
####           [-1, -1, -1, -1, -1, -1,  2,  2, -1, -1, -1, -1, -1, -1, -1],
####           [-1, -1, -1, -1, -1, -1,  2,  2,  2, -1, -1, -1, -1, -1, -1],
####           [-1, -1, -1, -1, -1,  0,  2,  2,  2, -1, -1, -1, -1, -1, -1],
####           [-1,  0,  0,  0,  0,  2,  0,  0,  0,  0,  0,  0,  0,  0, -1],
####           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
####           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
####           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
####           [-1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
####           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
####           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
####           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
####           [-1,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0, -1],
####           [-1, -1, -1, -1, -1,  1,  1,  0,  1, -1, -1, -1, -1, -1, -1],
####           [-1, -1, -1, -1, -1, -1,  1,  1,  1, -1, -1, -1, -1, -1, -1],
####           [-1, -1, -1, -1, -1, -1,  1,  1, -1, -1, -1, -1, -1, -1, -1],
####           [-1, -1, -1, -1, -1, -1, -1,  1, -1, -1, -1, -1, -1, -1, -1],
####           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
##
##tabuleiro=[[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1, -1,  1, -1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1,  1,  1, -1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1,  1,  1,  1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1,  1,  1,  1,  1, -1, -1, -1, -1, -1, -1],
##           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
##           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
##           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
##           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
##           [-1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
##           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
##           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
##           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
##           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
##           [-1, -1, -1, -1, -1,  2,  2,  2,  2, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1,  2,  2,  2, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1,  2,  2, -1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1, -1,  2, -1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
##
##tabuleiro_orig=[[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1, -1,  1, -1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1,  1,  1, -1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1,  1,  1,  1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1,  1,  1,  1,  1, -1, -1, -1, -1, -1, -1],
##           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
##           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
##           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
##           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
##           [-1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
##           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
##           [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
##           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
##           [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
##           [-1, -1, -1, -1, -1,  2,  2,  2,  2, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1,  2,  2,  2, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1,  2,  2, -1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1, -1,  2, -1, -1, -1, -1, -1, -1, -1],
##           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
##
##
##
##
##
##
####jogador 2=vermelho
####jogador 1=verde
##
##Circ_Verde = pygame.image.load("Sprites/Elipse_1.png")
##Circ_Verme = pygame.image.load("Sprites/Elipse_2.png")
##Circ_Azul = pygame.image.load("Sprites/Elipse_3.png")
##Circ_Verde = pygame.transform.scale(Circ_Verde, (24,24))
##Circ_Verme = pygame.transform.scale(Circ_Verme, (24,24))
##Circ_Azul = pygame.transform.scale(Circ_Azul, (24,24))
##
##
##cinza=128,128,128,255
##verde=0,200,0,255
##vermelho=200,0,0,255
##vermelho_forte=255,0,0,255
##azul=0,0,200,255
##azul_forte=0,0,255,255
##
##peca_bloqueada=(0,0)
##
##branco=255,255,255,255
##Cor_Circ_Verde=(26, 162, 26, 255)
##Cor_Circ_Verme=(195, 26, 26, 255)
##Cor_Circ_Azul=(65, 122, 162, 255)
##fundo = pygame.image.load("Sprites/tabuleiro.png")
##fundo = pygame.transform.scale(fundo, (480,480))
##(Tam_X_Elipse,Tam_Y_Elipse)=Circ_Verde.get_rect().size
##
##
##Plot_x=0
##Plot_y=0
##aux=0
##auy=0
##peca_atual=0;
##
##
##
##
##
##
##
##
##
##
##
##
##
##    
##    
##
##
##
##    
##
##
##def Att_Tabuleiro(tabuleiro_att,screen):
##    cinza=128,128,128,255
##    screen.fill(cinza)
##    screen.blit(fundo,(0,0))
##    jogador_vermelho = pygame.image.load("Sprites/icon_jogador_vermelho.png")
##    jogador_verde = pygame.image.load("Sprites/icon_jogador_verde.png")
##    resize_x_red=108
##    resize_x_green=104
##    resize_y=100
##    jogador_vermelho = pygame.transform.scale(jogador_vermelho, (resize_x_red, resize_y))
##    jogador_verde = pygame.transform.scale(jogador_verde, (resize_x_green, resize_y))
##    tam_matriz = (len(tabuleiro_att), len(tabuleiro_att[0]))
##    
##    pygame.draw.rect(screen,vermelho,(((250)-170),470,150,50))
##    message_display(((250)-95),(495),"Desistir",20,(255,255,255,255))
##    pygame.draw.rect(screen,azul,(((250)+20),470,150,50))
##    message_display(((250)+95),(495),"Passar a vez",20,(255,255,255,255))
##    
##    font = pygame.font.Font('freesansbold.ttf',20)
##    
##    if(minhas_pecas=="GREEN"):
##        screen.blit(jogador_verde,(0,570-(resize_y/2)))
####        message_display(100+(resize_x_green/2)+40,900+20,my_username,40,(0,255,0,255))
##        txt = font.render(my_username, True, (0,255,0,255))
##        screen.blit(txt, (110, 560))
##    elif(minhas_pecas=="RED"):
##        screen.blit(jogador_vermelho,(0,570-(resize_y/2)))
##        txt = font.render(my_username, True, (255,0,0,255))
##        screen.blit(txt, (110, 560))
####        message_display(100+(resize_x_red/2)+40,900+20,my_username,40,(255,0,0,255))
##    
##    
##    if(jogador_atual==minhas_pecas):
##        if(minhas_pecas=="GREEN"):
##            txt = font.render("Sua vez", True, (0,255,0,255))
##            screen.blit(txt, (0, 0))
##        elif(minhas_pecas=="RED"):
##            txt = font.render("Sua vez", True, (255,0,0,255))
##            screen.blit(txt, (0, 0))
##        
##    elif(jogador_atual!=minhas_pecas):
##        if(minhas_pecas=="GREEN"):
##            txt = font.render("Vez do adversário", True, (255,0,0,255))
##            screen.blit(txt, (0, 0))
##        elif(minhas_pecas=="RED"):
##            txt = font.render("Vez do adversário", True, (0,255,0,255))
##            screen.blit(txt, (0, 0))
##        
##    i=0
##    j=0
##    for i in range(0,tam_matriz[0]):
##        for j in range(0,tam_matriz[1]):
##            if(tabuleiro_att[i][j]==1):
##                screen.blit(Circ_Verde,(return_x_e_y_correspondete_tabela(j,i)))
##            elif(tabuleiro_att[i][j]==2):
##                screen.blit(Circ_Verme,(return_x_e_y_correspondete_tabela(j,i)))
##            elif(tabuleiro_att[i][j]==3):
##                screen.blit(Circ_Azul,(return_x_e_y_correspondete_tabela(j,i)))
##    pygame.display.update(pygame.Rect(0, 0, 500, 630))    
##
##
##                
##
##
##
##
##
##def criacao_tela_de_vitoria(screen,ganhador):
##    mario_feliz = pygame.image.load("Sprites/mario.png")
##    luigi_feliz = pygame.image.load("Sprites/luigi.png")
##    mario_triste = pygame.image.load("Sprites/mario_triste.png")
##    luigi_triste = pygame.image.load("Sprites/luigi_triste.png")
##    mario_feliz = pygame.transform.scale(mario_feliz, (229,400))
##    luigi_feliz = pygame.transform.scale(luigi_feliz, (287, 400))
##    mario_triste = pygame.transform.scale(mario_triste, (343, 400))
##    luigi_triste = pygame.transform.scale(luigi_triste, (235, 400))
##    screen.fill(cinza)
##    largura, altura = screen.get_size()
##    if(ganhador=="GREEN" and minhas_pecas=="GREEN"):
##        texto="Você ganhou"
##        screen.blit(luigi_feliz,(largura/2-luigi_feliz.get_width()/2,0))
##    elif(ganhador=="RED" and minhas_pecas=="RED"):
##        texto="Você ganhou"
##        screen.blit(mario_feliz,(largura/2-mario_feliz.get_width()/2,0))
##    elif(ganhador=="GREEN" and minhas_pecas=="RED"):
##        texto="Você perdeu"
##        screen.blit(mario_triste,(largura/2-mario_triste.get_width()/2,0))
##    elif(ganhador=="RED" and minhas_pecas=="GREEN"):
##        texto="Você perdeu"
##        screen.blit(luigi_triste,(largura/2-luigi_triste.get_width()/2,0))
##    
##    
##    
####    pygame.draw.rect(screen,vermelho,(((400)-75),800,150,50))
####    message_display((400),(825),"Fechar",20,(255,255,255,255))
##    message_display(largura/2,450,texto,35,(0,0,0,255))
##    pygame.draw.rect(screen,azul,(largura/2-75,500,150,50))
##    message_display((largura/2),(525),"Jogar denovo",20,(255,255,255,255))
##    
##    pygame.display.update()
##
##
##
##def tela_de_vitoria(ganhador):
##    sair=True
##    global Chat,jogador_atual
##    largura=600;
##    altura=600;
##    bloqueia=False
##    pygame.display.set_mode((largura, altura))
##    pygame.display.set_caption("Damas Chinesas")
##    pygame.display.flip()
##    screen = pygame.display.get_surface()
##    criacao_tela_de_vitoria(screen,ganhador)
##    flag=False
##    while sair:
##        
##        for event in pygame.event.get():
##            pygame.display.update()
##            try:
##                username,message=receive(client_socket)
##                
##                if(define_tipo_acao(message)=="RANDOM"):
##                    jogador_atual=escolha_aleatoria_jogador()
##                    send("PODE_COMECAR_DENOVO "+jogador_atual,client_socket)
##                    sair=False
##                    print("Aki foi a parte do random: "+jogador_atual)
##                    tela_de_jogo()
##                elif(define_tipo_acao(message)=="PODE_COMECAR_DENOVO"):
##                    sair=False
##                    args=message.split()
##                    jogador_atual=args[1]
##                    print("Aki foi a parte do random: "+jogador_atual)
##                    tela_de_jogo()
####                elif(define_tipo_acao(message)=="CONECTADO"):
####                    print("Servidor se conectou comigo")
##            except:
##                pass
##             
##                                               
##            if event.type==pygame.MOUSEMOTION and bloqueia==False:
##                
##                mouse=pygame.mouse.get_pos()
####                if( (400+75)>mouse[0]>(400-75) and 800+50>mouse[1]>800):
####                    pygame.draw.rect(screen,vermelho_forte,(((400)-75),800,150,50))
####                    message_display((400),(825),"Fechar",20,(255,255,255,255))
##                if((largura/2+75)>mouse[0]>(largura/2-75) and 500+50>mouse[1]>500):
##                    pygame.draw.rect(screen,azul_forte,(largura/2-75,500,150,50))
##                    message_display((largura/2),(525),"Jogar denovo",20,(255,255,255,255))
##                else:
####                    pygame.draw.rect(screen,vermelho,(((400)-75),800,150,50))
####                    message_display((400),(825),"Fechar",20,(255,255,255,255))
##                    pygame.draw.rect(screen,azul,(largura/2-75,500,150,50))
##                    message_display((largura/2),(525),"Jogar denovo",20,(255,255,255,255))
##                
##            elif event.type==pygame.MOUSEBUTTONDOWN and bloqueia==False:
##                mouse=pygame.mouse.get_pos()
##                if event.button==1:
####                    if( (400+75)>mouse[0]>(400-75) and 800+50>mouse[1]>800):
####                        sair=False
####                        pygame.display.quit()
##                    if((largura/2+75)>mouse[0]>(largura/2-75) and 500+50>mouse[1]>500):
##                        Chat=[]
##                        send("RANDOM",client_socket)
##                        bloqueia=True
##
##
##            
##            elif event.type==pygame.QUIT:
##                sair=False
##                pygame.display.quit()
##
##    
##
##
##
##
##
##
##def func_ganhou(ganhador):
##    if(ganhador=="GREEN"):
##        zera_matriz(tabuleiro, tabuleiro_orig)
##        
##        tela_de_vitoria("GREEN")
##    elif(ganhador=="RED"):
##        zera_matriz(tabuleiro, tabuleiro_orig)
##        
##        tela_de_vitoria("RED")
##
##
##
##def att_chat(screen):
##    altura=0;
##    global Chat
##    pygame.draw.rect(screen,(255,255,255,255),[500,10,690,570])
##    font = pygame.font.Font('freesansbold.ttf',15)
##    for i in Chat:
##        txt = font.render(i, True, (0,0,0,255))
##        screen.blit(txt, (510, 20+altura-10))
##        altura+=30;
##    pygame.display.update(pygame.Rect(500,10,690,570))
##
##def att_mensagem(text,screen):
##    font = pygame.font.Font('freesansbold.ttf',15)
##    pygame.draw.rect(screen,(255,255,255,255),[500,590,690,30])
##    txt = font.render(text, True, (0,0,0,255))
##    screen.blit(txt, (510, 600))
##    pygame.display.update(pygame.Rect(500,590,690,30))
##
##
##
##def criacao_tela_de_jogo():
##    screen=pygame.display.get_surface()
##    largura=1200;
##    altura=630;
##    
##    pygame.display.set_mode((largura, altura))
##    pygame.display.set_caption("Damas Chinesas")
####    pygame.display.flip()
##    screen=pygame.display.get_surface()
##    Att_Tabuleiro(tabuleiro,screen)
####    pygame.draw.rect(screen,(255,255,255,255),[800,100,800,600])
####    pygame.draw.rect(screen,(255,255,255,255),[800,720,800,200])
##
##
##def criacao_tela_de_colocar_nome():
##    global jogador_atual,my_username,minhas_pecas
##    Conectado=False
##    largura=700;
##    altura=500;
##    nome=''
##    porta=''
##    troca_campo=False
##    meio_x=largura/2
##    meio_y=altura/2
##    font = pygame.font.Font('freesansbold.ttf',25)
##    cor_adversario=""
##    bloqueio_cor=True
##    bloqueio_teclado=False
##    pygame.display.set_mode((largura, altura))
##    pygame.display.set_caption("Tela inicial")
##    screen = pygame.display.get_surface()
##    screen.fill(cinza)
####    pygame.display.flip()
##    screen=pygame.display.get_surface()
##    largura_input_box=400
##    altura_input_box=50
##    y_da_input_box=meio_y-altura_input_box/2
##    x_da_input_box=meio_x-largura_input_box/2
##    pygame.draw.rect(screen,(255,255,255,255),[x_da_input_box+75,y_da_input_box-200,largura_input_box,altura_input_box])
##    pygame.draw.rect(screen,(125,0,0,255),[(largura/2-50)-100,(altura/2+50)+100,100,50])
##    pygame.draw.rect(screen,(0,125,0,255),[(largura/2-50)+100,(altura/2+50)+100,100,50])
##    message_display(x_da_input_box-20,y_da_input_box-175,"Nome:",50,(0,255,255,255))
##    message_display(x_da_input_box-20,y_da_input_box-75,"Porta:",50,(0,255,255,255))
##    pygame.draw.rect(screen,(255,255,255,255),[x_da_input_box+75,y_da_input_box-100,largura_input_box,altura_input_box])
##    message_display(largura/2,altura/2+100,"Escolha sua cor:",50,(0,255,255,255))
##    sair=False
##    while(sair==False):
##        
##        for event in pygame.event.get():
##            pygame.display.update()
##            try:
##                username,message=receive(client_socket)
##                
##                if(define_tipo_acao(message)=="COR_ADVERSARIO"):
##                    args=message.split()
##                    cor_adversario=args[1]
##                    if(minhas_pecas!=""):
##                        jogador_atual=escolha_aleatoria_jogador()
##                        send("PODE_COMECAR "+jogador_atual,client_socket)
##                        sair=True
##                        tela_de_jogo()
##                   
##                elif(define_tipo_acao(message)=="PODE_COMECAR"):
##                    sair=True
##                    args=message.split()
##                    jogador_atual=args[1]
##                    tela_de_jogo()
####                elif(define_tipo_acao(message)=="CONECTADO"):
####                    print("Servidor se conectou comigo")
##            except:
##                pass
##            if event.type == pygame.KEYDOWN and bloqueio_teclado==False:
##                    
##        ##              K_RETURN é o enter, quando aperta imprime a mensagem
##                    if event.key == pygame.K_RETURN:
##                        if(troca_campo==False):
##                            troca_campo=True
##                        elif(nome!="" and porta!=""):
##                            my_username=nome
##                            client_socket.connect((IP, int(porta)))
##                            client_socket.setblocking(False)
##                            send(my_username,client_socket)
##                            while(Conectado==False):
##                                for event in pygame.event.get():
##                                    try:
##                                        message=receive2(client_socket)
##                                        if(message=="CONECTADO"):
##                                            print("CONECTADO COM O SERVER")
##                                            message_display(largura/2,altura/2+125+100,"Aguardando o outro jogador se conectar...",20,(0,0,0,255))
##                                            pygame.display.update()
##                                            
##                                        elif(message=="DESCONECT"):
##                                            print("NÃO PODE SE CONECTAR")
##                                            Conectado=True
##                                            sair=True
##                                        elif(message=="READY2GO."):
##                                            Conectado=True
##                                            pygame.draw.rect(screen,cinza,[0,(altura/2+50)+50+100,largura,50])
##                                            
##                                    except:
##                                        pass
##                            bloqueio_teclado=True
##                            bloqueio_cor=False
##                    elif event.key == pygame.K_BACKSPACE:
##                        if(troca_campo==False):
##                            nome = nome[:-1]
##                            txt = font.render(nome, True, (0,0,0,255))
##                            pygame.draw.rect(screen,(255,255,255,255),[x_da_input_box+75,y_da_input_box-200,largura_input_box,altura_input_box])
##                            screen.blit(txt, (x_da_input_box+75, y_da_input_box-100+15-100))
##                        elif(troca_campo==True):
##                            porta = porta[:-1]
##                            txt = font.render(porta, True, (0,0,0,255))
##                            pygame.draw.rect(screen,(255,255,255,255),[x_da_input_box+75,y_da_input_box-100,largura_input_box,altura_input_box])
##                            screen.blit(txt, (x_da_input_box+75, y_da_input_box-100+15))
##                    elif(len(nome)<21 and troca_campo==False):
##                        nome += event.unicode
##                        txt = font.render(nome, True, (0,0,0,255))
##                        pygame.draw.rect(screen,(255,255,255,255),[x_da_input_box+75,y_da_input_box-200,largura_input_box,altura_input_box])
##                        screen.blit(txt, (x_da_input_box+75, y_da_input_box-100+15-100))
##                    elif(len(porta)<21 and troca_campo==True):
##                        porta+= event.unicode
##                        txt = font.render(porta, True, (0,0,0,255))
##                        pygame.draw.rect(screen,(255,255,255,255),[x_da_input_box+75,y_da_input_box-100,largura_input_box,altura_input_box])
##                        screen.blit(txt, (x_da_input_box+75, y_da_input_box-100+15))
##            elif event.type==pygame.MOUSEMOTION and bloqueio_cor==False:
##                    mouse=pygame.mouse.get_pos()
##                    #verde
##                    if((largura/2-50)+200>mouse[0]>(largura/2-50)+100 and (altura/2+100+100)>mouse[1]>(altura/2+50+100) and cor_adversario!="GREEN"):
##                        pygame.draw.rect(screen,(0,255,0,255),[(largura/2-50)+100,(altura/2+50)+100,100,50])
##                    #vermelho
##                    elif((largura/2-50)>mouse[0]>(largura/2-150) and (altura/2+100+100)>mouse[1]>(altura/2+50+100)and cor_adversario!="RED"):
##                        pygame.draw.rect(screen,(255,0,0,255),[(largura/2-50)-100,(altura/2+50)+100,100,50])
##                    else:
##                        pygame.draw.rect(screen,(0,125,0,255),[(largura/2-50)+100,(altura/2+50)+100,100,50])
##                        pygame.draw.rect(screen,(125,0,0,255),[(largura/2-50)-100,(altura/2+50)+100,100,50])
##            elif event.type==pygame.MOUSEBUTTONDOWN and bloqueio_cor==False:
##                mouse=pygame.mouse.get_pos()
##                if event.button==1:
##                    #verde
##                    if( (largura/2-50)+200>mouse[0]>(largura/2-50)+100 and (altura/2+100+100)>mouse[1]>(altura/2+50+100) and nome!=''and cor_adversario!="GREEN"):
##                        minhas_pecas="GREEN"
##                        
##                        send("COR_ADVERSARIO GREEN",client_socket)
##                        bloqueio_cor=True
##                        if(cor_adversario==""):
##                            message_display(largura/2,altura/2+125+100,"Aguardando o outro jogador escolher a cor...",20,(0,0,0,255))
##                    #vermelho
##                    elif((largura/2-50)>mouse[0]>(largura/2-150) and (altura/2+100+100)>mouse[1]>(altura/2+50+100) and nome!=''and cor_adversario!="RED"):
##                        minhas_pecas="RED"
## 
##                        send("COR_ADVERSARIO RED",client_socket)
##                        bloqueio_cor=True
##                        if(cor_adversario==""):
##                            message_display(largura/2,altura/2+125+100,"Aguardando o outro jogador escolher a cor...",20,(0,0,0,255))
##            elif event.type==pygame.QUIT:
##                sair=True
##
##    
##
##def tela_de_jogo():
##    global jogador_atual
##    sair= True
##    screen=pygame.display.get_surface()
##    flag=False
##    
##    nome_do_jogador=my_username+": "
##    text=''
##    font = pygame.font.Font('freesansbold.ttf',15)
##    tam_nome_jogador=len(nome_do_jogador)
##    altura_texto=0
##    clock = pygame.time.Clock()
##    criacao_tela_de_jogo()
##    att_chat(screen)
##    att_mensagem(text,screen)
##    pygame.display.update()
##    print("Isso já é na tela de jogo: "+jogador_atual)
##    
##    
##    while sair:
##        
##        for event in pygame.event.get():
##            
##            try:
##                username,message=receive(client_socket)
##                if(define_tipo_acao(message)=="CHAT"):
##                    username=username+": "
##                    add_Lista_Chat(Chat,username+message[5:])
##                    Att_Tabuleiro(tabuleiro,screen)
##                    att_chat(screen)
##                    att_mensagem(text,screen)
##                elif(define_tipo_acao(message)=="MOVE"):   
##                    args=message.split()
##                    troca_cor(tabuleiro,(int(args[1]),int(args[2])),(int(args[3]),int(args[4])))
##                    Att_Tabuleiro(tabuleiro,screen)
##                    att_chat(screen)
##                    att_mensagem(text,screen)
##                elif(define_tipo_acao(message)=="TROCA_JOGADOR"):
##                    jogador_atual=troca_jogador(jogador_atual)
##                    Att_Tabuleiro(tabuleiro,screen)
##                    att_chat(screen)
##                    att_mensagem(text,screen)
##                elif(define_tipo_acao(message)=="GANHOU"):
##                    args=message.split()
##                    sair=False
##                    zera_matriz(tabuleiro, tabuleiro_orig)
##                    tela_de_vitoria(str(args[1]))    
##            except:
##                pass
##            
##            if(sair==True):                
##                if event.type == pygame.KEYDOWN:
##                    
##        ##              K_RETURN é o enter, quando aperta imprime a mensagem
##                    if event.key == pygame.K_RETURN and text!="":
##                        add_Lista_Chat(Chat,my_username+": "+text)
##                        pygame.draw.rect(screen,(255,255,255,255),[800,100,800,600])
##                        send("CHAT "+text,client_socket)
##                        text = ''
##                    elif event.key == pygame.K_BACKSPACE:
##                        text = text[:-1]
##                    elif(len(text)<=60 and event.key != pygame.K_RETURN):
##                        text += event.unicode
##                    Att_Tabuleiro(tabuleiro,screen)
##                    att_chat(screen)
##                    att_mensagem(text,screen)
##                elif event.type==pygame.MOUSEBUTTONDOWN:
##                    
##                    mouse=pygame.mouse.get_pos()
##                    if event.button==1:
##                        if(screen.get_at(mouse)==(Cor_Circ_Verme)and minhas_pecas=="RED" and jogador_atual=="RED"):
##                           if(flag==False):
##                               Elimina_o_3_da_matriz(tabuleiro)
##                               (aux,auy)=get_index_tabela(mouse[0],mouse[1])
##                               peca_atual=(auy,aux)
##                               pode_andar(tabuleiro,auy,aux)
##                        elif(screen.get_at(mouse)==(Cor_Circ_Verde) and minhas_pecas=="GREEN" and jogador_atual=="GREEN"):
##                           if(flag==False):
##                               Elimina_o_3_da_matriz(tabuleiro)
##                               (aux,auy)=get_index_tabela(mouse[0],mouse[1])
##                               peca_atual=(auy,aux)
##                               pode_andar(tabuleiro,auy,aux)
##                        elif(screen.get_at(mouse)==(Cor_Circ_Azul)):
##                           Elimina_o_3_da_matriz(tabuleiro)
##                           (aux,auy)=get_index_tabela(mouse[0],mouse[1])
##                           peca_destino=(auy,aux)
##                           troca_cor(tabuleiro,peca_destino,peca_atual)
##                           send("MOVE "+str(peca_destino[0])+" "+str(peca_destino[1])+" "+str(peca_atual[0])+" "+str(peca_atual[1]),client_socket)
##                           flag=ainda_pode_andar(tabuleiro,peca_destino,peca_atual)
##                           peca_atual=peca_destino
##                           if(ganhou(tabuleiro)==1):
##                                print("Verde ganhou")
##                                send("GANHOU GREEN",client_socket)
##                                func_ganhou("GREEN")
##                                sair=False
##                           elif(ganhou(tabuleiro)==2):
##                               print("Vermelho ganhou")
##                               send("GANHOU RED",client_socket)
##                               func_ganhou("RED")
##                               sair=False
##                           if(flag==False and sair==True):
##                               jogador_atual=troca_jogador(jogador_atual)
##                               send("TROCA_JOGADOR",client_socket)                       
##                        elif( (80+150)>mouse[0]>(80) and 470+50>mouse[1]>470 and minhas_pecas==jogador_atual):
##                            ##DESISTIU
##                            sair=False
##                            zera_matriz(tabuleiro, tabuleiro_orig)
##                            jogador_atual=troca_jogador(jogador_atual)
##                            
##                            send("GANHOU "+jogador_atual,client_socket)
##                            func_ganhou(jogador_atual)
##                        elif((270+150)>mouse[0]>(270) and 470+50>mouse[1]>470 and minhas_pecas==jogador_atual):
##                            flag=False
##                            Elimina_o_3_da_matriz(tabuleiro)
##                            send("TROCA_JOGADOR",client_socket)
##                            jogador_atual=troca_jogador(jogador_atual)
##                    Att_Tabuleiro(tabuleiro,screen)
##                    att_chat(screen)
##                    att_mensagem(text,screen)
##                elif event.type==pygame.MOUSEMOTION:
##                    mouse=pygame.mouse.get_pos()
##                    if( (80+150)>mouse[0]>(80) and 470+50>mouse[1]>470 and minhas_pecas==jogador_atual):
##                        pygame.draw.rect(screen,vermelho_forte,(((250)-170),470,150,50))
##                        message_display(((250)-95),(495),"Desistir",20,(255,255,255,255))
##                        pygame.display.update(pygame.Rect((80,470,150,50)))
##                    elif((270+150)>mouse[0]>(270) and 470+50>mouse[1]>470 and minhas_pecas==jogador_atual):
##                        pygame.draw.rect(screen,azul_forte,(((250)+20),470,150,50))
##                        message_display(((250)+95),(495),"Passar a vez",20,(255,255,255,255))
##                        pygame.display.update(pygame.Rect((270,470,150,50)))
##                    else:
##                        pygame.draw.rect(screen,vermelho,(((250)-170),470,150,50))
##                        message_display(((250)-95),(495),"Desistir",20,(255,255,255,255))
##                        pygame.draw.rect(screen,azul,(((250)+20),470,150,50))
##                        message_display(((250)+95),(495),"Passar a vez",20,(255,255,255,255))
##                        pygame.display.update(pygame.Rect((80,470,150,50)))
##                        pygame.display.update(pygame.Rect((270,470,150,50)))
##                elif event.type==pygame.QUIT:
##                    sair=False
##                    zera_matriz(tabuleiro, tabuleiro_orig)
##                    if(minhas_pecas=="RED"):
##                        send("GANHOU GREEN",client_socket)
##                    elif(minhas_pecas=="GREEN"):
##                        send("GANHOU RED",client_socket)
##
##        clock.tick(60)
##
##
##
##
##def animation_ganhador_sorteio():
##    time1=time.time()
##    time2=time1
##    texto="WIN"
##    if(jogador_atual=="GREEN"):
##        message_display((300),475,texto,20,(0,0,0,255))
##    elif(jogador_atual=="RED"):
##        message_display((700),475,texto,20,(0,0,0,255))
##    pygame.display.update()
##    while(time2-time1<=3):
##        time2=time.time()
##
##
##
##def text_objects(text, font,cor):
##    textSurface = font.render(text, True, cor)
##    return textSurface, textSurface.get_rect()
##def message_display(x,y,text,size,cor):
##    largeText = pygame.font.Font('freesansbold.ttf',size)
##    TextSurf, TextRect = text_objects(text, largeText,cor)
##    TextRect.center = (x,y)
##    pygame.display.get_surface().blit(TextSurf, TextRect)
##    
##   
##    
##
##def criacao_tela_de_escolha():
##    texto="Sorteio do primeiro jogador"
##    
##    largura, altura = screen.get_size()
##    screen.fill(cinza)
##    screen.blit(Circ_Verme,(((largura/2)+180),400))
##    screen.blit(Circ_Verde,(((largura/2)-220),400))
##    pygame.draw.rect(screen,verde,(((largura/2)-250),450,100,50))
##    pygame.draw.rect(screen,vermelho,(((largura/2)+150),450,100,50))
##    pygame.draw.rect(screen,azul,(((largura/2)-50),450,100,50))
##    message_display((largura/2),(475),"Vai",20,(255,255,255,255))
##    message_display(largura/2,altura/2,texto,35,(0,0,0,255))
##
##if __name__ == "__main__":
##    try:
##        pygame.init();
##        
##        
##
##    except:
##        print("O modulo pygame não foi inicializado corretamente")
##    pygame.display.init()
##    criacao_tela_de_colocar_nome()
##    pygame.quit()   
##        
##
##
##
