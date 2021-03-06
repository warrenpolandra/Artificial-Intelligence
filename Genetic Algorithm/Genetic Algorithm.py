import string
import random
count = 1


# Print population
def print_population():
    for x in range(0, len(population)):
        print('String ' + str(x + 1) + ': ' + population[x] + ', fitness: ' + str(fitnessValue[x]) + '%')


# Create randomized string
def randomize():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits,
                                  k=len(originalString)))


# Fitness function
def fitness(subject):
    counter = 0
    for c in range(0, len(subject)):
        if originalString[c] == subject[c]:
            counter += 1
    percentage = float(counter/len(subject) * 100)
    return "{:.2f}".format(percentage)


# Selection function
def selection():
    for x in range(2):
        min_value = min(fitnessValue)
        del population[fitnessValue.index(min_value)]
        del fitnessValue[fitnessValue.index(min_value)]


# Crossover function for both parents
def crossover():
    n = random.randint(0, len(originalString)-1)
    population.append(population[0][0:n] + population[1][n:len(originalString)])
    population.append(population[1][0:n] + population[0][n:len(originalString)])
    fitnessValue.append(fitness(population[2]))
    fitnessValue.append(fitness(population[3]))


# Mutation function to mutate random character in the string
def mutation():
    for x in range(4):
        for m in range(len(population[x])):
            if population[x][m] != originalString[m]:
                # Random character
                c = random.choice(string.ascii_letters)
                population[x] = population[x][:m] + c + population[x][m+1:]


def genetic_algorithm():
    global count
    selection()
    crossover()
    mutation()
    print('Generation ' + str(count) + ':')
    count += 1
    print_population()
    print()
    for x in range(4):
        if float(fitnessValue[x]) == 100.00:
            print('Perfect chromosome found!')
            return
    genetic_algorithm()


# Main function
originalString = input('Original String: ')
population = [randomize() for x in range(4)]
fitnessValue = [fitness(population[0]), fitness(population[1]), fitness(population[2]), fitness(population[3])]
for i in range(0, len(population)):
    print('Randomized String ' + str(i+1) + ': ' + population[i] + ', fitness: ' + str(fitnessValue[i]) + '%')
print()
genetic_algorithm()
