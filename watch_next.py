import spacy

nlp = spacy.load('en_core_web_md')


# Function that takes in a movie description and prints out/
# recommends the movie with the highest similarity .
def movie_recommendation(description):
    # Read in text file movies.txt
    with open("movies.txt", "r") as movie:
        lines = [line.rstrip() for line in movie]
        print(lines)

    model_sentence = nlp(description)

    for line in lines:
        similarity = nlp(line).similarity(model_sentence)
        print(line + " - ", similarity)

    # print the movie with the highest similarity.
    print(max((nlp(line).similarity(model_sentence), line) for line in lines))


movie_recommendation('''Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.''')