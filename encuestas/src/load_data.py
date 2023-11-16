import pandas as pd
import os


def load_from_folder(folder_dir):
    n_folder = os.listdir(folder_dir)
    archive = []
    for file_name in n_folder:
        file_dir = os.path.join(folder_dir, file_name)
        df = pd.read_csv(file_dir)
        archive.append(df)
    archive = pd.concat(archive)
    return archive