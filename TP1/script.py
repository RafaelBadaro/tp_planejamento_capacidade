import pandas as pd

# reading CSV file
df = pd.read_csv("logSupercomputador.csv")


# Calcular InterArrivalTime


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



