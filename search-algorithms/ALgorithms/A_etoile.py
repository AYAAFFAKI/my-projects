def A_etoile(start, end, graphe, distance):
    memoire = [start]  # List to store visited nodes (the path)
    pas = 0            # Step counter (used as a simplistic cost)

    while start != end:
        pas += 1  # Increase the number of steps taken

        # Get all neighboring nodes that haven't been visited yet
        element = [m for m in graphe[start] if m not in memoire]

        # If there are no unvisited neighbors, path cannot be completed
        if not element:
            print(f"A*: No path found between {memoire[0]} and {end}.")
            return

        # Choose the node with the minimum estimated cost (distance + steps)
        start = min(
            element,
            key=lambda x: distance.get(x, float('inf')) + pas
        )

        # Add the chosen node to the path
        memoire.append(start)

    # If we reached the goal, print the path taken
    print(f"The solution from A* is: {'->'.join(memoire)}.")

