update_energy = 1 # s
update_health = 1 # s

precent_max_health = 0.005
precent_max_energy = 0.01

coef_multiplier_recovery_health = 2
coef_multiplier_recovery_energy = 2

def recovery_energy(max_energy, repair_skills):
    return int(max_energy * precent_max_energy + repair_skills * coef_multiplier_recovery_energy)

def recovery_health(max_health, repair_skills):
    return int(max_health * precent_max_health + repair_skills * coef_multiplier_recovery_health)