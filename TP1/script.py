import pandas as pd

# reading CSV file
df = pd.read_csv("logSupercomputador.csv")


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


# Bloco 1, 0 <= x <= 50
# Bloco 2, 51 <= x <= 150
# Bloco 3, 151 <= x <= 350
# Bloco 4, 351 <= x <= 750
# Bloco 5, 751 <= x <= 1550
# Bloco 6, 1551 <= x <= 3150
# Bloco 7, 3151 <= x <= 6350
# Bloco 8, 6351 <= x <= 12750
# Bloco 9, 12750 <= x 
intervalos_menores = [0, 51, 151, 351, 751, 1551, 3151, 6351]
intervalos_maiores = [50, 150 , 350, 750, 1550, 3150, 6350, 12750]
def calcular_estatisticas_por_bloco():
    bloco = 1
    for x in range(9):
        print('-------------------------------')
        print('Bloco: ', bloco)
        if bloco == 9:
            print('Intervalo menor: 12750')
            df_bloco = df.loc[(df['ExeTime'] >= 12750)]
        else:
            intervalo_menor = intervalos_menores[x]
            intervalo_maior = intervalos_maiores[x]
            print('Intervalo menor: ', intervalo_menor)
            print('Intervalo maior: ', intervalo_maior)
            df_bloco = df.loc[(df['ExeTime'] >= intervalo_menor) & (df['ExeTime'] <= intervalo_maior)]
        bloco_media = df_bloco['ExeTime'].mean()
        bloco_desviopadrao = df_bloco['ExeTime'].std()
        bloco_coeficientevariacao = (bloco_desviopadrao/bloco_media)
        print('Média: ', round(bloco_media, 2))
        print('Desvio padrão: ', round(bloco_desviopadrao, 2))
        print('Coeficiente de variação: ', round(bloco_coeficientevariacao, 2))
        bloco += 1




calcular_estatisticas_por_bloco()