# # LISTS
# ## Exercice 3
# teams = ["ok", "ok2", "ok3"] 
# # remplacer les string par des arrays

# def losing_team_captain(t):
#     i = len(t)
#     return t[i-1]
# print(losing_team_captain(teams))


# ## Exercice 4
# racersList = ['Mike', 'Olivia', 'Mehdi']

# # Inverser la liste des noms des pilotes
# def purple_shell(racers):
#     temp = racers[-1]

#     racers[-1] = racers[0]
#     racers[0] = temp
    
#     return racers

# print(purple_shell(racersList))

## Exercice 4
### Lists des listes suivantes
# a = [1, 2, 3]
# b = [1, [2, 3]]
# c = []
# d = [1, 2, 3][1:]

# lengths = []
# lengths = [len(a), len(b), len(c), len(d)]

# print(lengths)

## Exercice 5
### Print les personnes listés entre le milieu et la fin de la liste

# arrivalsList = ['Patrice', 'Emilie', 'Mounir', 'Myriam']

# def fashionably_late(arrivals, name):
#     order = arrivals.index(name)
#     return order >= len(arrivals) / 2 and order != len(arrivals) - 1

# print(fashionably_late(arrivalsList, "Myriam"))

# Loops and conditions

## Exercice 1
### Corriger le bug
# numsArr = [18, 9, 87, 14, 99, 107]

# def has_lucky_number(nums):
#     for num in nums:
#         print(num)

#         if num % 7 == 0:
#             return True
#     return False

# print(has_lucky_number(numsArr))

## Exercice 2

# Return a list with the same length as L, where the value at index i is True if L[i] is greater than thresh, and False otherwise.
    
# >>> elementwise_greater_than([1, 2, 3, 4], 2)
# [False, False, True, True]

# L = [2, 44, 99, 104, 21]
# def elementwise_greater_than(L, thresh):
#     newArr = []
#     for n in L:
#         if n > thresh:
#             n = True
#         else:
#             n = False

#         newArr.append(n)
#     print(newArr)
# print(elementwise_greater_than(L, 2))

## Exercice 2
### Given a list of meals served over some period of time, return True if the same meal has ever been served two days in a row, and False otherwise.
# meals = ['repas1', 'repas2', 'repas3', 'repas4', 'repas4', 'repas5']

# def menu_is_boring(meals):
#     for i in range(len(meals)-1):
#         if meals[i] == meals[i+1]:
#             return True
#     return False

# print(menu_is_boring(meals))

# Strings and dictionnary
## Exercice 1 - Returns whether the input string is a valid (5 digit) zip code

# def is_valid_zip(zip_code):
    
#     if zip_code.isdigit() and len(zip_code) == 5:
#         return True
#     else :
#         return False

# print(is_valid_zip('22222'))

## Exercice 2 
# -Example:
    # doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    # >>> word_search(doc_list, 'casino')
    # >>> [0]

doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
indices = []
def word_search(doc_list, keyword):

    ### ma solution
    # for i in range(len(doc_list)-1):
    #     if keyword in doc_list[i]:
    #         indices.append(i)
    # return indices

    ###  solution attendue
    for i, doc in enumerate(doc_list):
        tokens = doc.split()
        normalized = [token.rstrip('.,').lower() for token in tokens]
        if keyword.lower() in normalized:
            indices.append(i)
    return indices

# print(word_search(doc_list, "bought"))

# Exercice 3
def multi_word_search(documents, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        # utilisation de la fonction créée précédemment
        keyword_to_indices[keyword] = word_search(documents, keyword)
    return keyword_to_indices

print(multi_word_search(doc_list, "bought"))