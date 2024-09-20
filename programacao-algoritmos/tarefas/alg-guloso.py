import random

def alocacao_atividades(atividades):

    atividades_alocadas = []
    sorted_fim_atividades = sorted(atividades.items(), key=lambda x: x[1][1])
    sorted_inicio_atividades = sorted(atividades.items(), key=lambda x: x[1][0])

    atividades_alocadas.append(sorted_fim_atividades[0])
    prox_tempo = atividades_alocadas[-1][1][1] # pega o fim da primeira atividade
    
    # para cada atividade, verifica se o inicio é maior ou igual ao fim da atividade anterior
    for atividade in sorted_inicio_atividades:
        if atividade[1][0] >= prox_tempo:
            atividades_alocadas.append(atividade)
            prox_tempo = atividade[1][1]

    # imprime as atividades alocadas
    for id_atividade, tempo in atividades_alocadas:
        print(f'{id_atividade} - Início: {tempo[0]} | Fim: {tempo[1]}')

# gera atividades aleatórias
def gerar_atividades_aleatorias(n):
    atividades = {}
    for i in range(n):
        inicio = random.randint(0, 10)
        fim = random.randint(inicio + 1, 10 + inicio)
        atividades[f'A{i+1}'] = [inicio, fim]
    return atividades


if __name__ == '__main__':
    input_usuario = int(input('Digite a quantidade de atividades: '))

    print('\n==== ATIVIDADES GERADAS ====\n')
    atividades = gerar_atividades_aleatorias(input_usuario)
    for atividade in atividades:
        print(f'{atividade} - Início: {atividades[atividade][0]} | Fim: {atividades[atividade][1]}')

    print('\n==== ATIVIDADES ALOCADAS ====\n')
    alocacao_atividades(atividades)