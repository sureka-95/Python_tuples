#create a list of comprehensive numebers

a=[1,2,3,4,5,6,7,8,9,10]

# To get a square of even number by lambda
# using modulas to check the number is even or not

square_of_even=[x**2 for x in a if (lambda x:x%2==0) (x)]

#print the output
print(square_of_even)