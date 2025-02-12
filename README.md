## Python Design Pattern

### Introduction
* A practice project for [Gang of Four design patterns](https://www.digitalocean.com/community/tutorials/gangs-of-four-gof-design-patterns).

### Creational Design Pattern
The design patterns that deal with the creation of an object.
- [x] Singleton Pattern
  - **Purpose**: ensure that no more than a single instance of a class exists.
  - **When to use**: when you want to control access to a shared resource.
  - **Examples**: Loggers, caching, thread pools, database connection, configuration access, ...
- [x] Factory Method Pattern
  - **Purpose**: allow a class to defer instantiation to its subclasses.
  - **When to use**:
    - when a caller can't anticipate the type of objects it must create.
    - when you have many objects of a common type.
  - **Examples**: strategy design pattern, object pool (facilitate caching)
- [x] Builder Pattern
  - **Purpose**: encapsulate reusable logic of building complex logic.
  - **When to use**:
    - when you have a complex class with many constructors.
    - when you have to build complex composite tree objects.
  - **Examples**: document readers

### Structural Design Pattern
The design patterns in this category deal with the class structure such as Inheritance and Composition.
- [x] Adapter Pattern
  - **Purpose**: convert the interface contract of one class to be compatible with another
  - **When to use**: when you have an existing class or contract that you would like to reuse but its interface isn't compatible with the rest of your code.
  - **Examples**: XML to JSON adapter

### Behavioral Design Pattern
This type of design pattern provides solutions for better interaction between objects, how to provide loose coupling, and flexibility to extend easily in the future.
- [x] Strategy Pattern
  - **Purpose**: extract related algorithms (or any piece of code) into separate classes and define a common interface for them.
  - **When to use**: when you want to abstract the business logic of a class from its implementation details.
  - **Examples**: discount handlers
- [ ] Observer Pattern
- [ ] State Pattern
