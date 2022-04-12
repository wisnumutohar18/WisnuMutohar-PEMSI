import random as ran 
import numpy as np 
import matplotlib.pyplot as plt 

#inisialisai
x=[]#angka random bahan
y=[]#frekuensi
z=[]#probabilitas
xx=[]#probabilitas kumulatif
yy=[]#batas bawah
zz=[]#batas atas
xxx=[]#angka random uji coba
yyy=[]#angka permintaan
zzz=[]#total prediksi
total=[]#total dana
aa=0#pengelompokan
bb=0#pengelompokan
cc=0#pengelompokan
dd=0#pengelompokan
ee=0#pengelompokan
aaa=[]#plot a
abc=[0,1,2,3,4]

print("Aplikasi Simulasi Metode Monte Carlo")
print("==========================================")
print("WISNU MUTOHAR 152018096 Pemerograman Simulasi 2")
print("==========================================")


#n angka
n=int(input("masukan jumlah angka : "))
for i in range (0,n) :
    a=ran.randint(0,4) #random angka sebanyak hasil inputan 
    x.append(a) #masukin data ke rai
print("data statistik : "+ str(x))

#n frekuensi
for i in range (0,n):
    if x[i] == 0 :
        aa+=1
    elif x[i] == 1 :
        bb+=1
    elif x[i] == 2 :
        cc+=1
    elif x[i] == 3 :
        dd+=1
    elif x[i] == 4 :
        ee+=1
y.append(aa)
y.append(bb)
y.append(cc)
y.append(dd)
y.append(ee)
print("frekuensi : "+ str(y))

#n probabilitas  
for i in range (0,5):
    a=y[i]/n
    z.append(a)
print("probabilitas : "+ str(z))

#n probabilitas kumulatif, penjumlshan probilitas kls ditambh probilitas sebelumnya
a=z[0]
xx.append(a)
for i in range (0,4):
    b=xx[i]+z[i+1] 
    xx.append(b)
print("probabilitas kumulatif : "+ str(xx))

#batas.bawah
a=0
yy.append(a)
for i in range (0,4):
    a=xx[i]
    yy.append (a)
print("batas bawah kelas : "+ str(yy))

#batas.atas
for i in range (0,4):
    a=xx[i]-0.01
    zz.append(a)
a=1
zz.append(a)
print("batas atas kelas : "+ str(zz))

#interval
for i in range (0,5):
    print("interval ke-"+str(i)+" : "+str(yy[i])+" - "+str(zz[i]))

#prediksi
print("jumlah data uji coba : "+ str(n))
for i in range (0,n) :
    a=round(ran.random(),4) #random nilai
    xxx.append(a)
print("data uji : "+str(xxx))

#nilai
for i in range (0,n) :
    if xxx[i]<zz[0] :
        a=0
    elif xxx[i]<zz[1]:
        a=1
    elif xxx[i]<zz[2]:
        a=2
    elif xxx[i]<zz[3]:
        a=3
    elif xxx[i]<zz[4]:
        a=4
    yyy.append(a)
    aaa.append(a)
print("prediksi permintaan : "+str(yyy))

#nilai prediksi
for i in range(0,n):
    a= yyy[i]*2500000
    zzz.append(a)
print("prediksi biaya : "+str(zzz))

#total nilai
res=0
for i in range(0,n):
    res=res+yyy[i]
print("prediksi permintaan total : "+str(res))
ren=0
for i in range(0,n):
    ren=ren+zzz[i]
print("prediksi total biaya : "+str(ren))

#ratarata penjualan per minggu
rev=res/n
print("rata rata penjualan per minggu : "+str(rev))

#frekuensi perminggu 
plt.title("Frekuensi")
plt.xlabel("Minggu")
plt.ylabel("Permintaan")
plt.plot(abc, y, color ="blue")
plt.show()

#prediksi permintaan per minggu
a=np.arange(1,n+1)
plt.title("Prediksi")
plt.xlabel("Minggu")
plt.ylabel("Permintaan")
plt.plot(a, aaa, color ="red")
plt.show()

#taksiran
print("Ramalan/Taksiran" + str(n)+"periode mendatang adalah jumlah permintaan =  "+str(res)+"barang, dengan estimasi nilai=Rp."+str(ren)+"rata-rata pemasukan mingguan adalah ="+str(rev)) 


