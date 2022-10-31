# HW2req

## Funzione xkcd_to_list_of_weights (trasformazione della stringa in lista di interi)

Cicla dalla fine all'inizio della stringa e se il carattere selezionato non è uno "0" aggiunge l'elemento all'inizio della stringa di interi.
In caso sia 0, aumenta un contatore di uno. Questo contatore è un esponente. Una volta che troverà un carattere che non corrisponde a "0" viene aggiunto come primo elemento della lista il numero selezionato moltiplicato per 10 elevato al valore dell'esponente. Ovviamente se questo secondo contatore (exp) è diverso da 0 viene resettato.

## Funzione list_of_weights_to_number (trasforma la lista di interi in un numero intero)

creo una variabile temporanea che è uguale all'ultimo numero della lista di interi

Si ha un ciclo che parte dal penultimo elemento della lista fino al primo.
se l'elemento selezionato è maggiore o uguale all'elemento successivo a quello selezionato aggiungo questo valore alla variabile temporanea (num), altrimento lo sottraggo.

## Funzione decode_value

Semplicemente vengono unite le due funzioni precedenti

## decode_XKCD_tuple

Viene creata una lista che contiene i valori decodificati (midlist). Successivamente midlist viene messa in ordine. Infine viene ritornata una lista che contiene i primi k valori di midlist.
