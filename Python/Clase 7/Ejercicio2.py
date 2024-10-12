import time

hora=time.localtime().tm_hour
minuto=time.localtime().tm_min
if hora>=19:
    print("Ya es la hora de ir a casa")

elif minuto==0:
    print(f"Aún quedan {19-hora}:00 para ir a casa")

else:
    print(f"Aún quedan {18-hora}:{60-minuto} para ir a casa")