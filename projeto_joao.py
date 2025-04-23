# Simulando um CRUD de pessoas (nome + idade)
pessoas = {}

# CREATE
def adicionar_pessoa(nome, idade):
    if nome in pessoas:
        return f"{nome} já está cadastrado."
    pessoas[nome] = idade
    return f"{nome} foi adicionado com idade {idade}."

# READ
def listar_pessoas():
    if not pessoas:
        return "Nenhuma pessoa cadastrada."
    return "\n".join([f"{nome} - {idade} anos" for nome, idade in pessoas.items()])

# UPDATE
def atualizar_pessoa(nome, nova_idade):
    if nome not in pessoas:
        return f"{nome} não encontrado."
    pessoas[nome] = nova_idade
    return f"{nome} agora tem {nova_idade} anos."

# DELETE
def remover_pessoa(nome):
    if nome in pessoas:
        del pessoas[nome]
        return f"{nome} foi removido."
    return f"{nome} não encontrado."

# Função de saudação opcional (para a funcionalidade extra do exercício)
def projeto(nome, idade=None):
    if idade:
        return f"Olá, {nome}! Você tem {idade} anos."
    return f"Olá, {nome}!"

# FUNCIONALIDADE  - Buscar pessoa pelo nome
def buscar_pessoa(nome):
    if nome in pessoas:
        return f"{nome} está cadastrado com {pessoas[nome]} anos."
    return f"{nome} não foi encontrado no sistema."

# Testes simples
if __name__ == "__main__":
    print(adicionar_pessoa("João", 25))
    print(adicionar_pessoa("Maria", 30))
    print(listar_pessoas())
    print(atualizar_pessoa("João", 26))
    print(remover_pessoa("Maria"))
    print(listar_pessoas())
    print(projeto("Carlos", 22))


     # Testando nova funcionalidade: buscar pessoa
    print(buscar_pessoa("João"))
    print(buscar_pessoa("José"))