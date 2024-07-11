# Lista de pessoas com seus aniversários
pessoas = [
    {"nome": "Alice", "dia": 5, "mes": "Janeiro"},
    {"nome": "Bob", "dia": 12, "mes": "Janeiro"},
    {"nome": "Carol", "dia": 23, "mes": "Fevereiro"},
    {"nome": "David", "dia": 15, "mes": "Março"},
    # Adicione mais pessoas conforme necessário
]

# Dicionário para agrupar aniversariantes por mês
aniversariantes_por_mes = {
    "Janeiro": [], "Fevereiro": [], "Março": [], "Abril": [],
    "Maio": [], "Junho": [], "Julho": [], "Agosto": [],
    "Setembro": [], "Outubro": [], "Novembro": [], "Dezembro": []
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
    print(f"Total de aniversariantes em {mes}: {len(aniversariantes)}")
