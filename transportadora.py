def dimensoesObjeto(): # função para informações sobre o volume do objeto
  while True: #dentro do laço iremos colocar condições de acordo com a tabela e também mensagem de erro caso o usuário digite valor não numérico
    try: #usando o try e except evitaremos que o programa pare caso o usuário digite um dado incorreto
      altura=int(input('\nDigite a altura do objeto(em cm):'))
      comprimento=int(input('\nDigite o comprimento do objeto(em cm):'))
      largura=int(input('\nDigite o largura do objeto(em cm):'))
      
      volumepacote = altura * largura * comprimento # cálculo p/ achar o volume do pacote
      
      if volumepacote <=1000 :  
        dimensao = 10
        return dimensao
      elif  (volumepacote >=1001) and (volumepacote <= 10000)  : 
        dimensao = 20        
        return dimensao        
      elif  (volumepacote >=10001) and (volumepacote <= 30000)  :
        dimensao = 30        
        return dimensao        
      elif  (volumepacote >=30001) and (volumepacote <= 100000)  :
        dimensao = 50         
        return dimensao
      else:
        print('\nVolume não permitido. Tente novamente.')
        continue
    except ValueError: #mensagem de erro caso o usuário não digite valor numérico, pois as variavéis são tipo int
      print('\nDado incorreto. Favor preencher novamente.')
      continue 

def pesoObjeto(): # função para informações sobre o peso do objeto
  while True:
    try:
      peso = float(input('\nDigite o peso do objeto(em kg):'))
      if peso <=0.1 :
        multiPeso = 1           
        return multiPeso        
      elif  (peso >=0.11) and (peso <= 1)  : 
        multiPeso = 1.5         
        return multiPeso               
      elif  (peso >=1.10) and (peso <= 10)  :
        multiPeso = 2           
        return multiPeso               
      elif  (peso >=10.1) and (peso <= 30)  :
        multiPeso = 3           
        return multiPeso               
      else:
        print('\nPeso não permitido. Tente novamente')
        continue
    except ValueError: #mensagem de erro caso o usuário não digite valor numérico, pois as variavéis são tipo float
      print('\nDado incorreto. Favor preencher novamente.')
      continue   
    
def rotaObjeto(): # função para informações sobre a rota objeto
  while True:
      print('\nNosso quadro de rotas:')
      print('|Código| |            ROTA               |')
      print('|  RS  | |De Rio de Janeiro até São Paulo|')
      print('|  SR  | |De São Paulo até Rio de Janeiro|')
      print('|  BS  | |De Brasília até São Paulo      |')
      print('|  SB  | |De São Paulo até Brasília      |')
      print('|  BR  | |De Brasília até Rio de Janeiro |')
      print('|  RB  | |De Rio de Janeiro até Brasília |')      
      rota = input('\nDigite a rota que deseja:')      
      if (rota == 'RS') or (rota == 'SR'):
        rotaEscolhida = 1          
        return rotaEscolhida
      elif  (rota == 'BS') or (rota == 'SB'): 
        rotaEscolhida = 1.2          
        return rotaEscolhida        
      elif  (rota == 'RB') or (rota == 'BR'):
        rotaEscolhida = 1.5           
        return rotaEscolhida      
      else:
        print('\nRota inexistente. Tente novamente')
        continue      

##Programa Principal
nomeloja= 'Tairine'
print('Bem Vindo a companhia de Logística {}'.format(nomeloja))
recebeVolume= dimensoesObjeto()
recebePeso= pesoObjeto()
recebeRota= rotaObjeto()
valorTotalFinal= recebeVolume * recebePeso * recebeRota 
print('\n')
print('*'*80)
print('Valor Total para o transporte é R${:.2F} (dimensões:{} * peso:{} * rota:{})'.format(valorTotalFinal, recebeVolume, recebePeso, recebeRota)) 
print('*'*80)
