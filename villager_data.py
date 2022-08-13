"""Functions to parse a file containing villager data."""


# def all_species(filename):
#     """Return a set of unique species in the given file.

#     Arguments:
#         - filename (str): the path to a data file

#     Return:
#         - set[str]: a set of strings

#     """
#     villagers_details = open(filename)
#     species = set()
#     for line in villagers_details:
#         detail = line.split('|')
#         species_detail = detail[1]
#         species.add(species_detail)

#     return species

# print(all_species('villagers.csv'))

# def get_villagers_by_species(filename, search_string="All"):
#     """Return a list of villagers' names by species.

#     Arguments:
#         - filename (str): the path to a data file
#         - search_string (str): optional, the name of a species

#     Return:
#         - list[str]: a list of names
#     """

#     villagers = []
#     villagers_details = open(filename)
#     for line in villagers_details:
#         details = line.split("|")
#         name = details[0]
#         if search_string == "All":
#             villagers.append(name)
#         elif search_string in line:
#             villagers.append(name)


#     return sorted(villagers)

# # print(get_villagers_by_species('villagers.csv', 'Bird'))

# def all_names_by_hobby(filename):
#     """Return a list of lists containing villagers' names, grouped by hobby.

#     Arguments:
#         - filename (str): the path to a data file

#     Return:
#         - list[list[str]]: a list of lists containing names
#     """
#     fitness_list = []
#     nature_list = []
#     education_list = []
#     music_list = []
#     fashion_list = []
#     play_list = []
#     hobby_list = []
#     villagers_details = open(filename)
#     for line in villagers_details:
#         details = line.split('|')
#         name = details[0]
#         hobby = details[3]
#         if 'Fitness' == hobby:
#             fitness_list.append(name)
#         elif 'Nature' == hobby:
#             nature_list.append(name)
#         elif 'Education' == hobby:
#             education_list.append(name)
#         elif 'Music' == hobby:
#             music_list.append(name)
#         elif 'Fashion' == hobby:
#             fashion_list.append(name)
#         elif 'Play' == hobby:
#             play_list.append(name)
#     hobby_list = [fitness_list, education_list, nature_list, music_list, fashion_list, play_list]
#     return hobby_list

# print(all_names_by_hobby('villagers.csv'))

# def all_data(filename):
#     """Return all the data in a file.

#     Each line in the file is a tuple of (name, species, personality, hobby,
#     saying).

#     Arguments:
#         - filename (str): the path to a data file

#     Return:
#         - list[tuple[str]]: a list of tuples containing strings
#     """

#     all_data = []
#     villagers_details = open(filename)
#     for line in villagers_details:
#         line = line.rstrip()
#         details = line.split('|')
#         name = details[0]
#         species = details[1]
#         personality = details[2]
#         hobby = details[3]
#         motto = details[4]
#         data_tuple = (name, species, personality, hobby, motto)
#         all_data.append(data_tuple)
#     return all_data
# print(all_data('villagers.csv'))

# def find_motto(filename, villager_name):
#     """Return the villager's motto.

#     Return None if you're not able to find a villager with the
#     given name.

#     Arguments:
#         - filename (str): the path to a data file
#         - villager_name (str): a villager's name

#     Return:
#         - str: the villager's motto or None
#     """
#     villagers_details = open(filename)
#     for line in villagers_details:
#         details = line.split('|')
#         name = details[0]
#         motto = details[4]
#         if name == villager_name:
#             return motto

# print(find_motto('villagers.csv', 'Kurt'))


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    common_personality = set()
    villagers_details = open(filename)
    for line in villagers_details:
        details = line.split('|')
        name = details[0]
        personality = details[2]
        if villager_name == name:
            villager_personality = personality

    for line in villagers_details:
        details = line.split('|')
        name = details[0]
        if villager_personality in details:
            common_personality.add(name)
    return common_personality


print(find_likeminded_villagers('villagers.csv', 'Bianca'))