import pandas as pd

# 1. Simulando datos reales y bagunçados de un hospital español
dados_hospital = {
    'id_paciente': [1, 2, 3, 4, 5, 6],
    'nombre': ['Juan García', 'María Rodríguez', 'Carlos Martínez', 'Juan García', 'Ana Fernández', 'Luis Gómez'],
    'fecha_analisis': ['2026-06-01', '02/06/2026', '2026-06-03', '2026-06-01', None, '2026-06-05'],
    'hemoglobina_g_dL': [14.2, 11.5, 98.0, 14.2, 13.8, None]
}

df = pd.DataFrame(dados_hospital)
print("=== DATOS ORIGINALES CON ERRORES ===")
print(df)

# 2. Limpieza de datos (Data Cleaning)
# Eliminando registros totalmente duplicados (como el de Juan García)
df_limpio = df.drop_duplicates()

# Asegurando que trabajamos sobre una copia limpia para evitar avisos de Pandas
df_limpio = df_limpio.copy()

# Estandarizando el formato de las fechas a año-mes-día
df_limpio['fecha_analisis'] = pd.to_datetime(df_limpio['fecha_analisis'], errors='coerce')

# Corrigiendo valores imposibles (Hemoglobina mayor a 20g/dL se ajusta a la media)
media_hemoglobina = df_limpio[df_limpio['hemoglobina_g_dL'] <= 20]['hemoglobina_g_dL'].mean()
df_limpio.loc[df_limpio['hemoglobina_g_dL'] > 20, 'hemoglobina_g_dL'] = media_hemoglobina

# Rellenando valores faltantes de análisis con la palabra 'Pendiente' o la media
df_limpio['fecha_analisis'] = df_limpio['fecha_analisis'].astype(str).fillna('Pendiente')
df_limpio['hemoglobina_g_dL'] = df_limpio['hemoglobina_g_dL'].fillna(media_hemoglobina)

print("\n=== DATOS CLÍNICOS LIMPIOS Y PROCESADOS ===")
print(df_limpio)
