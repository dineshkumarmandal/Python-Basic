#4.4. break and continue Statements, and else Clauses on Loops
#The break statement breaks out of the innermost enclosing for or while loop.
#A for or while loop can include an else clause.
#In a for loop, the else clause is executed after the loop reaches its final iteration.
#In a while loop, it’s executed after the loop’s condition becomes false.
#In either kind of loop, the else clause is not executed if the loop was terminated by a break.
#This is exemplified in the following for loop, which searches for prime numbers:
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

#(Yes, this is the correct code. Look closely: the else clause belongs to the for loop, not the if statement.)
#When used with a loop, the else clause has more in common with the else clause of a try statement than it does with that of if statements: a try statement’s else clause runs when no exception occurs, and a loop’s else clause runs when no break occurs

#The continue statement, also borrowed from C, continues with the next iteration of the loop:
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)