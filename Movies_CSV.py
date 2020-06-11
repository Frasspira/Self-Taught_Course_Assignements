movies_csv =  [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]


with open('movies.csv', 'w', newline='') as csv_file:

    csv_writer = csv.writer(csv_file, delimiter=',')

    for movies in movies_csv:

        csv_writer.writerow(movies)


