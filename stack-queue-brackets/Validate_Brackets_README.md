# Validate_Brackets

## Challenge 13

> - Multi-bracket Validation.

> - Create a function which Validates the Brackets
>   Takes Strings as Arguments and Returns True or False

### Structure and Testing

Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge.

and written Tests.

## whiteboarding

![image](./validate_brackets.png)

## Approach & Efficiency

    define a function called Validate+\_Brackets , Which takes string as an argument , and Outputs trye of false if the opeenings where matached.

    declare a stack Object equals to Stack Class.

    now starting a for loop to check each charecter of the string
    we start by checking the openning brackets of each type, if exist we push it to the stack , then we check the closing brackets , if exist we start checking our stack if its empty; since if there was`nt any openning then no need to continue the answer is False.
    Then we check each closing bracket type and if the top is the same, then we pop the top, and keep iterating through the for loop.

Big O(n) for time
big 0(n) for space

## API

---
