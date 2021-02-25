# coding: utf-8
import argparse
import configparser
import json
import os
from datetime import datetime

from src.numerar import numerar_requerimentos, ordenar
from src.parserdoc import parse_requerimento
from src.persistencia import read_excel, read_json, to_excel, to_json
from src.util import eh_requerimento_vereador, number2Month
from src.worddocument import (relacionar_requerimentos,
                              relacionar_requerimentos2)

TODAY = datetime.now()

parser = argparse.ArgumentParser(description="Redator Oficial CLI")

parser.add_argument("-A", "--ano", type=str, default=str(TODAY.year),
                    help="Entrada Ano: informação para localizar diretório dos documentos")
parser.add_argument("-M", "--mes", type=str, default=number2Month[TODAY.month].upper(),
                    help="Entrada mes: informação para localizar diretório dos documetos")
parser.add_argument("-d", "--dia", type=str, required=True,
                    help="Entrada DIA: informação para localizar diretório dos documentos")
parser.add_argument("--numerar", action='store_true',
                    help="Tenta numerar documentos")
parser.add_argument("--excel",   action='store_true',
                    help="Lê arquivo excel")
parser.add_argument("--json",    action='store_true',
                    help="Lê arquivo json")
parser.add_argument("--relacionar", action='store_true',
                    help="Relaciona os documentos em um arquivo Word")
parser.add_argument("--relacionar2", action='store_true',
                    help="Outra opção para numerar requerimentos")
parser.add_argument("--ordenar",    action='store_true',
                    help="Ordena novamente os arquivos")

args = parser.parse_args()


## ===========================================
config = configparser.ConfigParser()
config.read("config.ini")

## ===========================================

MAIN_FOLDER = os.path.join(config["DEFAULT"]["start_folder"], args.ano, args.mes, args.dia)

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

if args.ordenar :

    documentos = ordenar(documentos)

if args.relacionar:
    relacionar_requerimentos(documentos)

if args.relacionar2:
    relacionar_requerimentos2(documentos)


to_json(documentos)
# to_excel(documentos)
