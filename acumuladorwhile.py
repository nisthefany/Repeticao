total=0
itens=0
preco=1
print("digite o preço dos produtos - ou 0 para encerrar.")
while preco!=0:
    preco=float(input("preco?"))
    if preco!=0:
        total+=preco
        itens+=1
print("-"*35)
print("quantidade de itens:",itens)
print("valor total da compra:",total)
print("-"*35)