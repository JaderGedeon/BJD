######################################
# Disciplina: PI 2: Narrativa
# Título: Media Bimestral
# Autor: Jader G. O. Rocha
# Data: 16/02/20
#####################################

nota = 0

for i in range(1,5):
    nota += float(input("Digite a %dª nota: "%(i)))

print("A média bimestral é:",(nota/4))