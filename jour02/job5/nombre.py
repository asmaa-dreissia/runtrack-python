# Si c'est un multiple de 3 et 5 affichez "FizzBuzz"
# Si c'est un multiple de 3 affichez "Fizz" 
# Si c'est un multiple de 5 affichez "Buzz"
# Si ce n'est divisible par 3 ni par 5, laissez le même nombre

i= 1
while i < 100:
    if(i%3==0 and i%5==0): 
        print("FizzBuzz")
# Si i est un multiple de 3 et 5 affichez "FizzBuzz"
        
    elif(i%3==0): 
        print("Fizz")
# Si i est un multiple de 3 affichez "Fizz"
    elif(i%5 ==0):
        print("Buzz")
# Si i est un multiple de 5 affichez "Buzz6/"
    else:
        print(i)
    i +=1

for nombre in range (1,101):
    if nombre % 3 == 0 and nombre % 5 == 0:
     print("FizzBuzz")
    elif nombre % 3 == 0:
     print ("fizz")
    elif nombre % 5 == 0:
     print ("buzz")
    else:
       print(nombre)
