import pandas as pd

# reading CSV file
df = pd.read_csv("logSupercomputador.csv")
numero_processos_total = len(df.index)
print(numero_processos_total)
# Calcular InterArrivalTime

def calcular_estatisticas_gerais():
    print('------Média-----')
    numprocs_media = df['NumProcs'].mean()
    exetime_media = df['ExeTime'].mean()
    interarrivaltime_media = df['InterArrivalTime'].mean()
    print('NumProcs:', round(numprocs_media, 2))
    print('ExeTime:', round(exetime_media, 2))
    print('InterArrivalTime:', round(interarrivaltime_media, 2))

    print('------Desvio padrão-----')
    numprocs_desviopadrao = df['NumProcs'].std()
    exetime_desviopadrao = df['ExeTime'].std()
    interarrivaltime_desviopadrao = df['InterArrivalTime'].std()
    print('NumProcs:', round(numprocs_desviopadrao, 2))
    print('ExeTime:', round(exetime_desviopadrao, 2))
    print('InterArrivalTime:', round(interarrivaltime_desviopadrao, 2))

    print('------Coeficiente de variação-----')
    numprocs_coeficientevariacao = (numprocs_desviopadrao/numprocs_media)
    exetime_coeficientevariacao = (exetime_desviopadrao/exetime_media)
    interarrivaltime_coeficientevariacao = (interarrivaltime_desviopadrao/interarrivaltime_media)
    print('NumProcs:', round(numprocs_coeficientevariacao, 2))
    print('ExeTime:', round(exetime_coeficientevariacao, 2))
    print('InterArrivalTime:', round(interarrivaltime_coeficientevariacao, 2))


# - Exe Time - 
# Bloco 1, 0 <= x <= 50
# Bloco 2, 51 <= x <= 150
# Bloco 3, 151 <= x <= 350
# Bloco 4, 351 <= x <= 750
# Bloco 5, 751 <= x <= 1550
# Bloco 6, 1551 <= x <= 3150
# Bloco 7, 3151 <= x <= 6350
# Bloco 8, 6351 <= x <= 12750
# Bloco 9, 12751 <= x 25550
# Bloco 10, 25.551 <= x <= 51.150
# Bloco 11, 51.151 <= x <= 102.350
# Bloco 12, 102.351 <= x

def calcular_estatisticas_por_bloco_ExeTime():
    intervalos_menores = [0, 51, 151, 351, 751, 1551, 3151, 6351, 12751, 25551, 51151]
    intervalos_maiores = [50, 150 , 350, 750, 1550, 3150, 6350, 12750, 25550, 51150, 102350]
    bloco = 1
    for x in range(12):
        print('-------------------------------')
        print('Bloco: ', bloco)
        if bloco == 12:
            print('Intervalo menor: 102.351')
            df_bloco = df.loc[(df['ExeTime'] >= 102351)]
        else:
            intervalo_menor = intervalos_menores[x]
            intervalo_maior = intervalos_maiores[x]
            print('Intervalo menor: ', intervalo_menor)
            print('Intervalo maior: ', intervalo_maior)
            df_bloco = df.loc[(df['ExeTime'] >= intervalo_menor) & (df['ExeTime'] <= intervalo_maior)]
        
        bloco_media = df_bloco['ExeTime'].mean()
        bloco_desviopadrao = df_bloco['ExeTime'].std()
        bloco_coeficientevariacao = (bloco_desviopadrao/bloco_media)

        numero_processos_por_bloco = len(df_bloco.index)
        print('Numero Processos:', numero_processos_por_bloco)
        porcentagem = (numero_processos_por_bloco/numero_processos_total) * 100
        print('Porcentagem de processos do total: ', round(porcentagem, 2))
        print('Média: ', round(bloco_media, 2))
        print('Desvio padrão: ', round(bloco_desviopadrao, 2))
        print('Coeficiente de variação: ', round(bloco_coeficientevariacao, 2))
        bloco += 1

# - NumProcs - 
# 32, 64, 128, 256, 512, 1024
# Bloco 1, 0 <= x <= 32 
# Bloco 2, 33 <= x <= 64
# Bloco 3, 65 <= x <= 128
# Bloco 4, 129 <= x <= 256
# Bloco 5, 257 <= x <= 512
# Bloco 6, 1024 <= x

def calcular_estatisticas_por_bloco_NumProcs():
    intervalos_menores = [0, 33, 65, 129, 257]
    intervalos_maiores = [32, 64 , 128, 256, 512]
    bloco = 1
    for x in range(6):
        print('-------------------------------')
        print('Bloco: ', bloco)
        if bloco == 6:
            print('Intervalo menor: 1024')
            df_bloco = df.loc[(df['NumProcs'] >= 1024)]
        else:
            intervalo_menor = intervalos_menores[x]
            intervalo_maior = intervalos_maiores[x]
            print('Intervalo menor: ', intervalo_menor)
            print('Intervalo maior: ', intervalo_maior)
            df_bloco = df.loc[(df['NumProcs'] >= intervalo_menor) & (df['NumProcs'] <= intervalo_maior)]
        
        bloco_media = df_bloco['NumProcs'].mean()
        bloco_desviopadrao = df_bloco['NumProcs'].std()
        bloco_coeficientevariacao = (bloco_desviopadrao/bloco_media)

        numero_processos_por_bloco = len(df_bloco.index)
        print('Numero Processos:', numero_processos_por_bloco)
        porcentagem = (numero_processos_por_bloco/numero_processos_total) * 100
        print('Porcentagem de processos do total: ', round(porcentagem, 2))
        print('Média: ', round(bloco_media, 2))
        print('Desvio padrão: ', round(bloco_desviopadrao, 2))
        print('Coeficiente de variação: ', round(bloco_coeficientevariacao, 2))
        bloco += 1

# - InterArrivalTime - 
# Bloco 1, 0 <= x <= 0
# Bloco 2, 1 <= x <= 3
# Bloco 3, 4 <= x <= 6
# Bloco 4, 7 <= x <= 12
# Bloco 5, 13 <= x <= 25
# Bloco 6, 26 <= x <= 50
# Bloco 7, 51 <= x <= 150
# Bloco 8, 151 <= x <= 350
# Bloco 9, 351 <= x <= 750
# Bloco 10, 751 <= x <= 1550
# Bloco 11, 1551 <= x <= 3150
# Bloco 12, 3151 <= x <= 6350
# Bloco 13, 6351 <= x <= 12750
# Bloco 14, 12751 <= x 25550
# Bloco 15, 25.551 <= x <= 51.150
# Bloco 16, 51.151 <= x
def calcular_estatisticas_por_bloco_InterArrivalTime():
    intervalos_menores = [0, 1, 4, 7, 13, 26, 51, 151, 351, 751, 1551, 3151, 6351, 12751, 25551]
    intervalos_maiores = [0, 3, 6 , 12, 25, 50, 150 , 350, 750, 1550, 3150, 6350, 12750, 25550, 51150]
    bloco = 1
    numblocos = 16
    for x in range(numblocos):
        print('-------------------------------')
        print('Bloco: ', bloco)
        if bloco == numblocos:
            print('Intervalo menor: 51.151')
            df_bloco = df.loc[(df['InterArrivalTime'] >= 51151)]
        else:
            intervalo_menor = intervalos_menores[x]
            intervalo_maior = intervalos_maiores[x]
            print('Intervalo menor: ', intervalo_menor)
            print('Intervalo maior: ', intervalo_maior)
            df_bloco = df.loc[(df['InterArrivalTime'] >= intervalo_menor) & (df['InterArrivalTime'] <= intervalo_maior)]
        
        bloco_media = df_bloco['InterArrivalTime'].mean()
        bloco_desviopadrao = df_bloco['InterArrivalTime'].std()
        bloco_coeficientevariacao = 0 if bloco_media == 0 else (bloco_desviopadrao/bloco_media)

        numero_processos_por_bloco = len(df_bloco.index)
        print('Numero Processos:', numero_processos_por_bloco)
        porcentagem = (numero_processos_por_bloco/numero_processos_total) * 100
        print('Porcentagem de processos do total: ', round(porcentagem, 2))
        print('Média: ', round(bloco_media, 2))
        print('Desvio padrão: ', round(bloco_desviopadrao, 2))
        print('Coeficiente de variação: ', round(bloco_coeficientevariacao, 2))
        bloco += 1


#calcular_estatisticas_por_bloco_ExeTime()
#calcular_estatisticas_por_bloco_NumProcs()
calcular_estatisticas_por_bloco_InterArrivalTime()
