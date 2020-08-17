import pycep_correios

print('insert your cep:')
cep = input('>>')

try:
    endereco = pycep_correios.get_address_from_cep(cep)
        if endereco['complemento'] == '':
            print(endereco['logradouro'])
            print(endereco['bairro'])
            print(endereco['cidade'])
            print(endereco['uf'])
            print(endereco['cep'])
        else:
            print(endereco['logradouro'])
            print(endereco['bairro'])
            print(endereco['cidade'])
            print(endereco['complemento'])
            print(endereco['uf'])
            print(endereco['cep'])
except:
    print('search error')