def editDistance(str1, str2, m , n): 
  
        if m==0: 
             return n 
  
        if n==0: 
            return m 
  
 
        if str1[m-1]==str2[n-1]: 
            return editDistance(str1,str2,m-1,n-1) 

        return 1 + min(editDistance(str1, str2, m, n-1),    # Insert 
                     editDistance(str1, str2, m-1, n),    # Remove 
                     editDistance(str1, str2, m-1, n-1)    # Replace 
                     ) 
  


VB  = ['খাই','দৌড়ায়','ঘুর','পড়ে','গিয়ে','করি','ঘুম','বলে','চলে','আসছে','ঘুরতে','যাব','পছন্দ','আছে','খেলা','কাপছে'] 
    
substring = ['তেছি','ছিল','তেছে','ছিলাম'] 

fullstring = 'খাই' #i input from here
 
    
        
index1=-1
for i in substring:
    
    index1=index1+1
    if i in fullstring:
       
            #print(index1)
            Y= fullstring.split(substring[index1])[0]
            print("Input:",fullstring )
            print("Root word: ",Y)
        
#-----------------
kk=[]
for index in range(len(VB)): 
    
   k=editDistance(Y, VB[index], len(Y), len(VB[index])) 
   print("Distance: ",k,Y)

   kk.append(k)
    
    
for i in range (len(kk)):
      #print(kk[i])
    
  smallest = min(kk)
     # l.index(min(l))
       
    

print("lowest distance: ",smallest)

   
#print("Closest word with lowest distance value :",VB[kk.index(min(kk))])
print("Closest word with lowest distance value :",Y)