import re

linha = """
         18/05/2026 23:32 - Você criou este grupo
18/05/2026 23:32 - ‎Pedro Barbosa foi adicionado(a)
18/05/2026 23:32 - Nicolas: Oi
18/05/2026 23:33 - Nicolas: É para testar pra ver oq faz com as linhas separadas daqui já
18/05/2026 23:33 - Nicolas: Exportando a conversa daqui logo
18/05/2026 23:33 - Nicolas: Teste
18/05/2026 23:34 - Nicolas: A



"""

regex = r"^(\d{2}/\d{2}/\d{4})\s(\d{2}:\d{2})\s-\s([^:]+):\s(.*)$"

linhasTotal = linha.splitlines()



for linha in linhasTotal : 
    
 resultado = re.match(regex, linha)

 if resultado:
      print(resultado.groups())