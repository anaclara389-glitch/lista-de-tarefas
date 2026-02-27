tarefas = []

# Adicionamos algumas tarefas manualmente
tarefas.append("Estudar Python")
tarefas.append("Ir ao ginásio")
tarefas.append("Comprar pão")
tarefas.append("Fazer o dever de casa")

print("Minha lista atual:", tarefas)

# Removemos o primeiro item (índice 0)
tarefas.pop(1)

print("\nLista atualizada:")
for item in tarefas:
    print("- " + item)
print(tarefas)