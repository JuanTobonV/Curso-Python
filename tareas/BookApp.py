
friends = {}
books = {}
booking = {}


def main():
    while(True):
        print(menu())
        user_option = int(input("Escoje una opción: "))

        match user_option:
            case 1:
                createFriend()
            case 2:
                create_books()
            case 3:
                booking_books()
            case 4:
                show_friend()
            case 5:
                show_booking()
            case 6:
                show_books()
            case _:
                print("Hasta luego!")
                break

def menu():
    return (
        "¿Qué deseas hacer?\n\n"
        "1.  Registrar amigos\n"
        "2.  Registrar libros\n"
        "3.  Registrar Prestamos\n"
        "4.  Ver mis amiguitos\n"
        "5.  Ver mis prestamos\n"
        "6.  Ver mis libros\n"
        "7.  Salir\n\n"
    )

def createFriend():

    friend = []

    id_friend = int(input("Id Amigo: ") )
    name_friend = input("Nombre amigo:")
    friend.append(name_friend)
    phone = input("Telefono: ")
    friend.append(phone)
    friends.update({id_friend: friend})




def create_books():
    book = []
    id_book = int(input("Id libro: "))
    book_name = input("Nombre Libro: ")
    book.append(book_name)
    book_author = input("Autor: ")
    book.append(book_author)
    books.update({id_book: book})


def booking_books():
    lend_book=[]
    id_book_loan = int(input("id prestamo: "))
    id_friend = int(input("Buscar amigo por id: "))
    friend = search_friend_by_id(id_friend)
    user = friend[0] 
    lend_book.append(user) 
    id_book = int(input("Buscar libro por id: "))
    book = search_book_by_id(id_book)
    book_name = book[0]
    lend_book.append(book_name)
    loan_date= input("dia/mes/año")
    lend_book.append(loan_date)
    return_date = input("dia/mes/año")
    lend_book.append(return_date)
    booking.update({id_book_loan: lend_book})


def show_friend():
    for i,j in friends.items():
        print(i,j)


def show_books():
    for i,j in books.items():
        print(i,j)

def show_booking():
    for i,j in booking.items():
        print(i,j)



def search_friend_by_id(id_friend):
    friend = friends.get(id_friend)
    return friend 

def search_book_by_id(id_book):
    book = books.get(id_book)
    return book        


if __name__ == "__main__":
    main()
