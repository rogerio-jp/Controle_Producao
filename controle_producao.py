import sqlite3

# Criar ou conectar ao banco de dados
conn = sqlite3.connect("producao.db")
cursor = conn.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS producao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    operador TEXT,
    numero_ordem TEXT,
    tipo_aplicador TEXT,
    codigo_produto TEXT,
    quantidade_total INTEGER,
    quantidade_atual INTEGER,
    hora_inicio TEXT,
    hora_fim TEXT,
    trocas_rolo INTEGER,
    ocorrencias TEXT
)
""")
conn.commit()

def registrar_producao():
    operador = input("Nome do operador: ")
    numero_ordem = input("Número da ordem: ")
    tipo_aplicador = input("Tipo de aplicador: ")
    codigo_produto = input("Código do produto: ")
    quantidade_total = int(input("Quantidade total planejada: "))
    quantidade_atual = int(input("Quantidade atual produzida: "))
    hora_inicio = input("Hora de início (HH:MM): ")
    hora_fim = input("Hora de término (HH:MM): ")
    trocas_rolo = int(input("Número de trocas de rolo: "))
    ocorrencias = input("Ocorrências durante a produção: ")

    cursor.execute("""
    INSERT INTO producao (
        operador, numero_ordem, tipo_aplicador, codigo_produto,
        quantidade_total, quantidade_atual, hora_inicio, hora_fim,
        trocas_rolo, ocorrencias
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (operador, numero_ordem, tipo_aplicador, codigo_produto,
          quantidade_total, quantidade_atual, hora_inicio, hora_fim,
          trocas_rolo, ocorrencias))
    conn.commit()
    print("Registro salvo com sucesso!\n")

def listar_registros():
    cursor.execute("SELECT * FROM producao")
    registros = cursor.fetchall()
    print("\nRegistros de Produção:")
    print("ID | Operador | Ordem | Aplicador | Código | Total Planejado | Atual Produzido | Início | Fim | Trocas de Rolo | Ocorrências")
    for registro in registros:
        print(" | ".join(map(str, registro)))
    print()

def calcular_perdas():
    cursor.execute("SELECT id, trocas_rolo, quantidade_atual FROM producao")
    registros = cursor.fetchall()
    perda_total = 0

    print("\nCálculo de Perdas:")
    for registro in registros:
        registro_id, trocas_rolo, quantidade_atual = registro
        quantidade_esperada = trocas_rolo * 1000
        perda = quantidade_esperada - quantidade_atual

        # Exibir cálculo por registro
        print(f"Registro {registro_id}:")
        print(f" - Trocas de Rolo: {trocas_rolo}")
        print(f" - Produção Esperada: {quantidade_esperada}")
        print(f" - Produção Atual: {quantidade_atual}")
        print(f" - Perda: {perda}\n")

        # Somar as perdas
        perda_total += max(perda, 0)

    print(f"Perda total acumulada: {perda_total} conectores\n")

def menu():
    while True:
        print("1. Registrar Produção")
        print("2. Listar Registros")
        print("3. Calcular Perdas")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            registrar_producao()
        elif escolha == "2":
            listar_registros()
        elif escolha == "3":
            calcular_perdas()
        elif escolha == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    menu()
    conn.close()
