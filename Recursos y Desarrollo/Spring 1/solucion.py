lista_filtro_equipos_Stats = ['BOS', 'DEN', 'MIN', 'NYK', 'OKC']

# Identificar jugadores en la lista de equipos
jugadores_filtrados = df_Stats_Adv_2018[df_Stats_Adv_2018['Team'].isin(lista_filtro_equipos_Stats)]['Jugador'].unique()

# Filtrar incluyendo filas solo de esos  jugadores
df_filtrado = df_Stats_Adv_2018[df_Stats_Adv_2018['Jugador'].isin(jugadores_filtrados)]

# Ahora df_filtrado contiene las estadísticas de los jugadores que estuvieron en los equipos de la lista
print(df_filtrado)
