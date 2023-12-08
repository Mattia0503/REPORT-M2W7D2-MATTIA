import random
import string

#questa funzione genera una password di 8 caratteri alfanumerici casuali
#per farla, creo una variabile charaters con tutte le lettere e numeri
#utilizzo la funzione random.choice per selezionare casualmente uno
#di questi caratteri per poi aggiungerla alla variabile pswdchar
def passwordeasy():    
    pswdchar = ""
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    for i in range(0,8):
        pswdchar += random.choice(characters)
    print("password generata: ", pswdchar)

#questa funzione genera una password di 20 caratteri Ascii casuali
#per farla la logica è la stessa della funzione passwordeasy()
#ma mi avvalgo della librearia string e della funzione ascii_letters
#utlilizzando sempre random.choice seleziona casualemente uno di quei caratteri
def passwordAscii():
    pswdascii = ""        
    for i in range(0,20):
        pswdascii += random.choice(string.ascii_letters)
    print("password complessa di 20 caratteri: ", pswdascii)


#funzione principale
option = "a"

while option == 'a':
    #chiedo all'utente che password desidera generare
    print("Scegliere quale password generare fra le seguenti opzioni: \n")
    print("A - password di 8 caratteri alfanumerici\n")
    print("B - password complessa di 20 caratteri Ascii\n")
    option = input("Scelta: ")

    if option == 'a':
        #richiamo la funzione di password semplice
        passwordeasy()
    elif option == 'b':
        #richiamo la funzione di password Ascii
        passwordAscii()
    else:
        #opzione errata
        print("Valore errato! \n")
    #chiedo all'utente se ne vuole generare un'altra
    print("Vuoi generare un'altra password?\n")
    print("A = Sì\n")
    print("B = No\n")
    option = input("Scelta: ")
