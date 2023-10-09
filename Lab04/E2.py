import libnum

p=11
q=3 
N=p*q
PHI=(p-1)*(q-1)
e=3
d= libnum.invmod(e,PHI) 

print (e,N)
print (d,N)
M=4
print ("\nMessage:",M) 
cipher = M**e % N
print ("Cipher:",cipher) 
message = cipher**d % N 
print ("Message:",message)
