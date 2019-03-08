from enum import IntEnum

class Flow(IntEnum):
	TPH = 1200
	TC = 2200
	TSD = 2500
	TS = 1800
	TK = 800
	BUS = 300

#print(Flow.TPH.value)
print(Flow["TPH"])

'''def get_mean_waiting_time(flow: Flow):
    departure_interval = 1 / flow
    arrival_interval = random() * departure_interval
    queue_length = arrival_interval / departure_interval

    return queue_length / (departure_interval * (1 - queue_length))

get_mean_waiting_time(flow: Flow)
'''
