
lista_livros = []
id_global = 0
    
def cadastrar_livro():
    global id_global # para conseguir mudar a variável dentro da função
    id_global+= 1
    nome = str(input('Nome do livro: '))
    autor = str(input('Autor do livro: '))
    editora = str(input('Editora: '))

    livro = {
            'id': id_global,
            'nome': nome,
            'autor': autor,
            'editora': editora
        }

    lista_livros.append(livro)
    print('Livro cadastrado com sucesso')


def consultar_livro():
    while True:
        try:
            opc = int(input('Qual opção deseja:\n1. Consultar todos\n2. Consultar por ID\n3.Consultar por autor\n4. Retornar ao menu: '))
            if opc == 1:
                print(lista_livros)
            elif opc == 2:
                id_find = int(input('Qual ID deseja consultar?:'))
                livro_encontrado = None
                for livro in lista_livros:
                    if livro['id'] == id_find:
                        livro_encontrado = livro
                        break
                if livro_encontrado:
                    print('Livro encontrado:')
                    print('ID:', livro_encontrado['id'])
                    print('Nome:', livro_encontrado['nome'])
                    print('Autor:', livro_encontrado['autor'])
                    print('Editora:', livro_encontrado['editora'])
                else:
                    print('Livro não encontrado')
            elif opc == 3:
                autor_find = str(input('Nome do autor que deseja consultar:'))
                autor_encontrado = [autor for autor in lista_livros if autor['autor'] == autor_find]
                if autor_encontrado:
                        print('Livros encontrados do autor')
                        for autor in lista_livros:
                            print('ID', autor['id'])
                            print('Nome:', autor['nome'])
                            print('Autor: ', autor['autor'])
                            print('Editora: ', autor['autor'])
                else:
                    print('Livro não encontrado')
            elif opc == 4:
                break
            else:
                print('Opção inválida')
        except ValueError:
            print('Por favor, digite um número válido')


def remover_livro():
    id_remove = int(input('Qual o ID do livro a ser removido: '))
    for livro in lista_livros:
        if livro['id'] == id_remove:
            lista_livros.remove(livro)
            print('Livro removido com sucesso')
            return
    print('Livro não econtrado')

while True:
    try:
        opc_desejada = int(input(' 1. Cadastrar livro\n 2. Consultar livro\n 3. Remover livro\n 4. Encerrar programa\n Digite a opção desejada:'))
        if opc_desejada == 1:
            cadastrar_livro()
        elif opc_desejada == 2:
            consultar_livro()
        elif opc_desejada == 3:
            remover_livro()
        elif opc_desejada == 4:
            break
        else:
            print('Opção inválida')
    except ValueError:
        print('Valor não número, tente novamente')

