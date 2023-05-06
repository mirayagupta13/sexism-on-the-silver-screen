#seeing if there are any immediate differences w vader sentiment analysis

female_scores = [('Audrey Hepburn',
  {'compound': 1.0, 'neg': 0.063, 'neu': 0.786, 'pos': 0.151}),
 ('Barbara Stanwyck',
  {'compound': 0.9999, 'neg': 0.067, 'neu': 0.786, 'pos': 0.147}),
 ('Bette Davis', {'compound': 1.0, 'neg': 0.078, 'neu': 0.784, 'pos': 0.138}),
 ('Brigitte Bardot',
  {'compound': 0.9999, 'neg': 0.057, 'neu': 0.803, 'pos': 0.141}),
 ('Claudette Colbert',
  {'compound': 0.9999, 'neg': 0.058, 'neu': 0.78, 'pos': 0.162}),
 ('Doris Day', {'compound': 1.0, 'neg': 0.054, 'neu': 0.794, 'pos': 0.152}),
 ('Elizabeth Taylor',
  {'compound': 0.9999, 'neg': 0.071, 'neu': 0.812, 'pos': 0.116}),
 ('Grace Kelly', {'compound': 1.0, 'neg': 0.03, 'neu': 0.843, 'pos': 0.127}),
 ('Greta Garbo', {'compound': 0.9999, 'neg': 0.069, 'neu': 0.8, 'pos': 0.131}),
 ('Ingrid Bergman', {'compound': 1.0, 'neg': 0.072, 'neu': 0.777, 'pos': 0.15}),
 ('Jeanne Moreau',
  {'compound': 0.9972, 'neg': 0.035, 'neu': 0.863, 'pos': 0.102}),
 ('Joan Crawford',
  {'compound': 0.9998, 'neg': 0.075, 'neu': 0.813, 'pos': 0.112}),
 ('Judy Garland', {'compound': 1.0, 'neg': 0.07, 'neu': 0.814, 'pos': 0.116}),
 ('Julie Andrews', {'compound': 1.0, 'neg': 0.031, 'neu': 0.835, 'pos': 0.134}),
 ('Katharine Hepburn',
  {'compound': 1.0, 'neg': 0.069, 'neu': 0.764, 'pos': 0.167}),
 ('Lauren Bacall',
  {'compound': 0.9998, 'neg': 0.048, 'neu': 0.841, 'pos': 0.111}),
 ('Lillian Gish',
  {'compound': 0.9998, 'neg': 0.053, 'neu': 0.83, 'pos': 0.117}),
 ('Madhubala', {'compound': 1.0, 'neg': 0.058, 'neu': 0.826, 'pos': 0.116}),
 ('Mae West', {'compound': 0.9997, 'neg': 0.069, 'neu': 0.829, 'pos': 0.102}),
 ('Marilyn Monroe',
  {'compound': 0.9992, 'neg': 0.092, 'neu': 0.804, 'pos': 0.104}),
 ('Marlene Dietrich',
  {'compound': 0.9999, 'neg': 0.059, 'neu': 0.817, 'pos': 0.125}),
 ('Mary Pickford',
  {'compound': 0.9999, 'neg': 0.055, 'neu': 0.825, 'pos': 0.12}),
 ('Meryl Streep', {'compound': 1.0, 'neg': 0.067, 'neu': 0.755, 'pos': 0.178}),
 ('Rita Hayworth',
  {'compound': 0.9744, 'neg': 0.088, 'neu': 0.821, 'pos': 0.091}),
 ('Sarah Bernhardt',
  {'compound': 1.0, 'neg': 0.072, 'neu': 0.812, 'pos': 0.116}),
 ('Setsuko Hara',
  {'compound': 0.9621, 'neg': 0.053, 'neu': 0.877, 'pos': 0.07}),
 ('Shirley Temple',
  {'compound': 0.9999, 'neg': 0.047, 'neu': 0.831, 'pos': 0.122}),
 ('Sophia Loren',
  {'compound': 0.9999, 'neg': 0.04, 'neu': 0.796, 'pos': 0.165}),
 ('Vivien Leigh',
  {'compound': 0.9995, 'neg': 0.099, 'neu': 0.779, 'pos': 0.121})]

male_scores = [('Alain Delon', {'compound': 0.9999, 'neg': 0.058, 'neu': 0.81, 'pos': 0.132}),
 ('Alec Guinness',
  {'compound': 0.9998, 'neg': 0.062, 'neu': 0.794, 'pos': 0.144}),
 ('Amitabh Bachchan',
  {'compound': 1.0, 'neg': 0.059, 'neu': 0.787, 'pos': 0.155}),
 ('Cary Grant', {'compound': 1.0, 'neg': 0.072, 'neu': 0.726, 'pos': 0.202}),
 ('Clark Gable',
  {'compound': 0.9999, 'neg': 0.081, 'neu': 0.802, 'pos': 0.117}),
 ('Clint Eastwood', {'compound': 1.0, 'neg': 0.08, 'neu': 0.771, 'pos': 0.149}),
 ('Gary Cooper', {'compound': 1.0, 'neg': 0.067, 'neu': 0.757, 'pos': 0.177}),
 ('Gregory Peck', {'compound': 1.0, 'neg': 0.081, 'neu': 0.764, 'pos': 0.156}),
 ('Henry Fonda', {'compound': 0.9997, 'neg': 0.082, 'neu': 0.798, 'pos': 0.12}),
 ('Humphrey Bogart',
  {'compound': 0.9999, 'neg': 0.102, 'neu': 0.767, 'pos': 0.13}),
 ('Jack Nicholson',
  {'compound': 0.9999, 'neg': 0.077, 'neu': 0.779, 'pos': 0.143}),
 ('Jackie Chan', {'compound': 1.0, 'neg': 0.071, 'neu': 0.795, 'pos': 0.134}),
 ('James Cagney', {'compound': 1.0, 'neg': 0.077, 'neu': 0.79, 'pos': 0.133}),
 ('James Stewart', {'compound': 1.0, 'neg': 0.081, 'neu': 0.773, 'pos': 0.147}),
 ('Jean Gabin', {'compound': 0.996, 'neg': 0.042, 'neu': 0.869, 'pos': 0.089}),
 ('John Gielgud', {'compound': 1.0, 'neg': 0.068, 'neu': 0.782, 'pos': 0.15}),
 ('John Wayne', {'compound': 0.9999, 'neg': 0.081, 'neu': 0.801, 'pos': 0.118}),
 ('Klaus Kinski',
  {'compound': -0.9994, 'neg': 0.137, 'neu': 0.788, 'pos': 0.075}),
 ('Laurence Olivier',
  {'compound': 1.0, 'neg': 0.073, 'neu': 0.775, 'pos': 0.152}),
 ('Marcello Mastroianni',
  {'compound': 0.9998, 'neg': 0.048, 'neu': 0.766, 'pos': 0.186}),
 ('Marlon Brando',
  {'compound': 0.9999, 'neg': 0.092, 'neu': 0.79, 'pos': 0.119}),
 ("Peter O'Toole",
  {'compound': 0.9999, 'neg': 0.053, 'neu': 0.813, 'pos': 0.134}),
 ('Rajinikanth', {'compound': 1.0, 'neg': 0.043, 'neu': 0.822, 'pos': 0.135}),
 ('Robert De Niro', {'compound': 1.0, 'neg': 0.08, 'neu': 0.773, 'pos': 0.147}),
 ('Rudolph Valentino',
  {'compound': 0.9994, 'neg': 0.086, 'neu': 0.808, 'pos': 0.106}),
 ('Sean Connery',
  {'compound': 0.9999, 'neg': 0.062, 'neu': 0.818, 'pos': 0.121}),
 ('Sidney Poitier', {'compound': 1.0, 'neg': 0.05, 'neu': 0.764, 'pos': 0.186}),
 ('Spencer Tracy', {'compound': 1.0, 'neg': 0.08, 'neu': 0.784, 'pos': 0.136}),
 ('Tom Hanks', {'compound': 1.0, 'neg': 0.042, 'neu': 0.812, 'pos': 0.147}),
 ('Toshiro Mifune',
  {'compound': 0.9996, 'neg': 0.054, 'neu': 0.818, 'pos': 0.128})]

woman_count = 0
female_compound = 0
female_neg = 0
female_neu = 0
female_pos = 0

for actor in female_scores:
    woman_count += 1
    female_compound += actor[1]['compound']
    female_neg += actor[1]['neg']
    female_neu += actor[1]['neu']
    female_pos += actor[1]['pos']

female_avgs = (female_compound/woman_count, female_neg/woman_count,
                female_neu/woman_count, female_pos/woman_count)

man_count = 0
male_compound = 0
male_neg = 0
male_neu = 0
male_pos = 0

for actor in male_scores:
    man_count += 1
    male_compound += actor[1]['compound']
    male_neg += actor[1]['neg']
    male_neu += actor[1]['neu']
    male_pos += actor[1]['pos']

male_avgs = (male_compound/man_count, male_neg/man_count,
                male_neu/man_count, male_pos/man_count)

print(f'female compound, neg, neu, pos = {female_avgs}')
print(f'male compound, neg, neu, pos = {male_avgs}')