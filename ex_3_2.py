import random  
 minusculas=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  
 mayusculas=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']  
 todas=minusculas+mayusculas  
 vocales=['a','e','i','o','u']  
 toditas=''.join(todas) #convertimos la lista en un string  
 print(toditas)  
 toditas=toditas.lower()  
 vocalitas=''.join(vocales) #convierte la lista en un string  
 letra=random.choice(todas) #eleginos aleatoriamente una letra de la lista todas  
 #letra=random.randrange(len(todas)) #esto no daría la letra sino el orden  
 print(letra)  
 letra=letra.lower()  
 def vocalConsonante(letrita):  
  if letrita in vocalitas:  
   print(letrita," es vocal.")  
  else:  
   print(letrita," es consonante")  
 vocalConsonante(letra) 