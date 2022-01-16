Q1='''Which of these is not a core data type?
A.Lists
B.Dictionary
C.Tuples
D.Class
'''
Q2='''What data type is the object below ? L = [1, 23, ‘hello’, 1]
A.List
B.Dictionary
C.Tuple
D.Array'''
Q3='''
Which of the following function convert a string to a float in python?
A.int(x [,base])
B.long(x [,base] )
C.float(x)
D.str(x)'''
Q4='''
Which of the following correctly declares an array?
A.int geeks[20];
B.int geeks;
C.geeks{20};
D.array geeks[20];'''

questions = {Q1:"d", Q2:"a", Q3:"c", Q4:"a"}
name = input ("enter your name: ")
print ("hello" ,name, "welcome to the quiz world")
score=0
for i in questions:
    print(i)
    ans = input ("enter the answer (a/b/c/d): ")
    if ans==questions[i]:
        print ("correct answer!")
        score =score+1
    else:
        print ("wrong answer!")
print ("Final score is: ", score)