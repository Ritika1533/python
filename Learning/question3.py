#QUESTION1 : user input 3 movies nane and store in list

movie1=input("enter 1st movie : ")
movie2=input("enter 2st movie : ")
movie3=input("enter 3st movie : ")
movieList=[movie1,movie2,movie2]
print(movieList)



#QUESION2 : check list contain parildrome or not
parCheck = [1, 2, 3, 7]
i = 0
j = len(parCheck) - 1

while i < j:
    if parCheck[i] != parCheck[j]:
        print("not palindrome")
        break
    i += 1
    j -= 1


#QUESTION3: cout no of student with grade A
tupGrade=("C","D","A","A","B","B","A")
print("no of student having grade A : ",tupGrade.count("A"))


#QUESTION4: sort this list in asending order
grade=["C","D","A","A","B","B","A"]
grade.sort()
print(grade)