def DFS(start, end, graphe=dict):  # Depth-First Search
    memoire = [start]  # List to store visited nodes (the path)
    Pile = []          # Stack to keep track of nodes to explore

    while start != end:
        # Add unvisited neighbors to the stack
        for voi in graphe[start]:
            if voi not in memoire and voi not in Pile:
                Pile.append(voi)

        # If the stack is empty, there's no path to the goal
        if not Pile:
            print(f"DFS: No path found between {start} and {end}.")
            return

        # Check the top of the stack
        if Pile[-1] not in memoire:
            memoire.append(Pile[-1])  # Mark the node as visited
            start = Pile[-1]          # Move to the next node
            Pile.pop(-1)              # Remove it from the stack
        else:
            # No other nodes can be explored
            print(f"DFS: No path found between {start} and {end}.")
            return

    # If we reached the goal, print the path
    print(f"The solution from DFS is: {'->'.join(memoire)}.")
