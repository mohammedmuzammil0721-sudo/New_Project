import random
n_letters=int(input("Enter no of letters do you want : "))
n_numbers=int(input("Enter no of numbers do you want : "))
n_symbols=int(input("Enter no of symbols do you want :"))
password=[]
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','B','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','-','*','&','^','$','#','@','<','>']
for i in range(1,n_letters+1):
         ch=random.choice(letters)
         password+=ch
for j in range(1,n_numbers+1):
         ch1=random.choice(numbers)
         password+=ch1
for k in range(1,n_symbols+1):
         ch2=random.choice(symbols)
         password+=ch2
random.shuffle(password)
print("========Congratulations your password genrated !============")
print(password)
pass_w=" "
for i in password:
    pass_w+=i
print(pass_w)

               
