# class Student:
#     count=0
#     def __init__(self,neme='Вася',height=155):# вбудоаваний метод (конструктро)
#         self.height = 155
#         self.neme=neme
#         #print(self.height)
#         self.height=height
#         Student.count+=1
#     def info(self  ):
#         print(self.neme,self.height)
#
#
#
# st1 = Student()
# #Student.__init__(self=stil)
#
# #print(st1.height)
#
# st2 = Student('Саша',height=258)
# #print(st2.height)
#
# st3 = Student('Коля',height=58)
# #print(st3.height)
# #print(Student.count)
# #print('Ріст студента:')
# print ('Ріст та Імя студента')
# st1.info()
# st2.info()
# st3.info()
# print('Кількіcть:',Student.count)
#
class AAnimal:
    count=0
    def __init__(self,animal='Sobaka',age=15):
        self.age = 155
        self.animal=animal
        #print(self.height)
        self.age=age
        AAnimal.count+=1
    def info(self  ):
        print(self.animal,self.age)



an1 = AAnimal()


an2 = AAnimal('Cherepaha',age=48)


an3 = AAnimal('Kit',age=2)

print ('Вік та Назва Тварини')
an1.info()
an2.info()
an3.info()
print('Кількіcть:',AAnimal.count)

