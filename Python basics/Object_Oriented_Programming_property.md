# OOP Property 
 The Python built-in `property()` function accepts four optional arguments: `fget, fset, fdel`, and `doc`. The first three represent getter, setter, and deleter methods, respectively, and the last one is a docstring for the attribute.
```
class Box:
  def __init__(self, weight):
    self.__weight = weight
 
  def getWeight(self):
    return self.__weight
 
  def setWeight(self, weight):
    if weight >= 0:
      self.__weight = weight

  def delWeight(self):
    del self.__weight

  weight = property(getWeight, setWeight, delWeight, "Docstring for the 'weight' property")
```

- We then call the `property()` function and pass the getter, setter, and deleter in as arguments. This will immediately allow us to use the following syntax for our class:

```
box = Box(10)
 
print(box.weight) #this calls .getWeight()
 
box.weight = 5 #this called .setWeight()
 
del box.weight #this calls .delWeight()
 
box.weight = -5 #box.__weight is unchanged 
```

#### With this change, our program gains some immediate benefits:

- We can now use the `weight` attribute as if it was public. We no longer have to call the setters, getters, and deleter methods directly and thus giving our program a simpler syntax.
- Even though we no longer call the methods directly, we still can maintain constraints such as the weight limit in `setWeight()`. It’s the best of both worlds!
- If we had a huge codebase that used our methods multiple times in multiple places, a single change to the method name would seriously mess up our program since we would have to change it everywhere! We no longer have this issue using the `property()` method since we never call it directly.

## Let's use the @property decorator

#### Let’s break this down:

- First, we have renamed all of our methods to simply be `weight()`.
- Then we denoted our getter with a `@property`. This marks the property to be used as a prefix for decorating the setter and deleter methods.
- Lastly, we use `@weight.setter` and `@weight.deleter` to define our setter and deleter methods, respectively.

```
class Box:
 def __init__(self, weight):
   self.__weight = weight
 
 @property
 def weight(self):
   """Docstring for the 'weight' property"""
   return self.__weight
 
 
 @weight.setter
 def weight(self, weight):
   if weight >= 0:
     self.__weight = weight
 
 @weight.deleter
 def weight(self):
   del self.__weight
```
#### Must-know about @property
After we set the `@property` in class, we can know access `self.__weight` just like an attribute
```
In:
B = Box(20)
Box.weight

Out:
20
```   
However if we try to set the weight value through this `@property`, we will get an attribute error
```
In:
Box.weight = 30

Out:
AttributeError: can't set attribute
```
#### When using the decorator, remember three rules:

1. All three methods must use the same member name (ex. weight).
2. The first method must be the getter and is identified using `@property`.
3. The decorators for the setter and deleter are defined by the name of the method `@property` is used with.