

def troco(texto):
  quantidadeNotas = 0

  dic = {
    "nota de 100": 100,
    "nota de 50": 50,
    "nota de 20": 20,
    "nota de 10": 10
  }

  if texto==100:
   resposta="1 nota de R$100"
  elif texto==50:
    resposta="1 nota de R$50"
  elif texto==20:
    resposta="1 nota de R$20"
  elif texto==10:
    resposta="1 nota de R$10"
  elif texto==30:
    quantidadeNotas = 30//20
    resposta= str(quantidadeNotas) +  " nota de R$10 e " + str(quantidadeNotas)+" nota de R$20"
  elif texto==80:
    quantidadeNotas = (80//50) + ((80%50)//20) + ((30%20)//10)
    resposta= str(quantidadeNotas) + " nota de R$50 e " + str(quantidadeNotas) + " nota de R$20" + str(quantidadeNotas) + " nota de R$10"


  return resposta