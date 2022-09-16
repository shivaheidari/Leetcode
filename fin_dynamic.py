def fib(n,memo):
   if n in memo:
        return memo[n]
   if (n<=2):
         return 1
   memo[n]=fib(n-1,memo)+fib(n-2,memo)
   print("Memo: ", n, memo[n])
   print()
   return memo[n]
fib(5,memo={})
