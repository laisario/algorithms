def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if target_time is None or target_time == 0:
        return None
    count = 0
    for student in permanence_period:
        if type(student[0]) != int or type(student[1]) != int:
            return None
        if student[0] <= target_time <= student[1]:
            count += 1 
    return count
             
    raise NotImplementedError

print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5))

# student[0] <= target_time and student[1] >= target_time:
# count = [*range(student[0], student[1])]