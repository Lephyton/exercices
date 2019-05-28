#import des librairies
import serial
import numpy as np
from matplotlib import pyplot as plt
import time
import struct
import csv
 
 
ser = serial.Serial('com7', 115200) #ouverture du port série. Il faut appareiller au pc le boitier et vérifier le numéro du port
duree=2
 
AGyY=0 #Angle Gyroscope axe Y
AFcY=0 #Angle Filtre Complémentaire axe Y
delta_t=0 #pas de temps entre deux mesures (lecture sur le port série environ 0,04s) 
TabFiltreComp = [0] * 5000 #déclaration des tableaux de données
TabGyY=[0] * 5000 #tableau angle gyroscope axe Y
TabAcY=[0] * 5000 #tableau angle accéléromètre axe Y
TabAk=[0] * 5000 #tableau angle calculé Kalman
inc= [0] * 5000 #tableau incréments
i=0 #incrément temps de mesure
u=0
 
fig, ax = plt.subplots() #création du graphe
fig.canvas.draw()
 
#fonction lecture : renvoi l'accélération en mg (axes X et Z) et la vitesse en °/s (axe Y)
def lecture():
    ser.write(b'e') #demande reception message 'a,b,c,d,e' selon le protocole
    data = ser.read(10) #affectation à data du message renvoyé
    if len(data)==10: #on vérifie que le nombre d'octet correspond à la demande (voir protocole)
    #concaténation des octets
        Ax=(float(list(bytearray(data))[1]<<8)+float(list(bytearray(data))[0])) #accélération sur x
        Az=(float(list(bytearray(data))[3]<<8)+float(list(bytearray(data))[2])) #accélération sur z
        Gy=(float(list(bytearray(data))[5]<<8)+float(list(bytearray(data))[4])) #vitesse autour de y
        if Ax>32768: #test pour trouver le signe de l'accélération sur X
            Ax=(65520-Ax)/16
        else :
            Ax=(-Ax/16)
        if Az>32768: #test pour trouver le signe de l'accélération sur Z
            Az=(65520-Az)/16
        else :
            Az=(-Az/16)
        if Gy>32768: #test pour trouver le signe de la vitesse autour de Y
            Gy=(65535-Gy)*0.0175
        else :
            Gy=(-Gy*0.0175)
        Ak=-struct.unpack(">f", data[-4:])[0] #récupère les 4 derniers octets et conversion en decimal protocole IEEE; angle Kalman
    return (Ax,Az,Gy,Ak)
 
#fonction gyro: calcul de l'angle (axeY) issu de la mesure du gyroscope
def gyro(GyY,AGyY,delta_t):
    AGyY=((AGyY+float(GyY)*delta_t)) #intégration de la vitesse
    return (AGyY)
 
#fonction accel: calcul l'angle issu de le mesure de l'accéléromètre    
def accel(AcX,AcZ):
    AAcY=np.arctan(float(AcX)/float(AcZ))*180/np.pi #calcul de projection
    return (AAcY)
 
#fonction filtre_comp: calcul de l'angle filtré à partir des mesures de l'accéléromètre et du gyroscope    
def filtre_comp(AcX,AcZ,GyY,AFcY,delta_t):
    AFcY=0.3*(AFcY+float(GyY)*delta_t) + 0.7*np.arctan(float(AcX)/float(AcZ))*180/np.pi
    return (AFcY)
 
print("début d'acquisition") 
t=time.time()
while (i<duree):
    try:
        AcX,AcZ,GyY,Ak=lecture()
        delta_t=(time.time()-t)
        t=time.time()	# Releve le temps juste après le calcul du delta_t
        print(delta_t) #affichage possible des données dans la console...
        #print(AcX,AcZ,GyY)
        AGyY=gyro(GyY,AGyY,delta_t)
        AAcY=accel(AcX,AcZ)
        AFcY=filtre_comp(AcX,AcZ,GyY,AFcY,delta_t)
        TabGyY.append(AGyY) #on complète au fur et à mesure les données dans les tableaux
        TabAcY.append(AAcY)
        TabFiltreComp.append(AFcY)
        TabAk.append(Ak)
        inc.append(i)
        i=i+delta_t #incrément
 
 
    except:
        print("Oups!! problème...")
 
 
 
trace_filtre,=plt.plot(inc,TabFiltreComp, label="Filtre complémentaire") #affichage des tracés avec légendes
trace_gyr,=plt.plot(inc,TabGyY, label="Gyroscope")
trace_accel,=plt.plot(inc,TabAcY, label="Accéléromètre")
#trace_kalman,=plt.plot(inc,TabAk, label="Filtre de Kalman")
plt.legend(handles=[trace_filtre,trace_gyr,trace_accel], loc=4)
plt.show()
 
ser.close() #fermeture du port série
print("port série fermé :",ser.port)
 
print(inc)
 
 
with open('MONFICHIER.csv', 'w') as csv:
    writer = csv.writer(inc, delimiter=",")
    writer.writerows(inc)
 
csv.close()