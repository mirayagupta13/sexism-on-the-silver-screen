from dataclasses import dataclass
import spacy
import nltk
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pathlib import Path
from pprint import PrettyPrinter
from collections import Counter
from math import log

#loading file directory for scraped plain text of articles
directory = Path(__file__).resolve().parent
directory = Path(directory, 'fp_data')

#shortening functions
nlp = spacy.load('en_core_web_sm')
pp = PrettyPrinter()

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

list_of_names = [tup[0] for tup in a_list]
all_names = ''.join(list_of_names)

#creating an actor object for each article
all_actor_names = [a_tup[0] for a_tup in a_list]
actor_list = []

#i = 0
for item in directory.iterdir():
    if item.is_file():
        with item.open(encoding="utf8") as f:
            content = f.read()
            index_all_actor_names = all_actor_names.index(item.name[:len(item.name)-4])
            a_name = all_actor_names[index_all_actor_names]
            a_gender = a_list[index_all_actor_names][1]
            spacy_o = nlp(content)

            
            #Filtering out stopwords
            STOPWORDS = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'also', 'first', 'role', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'}

            nltk_o = nltk.word_tokenize(content)
            nltk_1 = [word for word in nltk_o if word.lower() not in STOPWORDS]
            nltk_2 = [word for word in nltk_1 if '=' not in word]
            nltk_3 = [word for word in nltk_2 if word.isalnum()]
            nltk_4 = [word for word in nltk_3 if word not in all_names]
            actor_list.append(actor(a_name, a_gender, content, spacy_o, nltk_4))
            #remove this after testing
#             i += 1
#             if i == 3:
#                 break

#test
print(actor_list[0].title)
print(actor_list[0].gender)

### NLTK VADER SENTIMENT ANALYSIS

#running VADER on each article, returns a tuple of (name, gender, score)
# analyzer = SentimentIntensityAnalyzer()
# female_scores = []
# male_scores = []
# for actor in actor_list:
#     vs = analyzer.polarity_scores(actor.text)
#     if actor.gender == 0:
#         female_scores.append((actor.title, vs))
#     elif actor.gender == 1:
#         male_scores.append((actor.title, vs))

# pp.pprint(female_scores)
# pp.pprint(male_scores)

#GENSIM TOPIC ANALYSIS
# def gensim_topic_model(actor_gender):
#     from gensim import models, corpora
#     from nltk.stem.wordnet import WordNetLemmatizer
#     import time
#     
#     
# 
#     topic_analysis_docs = [person.tokens for person in actor_list if person.gender == actor_gender]
#     
# 
#     lemmatizer = WordNetLemmatizer()
#     def lemmatize_tokens(tokens): 
#         return [lemmatizer.lemmatize(token) for token in tokens]
# 
#     texts = [lemmatize_tokens(tokens_lst) for tokens_lst in topic_analysis_docs]
#     dictionary = corpora.Dictionary(texts)
#     dictionary.filter_extremes(no_below=5, no_above=0.8) #keep_n = 100
#     corpus = [dictionary.doc2bow(text, allow_update=True) for text in texts]
# 
#     print("Done preprocessing the text. Finding topics...")
# 
#     # Set training parameters.
#     num_topics = 10
#     chunksize = 2000
#     
#     passes = 20
#     iterations = 400
# 
#     start_time = time.perf_counter()
#     model = models.LdaModel(
#         corpus=corpus,
#         id2word=dictionary,
#         chunksize=chunksize,
#         alpha='auto',
#         eta='auto',
#         iterations=iterations,
#         num_topics=num_topics,
#         passes=passes,
#     )
#     end_time = time.perf_counter()
# 
#     print(model.print_topics(10))
#     print(f"Took {end_time - start_time:0.2f} seconds")
#     
# #Testing topic modelling - prints out output
# print('Female actors')
# gensim_topic_model(0)
# print('Male actors')
# gensim_topic_model(1)
#     
#Entity Recognizer with spaCy
def dependent_adjectives(actor_gender):
    adjectives = {}

    for person in actor_list:
        if person.gender == actor_gender:
            adj = []
            for token in person.spacy_object:
                if token.pos_ == 'ADJ':
                    adj.append(token)         
            adjectives[person.title] = adj 
    return adjectives

female_adjectives = dependent_adjectives(0)
male_adjectives = dependent_adjectives(1)

female_adj_count = Counter(female_adjectives)
male_adj_count = Counter(male_adjectives)

#From lab1a
all_spacy_docs = [person.spacy_object for person in actor_list]

# 
# def get_term_frequency(term, doc, adj_count):
#     term = term.lower()
#     # Compute the term count using document.token_counter
#     term_count = adj_count[term]
#     # Get the count of all of the tokens in the document
#     token_count = len(doc.tokens)
#     # Compute term frequency (see docstring)
#     term_frequency = term_count/token_count
# 
#     return term_frequency
# 
# 
# def get_inverse_document_frequency(term, corpus):
#     term = term.lower()
#     docs_containing_term_count = 0
#     # Iterate through the docs and accumulate docs_containing_term_count
#     for doc in corpus:
#         if term in adj_list[term]: #term
#             docs_containing_term_count += 1
#     # Compute inverse document frequency (see docstring)
#     inverse_document_frequency = log(len(corpus)/docs_containing_term_count)
#     return inverse_document_frequency
# 
# def get_tfidf(term, document, corpus, adj_count):
#     tfidf = get_inverse_document_frequency(term, corpus) * get_term_frequency(term, document, adj_count)
#     return tfidf
# 
# def get_keywords(document, corpus, adj_list, adj_count, result_count=10):
#     # Calculate tf-idf for all unique tokens (use document.token_set)
#     all_token_tfidfs = []
#     for token in adj_list:
#         token_tuple = token, get_tfidf(token, document, corpus, adj_count)
#         all_token_tfidfs.append(token_tuple)
#     # sort all_token_tfidfs by tf-idf score
#     # use sorted() or list.sort()
#     all_token_tfidfs.sort(key = lambda x:x[1], reverse = True)
#     # get just the top result_count entries from the list
#     top_keywords = all_token_tfidfs[:result_count]
#     return top_keywords

def get_keywords_new(actor_adj_list, document, corpus, adj_count):
    # Step 1: get the frequency of each adjective in its document
    term_and_freq = {}
    for term in actor_adj_list:
        term_count = adj_count[term]
        token_count = len(document) #len(document.tokens)
        term_frequency = term_count/token_count
        term_and_freq[term] = term_frequency
    
    # Step 2: get the frequency of the term in the corpus
    docs_containing_term_count = 0
    # Iterate through the docs and accumulate docs_containing_term_count
    term_and_idf = {}
    for word in actor_adj_list:
        for doc in corpus:
            if word in doc: #doc.tokens 
                docs_containing_term_count += 1
        # Compute inverse document frequency
        inverse_document_frequency = log(len(corpus)/docs_containing_term_count)
        term_and_idf[word] = inverse_document_frequency
    
    # Step 3: compute tfidf
    term_and_tfidf = {}
    for adj in actor_adj_list:
        tfidf =  term_and_idf[adj] * term_and_freq[adj]
        term_and_tfidf[adj] = tfidf
        
    return term_and_tfidf

    
female_adj_tfidf = {}
for person in actor_list:
    if person.gender == 0:
        actor_adj_list = female_adjectives[person.title]
        counter = Counter(actor_adj_list)
        keywords = get_keywords_new(actor_adj_list, person.spacy_object, all_spacy_docs, counter)
        # Sorting the dictionary based on highest to lowest tfidf values
        sorted_keywords = sorted(keywords.items(), key=lambda x: x[1], reverse=True)
        female_adj_tfidf[person.title] = sorted_keywords


print(female_adj_tfidf)
        
#=======
# print(female_adj_tfidf)  
# >>>>>>> 725864b8d0c6ae343c1b023c49b53fda001b0cb4


