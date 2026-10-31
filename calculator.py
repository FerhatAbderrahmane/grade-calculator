def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


def is_passing(average):
    return average >= 10
