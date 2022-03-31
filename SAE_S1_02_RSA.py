from random import randint

# Donne tous les nombres premiers avant n
def list_prime(n) :
	tab = []
	if n < 2 :
		return -1
	for i in range(2,n+1) :
		occ = 0
		for j in range(1,i+1) :
			if i % j == 0 :
				occ += 1
		if occ == 2 :
			tab.append(i)
	return tab


# Test si deux nombres sont premier entre eux
def qotrem(a,b):
	iA=a
	iB=b
	quotient=0
	assert ((a>=0) and (b>0))
	while iA >=b :
		iA = iA - iB
		quotient += 1 
	r = a - (b*quotient)
	return(quotient,r)

def extended_pgcd(a,b) :
	return euclide_aux(a,b,1,0,0,1)
def euclide_aux(a,b,u0,u1,v0,v1):
	if qotrem(a,b)[1] == 0 :
		return b,u1,v1
	else :
		q,r = qotrem(a,b)
		return euclide_aux(b,r,u1,(u0-q*u1),v1,(v0-q*v1))


# crée les clés (clé publique et clés privé)
def key_creation() :
	# Sélection de deux nombre p et q premier distinct.
	p, q = 0, 0
	while p == q :
		p, q = list_prime(randint(100,1000))[-1], list_prime(randint(100,1000))[-1]

	# Calcule de n
	n = p * q

	# Calcule de Pn
	Pn = (p-1) * (q-1)

	# Préparation des clés
	# Calcule de e pour que extended_pgcd(e,Pn) = 1
	e = randint(2,1000)
	while extended_pgcd(e,Pn)[0] != 1 or extended_pgcd(e,Pn)[1] < 0 or extended_pgcd(e,Pn)[1] > Pn :
		e = randint(2,1000)

	# Calcule de d inverse de e
	d = extended_pgcd(e,Pn)[1]

	# Création de la clé publique
	pub = (n,e)

	# Création de la clé privée
	priv = d

	return n,pub,priv


# crypt le message
def encryption(n,pub,msg) :
	trad = convert_msg(msg)
	trad4 = []
	for i in range(0,len(trad),4) :
		trad4.append("".join(trad[i:i+4]))

	while len(trad4[-1]) < 4 :
		trad4[-1] = trad4[-1] + '0'

	trad4_int = []
	for j in range(len(trad4)) :
		trad4_int.append(str((int(trad4[j])**pub[1])%n))

	return trad4_int

# Converti le msg en ASCII
def convert_msg(msg) :
	res = []
	for i in range(len(msg)) :
		tmp = ord(msg[i])
		str_tmp = str(tmp)
		while len(str_tmp) < 3 :
			str_tmp = '0' + str_tmp
		for j in range(len(str_tmp)) :
			res.append(str_tmp[j])
	return res

# decrypt le message
def decryption(n,priv,msg) :
	decrypt = []
	for i in range(len(msg)) :
		decrypt.append(str((int(msg[i])**priv)%n))
		while len(decrypt[i]) < 4 :
			decrypt[i] = '0' + decrypt[i]

	while decrypt[-1][-1] == '0' :
		tmp = decrypt[-1][0:-1]
		decrypt[-1] = tmp


	decrypt = "".join(decrypt)
	decrypt3 = []
	for i in range(0,len(decrypt),3) :
		decrypt3.append(decrypt[i:i+3])

	res = ""
	for i in range(len(decrypt3)) :
		res = res + chr(int(decrypt3[i]))

	return res