import numpy as np
import matplotlib.pyplot as plt
import heapq
import matplotlib.animation as animation


# Função para gerar um mapa aleatório
def generate_random_map(size, obstacles_ratio=0.2):
    # Cria um mapa vazio (0s)
    mapa = np.zeros((size, size))

    # Adiciona obstáculos (1s) com base em uma razão
    obstacles = np.random.rand(size, size) < obstacles_ratio
    mapa[obstacles] = 1

    return mapa


# Função heurística (distância de Manhattan)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Algoritmo A* para encontrar o menor caminho, com animação
def astar(mapa, start, end):
    size = mapa.shape[0]
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    cost_so_far = {start: 0}

    steps = []  # Lista para armazenar o progresso do algoritmo

    while open_list:
        _, current = heapq.heappop(open_list)

        steps.append((current, "explored"))  # Registrar o nó explorado

        if current == end:
            break

        neighbors = [
            (current[0] + 1, current[1]),
            (current[0] - 1, current[1]),
            (current[0], current[1] + 1),
            (current[0], current[1] - 1),
        ]

        for next in neighbors:
            if 0 <= next[0] < size and 0 <= next[1] < size and mapa[next] == 0:
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(next, end)
                    heapq.heappush(open_list, (priority, next))
                    came_from[next] = current
                    steps.append(
                        (next, "open")
                    )  # Registrar o nó adicionado à lista aberta

    # Reconstrução do caminho
    current = end
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    for step in path:
        steps.append((step, "path"))  # Registrar os passos no caminho final

    return steps


# Função para animar o progresso do algoritmo A*
def animate_astar(mapa, steps, start, end):
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(-0.5, len(mapa), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(mapa), 1), minor=True)
    ax.grid(which="minor", color="black", linestyle="-", linewidth=2)

    # Desenhar o mapa inicial
    ax.imshow(mapa, cmap="gray_r")

    # Marcar os pontos de início e fim
    ax.scatter(start[1], start[0], color="green", s=100, label="Start")
    ax.scatter(end[1], end[0], color="red", s=100, label="End")

    explored = []
    open_list = []
    path = []

    def update(frame):
        nonlocal explored, open_list, path
        current, status = steps[frame]

        if status == "explored":
            explored.append(current)
        elif status == "open":
            open_list.append(current)
        elif status == "path":
            path.append(current)

        ax.clear()
        ax.imshow(mapa, cmap="gray_r")
        ax.scatter(start[1], start[0], color="green", s=100, label="Start")
        ax.scatter(end[1], end[0], color="red", s=100, label="End")

        # Desenhar nós explorados
        if explored:
            explored_coords = np.array(explored)
            ax.scatter(
                explored_coords[:, 1],
                explored_coords[:, 0],
                color="blue",
                s=50,
                label="Explored",
            )

        # Desenhar nós na lista aberta
        if open_list:
            open_coords = np.array(open_list)
            ax.scatter(
                open_coords[:, 1], open_coords[:, 0], color="gray", s=20, label="Open"
            )

        # Desenhar o caminho final
        if path:
            path_coords = np.array(path)
            ax.plot(
                path_coords[:, 1],
                path_coords[:, 0],
                color="green",
                linewidth=2,
                label="Path",
            )

        ax.legend()

    animation.FuncAnimation(fig, update, frames=len(steps), interval=1, repeat=False)
    plt.show()


# Tamanho do mapa
size = 20

# Gerando o mapa aleatório
mapa = generate_random_map(size)

# Definindo pontos de início e fim
start = (0, 0)
end = (size - 1, size - 1)

# Garantindo que início e fim não sejam obstáculos
mapa[start] = 0
mapa[end] = 0

# Executando o algoritmo A* e armazenando os passos
steps = astar(mapa, start, end)

# Animando o progresso do algoritmo
animate_astar(mapa, steps, start, end)
