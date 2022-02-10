entrada = [0,0]
pesos =   [0,0]
saida = 0
n = 0.1
bias = 0.1



#-------------------------------------------------------------------------------
def limparTela():
    for a in range(1,25):
        print("\n")


def lerEntradas():
    for i in range(0,len(entrada)):
        entrada[i] = input("Entrada "+str(i+1)+": ")

def validarAcerto():
    escolha = input("Está correto? ")
    if (escolha == "n"):
        return False
    else:
        return True
# -------------------------------------------------------------------------------







# -----------Neuronio--------------------------------------------------------------
#--retorna a saida
def operacao():
    somaPesosEntrada = 0
    for e, p in zip(entrada, pesos):
        somaPesosEntrada += float(e) * p
    return (somaPesosEntrada-1*bias)

#--------------------------------------------------------------------

def ajustarPesos(erro):
    for i in range(0,len(entrada)):
        pesos[i] = pesos[i] + (n * float(erro) * float(entrada[i]))
    return (bias + (n * -1 * erro))


#--------------------------------------------------------------------


# -------------------------------------------------------------------------------










run = True
while(run):

    limparTela()

    lerEntradas()
    saida = operacao()
    if(saida >=0 ):
        print('\033[92m'+"True"+'\033[0m')
        if(validarAcerto()==False):
            bias = ajustarPesos(-1)
    else:
        print('\033[91m'+"False"+'\033[0m')
        if(validarAcerto()==False):
            bias = ajustarPesos(1)
