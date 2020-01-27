import json

# Lê o ficheiro JSON com os IDs e nomes das pessoas
with open('nomes.json', 'r') as nomes:
    data = json.load(nomes)


# print('Nomes:', data['pessoas'])

# Retorna o nome do ID procurado
def get_nome(id_procurado):
    for id in data['pessoas']:
        if id == str(id_procurado):
            # print('Nome da pessoa:', data['pessoas'][id])  # pessoas[id] é o nome da pessoa
            return data['pessoas'][id]
    # print('Este nome não consta na BD.')
    return 'Desconhecido'
