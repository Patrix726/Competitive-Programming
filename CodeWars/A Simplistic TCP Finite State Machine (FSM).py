def traverse_TCP_states(events):
    state = "CLOSED"  # initial state, always
    eventDictionary = {
        'CLOSED': {'APP_PASSIVE_OPEN': 'LISTEN', 'APP_ACTIVE_OPEN': 'SYN_SENT'}, 
        'LISTEN': {'RCV_SYN': 'SYN_RCVD', 'APP_SEND': 'SYN_SENT', 'APP_CLOSE': 'CLOSED'}, 
        'SYN_RCVD': {'APP_CLOSE': 'FIN_WAIT_1', 'RCV_ACK': 'ESTABLISHED'}, 
        'SYN_SENT': {'RCV_SYN': 'SYN_RCVD', 'RCV_SYN_ACK': 'ESTABLISHED', 'APP_CLOSE': 'CLOSED'}, 
        'ESTABLISHED': {'APP_CLOSE': 'FIN_WAIT_1', 'RCV_FIN': 'CLOSE_WAIT'}, 
        'FIN_WAIT_1': {'RCV_FIN': 'CLOSING', 'RCV_FIN_ACK': 'TIME_WAIT', 'RCV_ACK': 'FIN_WAIT_2'}, 
        'CLOSING': {'RCV_ACK': 'TIME_WAIT'}, 'FIN_WAIT_2': {'RCV_FIN': 'TIME_WAIT'}, 
        'TIME_WAIT': {'APP_TIMEOUT': 'CLOSED'}, 
        'CLOSE_WAIT': {'APP_CLOSE': 'LAST_ACK'}, 'LAST_ACK': {'RCV_ACK': 'CLOSED'}}
    for i in events:
        if i in eventDictionary[state].keys():
            state = eventDictionary[state][i]
        else:
            return "ERROR"
    return state

# allEvents = ["APP_PASSIVE_OPEN", "APP_ACTIVE_OPEN", "APP_SEND",
#               "APP_CLOSE", "APP_TIMEOUT", "RCV_SYN", "RCV_ACK", 
#               "RCV_SYN_ACK", "RCV_FIN", "RCV_FIN_ACK"]
# states = ["CLOSED", "LISTEN", "SYN_SENT", "SYN_RCVD", "ESTABLISHED", 
#           "CLOSE_WAIT", "LAST_ACK", "FIN_WAIT_1", "FIN_WAIT_2", 
#           "CLOSING", "TIME_WAIT"]
# eventDictionary = [
#     [{0 : 1},{1:2}],
#     [{5:3},{2:2},{3:0},
#      [{3:7}],
#      [{3:7}]
#      ]
# ]
print(traverse_TCP_states(["APP_ACTIVE_OPEN"]))