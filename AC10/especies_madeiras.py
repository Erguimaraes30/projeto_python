n = int(input())
input()

for i in range(n):
    quantidade_arvores = 0
    arvores = {}


    while True:
        if i == n-1:
            try:
                x = input()

                if(x in arvores):
                    arvores[x] += 1
                else:
                    arvores[x] = 1
                quantidade_arvores += 1
            except EOFError:
                break
        else:



            x = input()
            if x == "":
                break

            if(x in arvores):
                arvores[x] += 1
            else:
                arvores[x] = 1
            quantidade_arvores += 1




    arvores_ordenadas = dict(sorted(arvores.items()))
    for arvore, quantidade in arvores_ordenadas.items():
        print(f"{arvore} {((quantidade/quantidade_arvores)*100):.4f}")
    arvores={}
    quantidade_arvores = 0
    if i < n-1:
        print()