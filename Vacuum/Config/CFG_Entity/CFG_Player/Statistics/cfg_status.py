cfg_status = {
    0: 0,
    1: 5000,
    2: 12000,
    3: 22000,
    4: 35000,
    5: 50000,
    6: 70000,
    7: 100000,
    8: 140000,
    9: 200000
}

import random

default_coef = 1

coef_status_by_weapon = 1
coef_status_by_device = 0

random_value = 1.1

def get_status_for_kill(Whom, coef):
    status = int(Whom.status * coef * default_coef)
    status = random.randint(status, int(random_value * status))
    return status

