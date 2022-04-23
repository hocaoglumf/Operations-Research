# Depth First Search

visited=[] # Ziyaret edilen düğümler
# node : aramaya başladığımız düğüm

def dfs(visited, graph, node ):
    if (node not in visited):
        #print(node.value)
        s=0
        for uye in node.valueSet:

            dfs(visited, graph, uye)
            visited.append(uye)


    return visited