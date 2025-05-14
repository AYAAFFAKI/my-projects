def GBFS(start, end, graphe, distance):
    memoire = [start]  # List to store visited nodes (the path)

    while start != end:
        # Get all neighboring nodes that haven't been visited yet
        element = [m for m in graphe[start] if m not in memoire]

        # If there are no unvisited neighbors, the path cannot be completed
        if not element:
            print(f"GBFS: No path found between {memoire[0]} and {end}.")
            return

        # Choose the neighbor with the smallest estimated distance to the goal
        start = min(element, key=lambda x: distance.get(x, float('inf')))
        memoire.append(start)  # Add the chosen node to the path

    # If we reached the goal, print the path taken
    print(f"The solution from GBFS is: {'->'.join(memoire)}.")
