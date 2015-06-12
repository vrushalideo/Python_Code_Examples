grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    avg = sum_of_grades / float(len(grades))
    return avg

def grades_variance(scores):
    average = grades_average(scores)
    var = 0
    for i in scores:
        var += (average - i)**2
    return float(var)/len(scores)

def grades_std_deviation(variance):
    return variance**(0.5) 
    variance = grades_variance(grades)

print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)
