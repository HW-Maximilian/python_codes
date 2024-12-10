

'''
    Es 9: 3 punti
    Si definisca la funzione es9(pathDir ) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che:
    - riceve come argomento l'indirizzo di una cartella.
    - restituisce una lista contenente i nomi delle sottocartelle in essa contenute a
      qualsiasi livello e per ogni sottocartella anche lo spazio  (in byte) occupato all'interno 
      della cartella da eventuali file di tipo .txt.
      La lista contiene dunque coppie, il primo elemento della coppia e' il nome di 
      una sottocartella ed il secondo e' lo spazio occupato dai file .txt presenti nella
      sottocartella.
      Le coppie devono comparire nella lista ordinate in modo decrescente rispetto 
      alla loro seconda componente e  a parita' vanno ordinate poi in modo lessicografico 
      crescente rispetto alla prima componente.
      File e cartelle il cui nome comincia  col carattere '.' non vanno considerati. 
      
      Ai fini dello svolgimento dell'esercizio possono risultare utili 
      le seguenti funzioni nel modulo os:
      os.listdir(), os.path.isfile(), os.path.isdir(), os.path.basename(), 
      os.path.getsize()

    Esempio: con es9('Informatica/Software') viene restituita la lista:
    [('SistemiOperativi', 287), ('Software', 10), ('BasiDati', 0)]

'''

import os

from IPython.testing.tools import full_path


def search_node(pathDir):
    objects = os.listdir(pathDir)
    lista = []
    size = 0

    if objects == "":
        return []

    for obj in objects:
        f_path = f'{pathDir}/{obj}'

        if os.path.isdir(obj) and not obj.startswith("."):
            next_level = search_node(f_path)
            lista.extend(next_level)

        elif os.path.isfile(obj) and not obj.startswith('.') and obj.endswith('.txt'):
            size += os.path.getsize(f_path)

    return lista.append((os.path.basename(pathDir), size))

def es9(pathDir):
    return search_node(pathDir)
                
    
        
