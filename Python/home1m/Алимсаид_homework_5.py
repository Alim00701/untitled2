movies = {
    "Django Unchained": {"John": 10, "Jack": 9},

    "Spider-Man": {}
}

def add_movies(movie):
    if movie in movies.keys():
        print("This movie already exist!")
    else:
        movies.update({movie: dict()})
        print("Movie added successfully")

def rate_movies(movie):
    if movie in movies.keys():
        name = input("Enter your name: ")
        numb = int(input("Enter your rate: "))
        if numb < 1 or numb > 10:
            print("Rate must be 1-10! ")
        else:
            movies[movie].update({name: numb})
            print(f"A rating has been added for {movie}: {name} rated it {numb}")
    else:
        print("This movie doesn't exist")

def average1():
    for movie, rates in movies.items():
        numb = []
        for i in rates.values():
            numb.append(i)
        if len(numb) == 0:
            print(f"Rating is not yet available for {movie}")
        else:
            print(f"{movie} is rated {sum(numb)/len(numb)}")

while True:
    for f, r in movies.items():
        print(f"{f}: {r}")

    command = input("\nEnter command(1 - add film, 2 - add rate, 3 view rates, 0 - finish program): ")

    if command == '0':
        print("The program is completed!")
        break

    if command == '1':
        film = input("Введите название фильма: ")
        add_movies(film)

    if command == '2':
        film = input("Введите фильм который хотите оценить: ")
        rate_movies(film)

    if command == '3':
        average1()

    else:
       print("Command doesn't exist")



