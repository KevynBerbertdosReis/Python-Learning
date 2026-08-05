#soma
5+2==7
#subtração
5-2==3
#multiplicação
5*2==10
#divisão
5/2==2.5
#potência
5**2==25
#divisão inteira
5//2==2
#restp da divisão
5%2==1

#ORDEM DE PRECÊDENCIA
#1-()
#2-**
#3-*,/,//,%
#4-+, -

n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print ('A soma vale {}, o produto vale {} e a divisão vale {:.2f}'.format(s, m, d), end=' ')
print ('A divisão inteira vale {} e a potência vale {}'.format(di, e))