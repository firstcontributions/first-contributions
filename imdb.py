#IT IS A MINI-IMDB PROJECT THAT PROVIDES INFORMATION ABOUT ANY MOVIE OR TV SERIES WHEN SEARCHED.

#READ THE DOCUMENTATION FIRST, THEN MOVE ON TO THE SOURCE CODE AS DOCUMENTATION WILL BRIEF YOU ABOUT THE PYTHON MODULE, DATA STRUCTURES USED AND ALSO HOW TO WORK THROUGH THIS PROGRAM.

"""For running this code you have to download IMDbPy package from google. IMDbPY is a Python package useful to retrieve and manage the data of the IMDb movie database about movies, people,
characters and companies.Platform-independent and written in Python 3 it can retrieve data from both the IMDb’s web server and a local copy of the whole database.
IMDbPY package can be very easily used by programmers and developers to provide access to the IMDb’s data to their programs."""

#For understanding this project you need to have a basic knowledge about python, definition of database, module, instances and lists.

"""While running the code it asks for a movie or tv series name. After you enter the movie or a  tv series name it returns a list of movies or tv series with its id which are related to the
movies or tv series you entered. Since every movie or tv series has a unique id, this program asks for a id for the particular movie or tv series you want to search after you enter the id
it reuturns plot, cast name, director of movie or writer of a tv series, rating, genre. """


import imdb                      # importing the module
ia = imdb.IMDb()                 # creating instance of IMDB
print("=======================")
name = input("Enter movie, tv series name : ")                # movie name
search = ia.search_movie(name)   # searching the movie
lst = list()	# defining a list
lst1 = list()
lst2 = list()
for j in range(len(search)) :
    id = search[j].movieID
    lst1.append(search[j]["title"] + " : " + id)
    lst2.append(id)
print(lst1)
print("====================================")
print("As there might me many unwanted results. Please select the movie you want the plot of")
print("\n")
movie = input("Enter the id of the movie or tv series whose plot you want : ")
index = lst2.index(movie)
Movie = search[index]
ia.update(Movie, info = ["plot"])	# to get the plot of the movie
print(Movie["plot"])
print("\n")
print("Cast of the movie or tv series : ")
movies = ia.get_movie(movie)
cast = movies["cast"]	# to get the cast of the movie
for i in cast :
    actor = i
    print(actor)
print("\n")
print("Director of film or writer of series : ")
try :
    for director in movies["directors"] :	# try and except is used to prevent error messages that show up while compiling
        print(director["name"])
except :
    for writer in movies["writer"] :
        print(writer["name"])
print("\n")
try :
    print("Ratings : ")
    rating = movies.data["rating"]
    print(rating)
except :
    print("Sorry something went wrong, could't get the ratings :(")
print("\n")
try :
    print("Genres : ")
    genre = movies.data["genres"]
    print(genre)
except :
    print("Sorry something went wrong, could't get the genres :(")
    
    
