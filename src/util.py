
number2Month = {
    1 : 'janeiro',
    2 : 'fevereiro',
    3 : 'março',
    4 : 'abril',
    5 : 'maio',
    6 : 'junho',
    7 : 'julho',
    8 : 'agosto',
    9 : 'setembro',
    10 : 'outubro',
    11 : 'novembro',
    12 : 'dezembro'
}

month2Number = {
    'janeiro'   :  1,
    'fevereiro' :  2,
    'março'     :  3,
    'abril'     :  4,
    'maio'      :  5,
    'junho'     :  6,
    'julho'     :  7,
    'agosto'    :  8,
    'setembro'  :  9,
    'outubro'   : 10,
    'novembro'  : 11,
    'dezembro'  : 12
}


requerimentos_modelo = set([
    "Edson Muniz.docx",
    "EdsonMuniz.docx",
    "Edson.docx",
    "Flávio.docx",
    "Flavio.docx",
    "Genivaldo.docx",
    "Jefferson.docx",
    "José Jaime.docx",
    "Jose Jaime.docx",
    "JoséJaime.docx",
    "JoseJaime.docx",
    "Luciano.docx",
    "Mirian.docx",
    "Odemir.docx",
    "Rudinei.docx",
    "Todos.docx"
])

# https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def eh_requerimento_vereador(arquivo):
    return arquivo.endswith(".docx") and (arquivo in requerimentos_modelo)
