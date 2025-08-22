#4. Busca Linear


def busca_nome():

  while True:
    entrada = input("\nBusque um nome: ")
    lista_nome = ['Ana', 'Beatriz', 'Silva', 'Chris', 'Emelly', 'João', 'Carlos', 'Maria', 'Pedro', 'Gabriela', 'Mário', 'Naruto', 'Goku', 'Pikachu', 'Gioliano']
    

    if entrada in lista_nome:
      print("\n[ Esse nome está na posição:", lista_nome.index(entrada),"]")
      break
     
    if entrada not in lista_nome:
      print("\nEsse nome não está na lista :(") 
      break

busca_nome()