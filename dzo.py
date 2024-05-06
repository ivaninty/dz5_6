class Animal:
    def __init__(self,paws,bite_force,breed ):
        self.paws = paws
        self.bite_force = bite_force
        self.breed = breed

    def pr_1(self):
        print(f'Paws = {self.paws}\n'
              f'Bite force = {self.bite_force}\n'
              f'Breed = {self.breed}\n')
class Cat(Animal):
    def __init__(self,paws,bite_force,breed ):
        super().__init__(paws,bite_force,breed )

    def pr_1(self):
        super().pr_1()

class Dog(Animal):
    def __init__(self,paws,bite_force,breed):
        super().__init__(paws,bite_force,breed)

    def pr_1(self):
        super().pr_1()

cat_1 = Cat(4, 55,"Британський висловухий",)
dog_1 = Dog(4,95,"Вівчарка")

cat_1.pr_1()
dog_1.pr_1()