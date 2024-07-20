# def minReorder(n: int, connections: list[list[int]]) -> int:
#     q = [0]
#     edits = 0
#     ind = 0
#     while ind < len(q):
#         val = q[ind:]
#         i = 0
#         length = len(connections)
#         while i < length:
#             if connections[i][0] in val and connections[i][1] not in q:
#                 edits += 1
#                 q.append(connections[i][1])
#             elif connections[i][1] in val and connections[i][0] not in q:
#                 q.append(connections[i][0])
#             elif (connections[i][0] in val and connections[i][1] in q) or (
#                 connections[i][1] in val and connections[i][0] not in q
#             ):
#                 connections.pop(i)
#                 i -= 1
#                 length -= 1
#             i += 1
#         ind += len(val)


#     return edits
def minReorder(n: int, connections: list[list[int]]) -> int:
    conn, edits = order(0, connections, [])
    return edits


def order(n: int, connections: list[list[int]], previous: list[int]):
    edits = 0
    length = len(connections)
    i = 0
    while i < length:
        if n in connections[i]:
            fir = connections[i][0]
            sec = connections[i][1]
            if sec not in previous and fir == n:
                edits += 1
                connections.pop(i)
                conn, ed = order(sec, connections, previous + [n])
                edits += ed
                connections = conn
                length = len(connections)
                i -= 1
            elif fir not in previous and sec == n:
                connections.pop(i)
                conn, ed = order(fir, connections, previous + [n])
                edits += ed
                connections = conn
                length = len(connections)
                i -= 1
        i += 1
    return [connections, edits]


print(minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]))
