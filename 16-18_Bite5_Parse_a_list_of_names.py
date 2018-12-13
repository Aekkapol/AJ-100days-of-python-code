NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    return [name.title() for name in list(set(names))]

names = dedup_and_title_case_names(NAMES)

def swap_front_back(list): # This function is not prior-suggested from pybites, I created it.
    swap = []
    for name in list:
        front, back = name.split()
        last_front_text = f'{back} {front}'
        swap.append(last_front_text)
    return swap

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    swap_1 = swap_front_back(names)
    swap_1.sort(reverse = True)
    swap_2 = swap_front_back(swap_1)
    return swap_2

sort_by_surname_desc(names)

def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    first_name = [name.split()[0] for name in names]
    return min(first_name, key=len)

shortest_first_name(NAMES)
