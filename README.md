# Gerenciar Requerimentos

Automatizando tarefas simples que devem ser executadas todas as semanas.

## Descrição do uso

Para criar o arquivo `requerimentos.json`.

´´´python
python main.py -d 18
´´´

Para criar a relação de requerimentos em arquivo `.docx`.

Se já tiver sido criado o arquivo `requerimentos.json`.
´´´python
python main.py -d 18 --json --numerar --relacionar
´´´

## Ajuda

Descrição da ajuda fornecida por padrão.

```cmd
usage: main.py [-h] [-A ANO] [-M MES] -d DIA [--numerar] [--excel] [--json]
               [--relacionar] [--relacionar2]

Redator Oficial CLI

optional arguments:
  -h, --help         show this help message and exit
  -A ANO, --ano ANO  Ano entrada
  -M MES, --mes MES  Mes entrada
  -d DIA, --dia DIA  Dia entrada
  --numerar          Tenta numerar documentos
  --excel            Lê arquivo excel
  --json             Lê arquivo json
  --relacionar       Relaciona os documentos em um arquivo Word
  --relacionar2      Another option
```

## Funcionalidades (desejadas e implementadas)

- [x] Criar a lista de requerimentos para constar na ata;

- [x] Criar utilitário (CLI) para ajudar a atribuir números aos documentos;

- [x] Odernar os requerimentos por número se uma numeração for fornecida;

- [x] Relacionar os requerimentos para um arquivo `.json`;

- [ ] Criar uma planilha de requerimento para fins de mala direta e de controle de requerimento. Outros usuário poderão querer acessar esses dados de outras formas;

- [ ] Prover a funcionalidade de log do sistema para verificar rapidamente os locais que o parse de documento está falhando;

- [ ] Corrigir numeração de requerimentos ao mesmo tempo que evita que requerimentos já numerados fiquem retornando na busca de palavras ou seja reprocessados pela funcionalidade numerar_requerimentos;

- [ ] Copiar os requerimentos e documentos relacionaldos para outro computador da rede;

- [ ] Checar se os documentos do servidor são os mesmos dos documentos locais;

- [ ] Transformar o projeto em um pacote para poder ser instalado e suas funcionalidade acessadas a partir da linha de comando, sem a necessidade de invocar o ```python main.py```;

- [ ] Utilitario para ajudar a produzir os ofícios de encaminhamento dos requerimentos.

## Autor

Desenvolvido nas horas vagas por Giliard Godoi <https://github.com/GiliardGodoi/>
