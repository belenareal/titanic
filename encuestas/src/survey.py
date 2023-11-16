import pandas as pd
from src.load_data import load_from_folder

def from_folder(cls, folder_path):
    df = load_from_folder(folder_path)
    obj = cls(df)
    return obj

def remove_basic_columns(self):
    basic_columns = ['ID', 
                     'Started on', 
                     'Last updated on', 
                     'IP address', 
                     'Status', 
                     'Collector', 
                     'Language', 
                     'Device', 
                     '{fbclid}', 
                     'Nombre y Apellido', 
                     'Numero de Documento', 
                     'Email', 
                     'Número de Teléfono', 
                     'Número de Celular'
                     ]
    return self.drop(columns=basic_columns)

def filter_nan_from_question(self, question):
    return self.dropna(subset=question)

def rename_columns(self):
    return self.rename({
        '¿Podría indicarnos su género?': 'genero', 
        'Para empezar, ¿podría indicarnos su edad?': 'clase',
        '¿Cuál es su máximo nivel de educación alcanzado?': 'educacion'
    }, axis = 1)
