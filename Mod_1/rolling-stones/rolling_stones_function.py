# Find by name - Takes in a string representing album name. Return a dictionary with the correct album, or return None.

def find_name(album_name):
    name = []
    for dic in stones_list:
        if album_name == dic['album']:
            name.append(dic)
    return(name)



# Find by rank - Takes in a number that represents the rank in the list of top albums and returns the album with that
# rank. If there is no album with that rank, it returns None.   stones_list

def find_rank(desired_rank):
    rank = []
    for dic in stones_list:
        if desired_rank == dic['number']:
            rank.append(dic)
    return rank



# Find by year - Takes in a number for the year in which an album was released and returns a list of albums that were
# released in that year. If there are no albums released in the given year, it returns an empty list.    stones_list

def find_year(year):
    years = []
    for dic in stones_list:
        if year == dic['year']:
            years.append(dic)
    return years


years = list(map(lambda x: x['year'], stones_list))


albums = list(map(lambda x: x['album'], stones_list))


artists = list(map(lambda x: x['artist'], stones_list))


genre = list(map(lambda x: x['genre'], stones_list))


subgenre = list(map(lambda x: x['subgenre'], stones_list))
