## WORK IN PROGRESS

# Lisp Interpreter

A python lisp interpreter

## syntax

### PREDEFINED FUNCTIONS

#### +, =, print, list, first, rest, append

```
(+ 1 2) # -> 3
(= 1 1) # -> true
(= 1 2) # -> () which is an empty list and equivalent to false
(print 1) # outputs  1
(list 1 2 3) # -> (1 2 3)
(first (list 1 2 3)) # -> 1
(rest (list 1 2 3)) # -> (2 3)
(append (list 1 2 3) 4) # -> (1 2 3 4)
```

### BIND EXPRESSIONS

#### define

```
(define a 1)  # a is bound to 1
(define b (+ 3 4)) # b is bound to 7
```

### DEFINE FUNCTIONS

#### lambda

```
(define twice (lambda (a) (+ a a)))  # twice is a function that calculates a + a
(define sum (lambda (a b) (+ a b)))
```

### CONDITIONALS

#### if

```
(define a 5)
(if (= a 7) (twice a) (twice 2)) # evaluates to 4 (twice 2)
(if (= a 5) (twice a) (twice 2)) # evaluates to 10 (twice a)
```
