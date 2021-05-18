# SOLID-principles-Python
Simple explanation of SOLID principles with examples in Python 

# Defining the SOLID principles 

## 1. Single Responsibility
-
- Make things (subsystem, classes, modules, functions, etc.) responsible for fulfilling one type of role.
- A class should do one thing and therefore it should have only a single reason to change
- Only one potential change (database logic, logging logic, and so on.) in the software’s specification should be able to affect the specification of the class.

### Why useful?
    •	Team collaboration on the same project, less prone to incompatibility.
    •	Help in unit testing.
    •	It makes version control easier, fewer conflicts will appear.

---

## 2. Open/Closed
-
- Be able to add new functionality to existing code(subsystem, classes, modules, functions, etc.) easily without modifying existing code.
- Use abstract classes.

### Why useful?
    •	When you have algorithms that perform a calculation (cost, tax, game score, etc.): the algorithm will likely change over time.
    •	When you have data coming or going from the system: the endpoint (file, database, another system) is likely to change. So is the actual format of the data.
    •	Building applications that are reusable and can be maintained easily.

---

## 3. Liskov Substitution
-
- When a class inherits from another class, the program shouldn't break and you shouldn't need to hack anything to use the subclass.
- The problem is usually caused by inheriting class S from class T where S and T seem related but have one or more fundamental interface differences.
- Liskov substitution principle applies to inheritance hierarchies. It is violated when a derived class cannot take the place of a base class without the system breaking.
- To make sure you avoid violating this rule, try to first think of high-level abstractions/interfaces instead of low-level/concrete implementations.
    - e.g. Define constructor arguments to keep inheritance flexible.
- LSP is a concept that applies to polymorphism. 
- If you don’t use polymorphism at all you don’t need to care about the LSP.

---

## 4. Interface Segregation
- 
- Make interfaces (parent abstract classes) more specific, rather than generic.
- Clients should not be forced to implement a function they do no need.
    - e.g. Create more interfaces (classes) if needed and/or provide objects to constructors.

---

## 5. Dependency Inversion
- 
- High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g. Make classes inherit from abstract classes).
- Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.
- It helps you separate components and helps reduce coupling in the code

---

# Reference: 
-
- [1](https://www.infoworld.com/article/2953976/realize-the-open-closed-principle-using-abstractions.html)
- [2](https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/)
- [3](https://www.youtube.com/watch?v=pTB30aXS77U)
- [4](https://www.stevebrownlee.com/open-closed-principle-practical-example/)
- [5](https://www.pythonforeveryone.com/articles/liskov-substitution-principle-python.html)
- [6](https://openclassrooms.com/en/courses/6900866-write-maintainable-python-code/7010225-l-for-the-liskov-substitution-principle)
- [7](https://www.linisnil.com/articles/python-dependency-inversion-principle/)
	

