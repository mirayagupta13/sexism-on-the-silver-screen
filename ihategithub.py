from dataclasses import dataclass
import spacy
import nltk
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from pathlib import Path  
import glob


#loading file directory for scraped plain text of articles
directory = Path(__file__).resolve().parent
directory = Path(directory, 'fp_data')

#shortening functions
nlp = spacy.load('en_core_web_sm')
#pp = PrettyPrinter()

#creating object to hold each article
@dataclass
class actor:

    """
    Dataclass for storing actors and articles from analysis
    
    Title is the name of the actor as a string
    Gender is an int, 0 = female and 1 = male
    Text is a string of the plain text
    Spacy_object is a Spacy Language object of the article
    Tokens is an NLTK list of tokenized sentences
    """

    title : str
    gender : int
    text : str
    spacy_object : object
    tokens : list[str]

#pretagged list of actors and corresponding gender
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

#creating an actor object for each article
all_actor_names = [a_tup[0] for a_tup in a_list]
actor_list = []

# i = 0
for item in directory.iterdir():
    if item.is_file():
        with item.open(encoding="utf8") as f:
            content = f.read()
            index_all_actor_names = all_actor_names.index(item.name[:len(item.name)-4])
            a_name = all_actor_names[index_all_actor_names]
            a_gender = a_list[index_all_actor_names][1]
            spacy_o = nlp(content)
            
            #Filtering out stopwords
            STOPWORDS = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'}

            nltk_o = nltk.word_tokenize(content)
            nltk_o = [word for word in nltk_o if word.lower() not in STOPWORDS]
            
            actor_list.append(actor(a_name, a_gender, content, spacy_o, nltk_o))
            nltk_o = nltk.word_tokenize(content)
            #actor_list.append(actor(a_name, a_gender, content, spacy_o, nltk_o))
            #remove this after testing
            # i += 1
            # if i == 2:
            #     break

#test
print(actor_list[0].title)
print(actor_list[0].gender)

#running tf-idf no ents
# adj_list = []
# for actor in actor_list:
#     actor_adj = [token.text for token in actor.spacy_object if not token.ent_type]
#     adj_list.append(' '.join(actor_adj))

# print(adj_list[0])
# print('ents worked')

#just adjs
adj_list = []
for actor in actor_list:
    actor_adj = [token.text for token in actor.spacy_object if token.pos_ == 'ADJ']
    if actor_adj:
        adj_list.append(' '.join(actor_adj))
    else:
        adj_list.append(actor.title)

print(adj_list[0])
print('ents worked')

#running tf-idf
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_vector = tfidf_vectorizer.fit_transform(adj_list)

#putting it in a dataframe
tfidf_df = pd.DataFrame(tfidf_vector.toarray(), index=all_actor_names, columns=tfidf_vectorizer.get_feature_names_out())

#getting top 10 tfidf words for each actor
tfidf_df = tfidf_df.stack()
tfidf_df = tfidf_df.reset_index()
tfidf_df = tfidf_df.rename(columns={0:'tfidf', 'level_0': 'document','level_1': 'term', 'level_2': 'term'})
tfidf_df = tfidf_df.sort_values(by=['document','tfidf'], ascending=[True,False]).groupby(['document']).head(10)
print(tfidf_df)

#sending results to file
tfidf_df.to_csv('adj_tfidf.csv')