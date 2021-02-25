import docx
import re

def get_TipoNroAno(text):
    '''
    Returns:
        tipo : str
        nro : str
        ano : str
    '''

    regex = re.compile(r"(Requerimento|Indicação).+\s+([0-9]{0,})\/([0-9]{4})")
    result = regex.findall(text)

    if result:
        return result[0]
    else:
        # print("Erro  >> ", text)
        return '', '', ''

def get_LongDate(text):
    '''
    Returns:
        dia : str
        mes : str
        ano : str
    '''
    regex = re.compile(r"(\d{0,2})\s+de\s+(\w+)\s+de\s+(\d{4})")
    result = regex.findall(text)

    if result:
        return result[0]
    else:
        # print("Erro  >> ", text)
        return '', '', ''

def get_DestinatarioCargoNome(text):
    regex = re.compile(r"ofício ao\s+([\w\s\d-]+)[,\s]{1,4}([\d\.º°ª\w\s]+),")
    result = regex.findall(text)

    if result:
        return result[0]
    else:
        # print("Erro  >> ", text)
        return '', ''

def get_Autor(text):
    regex = re.compile(r"[OAs]{1,2}\s+(Vereado[raes]{0,3}[\w\s]{1,}).+infra-assinad[aos]{1,2}")
    result = regex.findall(text)

    if result:
        return result[0]
    else :
        # print("Erro  >> ", text)
        return ''

def parse_requerimento(filename):
    '''Parse documento'''

    document = docx.Document(filename)
    paragraphs = (p.text.strip() for p in document.paragraphs if p.text.strip())

    requerimentos = list()

    try:
        while paragraphs:
            text = next(paragraphs)
            if text.startswith("Requerimento") or text.startswith("Indica"):

                tipo, nro, ano = get_TipoNroAno(text)

                text = next(paragraphs)
                if text.startswith("Excelentíssimo"):
                    pass

                text = next(paragraphs)
                if text.startswith("Presidente"):
                    pass

                text = next(paragraphs)

                dest_cargo, dest_nome = get_DestinatarioCargoNome(text)
                autor = get_Autor(text)

                main_content = list()

                while not text.startswith("Nestes termos,"):
                    main_content.append(text)
                    text = next(paragraphs)

                content = ' '.join(main_content)

                text = next(paragraphs)
                if text.startswith("Pede deferimento"):
                    pass

                text = next(paragraphs)

                dia, mes, ano = get_LongDate(text)

                documento = {
                    'tipo' : tipo or "Requerimento",
                    'nro' : nro,
                    'ano' : ano,
                    "autor" : autor,
                    "destinatario" : dest_nome,
                    "cargo_destinatario" : dest_cargo,
                    "conteudo" : content,
                    "data" : {
                        "dia": dia,
                        "mes" : mes,
                        "ano" : ano
                    },
                    "protocolo" : ""
                }

                requerimentos.append(documento)

            else:
                pass
    except StopIteration:
        pass

    return requerimentos
