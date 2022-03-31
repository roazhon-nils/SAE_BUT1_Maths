import numpy as np

F24 = [[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]
matrice = np.array([[1,1,0,1],[1,0,1,1],[1,0,0,0],[0,1,1,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

# crée tous les vecteurs de taille 7 grâce aux vecteurs de taille 4
def vect7() :
	res = []
	for i in F24 :
		b = np.array(i)
		res.append(matrice.dot(b)%2)
	return res

# vérifie si le poid de toutes les additions des vecteurs de taille 7 est supérieur ou égal à 3
def addition(F27) :
	occ = 0
	for i in range(len(F27)) :
		for j in range(i+1,len(F27)) :
			c = np.add(F27[i],F27[j])
			for k in c :
				if k == 1 :
					occ += 1
			if occ < 3 :
				return False
			occ = 0
	return True

# multiplie la matrice au vecteur donné
def multiplication(msg) :
	msg_bis = np.array(msg)
	return matrice.dot(msg_bis)%2

# renvoie le poid d'un vecteur
def poids(msg) :
	occ = 0
	for i in msg :
		if i == 1 :
			occ += 1
	return occ

# génère du bruit sur un vecteur (1 chance sur 4 de changer 1 bit)
def noise(vect_msg):
	"""
	prend un vecteur vect_msg et renvoie ce vecteur potentiellement bruite
	"""
	### on fait une copie du vecteur initial
	vect = vect_msg.copy()
	### une chance sur quatre de ne pas bruiter le vecteur
	test = np.random.randint(0,4)
	if test>0:
		index = np.random.randint(0,np.size(vect))
		vect[index] = (vect[index] +1)%2
	return vect

# corrige le bruit
def correction(msg):
	msg_bis = np.array(msg)
	for i in F24 :
		count = 0
		msg2 = np.add(matrice.dot(i),msg_bis)%2
		for j in msg2 :
			if poids(msg2) == 1 :
				if j == 1 :
					msg_bis[count] = (msg_bis[count] + 1) % 2
			count += 1

	return msg_bis

# converti en binaire
def convert_bi(msg) :
	msg_bis = msg.copy()
	tab_bi_bis = []
	for i in range(len(msg_bis)) :
		tab_bi = []
		for j in range(len(msg_bis[i])) :
			tmp = []
			tmp2 = int(msg_bis[i][j])
			while tmp2 >= 1 :
				tmp.append(tmp2%2)
				tmp2 = tmp2//2

			while len(tmp) < 4 :
				tmp.append(0)

			tmp.reverse()
			tab_bi.append(tmp)

		tab_bi_bis.append(tab_bi)

	return tab_bi_bis

# converti en décimal
def convert_deci(msg) :
	decimal = 0
	msg.reverse()
	for i in range(len(msg)) :
		decimal = decimal + msg[i]*(2**i)
	return str(decimal)