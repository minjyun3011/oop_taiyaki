# Taiyakiクラス
class Taiyaki:
    def __init__(self, anko):
        self.anko = anko

azuki = Taiyaki(anko="あずき")
print(azuki.anko)  # あずき

ogura = Taiyaki(anko="おぐら")
print(ogura.anko) 


# Personクラス
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def self_introduction(self):
        return f"私の名前は{self.name}です。{self.age}才です。"


bob = Person(name="Bob", age=12)
print(bob.name)  # Bob
print(bob.age)  # 12
print(bob.self_introduction())  # 私の名前はBobです。12才です。

tom = Person(name="Tom", age=15)
print(tom.self_introduction())  # 私の名前はTomです。15才です。
