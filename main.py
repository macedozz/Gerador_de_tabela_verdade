expressao_logica = input("Escreva a senteça desejada:").upper()

expressao_logica.strip()

expressao_logica = expressao_logica.replace("AND", " ^ ")
expressao_logica = expressao_logica.replace("OR", " V ")
expressao_logica = expressao_logica.replace("NOT", " ~ ")

print("Expressão:", expressao_logica)
