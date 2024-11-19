class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0   
        k=int(n**(1/2))
        primes=[0]*(n)
        for i in range(2,len(primes)):
            primes[i]=1
        for i in range(2,k+1):
            if primes[i]==1:
                j=i*i
                while j<n:
                    primes[j]=0
                    j+=i
        c=0            
        for i in range(2,len(primes)):
            if primes[i]==1:
                c+=1
        return c                    
        



        