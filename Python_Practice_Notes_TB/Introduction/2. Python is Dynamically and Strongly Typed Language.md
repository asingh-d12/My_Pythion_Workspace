So what does that mean?

## Dynamically Typed Language

Basically let's say we have this variable

```
i = 10
```

right now, a memory location that has int data is bound to variable name i.

Then i can do simply this
```
i = "A String"
```

this is not valid in many languages(like Java and C).
**Though in Python this is valid**.

Now i is bound to a String memory type.

This is why Python is called **Dynamically Typed Language**.

So a **Definition**?
> A language is **statically typed** if the type of a variable is known at compile time. Ex. Java, C etc

> A language is **dynamically typed** if the type is associated with run-time values, and not named variables/fields/etc. Ex. Python, Ruby etc

Let's check an example:



**In Dynamically Typed Language, it is better to not say variable is assigned to a value <a>but actually it is bound to value</a>**. That way, a variable can be revound to another value.
```
a_variable = 10
print(a_variable)
a_variable = "Amrit"
print(a_variable)
a_variable = 13.43
print(a_variable)
a_variable = [1, 2, 3, 4]
print(a_variable)
print('I can "bind and not assign" all these values to same variable name, because Python is Dynamically typed!!')

```

![[Pasted image 3.png]]

***

## Strongly Typed Language

**Strongly typed language basically means operations can be performed between 2 different types.**
	
**Python is Strongly Typed Language**
	
Weakly Typed Language on the other hand, we can perform operations between separate types of data.
ex. C, C++.

Let's check out an example:
```
x = 1
y = "Amrit"
print("Hello" + x + y)
```
![[Pasted image 4.png]]

**Basically what this means is apart from some special defined operations(like ''\*'' between String and int), operations between different types is not possible**.

***

Link to Refer:
https://android.jlelse.eu/magic-lies-here-statically-typed-vs-dynamically-typed-languages-d151c7f95e2b