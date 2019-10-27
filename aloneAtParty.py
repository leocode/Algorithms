def aloneAtParty(A):
    paired = []
    for i in A:
        if A.count(i) < 2:
             return 'The person alone is ' + str(i) + ' years old.'
    return 'Everybody\'s got a pair.'
