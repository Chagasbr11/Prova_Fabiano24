# Função para adicionar um livro à biblioteca
def add_book(library, title, author):
    book = {"title": title, "author": author}
    library.append(book)
    print(f'Livro "{title}" de {author} adicionado com sucesso!\n')

# Função para listar todos os livros da biblioteca
def list_books(library):
    if len(library) == 0:
        print("A biblioteca está vazia.\n")
    else:
        print("Lista de livros na biblioteca:")
        for idx, book in enumerate(library):
            print(f'{idx+1}. Título: {book["title"]}, Autor: {book["author"]}')
        print()

# Função para buscar um livro pelo título
def find_book_by_title(library, title):
    for book in library:
        if book["title"].lower() == title.lower():
            print(f'Livro encontrado! Título: {book["title"]}, Autor: {book["author"]}\n')
            return
    print("Livro não encontrado.\n")

# Função para exibir o menu de opções e interagir com o usuário
def menu():
    library = []
    while True:
        print("----- MENU -----")
        print("1. Adicionar um livro")
        print("2. Listar todos os livros")
        print("3. Buscar um livro por título")
        print("4. Sair")
        choice = input("Escolha uma opção (1-4): ")

        if choice == '1':
            title = input("Digite o título do livro: ")
            author = input("Digite o autor do livro: ")
            add_book(library, title, author)
        elif choice == '2':
            list_books(library)
        elif choice == '3':
            title = input("Digite o título do livro que deseja buscar: ")
            find_book_by_title(library, title)
        elif choice == '4':
            print("Saindo do sistema de biblioteca. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.\n")

# Chamar a função menu para iniciar o programa
menu()
