from pyamaze import maze, COLOR, agent


def compute_path(my_maze, my_agent):
    """
    Exercício:
    Implemente um algoritmo de busca por profundidade, que encontre o caminho
    que o agente deve percorrer para encontrar a saída do labirinto.

    Dicas:
    - Use o atributo my_maze.maze_map para checar os movimentos possíveis.
    - Use o atributo my_agent.position para saber a posição do agente.
    - Verifique os formatos adequados para um caminho nesse post do
    Towards Data Science, feito pelo autor do pacote:
    https://towardsdatascience.com/a-python-module-for-maze-search-algorithms-64e7d1297c96

    Integrantes do Grupo 5:
    Enrico Ribeiro Farina         - RA: 22007679
    Guilherme Ferreira Jorge      - RA: 22007283
    Marcos Antônio Valério Filho  - RA: 22006092
    """
    # cria célula com posição do Agente
    start_cell = my_agent.position

    # cria Pilhas para conter células exploradas e que devem ser exploradas, respectivamente
    explored_cells = [start_cell]
    cells_to_be_explored = [start_cell]

    # cria dicionário com as células exploradas filha e pai, sendo a chave e o valor, respectivamente
    path_prof = {}

    # Busca por Profundidade enquanto há células para explorar ou caia na condição de parada do loop
    while len(cells_to_be_explored) > 0:

        # guarda uma célula a ser explorada na variável
        currCell = cells_to_be_explored.pop()

        # condição de parada caso a célula seja o resultado do labirinto
        if currCell == my_maze._goal:
            break

        # loop para checar as células que devem ser exploradas a partir da célula guardada
        for direction in "NSEW":

            # checa se a direção escolhida é possivel de ser feita
            if my_maze.maze_map[currCell][direction] == True:

                # se o norte é possível, então ele guarda a célula ao norte como filha
                if direction == "N":
                    childCell = (currCell[0] - 1, currCell[1])

                # se o sul é possível, então ele guarda a célula ao norte como filha
                elif direction == "S":
                    childCell = (currCell[0] + 1, currCell[1])

                # se o leste é possível, então ele guarda a célula ao norte como filha
                elif direction == "E":
                    childCell = (currCell[0], currCell[1] + 1)

                # se o oeste é possível, então ele guarda a célula ao norte como filha
                elif direction == "W":
                    childCell = (currCell[0], currCell[1] - 1)

                # checa se a célula filha já foi explorada
                # se sim, ele checa a próxima direção possível, se houver
                if childCell in explored_cells:
                    continue

                # adiciona a célula filha como explorada e para ser explorada
                explored_cells.append(childCell)
                cells_to_be_explored.append(childCell)

                # adiciona na chave da célula filha a célula pai
                path_prof[childCell] = currCell

    # cria dicionário que irá conter o caminho resultado, que conecta o agente com o fim do labirinto
    path_final = {}

    # inverte as células encontradas do fim do labirinto até o agente
    cell = my_maze._goal
    while cell != start_cell:
        path_final[path_prof[cell]] = cell
        cell = path_prof[cell]

    return path_final


if __name__ == "__main__":
    # cria environment
    my_maze = maze(25, 25)
    # lê labirinto do exercício
    my_maze.CreateMaze(theme=COLOR.light, x=9, y=20)
    # cria agente
    my_agent = agent(my_maze, 5, 2, shape="arrow", filled=True, footprints=True)
    # calcula passos que o agente seguirá para sair do labirinto
    my_path = compute_path(my_maze, my_agent)
    # executa os passos calculados
    my_maze.tracePath({my_agent: my_path}, delay=50, kill=False)
    # roda a animação mostrando o movimento do agente
    my_maze.run()
