import SAE_S1_02_RSA as RSA
import SAE_S1_02_Corr as Corr


# création du message
message = input("Quel message souhaité vous envoyer : ")

# création des clés
cle = RSA.key_creation()

# cryptage du message
msg = RSA.encryption(cle[0],cle[1],message)

# convertion du message crypté en binaire (vecteur de 4 bits)
msg2 = Corr.convert_bi(msg)

# convertion des vecteurs de 4 en vecteurs de 7
msg3 = msg2.copy()
for i in range(len(msg3)) :
	for j in range(len(msg3[i])) :
		msg3[i][j] = Corr.multiplication(msg3[i][j])

# bruitage du message
msg4 = msg3.copy()
for i in range(len(msg4)) :
	for j in range(len(msg4[i])) :
		msg4[i][j] = Corr.noise(msg4[i][j])

# correction du bruit
msg5 = msg4.copy()
for i in range(len(msg5)) :
	for j in range(len(msg5[i])) :
		msg5[i][j] = Corr.correction(msg5[i][j])

# convertion des vecteurs de 7 en vecteurs de 4 (index 2,4,5 et 6 sur le vecteur de 7)
msg6 = msg5.copy()
msg8 = []
for k in range(len(msg6)) :
	msg7 = []
	for i in range(len(msg6[k])) :
		tmp = []
		tmp.append(msg6[k][i][2])
		for j in range(4,7):
			tmp.append(msg6[k][i][j])
		msg7.append(tmp)
	msg7.reverse()
	msg8.append(msg7)

# convertion de binaire en decimale
msg9 = msg8.copy()
for k in range(len(msg9)) :
	for i in range(len(msg9[k])) :
		msg9[k][i] = Corr.convert_deci(msg9[k][i])

# remet dans le bon sens le message
for i in range(len(msg9)):
	msg9[i].reverse()
	msg9[i] = "".join(msg9[i])

# decryptage du message
msg10 = msg9.copy()
print(RSA.decryption(cle[0],cle[2],msg10))