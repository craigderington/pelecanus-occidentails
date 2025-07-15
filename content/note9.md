Title: Python's Static Methods vs. Class Methods
Date: 2025-07-14 16:55
Modified: 2025-07-16 14:55
Category: Python
Tags: python, programming, linux, ubuntu, class, static, methods
Slug: python-static-vs-class-methods
Authors: Craig Derington
Summary: What's the difference between Python's static and class methods

#### Python:  Class Method vs Static Method

```
class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x    

a=A()
````
Below is the usual way an object instance calls a method. The object instance, a, is implicitly passed as the first argument.
```
a.foo(1)
# executing foo(<__main__.A object at 0xb7dbef0c>,1)
```

With classmethods, the class of the object instance is implicitly passed as the first argument instead of self.
```
a.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)
```

You can also call class_foo using the class. In fact, if you define something to be a classmethod, it is probably because you intend to call it from the class rather than from a class instance. A.foo(1) would have raised a TypeError, but A.class_foo(1) works just fine:
```
A.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)
```

One use people have found for class methods is to create inheritable alternative constructors.

With staticmethods, neither self (the object instance) nor cls (the class) is implicitly passed as the first argument. They behave like plain functions except that you can call them from an instance or the class:
```
a.static_foo(1)
# executing static_foo(1)
```

```
A.static_foo('hi')
# executing static_foo(hi)
```

Staticmethods are used to group functions which have some logical connection with a class to the class.
