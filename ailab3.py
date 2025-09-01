movies=[
     ("Eternal Sunshine of the Spotless Mind", 20000000),
     ("Memento", 9000000),
     ("Requiem for a Dream", 4500000),
     ("Pirates of the Caribbean: On Stranger Tides", 379000000),
     ("Avengers: Age of Ultron", 365000000),
     ("Avengers: Endgame", 356000000),
     ("Incredibles 2", 200000000)
]

new_movies=int(input("How many movies would you like to add:"))
for i in range(new_movies):
    name=input(f"Enter the name of movie{i+1}:")
    budget=int(input("Enter the budget of '{name}':"))
    movies.append((name,budget))
total_budget=0
for movie in movies:
    total_budget+= movie[1]
    avg_budget=total_budget/len(movies)

above_avg_movies=[]
for name,budget in movies:
    if budget > avg_budget:
        difference=budget - avg_budget
        print(f"'{name}' had a budegt higher than average by ${difference:,.0f}")
        above_avg_movies.append(name)
print(f"\n Number of movies above average budget: {len(above_avg_movies)}")