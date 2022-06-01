# adição / - subtração / * multiplicação /  / divisão / ** potencia / dvisão inteira //  / resto da divisão % /
# operadores aritimeticos, todo operador precisa de operandos, pode ser numeros, strings, variaveis

# 5+2 == 7
# 5-2== 3
# 5*2== 10
# 5**2== 25
# 5/2==2.5
# 5//2== 2 resta 1
# 5% 2== 1

# ordem de precedencia
# 1 - ( )
# 2 - **
# 3 - *, /, //, %
# 4 - +,-

#5+3*2==11
#3*5+ 4**2== 31
# 3*(5+4)**2==243
# 81**)1/2)== 9 raiz quadrada

nome = input( ' qual seu nome? ')
print('prazer em te conhecer {} !'.format(nome))

n1=int(input('um valor: '))
n2=int(input('outro valor: '))
s=n1+n2
m=n1*n2
d=n1/n2
div=n1 // n2
e=n1**n2
print(' a soma vale {}'.format(n1+n2))
print('a soma é {}, o produto é {}, \n e a \n divisão é {:.3f}'.format(s, m, d), end='')
print('divisão inteira {} e pontencia {}'.format(div,e))













