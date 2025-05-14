def BFS(start, end, graphe=dict):  # Breadth-First Search
    memoire = [start]  # List to store visited nodes (the path)
    file = []          # Queue to store nodes to explore (FIFO)

    while start != end:
        # Add all unvisited neighbors to the queue
        for frend in graphe[start]:
            if frend not in file and frend not in memoire:
                file.append(frend)

        # If the queue is empty, no path was found
        if not file:
            print(f"BFS: No path found between {start} and {end}.")
            return

        # Check the front of the queue
        if file[0] not in memoire:
            memoire.append(file[0])  # Mark the node as visited
            start = file[0]          # Move to the next node
            file.pop(0)              # Remove it from the queue
        else:
            # No more nodes to explore
            print(f"BFS: No path found between {start} and {end}.")
            return

    # If we reached the goal, print the path
    print(f"The solution from BFS is: {'->'.join(memoire)}.")
