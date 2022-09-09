import questionary
import random

mood = [
'Action',
'Adventure',
'Biography',
'Comedy',
'Crime',
'Drama',
'Horror',
'Mystery',
'Romance',
'Sci-Fi',
'Sport',
'Thriller',
'Western'
]

movies = [
['Fight Club', 'Drama'],
['Taxi Drive', 'Crime, Drama'],
['Pulp Fiction', 'Crime, Drama'],
['Forrest Gump', 'Drama, Romance'],
['Goodfellas', 'Biography, Crime, Drama'],
['Back to the Future', 'Adventure, Comedy, Sci-Fi'],
['Once Upon a Time in the West', 'Western'],
['Jaws', 'Adventure, Thriller'],
['Alien', 'Horror, Sci-Fi'],
['Blade Runner', 'Action, Drama, Sci-Fi'],
['Jurassic Park', 'Action, Adventure, Sci-Fi'],
['Rambo', 'Action, Adventure, Thriller'],
['Rocky', 'Drama, Sport'],
['Fargo', 'Crime, Thriller'],
['No Country for Old Men', 'Crime, Drama, Thriller'],
['Nightcrawler', 'Crime, Drama, Thriller'],
['Donnie Darko', 'Drama, Mystery, Sci-Fi'],
['A Clockwork Orange', 'Crime, Sci-Fi'],
['Se7en', 'Crime, Drama, Mystery'],
['Joker', 'Crime, Drama, Thriller'],
['American Psycho', 'Crime, Drama, Horror'],
['Drive', 'Action, Drama'],
['Pulp Fiction', 'Crime, Drama'],
['The Machinist', 'Drama, Thriller'],
['Scarface', 'Crime, Drama'],
['No Country for Old Men', 'Crime, Drama, Thriller'],
['The Godfather', 'Crime, Drama'],
['Shutter Island', 'Mystery, Thriller'],
]

def main(): 
    print("\n***********************\n*Based Movies Selector*\n***********************\n")
    menu = questionary.select(
        "What do you want to do:",
        choices= [
            "Choose random movie",
            "Select your mood",
            "About",
            "Exit :("
        ],
        qmark="🎬",
        pointer="*"
    ).ask()
    # print(menu)
    # if menu == None:
    #     print("You are a looser!")
    if menu == "Choose random movie":
        movie = random.choice(movies)
        print(f"\nTitle: {movie[0]}\n\nGenre: {movie[1]}\n")
        exit()
    elif menu == "Select your mood":
        genre = questionary.select(
            "What are your mood?",
            choices= mood,
            qmark="🎬",
            pointer="*"
        ).ask()
        i = 0
        while i <= 27:
            movie = movies[i]
            if genre in movie[1]:
                print(f"\nTitle: {movie[0]}\nGenre: {movie[1]}\n")
                i += 1
            else:
                i += 1

    elif menu == "About":
        print("This is a simple script to choose a random movie based on your mood\n")
        print("This script is based on OMDB API\n")
        print("My Github: https://github.com/felipeNegrelle\n")
        print("Made by Felipe with ❤️\n")
    
    elif menu == "Exit :(":
        print("Bye bye!")
        exit()

if __name__ == '__main__':
    main()
