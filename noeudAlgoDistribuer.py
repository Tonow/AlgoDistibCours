class Noeud
    '''un noeud sur le quelle on peut envoyer des messages'''

    def __init__ (self, nom):
        self.nom = nom

    def brodcast()




'''#correction  Topographie centraliser
### nb envoie de message = O(nbNode)
### temps O(nbNode)

if myId == 1
for i 0:nbNode:
    if i =! myId:
        send (i,msg)
else:
    recive(1,msg)
'''


'''#correction  Topographie distibuer anneaux
### nb envoie de message = O(nbNode)
### temps O(nbNode)

for i 0:nbNode:
    #envoie l'information au suivant
    if myId == i and is not nbNode:
        send (i+1,msg)

    #reçois le message du precédant
    elif myId == i+1 and myId != nbNode +1:
        recive(i,msg)

    # si non concerner alors attent
    else:
        pass


######### sol prof
if myId == 1:
    send(2,msg)
else:
    recive(myId - 1, msg)
    if (myId != nbNode):
        send(myId + 1 , msg)




#correction  Topographie distibuer anneau dans les deux sens
### nb envoie de message = O(nbNode)
### temps O(nbNode/2)

if myId == 0:
    send(1,msg)
    send(nbNode,msg)

if nbNode/2 + 1 >= myId:
    recive(myId-1, msg)
    if myId != (nbNode+1):
        send(myId+1, msg)

else:
    recive((myId+1) % nbNode, msg)
    if myId != (myId-1):
        send(myId-1, msg)


# hypercube
send(myId + 2^t) # on met le t dans le message et on l'incremente




##Scatter
'''
decoupe un tableau
envoyer la meme propostion d'un tableau a differant noeud
'''

nbNoeud = getNbNoeud()
myId = getId()
tab = tableau

portionPourChaquePartie = int( (tab.leng() / nbNoeud) +1 )

if myId == 0:
    MyChunk = tab[0:portionPourChaquePartie]

def scatter(id,tab):


for i 0:nbNode -1:
    if i =! myId:
        send (i,tab[portionPourChaquePartie * i:portionPourChaquePartie * i+1])
    else:
        recive(1,tableauOk)

send (nbNoeud -1 , tab[nbNoeud - 1 * portionPourChaquePartie : tab.leng()])
'''
