
def aloneAtParty(all_ages):
    all_ages = all_ages.strip().split(' ')

    results = { }
    output = []

    for age in all_ages:
        numOfCurrentAge = results.get(age,0)
        if numOfCurrentAge == 0:
            results[age]=1
        else:
            results[age]=results[age]+1

    for age, num in results.items():
        if num%2 != 0:
            output.append(age)

    if len(output) == 0:
        print("Everybody's got a pair")
    else:
        print(f"People alone ages: {','.join(output)}")


tab = input('Podaj wiek ludzi po kolei, oddzielajac go spacja. Np. 20 12 32 34 93 23\n')
aloneAtParty(tab)
