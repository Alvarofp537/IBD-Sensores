import requests
import pandas as pd

def comprobar(metrica):
    return metrica in ['temperatura', 'consumo', 'ocupacion', 'seguridad']

def get_datos(metrica):
    if not comprobar(metrica):
        raise ValueError("Métrica no válida: ['temperatura', 'consumo', 'ocupacion', 'seguridad']")
    data = requests.get(f'http://localhost:8080/{metrica}')
    df = pd.DataFrame(data.json())
    return df.set_index('id')