import time
sekil1= "\U00002B50"
sekil2= "\U0001F380"
sekil3= "\U0001F38A"
sekil4= "\U0001F380"
count = 1

for i in range(10):
    print((sekil2*count).center(30))
    count+=2
    if(i==0):
        sekil2=sekil1
    #time.sleep(0.5)
    if(i==3):
        print("Ekonomi UNV".center(32))
        time.sleep(0.5)
    if(i==7):
        print("mutlu bir yıl diler ".center(33))
        time.sleep(0.5)
        continue
        
    
        
print((sekil4*12).center(22))  
time.sleep(0.5)  
print("||".center(34))
        
    
