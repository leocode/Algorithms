
def aloneAtParty(all_ages):
    all_ages = all_ages.strip().split(' ')

    results = { }
    output = []

    for age in all_ages:
        numOfCurrentAge = results.get(age,0)
        if numOfCurrentAge == 0:
            results[age]=1
        else:
            results[age]=0

    for age, num in results.items():
        if num != 0:
            output.append(age)

    if len(output) == 0:
        print("Everybody's got a pair")
    else:
        print(f"People alone ages: {','.join(output)}")

    print(results)

tab = input('Type people ages, divided by space. Example: 20 12 32 34 93 23\n')
aloneAtParty(tab)
