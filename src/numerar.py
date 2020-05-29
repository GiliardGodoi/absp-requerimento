from operator import attrgetter

def numerar_requerimentos(documentos):

    print("                 ..:: NUMERAR REQUERIMETNOS ::..")

    if not isinstance(documentos, list):
        raise TypeError("esperava um list de requerimentos")

    numerados = [ doc for doc in documentos if ('nro' in doc) and doc['nro'].isdigit() ]

    sem_numerar = list()
    for doc in documentos :
        if 'nro' not in doc:
            doc['nro'] = ''
            sem_numerar.append(doc)
        elif not doc['nro'].isdigit():
            sem_numerar.append(doc)

    executar = criterio_parada(sem_numerar, deseja_continuar=True)
    while executar:
        buscar_and_numerar(sem_numerar, numerados)
        executar = criterio_parada(sem_numerar)

    numerados.extend(sem_numerar)

    return ordenar(numerados)

def criterio_parada(documentos, deseja_continuar=False, resposta_negativa = {"n", "no", "não"}):

    if len(documentos) == 0:
        print("\n:: Todos os documentos foram numerados ::")
        return False

    if deseja_continuar:
        return deseja_continuar

    resp = input("[?] Deseja continuar? [s/n] >> ")
    if resp.lower() in resposta_negativa :
        return False

    return True

def procurar_por_palavra_chave(palavrachave, documentos):
    return [documento for documento in documentos if palavrachave.lower() in documento["conteudo"].lower()]

def atribuir_numero(documento):
    print("[?] O seguinte item corresponde a pesquisa? [s/n]\n")
    print(documento["conteudo"])

    resp = input("\n>>> [s/n] ")
    if resp.lower() == 's':
        nro = input("Digite o número do requerimento: >>  ")
        documento["nro"] = nro
        return documento
    else:
        raise NameError("Item não encontrado")

def buscar_and_numerar(documentos, numerados):

    palavra_chave = input(">> Digite uma paravra de busca :: ")
    selecionados  = procurar_por_palavra_chave(palavra_chave, documentos)

    if len(selecionados) == 0:
        print("Palavra chave não encontrada!")
    elif len(selecionados) == 1:
        try:
            documento_numerado = atribuir_numero(selecionados.pop())
            numerados.append(documento_numerado)
        except NameError as msg:
            print(msg)
        else:
            documentos.remove(documento_numerado)

    elif len(selecionados) > 1:

        while selecionados:
            doc = selecionados.pop()
            try:
                documento_numerado = atribuir_numero(doc)
                numerados.append(documento_numerado)
            except NameError as msg:
                print(msg)
            else:
                documentos.remove(documento_numerado)

def ordenar(documentos, attr_name="nro"):
    print(type(documentos))
    from pprint import pprint

    for doc in documentos:
        if "nro" not in doc:
            pprint(doc)

    return sorted(documentos, key=lambda item: item['nro'])
