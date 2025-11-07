import yaml

data = {
    "MANAGERS": [
        "Alice Johnson", "Bob Smith", "Charlie Brown", "Diana Prince", "Edward Norton",
        "Fiona Gallagher", "George Clooney", "Hannah Montana", "Isaac Newton", "Julia Roberts",
        "Kevin Hart", "Laura Linney", "Michael Jordan", "Natalie Portman", "Oscar Wilde",
        "Penelope Cruz", "Quentin Tarantino", "Rachel Green", "Samuel L. Jackson", "Tina Fey",
        "Ulysses Grant", "Victoria Beckham", "William Shakespeare", "Xander Cage", "Yara Shahidi",
        "Zachary Quinto", "Angela Merkel", "Brandon Lee", "Catherine Zeta-Jones", "David Beckham",
        "Elaine Benes", "Frank Underwood", "Grace Hopper", "Harry Potter", "Irene Adler",
        "Jack Sparrow", "Karen Gillan", "Liam Neeson", "Monica Geller", "Nicolas Cage",
        "Olivia Wilde", "Peter Parker", "Queen Latifah", "Ronald Reagan", "Samantha Carter",
        "Tony Stark", "Uma Thurman", "Vin Diesel", "Wendy Darling", "Xenia Onatopp",
        "Yvonne Strahovski", "Zane Malik", "Abigail Adams", "Brian O’Conner", "Clara Oswald",
        "Daniel Craig", "Eleanor Rigby", "Frederick Douglass", "Gwen Stacy", "Henry Cavill",
        "Isabelle Huppert", "James Bond", "Katherine Johnson", "Leonardo DiCaprio", "Mary Poppins",
        "Nathan Drake", "Oprah Winfrey", "Paul Rudd", "Queenie Goldstein", "Richard Feynman",
        "Sarah Connor", "Thomas Shelby", "Ursula K. Le Guin", "Victor Hugo", "Winston Churchill", "Donald Trump"

    ],
    "active": True
}

# Optionally write it to a YAML file
with open("config.yaml", "w") as file:
    yaml.dump(data, file)
