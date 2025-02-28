# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
  if conceito == "Especificidade":
    return "Adicionar detalhes para reduzir ambiguidades"

# COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:
  elif conceito == "Divisão em Passos":
    return "Quebrar tarefas em etapas menores"

  elif conceito == "Inserção de Exemplos":
    return "Fornecer exemplos para contextualizar"

  elif conceito == "Reformulação":
    return "Alterar o formato para maior clareza"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito". 
print(descrever_conceito(entrada))
