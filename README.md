# A brief guide to understanding SOLID principles with examples written Python.

SOLID Principles is an acronym of 5 principles in Object Oriented Design (OOD).
Robert C. Martin introduced these 5 principles in his 2000 paper "Design Principles and Design Patterns".

## 1. Single Responsibility
- Make things (subsystem, classes, modules, functions, etc.) responsible for fulfilling single functionality. In other words, it should have only a single reason to change
- Only one potential change (database logic, logging logic, and so on.) in the software’s specification should be able to affect the specification of the class.

### Why useful?
    • Team collaboration on the same project, less prone to incompatibility.
    • Help in unit testing.
    • It makes version control easier, fewer conflicts will appear.

---

## 2. Open/Closed
- Be able to add new functionality to existing code(subsystem, classes, modules, functions, etc.) easily without modifying existing code.
- This could be done via abstract classes, Inheritance, or Composition.


### Why useful?
    • Avoid tweaking the code to handle new requiremnts.
        - e.g. When you have algorithms that perform a calculation (cost, tax, game score, etc.): the algorithm will likely change over time.
        - e.eg When you have data coming or going from the system: the endpoint (file, database, another system) is likely to change. So is the actual format of the data.
    • Building applications that are reusable and can be maintained easily.

---

## 3. Liskov Substitution
- States that Objects in a program should be substitutable by the instances of their subtypes without modifying the correctness of a program.
- The problem is usually caused by inheriting class S from class T where S and T seem related but have one or more fundamental interface differences.
- To make sure you avoid violating this rule, try to first think of high-level abstractions/interfaces instead of low-level/concrete implementations.
    - e.g use inheritance hierarchies
    - e.g. Define constructor arguments to keep inheritance flexible.

## Why useful?
    • Helps programmers design good polymorphism. 
    • Constrains subclass design

> LSP is a concept that applies to polymorphism. 
>> If you don’t use polymorphism at all you don’t need to care about the LSP.

---

## 4. Interface Segregation
- Make interfaces (parent abstract classes) more specific, rather than generic.
- Clients should not be forced to implement a function they do not require.
    - e.g. Create more interfaces (abstract classes) if needed and/or provide objects to constructors.

### Why useful?
    • Help write good classes.
    • Help write unit tests.
---

## 5. Dependency Inversion
- High-level modules should not depend on low-level modules. Both should depend on abstractions or interfaces.
    - e.g. Make classes inherit from abstract classes.
- A direct dependecy - on a concrete class - need to be "inverted".

### Why useful?
    • It helps you separate components and helps reduce coupling in the code.

---

# Reference: 
- [1](https://www.infoworld.com/article/2953976/realize-the-open-closed-principle-using-abstractions.html)
- [2](https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/)
- [3](https://www.youtube.com/watch?v=pTB30aXS77U)
- [4](https://www.stevebrownlee.com/open-closed-principle-practical-example/)
- [5](https://www.pythonforeveryone.com/articles/liskov-substitution-principle-python.html)
- [6](https://openclassrooms.com/en/courses/6900866-write-maintainable-python-code/7010225-l-for-the-liskov-substitution-principle)
- [7](https://www.linisnil.com/articles/python-dependency-inversion-principle/)
	

