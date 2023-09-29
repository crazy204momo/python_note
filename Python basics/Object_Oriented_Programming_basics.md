# OOP class method basics

#### Inheritance & Overriding methods
- The methods with same name in child class will override those in parent class
- Child class `Admin` inherits from parent class `Employee`,  which means it will contain methods used in parent class without defining them.

#### Super() (Call the method in parent class) 
When overriding methods we sometimes want to still access the behavior of the parent method. In order to do that we need a way to call the method of the parent class. Python gives us a way to do that using `super()`.

`super()` gives us a proxy object. With this proxy object, we can invoke the method of an object’s parent class (also called its superclass). We call the required function as a method on `super()`:

```
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def __init__(self):
    super().__init__()
    
  def say_id(self):
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()
```

#### Multiple inheritance
- One form of multiple inheritance is when there are ==multiple levels of inheritance==. This means a class inherits members from its superclass and its super-superclass.
```
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

# Write your code below
class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge.")


e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()
e4.say_id() # Now you will get output from all 3 classes
```

```
Output:
My id is 4.
I am an admin.
I am in charge.
```
- Another form of multiple inhertance involves a subclass that ==inherits directly from two classes==  and can use the attributes and methods of both.
```
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))


class Admin(Employee, User):
  def __init__(self):
    super().__init__()
    User.__init__(self, self.id, "Admin")


  def say_id(self):
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()
```
```
Output:
My username is 3
My role is Admin
```

#### OOP Pillar: Polymorphism
In computer programming, *polymorphism* is the ability to apply an identical operation onto different types of objects. This can be useful when an object type may not be known at the program runtime. Polymorphism can be applied using Python in multiple ways. We have already experienced a form of it when exploring inheritance.
```
class Animal:
  def __init__(self, name):
    self.name = name
 
  def make_noise(self):
    print("{} says, Grrrr".format(self.name))
 
class Cat(Animal):
 
  def make_noise(self):
    print("{} says, Meow!".format(self.name))
 
class Robot:
 
  def make_noise(self):
    print("beep.boop...BEEEEP!!!")
```
The example above shows an `Animal` class, its subclass `Cat`, and another standalone class `Robot`. Each class has a method `.make_noise()` with different outputs. The identical method name with different behaviors is a form of *polymorphism*.

```
an_animal = Animal("Bear")
my_pet = Cat("Maisy")
my_vacuum = Robot()
objects = [an_animal, my_pet, my_vacuum]
for o in objects:
  o.make_noise()
 
# OUTPUT
# "Bear says, Grrrr"
# "Maisy says, Meow!"
# "beep.boop...BEEEEP!!!"
```

With the classes instantiated and added to a list, we are able to iterate through the list and call `.make_noise()`. This is done without needing to know what type of class `.make_noise()` belongs to.

#### D(ouble)UNDER methods

Every defined class in Python has access to a group of these special methods. We’ve explored a few already, the constructor `__init__()` and the string representation method `__repr__()`. The name dunder method is derived from the **D**ouble **UNDER**scores that surround the name of each method.

Recall that the `__repr__()` method takes only one parameter, self, and must return a string value. The returned value should be a string representation of the class, which can be seen by using `print()` on an instance of the class. Review the sample code below for an example of how this method is used.

Defining a class’s dunder methods is a way to perform operator overloading.
```
class Animal:
  def __init__(self, name):
    self.name = name
 
  def __repr__(self):
    return self.name
 
  def __add__(self, another_animal):
    return Animal(self.name + another_animal.name)
 
a1 = Animal("Horse")
a2 = Animal("Penguin")
a3 = a1 + a2
print(a1) # Prints "Horse"
print(a2) # Prints "Penguin"
print(a3) # Prints "HorsePenguin"
```
- Check out how the `__add__()` metohd is used in the following example
```
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

class Meeting:
  def __init__(self):
    self.attendees = []
  
  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)

  # Write your code
  def __len__(self):
    return len(self.attendees)
    
e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
m1+e1
m1+e2
m1+e3
print(len(m1))
```
```
Output:
ID 1 added.
ID 2 added.
ID 3 added.
3
```
#### OOP Pillar: Abstraction
When a program starts to get big, classes might start to share functionality or we may lose sight of the purpose of a class’s inheritance structure. In order to alleviate issues like this, we can use the concept of abstraction.

==Abstraction helps with the design of code by defining necessary behaviors to be implemented within a class structure.== By doing so, abstraction also helps ==avoid leaving out or overlapping class functionality== as class hierarchies get larger.

```
from abc import ABC, abstractmethod
 
class Animal(ABC):
  def __init__(self, name):
    self.name = name
 
  @abstractmethod
  def make_noise(self):
    pass
 
class Cat(Animal):
  def make_noise(self):
    print("{} says, Meow!".format(self.name))
 
class Dog(Animal):
  def make_noise(self):
    print("{} says, Woof!".format(self.name))
 
kitty = Cat("Maisy")
doggy = Dog("Amber")
kitty.make_noise() # "Maisy says, Meow!"
doggy.make_noise() # "Amber says, Woof!"
```
Above we have `Cat` and `Dog` classes that inherit from `Animal`. The `Animal` class now inherits from an imported class `ABC`, which stands for Abstract Base Class.

This is the first step to making `Animal` an abstract class that cannot be instantiated. The second step is using the imported decorator `@abstractmethod` on the empty method `.make_noise()`.

The below line of code would throw an error.
```
an_animal = Animal("Scruffy")
 
# TypeError: Can't instantiate abstract class Animal with abstract method make_noise
```

The abstraction process defines what an Animal is but does not allow the creation of one. The `.__init__()` method still requires a name, since we feel all animals deserve a name.

The `.make_noise()` method exists since all animals make some form of noise, but the method is not implemented since each animal makes a different noise. Each subclass of `Animal` is now required to define their own `.make_noise()` method or an error will occur.

#### OOP Pillar: Encapsulation
*Encapsulation* is the process of making methods and data hidden inside the object they relate to. Languages accomplish this with what are called access modifiers like:
- Public
- Protected
- Private

In general, public members can be accessed from anywhere, protected members can only be accessed from code within the same module and private members can only be accessed from code within the class that these members are defined.

Python doesn’t have any inbuilt mechanism to prevent access from any member (i.e. all members are public in Python). However, there is a common convention amongst developers to use a single underscore `self._x` to indicate that a member is protected. Accessing a protected member outside of the module will not cause an error, it is added by developers to inform other developers that they should be careful when accessing this member in such a manner.

Similarly, we can declare a member as private with two leading underscores `self.__x`. This is more than just a convention in Python because of a mechanism called name mangling. Members that are preceded with two underscores have their names modified in the background to `obj._Classname__x`. While they can still be publicly accessed, the purpose of this mechanism is to prevent clashing member names of any inheriting classes that might define a member of the same name.

Note that this is different from the dunder methods we discussed earlier. A dunder method has two leading and two trailing underscores and is treated differently than a private member. One important difference is that dunder method names are not mangled.
```
class Employee():
    def __init__(self):
        self.id = None
        self._id = 'single_id'
        self.__id = 'double_id'
        # Write your code below
        
e = Employee()

print(dir(e))
```
- `dir()` is a built-in Python function that returns a list of all class members, including dunder methods.
When you run the code, you will see a list of class members with `id` as the last element.

```
Output:
['_Employee__id', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_id', 'id']
```
#### Getters, Setters and Deleters
Using getter, setter, and deleter functions are one way to implement encapsulation within Python where the state of class attributes can be handled within the class. These functions are useful in making sure that the data being handled is appropriate for the defined class functionality.

```
class Employee():
  new_id = 1
  def __init__(self, name=None):
    self.id = Employee.new_id
    Employee.new_id += 1
    self._name = name

  # Write your code below
  def get_name(self):
    return self._name

  def set_name(self, name_str):
    self._name= name_str

  def del_name(self):
    del self._name
e1 = Employee("Maisy")
e2 = Employee()



e1 = Employee("Maisy")
e2 = Employee()
print(e1.get_name())

e2.set_name("Fluffy")
print(e2.get_name())

e2.del_name()
print(e2.get_name()) # Raises a AttributeError
```
```
Output:
Maisy
Fluffy
Traceback (most recent call last):
  File "script.py", line 30, in <module>
    print(e2.get_name())
  File "script.py", line 10, in get_name
    return self._name
AttributeError: 'Employee' object has no attribute '_name'
```

#### Class Example with all the concepts mentioned above
```
class School:
  def __init__(self, name, level, numberOfStudents=0):
    self.name= name
    self.level= level
    self.numberOfStudents= str(numberOfStudents)
  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_num(self):
    return self.numberOfStudents

  def set_num(self, number):
    self.numberOfStudents=str(number)

  def __repr__(self):
    return f'A {self.level} school named {self.name} with {self.numberOfStudents} students'

# S=School("NTHU", "medium")
# print(S.get_name())
# print(S.get_level())
# print(S.get_num())
# S.set_num(1000)
# print(S)


class PrimarySchool(School):
  def __init__(self,name, num, pickup):
    level='primary'
    super().__init__(name, level, num)
    self.pickupPolicy= pickup
  def get_pickup(self):
    return self.pickupPolicy

  def __repr__(self):
    k=super().__repr__()
    return k+f' pickup policy {self.pickupPolicy}'

# P=PrimarySchool("NU",500,"Bus")
# print(P.get_name())
# print(P.get_level())
# print(P.get_num())
# print(P.get_pickup())
# print(P)


class HighSchool(School):
  def __init__(self,name, num, sportsTeams):
    level= 'high'
    super().__init__(name,level, num)
    self.sportsTeams = sportsTeams
  def get_team(self):
    return self.sportsTeams

  def __repr__(self):
    k=super().__repr__()
    return k+f'sports Team: {sportsTeams}'

# H=HighSchool("Focus",500,["Swim","Basketball"])
# print(H.get_team())
```