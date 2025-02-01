pseudocode = """\
Shortest Path using Dijkstra Algorithm
1. function dijkstra(G, S)
2. for each vertex V in G:
    dist[V] <- infinite
    prev[V] <- NULL
    if V != S, add V to priority queue Q
3. dist[S] <- 0
4. while Q is not empty:
    U <- extract min from Q
    for each unvisited neighbor V of U:
        TDistance <- dist[U] + edge_weight(U, V)
        if TDistance < dist[V]:
            dist[V] <- TDistance
            prev[V] <- U
5. Return dist[], prev[]
"""
