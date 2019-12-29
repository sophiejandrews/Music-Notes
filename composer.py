import operator

Composers = sorted(['Bach','Beethoven', 'Brahms', 'Byrd','Chopin', 'Debussy', 'Handel', 'Haydn', 'Liszt', 'Mozart', 'Mendelssohn','Saint-Saens', 'Scarlatti','Schubert', 'Schumann', 'Tchaikovsky', 'Telemann', 'Vivaldi', 'Wagner'])

year = {}

year['Bach']= 1685
year['Beethoven']= 1770 # 1782 - 1826
year['Brahms']= 1833
year['Byrd']= 1540
year['Chopin']= 1810
year[ 'Debussy']= 1862
year['Handel']= 1685
year['Haydn']= 1732  # 1760 - 1801
year['Liszt']= 1811
year['Mendelssohn']= 1809
year['Mozart']= 1756  # 1739 - 1791
year['Saint-Saens']= 1835
year['Scarlatti']= 1685
year['Schubert']= 1797
year['Schumann']= 1810
year['Tchaikovsky']= 1840
year['Telemann']= 1681
year['Vivaldi']= 1678
year['Wagner']= 1813

Composers_Birthyear = [x for (x,y) in sorted(year.items(), key = operator.itemgetter(1))]

map = {}
whole = ['C','D','E','F','G','A','B']
for n in whole:
    for oct in [-1,0,1,2,3,4,5,6,7,8,9]:
        note = n+str(oct)
        map[note] = note

half = ['C#','D-','D#','E-','E#','F-','F#','G-','G#','A-','A#','B-']
map['C#']='C#D-'
map['D-']='C#D-'
map['D#']='D#E-'
map['E-']='D#E-'
map['E#']='F'
map['F-']='E'
map['F#']='F#G-'
map['G-']='F#G-'
map['G#']='G#A-'
map['A-']='G#A-'
map['A#']='A#B-'
map['B-']='A#B-'

for n in half:
    for oct in [-1,0,1,2,3,4,5,6,7,8,9]:
        note = n+str(oct)
        map[note]=map[n]+str(oct)

Alphabet = []
for oct in [-1,0,1,2,3,4,5,6,7,8,9]:
    for n in ['C','C#D-', 'D','D#E-','E','F','F#G-','G','G#A-','A','A#B-','B']:
        Alphabet.append(n+str(oct))

