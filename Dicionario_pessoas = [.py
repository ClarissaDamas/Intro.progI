Dicionario_pessoas = [
    {"nome": "Alice", "dia do niver": 5, "mes do niver": 4},
    {"nome": "Bob", "dia": 12, "mes": 6},
    {"nome": "Carol", "dia": 23, "mes": 9},
    {"nome": "David", "dia": 15, "mes": 8},
    {"nome": "David", "dia": 15, "mes": 8},
    {"nome": "David", "dia": 15, "mes": 8},
    {"nome": "David", "dia": 15, "mes": 8},
    {"nome": "David", "dia": 15, "mes": 8},
    {"nome": "David", "dia": 15, "mes": 8},
    {"nome": "David", "dia": 15, "mes": 8},
    {"nome": "David", "dia": 15, "mes": 8},
    {"nome": "David", "dia": 15, "mes": 8},
    {"nome": "David", "dia": 15, "mes": 8},
]

# Dicionário para agrupar aniversariantes por mês
aniversariantes_por_mes = {
    "Janeiro": [],
    "Fevereiro": [],
    "Março": [],
    "Abril": [],
    "Maio": [],
    "Junho": [],
    "Julho": [],
    "Agosto": [],
    "Setembro": [],
    "Outubro": [],
    "Novembro": [],
    "Dezembro": []
}

# Agrupar aniversariantes por mês
for pessoa in pessoas:
    mes = pessoa["mes"]
    aniversariantes_por_mes[mes].append(pessoa)

# Exibir aniversariantes por mês e total
for mes, aniversariantes in aniversariantes_por_mes.items():
    print(f"\nAniversariantes de {mes}:")
    for aniversariante in aniversariantes:
        print(f"- {aniversariante['nome']} (Dia: {aniversariante['dia']})")
    print(f"Total de aniversariantes em {mes}: {len(aniversariante