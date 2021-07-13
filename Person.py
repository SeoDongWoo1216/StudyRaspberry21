class Person(object):  # 모든 클래스는 object를 상속받는다
    total = 0

    def __init__(self, name, age): # 기본생성자 (self) / 오버로딩
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

class Man(Person):  # Person을 상속받음
    gender = 'male'

class Korean(Person):
    nationity = 'Korea'

class KoreanMan(Man, Korean): # Man과 Korean을 상속받음
    pass

        

        