import random

default_coef = 0.01

coef_rating_by_weapon = 1
coef_rating_by_device = 0

get_rating_for_level = 1000
random_value = 1.1

def remove_dead_rating_player(Whom):
    return Whom.rating * 0.01

def get_rating_for_kill(Whom, coef):
    rating = int(Whom.rating * default_coef * coef)
    rating = random.randint(rating, int(random_value * rating))
    return rating
