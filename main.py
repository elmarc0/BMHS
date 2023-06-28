texto = 'lblalblanbla'
dis = 'bla'
cont = 0  #variavel que indica a posição que devemos começar a compareação na lista texto
veri = 0  #variavel que indica quantos caracteres iguais as strings tem
num = 0  #numero de vezes que a palavra apareceu


def compara(texto, palavra, trecho):
  tamanho = len(palavra)
  cont = 0
  while cont < tamanho:
    if palavra[cont] != texto[trecho + cont]:
      return False
    cont += 1
  return True

def ultimo(cha, st):
  n = len(st)  #caso o caracter procurado seja igual ao ultimo ou não tenha na palavra, retornamos o tamanho da string
  for i in range(len(st)):  # caso o caracter não seja o ultimo e ele exista na palavra, retornamos um valor que dempedera da posição dele
    if cha == st[i]:
      n = len(st) - (i)
  return n

def BMHS(texto, palavra):
  tamanho = len(texto)
  cont = 0
  ocorrencia = 0
  indice = len(palavra)
  while cont < tamanho:
    if compara(texto, palavra, cont):
      ocorrencia+= 1
    if cont + indice < len(texto):
      cont+= ultimo(texto[cont + indice], palavra)
    else:
      break
  return ocorrencia



print(BMHS(texto, dis))
