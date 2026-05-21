import re

def processar_conversa(texto):
   
 linhasTotal = texto.splitlines()

 regex = r"^(\d{2}/\d{2}/\d{4})\s(\d{2}:\d{2})\s-\s([^:]+):\s(.*)$"





 for linha in linhasTotal : 
    
  resultado = re.match(regex, linha)

  if resultado:
      print(resultado.groups()) #isso aqui vai trazer os dados separado por grupo, data, hora,remetente e conversa
       
     
 