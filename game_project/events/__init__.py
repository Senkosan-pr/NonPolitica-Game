import random
from events.event_1_150 import event_1_150
from events.event_151_400 import event_151_400
from events.event_401_450 import event_401_450
from events.event_451_475 import event_451_475
from events.event_476_750 import event_476_750
from events.event_751_1000 import event_751_1000

def handle_event(random_value):
    if 1 <= random_value <= 150:
        return event_1_150()
    elif 151 <= random_value <= 400:
        return event_151_400()
    elif 401 <= random_value <= 450:
        return event_401_450()
    elif 451 <= random_value <= 475:
        return event_451_475()
    elif 476 <= random_value <= 750:
        return event_476_750()
    elif 751 <= random_value <= 1000:
        return event_751_1000()
    return random_value