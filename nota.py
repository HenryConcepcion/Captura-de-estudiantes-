nombre_estudiante=input("ingrese el nombre del estudiante: ")

nota_1= int(input("ingrese la primera nota: "))

nota_2= int(input("ingrese la segunda nota: "))

nota_3= int(input("ingrese la tercera nota: "))

nota_4= int(input("ingrese la cuarta nota: "))

resultado =(nota_1+nota_2+nota_3+nota_4)/4
if resultado <=69:
  print("el estudiante",nombre_estudiante,"tiene un promedio de",{resultado}, " reprobado ") 
elif resultado >=70 and resultado <=79:
  print("el estudiante",nombre_estudiante,"tiene un promedio de",{resultado}, "2.0 ")
elif resultado >=80 and resultado <=89:
  print(" el estudiante ",nombre_estudiante," tiene un promedio de ",{resultado},"3.0")  
elif resultado >=90 and resultado <=100:
  print("el estudiante",nombre_estudiante,"tiene un promedio de",{resultado}, "4.0 ")






