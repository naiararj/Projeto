import os
compr =float(input('Comprimento do comodo: '))
larg = float(input('Largura do comodo: '))
área = compr * larg
myorder = ('O comodo tem a dimensão de {}x{} e sua área é de {}m²')
print(myorder .format(compr,larg,área))
produto = área/2
txt = ('Para limpar esse comodo irá precisar de {}L de produto.')
print(txt.format(produto))