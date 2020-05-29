# coding: utf-8
import argparse
import json
import os
from datetime import datetime

from src.numerar import numerar_requerimentos
from src.parserdoc import parse_requerimento
from src.persistencia import read_excel, read_json, to_excel, to_json
from src.util import eh_requerimento_vereador, number2Month
from src.worddocument import (relacionar_requerimentos,
                              relacionar_requerimentos2)

TODAY = datetime.now()

# https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser(description="Redator Oficial CLI")
parser.add_argument("-A", "--ano", help="Ano entrada", type=str, default=str(TODAY.year))
parser.add_argument("-M", "--mes", help="Mes entrada", type=str, default=number2Month[TODAY.month].upper())
parser.add_argument("-d", "--dia", help="Dia entrada", type=str, required=True)

parser.add_argument("--numerar",    help="Tenta numerar documentos", action='store_true')
parser.add_argument("--excel",      help="Lê arquivo excel",         action='store_true')
parser.add_argument("--json",       help="Lê arquivo json",          action='store_true')
parser.add_argument("--relacionar", help="Relaciona os documentos em um arquivo Word", action='store_true')
parser.add_argument("--relacionar2", help="Another option", action='store_true')
# parser.add_argument("-P", "--planilha", help="Criar planilha de requerimentos", type=str2bool, default=False)
# parser.add_argument("-I", "--imprimir", help="Imprimir na tela", type=str2bool, default=False)


args = parser.parse_args()

print(args)
## ===========================================

MAIN_FOLDER = os.path.join(r"C:\Users\User\Arquivo\R\REQUERIMENTOS", args.ano, args.mes, args.dia)

if not os.path.exists(MAIN_FOLDER):
    raise NotADirectoryError(f"Folder doesn't exist :: {MAIN_FOLDER}")
else:
    os.chdir(MAIN_FOLDER)

## ===========================================

if (not args.excel) and (not args.json) :
    filenames = [ file for file in os.listdir() if eh_requerimento_vereador(file)]

    documentos = list()
    for file in filenames:
        print(file)
        documentos.extend(parse_requerimento(file))

elif args.json :
    documentos = read_json()

elif args.excel :
    # Busca o arquivo requerimentos.json criado na etapa anterior
    documentos = read_excel(to_dict=True)

if args.numerar :
    documentos = numerar_requerimentos(documentos)

if args.relacionar:
    relacionar_requerimentos(documentos)
elif args.relacionar2:
    relacionar_requerimentos2(documentos)


to_json(documentos)
# to_excel(documentos)
