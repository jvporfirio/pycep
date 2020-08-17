import pycep_correios

print('insert your cep:')
cep = input('>>')

try:
    endereco = pycep_correios.get_address_from_cep(cep)
    logradouro = endereco['logradouro']
    bairro = endereco['bairro']
    cidade = endereco['cidade']
    uf = endereco['uf']
    cep = endereco['cep']
    complemento = endereco['complemento']

    if complemento == "":
        print(logradouro)
        print(bairro)
        print(cidade)
        print(uf)
        print(cep)
    else:
        print(logradouro)
        print(bairro)
        print(cidade)
        print(complemento)
        print(uf)
        print(cep)

except:
    print('search error')