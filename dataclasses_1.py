from dataclasses import dataclass
import spacy
import nltk
from pathlib import Path

directory = Path(__file__).resolve().parent
directory = Path(directory, 'fp_data')
nlp = spacy.load('en_core_web_sm')

@dataclass
class actor:
    title : str
    gender : int
    text : str
    spacy_object : object
    tokens : list[str]

a_list = [("Julie Andrews", 0),
( "Lauren Bacall", 0),
  ("Amitabh Bachchan", 1),
( "Brigitte Bardot", 0),
 ("Ingrid Bergman", 0),
 ("Sarah Bernhardt", 0),
  ("Humphrey Bogart", 1),
 ("Marlon Brando", 1),
 ("James Cagney", 1),
  ("Jackie Chan",1),
 ("Claudette Colbert",0),
 ("Sean Connery",1),
 ("Gary Cooper", 1),
( "Joan Crawford", 0),
 ( "Bette Davis", 0),
 ("Doris Day",0),
 ("Robert De Niro", 1),
 ("Alain Delon", 1),
 ("Marlene Dietrich",0),
 ("Clint Eastwood",1),
 ( "Henry Fonda", 1),
 ("Jean Gabin", 1),
  ("Clark Gable",1),
( "Greta Garbo",0),
 ( "Judy Garland",0),
 ("John Gielgud",1),
( "Lillian Gish",0),
 ("Cary Grant",1),
( "Alec Guinness",1),
(  "Tom Hanks",1),
( "Setsuko Hara",0),
 ("Rita Hayworth",0),
 ("Audrey Hepburn",0),
 ("Katharine Hepburn",0),
 ( "Grace Kelly",0),
( "Klaus Kinski",1),
( "Vivien Leigh",0),
( "Sophia Loren",0),
 ("Madhubala", 0),
 ("Marcello Mastroianni", 1),
 ("Toshiro Mifune", 1),
 ("Marilyn Monroe", 0),
 ("Jeanne Moreau", 0),
 ("Jack Nicholson", 1),
 ("Laurence Olivier", 1),
 ("Peter O'Toole", 1),
 ("Gregory Peck", 1),
 ("Mary Pickford", 0),
 ("Sidney Poitier", 1),
 ("Rajinikanth", 1),
 ("Barbara Stanwyck", 0),
 ("James Stewart", 1),
 ("Meryl Streep", 0),
  ("Elizabeth Taylor", 0),
 ("Shirley Temple", 0),
 ("Spencer Tracy", 1),
 ("Rudolph Valentino", 1),
 ("John Wayne", 1),
 ("Mae West", 0)]

all_actor_names = [a_tup[0] for a_tup in a_list]

actor_list = []

for item in directory.iterdir():
    if item.is_file():
        with item.open() as f:
            content = f.read()
            index_all_actor_names = all_actor_names.index(item.name[:len(item.name)-4])
            a_name = all_actor_names[index_all_actor_names]
            a_gender = a_list[index_all_actor_names]
            spacy_o = nlp(content)
            nltk_o = nltk.word_tokenize(content)
            actor_list.append(actor(a_name, a_gender, content, spacy_o, nltk_o))
            break

print(actor_list[0].title)
print(actor_list[0].gender)
