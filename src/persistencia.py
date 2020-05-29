import os
import json
import pandas as pd

EXCEL_FILE_STD = "relacao.xlsx"
JSON_FILE_STD = 'requerimentos.json'


def to_json(documents, dest = "."):
    with open(os.path.join(dest, JSON_FILE_STD), 'w') as file:
        json.dump(documents, fp=file, indent=4)

def read_json(source = '.'):
    with open(os.path.join(source, JSON_FILE_STD), 'r') as file:
        documents = json.load(file)

    return documents


def to_excel(documents, dest = "."):

    col = ['tipo', 'nro', 'protocolo', 'ano', 'autor', 'conteudo', 'destinatario', 'cargo_destinatario']
    df = pd.DataFrame(documents, columns=col)

    filename = os.path.join(dest, EXCEL_FILE_STD)
    # filename = EXCEL_FILE_STD

    df.to_excel(filename, index=False, sheet_name='requerimentos')

def read_excel(source = '.', to_dict=False):

    filename = os.path.join(source, EXCEL_FILE_STD)
    df = pd.read_excel(filename, index_col=None).fillna('')
    df.sort_values(by=["nro"], inplace=True)

    if not to_dict:
        return df
    else:
        return convert_frame2dict(df)

def convert_frame2dict(frame):
    return frame.to_dict('records')
