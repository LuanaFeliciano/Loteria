from random import randint
jogo = []
listaJogadores = []
jogadores = []
jogadas = 1
acertos = []
quadraLista = []
quinaLista =[]
megaLista=[]
contador = 0
#gerando jogo aleatorio
for i in range(6):
   jogo.append(randint(1, 60))

print('========== NÚMERO DA MEGASENA ==========')  
print(jogo)
print('')


total = int(input("PREMIAÇÃO TOTAL: R$ "))
print('='*40)

while jogadas ==1:
  #zerando jogadores
  jogadores = []
  #Gerando numero dos jogadores
  count = 1 
  for i in range(6):
      jogadores.append(int(input(f'{count}º Número: ')))
      count+=1
  print('')   
      #guardando numero dos jogadores em uma lista
  listaJogadores.append(jogadores)
  jogadas = int(input("1-Gerar Mais Jogadores   0-Encerrar: "))
  

  #verificando numero do jogador dentro da lista (lista dentro de lista)
  for jogador in listaJogadores:
      jogadorAcertou = []
      for elem in range(len(jogador)):
        #passar em cada elemento da lista comparando
        for x in range(len(jogo)):
          if jogador[elem] == jogo[x]:
            jogadorAcertou.append(elem)
  #guardar so os elementos acertados
  acertos.append(jogadorAcertou)   

contador = 0
for lista in acertos:
  if len(lista)==4:
      quadraLista.append(listaJogadores[contador])
      
  elif len(lista)==5:
      quinaLista.append(listaJogadores[contador])
      
  elif len(lista)==6:  
      megaLista.append(listaJogadores[contador])

  contador = contador+1

print('')

if len(quadraLista) >= 1:
  print('========== QUADRA ==========')
  quadra = total*0.2
  quadraPremio = quadra/len(quadraLista)
  print(f'{len(quadraLista)} Ganhador(es)')
  print(f'Número(s) ganhador(es): {quadraLista} ')
  print(f"Prêmio: R$ {quadraPremio:.2f}")
  print('')

if len(quinaLista) >= 1:
  print('========== QUINA ==========')
  quina = total*0.3
  premioQuina = quina/len(quinaLista)
  print(f'{len(quinaLista)} Ganhador(es)')
  print(f'Número(s) ganhador(es): {quinaLista} ')
  print(f"Prêmio: R$ {premioQuina:.2f}")
  print('')

if len(megaLista) >= 1:
  print('========== MEGA ==========')
  mega = total*0.5
  premioMega = mega/len(megaLista)
  print(f'{len(megaLista)} Ganhador(es)')
  print(f'Número(s) ganhador(es): {megaLista} ')
  print(f'Prêmio: R$ {premioMega:.2f}')
  print('') 