#credit to https://melaniewalsh.github.io/Intro-Cultural-Analytics/05-Text-Analysis/03-TF-IDF-Scikit-Learn.html

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from pathlib import Path  
import glob
from pprint import PrettyPrinter as pp

### TFIDF FOR EACH DOCUMENT

#getting file names
directory = Path(__file__).resolve().parent
directory = Path(directory, 'fp_data')
text_files = glob.glob(f"{directory}/*.txt")

#getting file titles
a_list = [("Julie Andrews", 0), ( "Lauren Bacall", 0), ("Amitabh Bachchan", 1),
("Brigitte Bardot", 0), ("Ingrid Bergman", 0), ("Sarah Bernhardt", 0), ("Humphrey Bogart", 1),
("Marlon Brando", 1), ("James Cagney", 1), ("Jackie Chan",1), ("Claudette Colbert",0),
("Sean Connery",1), ("Gary Cooper", 1), ("Joan Crawford", 0), ( "Bette Davis", 0), 
("Doris Day",0), ("Robert De Niro", 1), ("Alain Delon", 1), ("Marlene Dietrich",0),
("Clint Eastwood",1), ("Henry Fonda", 1), ("Jean Gabin", 1), ("Clark Gable",1),
("Greta Garbo",0), ( "Judy Garland",0), ("John Gielgud",1), ("Lillian Gish",0),
("Cary Grant",1), ("Alec Guinness",1), ("Tom Hanks",1), ("Setsuko Hara",0),
("Rita Hayworth",0), ("Audrey Hepburn",0), ("Katharine Hepburn",0), ("Grace Kelly",0),
("Klaus Kinski",1), ("Vivien Leigh",0), ("Sophia Loren",0), ("Madhubala", 0),
("Marcello Mastroianni", 1), ("Toshiro Mifune", 1), ("Marilyn Monroe", 0), ("Jeanne Moreau", 0),
("Jack Nicholson", 1), ("Laurence Olivier", 1), ("Peter O'Toole", 1), ("Gregory Peck", 1),
("Mary Pickford", 0), ("Sidney Poitier", 1), ("Rajinikanth", 1), ("Barbara Stanwyck", 0),
("James Stewart", 1), ("Meryl Streep", 0), ("Elizabeth Taylor", 0), ("Shirley Temple", 0),
("Spencer Tracy", 1), ("Rudolph Valentino", 1), ("John Wayne", 1), ("Mae West", 0)]
all_actor_names = [a_tup[0] for a_tup in a_list]
all_actor_genders = [a_tup[1] for a_tup in a_list]

#running tf-idf on entire document
tfidf_vectorizer = TfidfVectorizer(input='filename', stop_words='english', min_df=2)
tfidf_vector = tfidf_vectorizer.fit_transform(text_files)

#putting it in a dataframe
tfidf_df = pd.DataFrame(tfidf_vector.toarray(), index=all_actor_names, columns=tfidf_vectorizer.get_feature_names_out())

#getting top 10 tfidf words for each actor
tfidf_df = tfidf_df.stack()
tfidf_df = tfidf_df.reset_index()
tfidf_df = tfidf_df.rename(columns={0:'tfidf', 'level_0': 'document','level_1': 'term', 'level_2': 'term'})
tfidf_df = tfidf_df.sort_values(by=['document','tfidf'], ascending=[True,False]).groupby(['document']).head(10)
print(tfidf_df)

#sending results to file
tfidf_df.to_csv('adj_out.csv')