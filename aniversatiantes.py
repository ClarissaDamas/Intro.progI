
pessoas = [
    {"nome": "Anabell", "dia": 5, "mes": "maio"},
    {"nome": "Barbie", "dia": 12, "mes": "agosto"},
    {"nome": "Carol", "dia": 23, "mes": "Fevereiro"},
    {"nome": "Douglas", "dia": 15, "mes": "Março"},
    {"nome": "Eliza", "dia": 5, "mes": "dezembro"},
    {"nome": "Hugo", "dia": 12, "mes": "Janeiro"},
    {"nome": "Jessica", "dia": 23, "mes": "Fevereiro"},
    {"nome": "Tang", "dia": 15, "mes": "Março"},
    {"nome": "Guillermo", "dia": 5, "mes": "Janeiro"},
    {"nome": "Vitoria", "dia": 12, "mes": "Janeiro"},
    {"nome": "Carla", "dia": 23, "mes": "Fevereiro"},
    {"nome": "David", "dia": 15, "mes": "Março"},
    {"nome": "Julia", "dia": 5, "mes": "Janeiro"},
    {"nome": "Bob", "dia": 12, "mes": "Janeiro"},
    {"nome": "Carol", "dia": 23, "mes": "Fevereiro"},
    {"nome": "David", "dia": 15, "mes": "Março"},
    {"nome": "Priscila", "dia": 5, "mes": "Janeiro"},
    {"nome": "Bob", "dia": 12, "mes": "Janeiro"},
    {"nome": "Carol", "dia": 23, "mes": "Fevereiro"},
    {"nome": "David", "dia": 15, "mes": "Março"},
    {"nome": "Daniel", "dia": 5, "mes": "Janeiro"},
    {"nome": "Bob", "dia": 12, "mes": "Janeiro"},
    {"nome": "Carol", "dia": 23, "mes": "Dezembro"},
    {"nome": "Lorena", "dia": 15, "mes": "Março"},
    {"nome": "Belinda", "dia": 5, "mes": "Janeiro"},
    {"nome": "Bob", "dia": 12, "mes": "Janeiro"},
    {"nome": "Izabel", "dia": 23, "mes": "Fevereiro"},
    {"nome": "David", "dia": 15, "mes": "Março"},
    {"nome": "Agatha", "dia": 5, "mes": "Janeiro"},
    {"nome": "Bob", "dia": 12, "mes": "Janeiro"},
    {"nome": "Bruno", "dia": 23, "mes": "setembro"},
    {"nome": "David", "dia": 15, "mes": "Março"},
    {"nome": "Alice", "dia": 5, "mes": "Janeiro"},
    {"nome": "Jonas", "dia": 12, "mes": "Janeiro"},
    {"nome": "Carol", "dia": 23, "mes": "abril"},
    {"nome": "David", "dia": 15, "mes": "Março"},
    {"nome": "Alice", "dia": 5, "mes": "Janeiro"},
    {"nome": "Bob", "dia": 12, "mes": "Janeiro"},
    {"nome": "Ester", "dia": 23, "mes": "Fevereiro"},
    {"nome": "Felipe", "dia": 15, "mes": "junho"},
]

def agrupar_aniversariantes(pessoas):
    janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro = [], [], [], [], [], [], [], [], [], [], [], []
    
    for pessoa in pessoas:
        mes = pessoa["mes"]
        if mes == "Janeiro":
            janeiro.append(pessoa)
        elif mes == "Fevereiro":
            fevereiro.append(pessoa)
        elif mes == "Março":
            marco.append(pessoa)
        elif mes == "Abril":
            abril.append(pessoa)
        elif mes == "Maio":
            maio.append(pessoa)
        elif mes == "Junho":
            junho.append(pessoa)
        elif mes == "Julho":
            julho.append(pessoa)
        elif mes == "Agosto":
            agosto.append(pessoa)
        elif mes == "Setembro":
            setembro.append(pessoa)
        elif mes == "Outubro":
            outubro.append(pessoa)
        elif mes == "Novembro":
            novembro.append(pessoa)
        elif mes == "Dezembro":
            dezembro.append(pessoa)
    
    return janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro


def exibir_aniversariantes(mes, lista):
    print('Aniversariantes de mes', mes)
    for aniversariante in lista:
        print(aniversariante['nome'], 'faz aniversario Dia:', aniversariante['dia'])
    print("Total de aniversariantes em", mes)
    print(len(aniversariante))


janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro = agrupar_aniversariantes(pessoas)

exibir_aniversariantes("Janeiro", janeiro)
exibir_aniversariantes("Fevereiro", fevereiro)
exibir_aniversariantes("Março", marco)
exibir_aniversariantes("Abril", abril)
exibir_aniversariantes("Maio", maio)
exibir_aniversariantes("Junho", junho)
exibir_aniversariantes("Julho", julho)
exibir_aniversariantes("Agosto", agosto)
exibir_aniversariantes("Setembro", setembro)
exibir_aniversariantes("Outubro", outubro)
exibir_aniversariantes("Novembro", novembro)
exibir_aniversariantes("Dezembro", dezembro)

print('fim')
