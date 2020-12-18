import numpy as np
class MyClass():
    def Progression(self,b,q,n):
        self.b=b
        self.q=q
        self.n=n
        a= np.zeros(shape=[n])
        i=0
        
        while(i<n):
            b+=q
            i+=1
            a[i-1]=b
            print(a[i-1])
        return a
    def Return_k(self,a,k):
        ku=0
        i=0
        while(i<self.n):
            self.b+=self.q
            if(i<=k)&(k<=self.n):
                ku+=self.b
                print(ku)
            i+=1
            a[i-1]=self.b
        return(ku)
if __name__ == '__main__':
    c=MyClass()
    cer=c.Progression(1,3,5)
    c.Return_k(cer,5)
