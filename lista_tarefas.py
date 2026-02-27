tarefas = []

# Adicionamos algumas tarefas manualmente
tarefas.append("Estudar Python")
tarefas.append("Ir ao ginásio")
tarefas.append("Comprar pão")

print("Minha lista atual:", tarefas)

# Removemos o primeiro item (índice 0)
tarefas.pop(0)

print("\nLista atualizada:")
for item in tarefas:
    print("- " + item)
print(tarefas)