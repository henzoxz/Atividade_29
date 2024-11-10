# Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos estão presentes e a lista dos nomes. Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.

# Exemplo de entrada:
# Alunos presentes: ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Exemplo de saída:
# Alunos presentes: 4
# Lista de alunos presentes: Ana, Bruno, Carlos, Daniela
# Aviso: Poucos alunos presentes. Revisar lista de chamada.

lista_alunospresentes = []
quantidade = []

while True:
    alunos = input("Digite o nome do aluno: ")
    lista_alunospresentes.append(alunos)
    quantidade.append(alunos)
    
    if alunos == "fim":
        lista_alunospresentes.remove("fim")
        break
    
    

print("Alunos presentes: {}".format(len(lista_alunospresentes)))
print(lista_alunospresentes)

if len(lista_alunospresentes)<5:
    print("Poucos alunos presentes, favor revisar a lista de chamada.")
else:
    print("Ok")