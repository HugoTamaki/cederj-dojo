def converte_telefone(texto):
  dic = {
    'ABC': '2',
    'DEF': '3',
    'GHI':'4',
    'JKL':'5',
    'MNO':'6',
    'PQRS':'7',
    'TUV':'8',
    'WXYZ':'9',
    ' ': ' ',
    '-':'-',
    '1': '1',
    '0': '0'

  }
  result = ""
  for i in range(len(texto)):
    for k, v in dic.items():
      if texto[i] in k:
        result += v

    # if texto[i] == 'A' or texto[i]== 'B'or texto[i]== 'C':
    #   result += "2"
    # elif texto[i] == 'D' or texto[i] == 'E' or texto[i] == 'F':
    #   result += "3"
    # elif texto[i]=='G' or texto[i] == 'H'or texto[i] == 'I':
    #   result+="4"
    # elif texto[i] == ' ':
    #   result += "-"
    # elif texto[i] == '1':
    #   result += '1'
    # elif texto[i] == '0':
    #   result += '0'




  return result