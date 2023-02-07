from Parent import Parent


class Child(Parent):
    def __init__(self, name):
        super().__init__(name)


child = Child("北川")
child.hello()
print(child.name)
