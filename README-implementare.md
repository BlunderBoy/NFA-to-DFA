% Tema2 
% Macarie Razvan Cristian 332CB

## Clasa NFA
Initial citim intr-o clasa NFA fisierul de input. Clasa are ca membri:   
- Numarul de stari (un numar)   
- O lista (sau un singur numar) cu starile finale   
- Un tabel de tranzitii reprezentat ca un dictionar ce are ca chei un tuplu (stare, simbol)
si ca valoare o lista de stari sau o stare (un numar)    

## Functia `epsilonClojure()`
Intoarce pentru o stare sau o lista de stari inchiderea epsilon pentru aceasta.
Am folosit un algoritm de tipul Depth First Search (implementat cu o stiva in loc de recursie) pentru a gasi 
inchiderea epsilon pentru o stare. Pentru a reprezenta rezultatul folsim un set astfel incat sa nu avem duplicate.

## Functia `availableSimbols()`
Intoarce o lista cu toate simboluri pe care exista macar o tranzitie. Folositoare atunci cand cautam tranzitia
dintr-un subset catre alt subset pentru a itera prin simboluri.

## Transformarea
In stariRezultate tinem un set de tupluri (nu putem sa avem set de liste) pentru subseturile gasite pana in acest 
moment. Folosim un set pentru a nu adauga stari duplicat. Lista stari este folosita pentru a pastra ordinea 
in care am gasit starile.  
Folosim o coada pentru a parcurge subseturile gasite prin algoritm.  
Pasii pe care ii urmam:    
1. Initial in coada avem epsilonClojure(starea initiala) si pornim de acolo.  
2. Pentru fiecare simbol gasim subsetul urmator si daca nu e in coada introducem acel subset.  
3. Salvam tranzitia din subsetul curent in epsilonClojure(subset urmator) intr-un nou dictionar.  
4. Repetam acest proces dand deque pana cand coada este goala si nu mai adaugam nimic in coada.   
5. Returnam un tuplu de (stari[^1], tranzitii)   

## Printarea finala
* Numarul de stari reprezinta lungimea listei de stari.
* Numerotarea starilor se face in functie de index-ul din lista de stari. Starile finale sunt cele care contin in ele
starea finala initiala din NFA.
* Dictionarul este transformat intr-o lista prin `dict.items()` si apoi lista este sortata[^2] dupa indexul starii


[^1]: Lista de stari contine duplicate asa ca ele sunt scoase la final din lista. Asta a fost singura abordare care sa imi
pastreze ordinea (sa evit un cast la/folosirea unui set).
[^2]: Ca sa apara in output frumos starile in ordine 0,1,2.. etc.
