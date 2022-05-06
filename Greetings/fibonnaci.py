def fib(n):
 if n <= 1:
  return 1
 else:
  return fib(n - 1) +  fib(n - 2)

print("How many numbers do you want to view?")
noRange = int(input())
for i in range(noRange):
    print(fib(i))

#Uses recursion to calculate values in a sequence
