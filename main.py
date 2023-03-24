import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
fundo = "#3b3b3b"

#criação da janela
janela = Tk()
janela.title('JOKENPO')
janela.geometry('260x280')
janela.configure(bg=fundo)
janela.resizable(False,False)

#criação dos frames e dividindo a janela
frame_topo = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_topo.grid(row=0, column=0, sticky=NW)
frame_base = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_base.grid(row=1, column=0, sticky=NW)
#estilo da janela
estilo = ttk.Style(janela)
estilo.theme_use('clam')

#configurando o frame topo nome do jogador
jogador = Label(frame_topo, text='Jogador', height=1, anchor='center', font=('Ivy 10  bold'), bg=co1, fg=co0)
jogador.place(x=35, y=70)
#inserindo linha verde no canto sua vez
jogador_linha = Label(frame_topo, text='', height=10, anchor='center', font=('Ivy 10  bold'), bg=co0, fg=co0)
jogador_linha.place(x=0, y=0)
#pontuação
jogador_pontos = Label(frame_topo, text='0', height=1, anchor='center', font=('Ivy 30  bold'), bg=co1, fg=co0)
jogador_pontos.place(x=50, y=20)

#criando divisor entre pontos
divisor_pontos = Label(frame_topo, text=':', height=1, anchor='center', font=('Ivy 30  bold'), bg=co1, fg=co0)
divisor_pontos.place(x=125, y=20)

#configurando o pontuação do BOT
bot = Label(frame_topo, text='0', height=1, anchor='center', font=('Ivy 30  bold'), bg=co1, fg=co0)
bot.place(x=190, y=20)
#configurando o frame nome do BOT 
bot_linha = Label(frame_topo, text='Bot', height=1, anchor='center', font=('Ivy 10  bold'), bg=co1, fg=co0)
bot_linha.place(x=190, y=70)
#inserindo linha verde no canto vez do BOT
bot_pontos = Label(frame_topo, text='', height=10, anchor='center', font=('Ivy 30  bold'), bg=co0, fg=co0)
bot_pontos.place(x=255, y=0)


#criando linha base de empate
linha_decisao = Label(frame_topo, text='', width='255',anchor='center', font=('Ivy 1  bold'), bg=co0, fg=co0)
linha_decisao.place(x=0, y=95)

#Mostrando a escolha do JOGADOR
player = Label(frame_base, text='', height=1, anchor='center', font=('Ivy 10  bold'), bg=co0, fg=co0)
player.place(x=20, y=10)

#Mostrando a escolha do BOT
app_bot = Label(frame_base, text='', height=1, anchor='center', font=('Ivy 10  bold'), bg=co0, fg=co0)
app_bot.place(x=190, y=10)

#criando a variavel global dos jogadores
global desafiante
global bot_ia
global rodadas
global pontos_desafiante
global pontos_bot

pontos_desafiante = 0
pontos_bot = 0
rodadas = 7

#Criando a lógica do jogo
def jogar(i):
    global rodadas
    global pontos_desafiante
    global pontos_bot

    if rodadas > 0:
        print(rodadas)
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        bot_ia = random.choice(opcoes)
        desafiante = i

        app_bot['text'] = bot_ia
        app_bot['fg'] = co1

        player['text'] = desafiante
        player['fg'] = co1
        
        if desafiante == 'Pedra' and bot_ia == 'Pedra':
            print('Empate')
            jogador_linha['bg'] = co0
            bot_pontos['bg'] = co0
            linha_decisao['bg'] = co5
        
        if desafiante == 'Papel' and bot_ia == 'Papel':
            print('Empate')
            jogador_linha['bg'] = co0
            bot_pontos['bg'] = co0
            linha_decisao['bg'] = co5
        
        if desafiante == 'Tesoura' and bot_ia == 'Tesoura':
            print('Empate')
            jogador_linha['bg'] = co0
            bot_pontos['bg'] = co0
            linha_decisao['bg'] = co5

        elif desafiante == 'Pedra' and bot_ia == 'Papel':
            print('Bot Ganhou')
            jogador_linha['bg'] = co0
            bot_pontos['bg'] = co4
            linha_decisao['bg'] = co0
            pontos_bot += 10

        elif desafiante == 'Pedra' and bot_ia == 'Tesoura':
            print('Você Ganhou')
            jogador_linha['bg'] = co4
            bot_pontos['bg'] = co0
            linha_decisao['bg'] = co0
            pontos_desafiante += 10

        elif desafiante == 'Papel' and bot_ia == 'Tesoura':
            print('Bot ganhou')
            jogador_linha['bg'] = co0
            bot_pontos['bg'] = co4
            linha_decisao['bg'] = co0
            pontos_bot += 10

        elif desafiante == 'Papel' and bot_ia == 'Pedra':
            print('Você Ganhou')
            jogador_linha['bg'] = co4
            bot_pontos['bg'] = co0
            linha_decisao['bg'] = co0
            pontos_desafiante += 10

        elif desafiante == 'Tesoura' and bot_ia == 'Pedra':
            print('Bot Ganhou')
            jogador_linha['bg'] = co0
            bot_pontos['bg'] = co4
            linha_decisao['bg'] = co0
            pontos_bot += 10
            
        elif desafiante == 'Tesoura' and bot_ia == 'Papel':
            print('Você Ganhou')
            jogador_linha['bg'] = co4
            bot_pontos['bg'] = co0
            linha_decisao['bg'] = co0
            pontos_desafiante += 10

        #Contagem de pontos
        jogador_pontos['text'] = pontos_desafiante
        bot['text'] = pontos_bot
        #Rodadas
        rodadas -= 1

    else:
        #Contagem de pontos
        jogador_pontos['text'] = pontos_desafiante
        bot['text'] = pontos_bot

        encerrar_jogo()
        

#Definindo a função para iniciar o jogo, criando frame do meio das imagens e ocultando imagens na inicialização
def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global btn_ico_1
    global btn_ico_2
    global btn_ico_3

    btn_play.destroy()

    icon_1 = Image.open('img/pedra.png')
    icon_1 = icon_1.resize((50,50), Image.ANTIALIAS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    btn_ico_1 = Button(frame_base, command = lambda: jogar('Pedra'),width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font=('Ivi 10 bold'), anchor=CENTER, relief = FLAT)
    btn_ico_1.place(x=25, y=60)

    icon_2 = Image.open('img/papel.png')
    icon_2 = icon_2.resize((50,50), Image.ANTIALIAS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    btn_ico_2 = Button(frame_base, command=lambda: jogar('Papel'),width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font=('Ivi 10 bold'), anchor=CENTER, relief=FLAT)
    btn_ico_2.place(x=105, y=60)

    icon_3 = Image.open('img/tesoura.png')
    icon_3 = icon_3.resize((50,50), Image.ANTIALIAS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    btn_ico_3 = Button(frame_base, command=lambda: jogar('Tesoura'),width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font=('Ivi 10 bold'), anchor=CENTER, relief=FLAT)
    btn_ico_3.place(x=180, y=60)


#criando a função finalizar o jogo
def encerrar_jogo():
    global rodadas
    global pontos_desafiante
    global pontos_bot

    #reiniciando o jogo
    pontos_desafiante = 0
    pontos_bot = 0
    rodadas = 7

    btn_ico_1.destroy()
    btn_ico_2.destroy()
    btn_ico_3.destroy()

    #definindo o vencedor
    player_1 = int(jogador_pontos['text'])
    player_bot = int(bot['text'])

    if player_1 > player_bot:
        app_vencedor = Label(frame_base, text='PARABÉNS VOCÊ VENCEU !!!', height=1, anchor='center', font=('Ivy 10  bold'), bg=co0, fg=co4)
        app_vencedor.place(x=35, y=60)

    elif player_1 < player_bot:
        app_vencedor = Label(frame_base, text='AAHHH VOCÊ PERDEU!', height=1, anchor='center', font=('Ivy 10  bold'), bg=co0, fg=co5)
        app_vencedor.place(x=60, y=60)

    else: 
        app_vencedor = Label(frame_base, text='JOGO EMPATADO', height=1, anchor='center', font=('Ivy 10  bold'), bg=co0, fg='red')
        app_vencedor.place(x=70, y=60)

#Reiniciar jogo
    def jogar_novamente():
        jogador_pontos['text'] = '0'
        bot['text'] = '0'
        app_vencedor.destroy()
        btn_jogar_novamente.destroy()
        iniciar_jogo()
    
    #criando botão jogar denovo
    btn_jogar_novamente = Button(frame_base, command=jogar_novamente,width=30, text='JOGAR NOVAMENTE', bg='green', fg=co0, font=('Ivi 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    btn_jogar_novamente.place(x=5, y=151)



#criando botão PLAY JOKENPO
btn_play = Button(frame_base, command=iniciar_jogo,width=30, text='PLAY JOKENPO', bg='green', fg=co0, font=('Ivi 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
btn_play.place(x=5, y=151)

janela.mainloop()
