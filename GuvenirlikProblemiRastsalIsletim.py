import random
# =.90 \times .70 \times .50 \times .70
liste=[90, 70,50,70]

toplam =0
iter=10000000
for i in range(iter):
    say =0
    for j in range(4):
        n=random.randint(0,100)
        if (n <=100-liste[j]):
            say +=1
    if (say >=1):
        toplam +=1



print ("Sonuç : ", 1-toplam/iter)