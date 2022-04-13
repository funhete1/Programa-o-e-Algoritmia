from Person import Person
import random

class Student(Person):
    def __init__(self, name, id, birth_date,curso,mec):
        self.curso = curso
        self.mec = mec
        super().__init__(name, id, birth_date)

    def get_curso(self):
        return self.curso
    
    def get_mec(self):
        return self.mec

    def set_curso(self,curso):
        self.curso = curso
    
    def set_mec(self,mec):
        self.mec = mec

    def __repr__(self):
        return f"Professor:{self.get_name()}\t id:{self.get_id()}\t born:{str(self.get_birth_date())}\t curso:{self.get_curso()}\t mec:{self.get_mec()}"
    
class Teacher(Person):
    def __init__(self, name, id, birth_date,ucs):
        self.ucs = ucs
        super().__init__(name, id, birth_date)  
    def get_ucs(self):
        return self.ucs

    def add_ucs(self,uc):
        self.get_ucs.append(uc)
    def __repr__(self):
        return f"Professor: {self.get_name()}\nid: {self.get_id()}\nborn: {self.get_birth_date()}\nUcs lecionadas: {str(self.get_ucs())}"
def main():
    cursos = ["Matematica","Engenharia de Computadores","Engenharia Mecanica"]
    lst = []
    lst.append(Teacher("Caetano",123456789,"10/10/1910","Matematica,Engenharia de Computadores,Engenharia Mecanica"))
    names = ["Ines","Carol","Mariana","Carlos","Claudio","Alex","Luiz","Joao","Ana","Bia"]
    for i in range(9):
        lst.append(Student(names[i],i*1000,f"{random.sample(range(1,30),1)}/{random.sample(range(1,12),1)}/{random.sample(range(1950,2022),1)}",cursos[i//3],100000+i*1000+i*100))
    print(lst[0])
    for i in lst[1:9]:
        print(i)   
        


if __name__=="__main__":
    main()