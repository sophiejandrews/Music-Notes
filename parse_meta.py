######
#
# readfile()
#
# Input: YCAC-metadata1.csv
# Output:  firstlast10 year of each composer
#         whichpieces: filter based on composer, begin/end years, instrument, genre
#
#####

import csv
import os

def whichpieces(comp,year1,year2,inst,genre):
    print(comp, year1, year2, inst, genre)

    whichpieces = []
    with open('YCAC-metadata1.csv',encoding='Latin-1') as csvfile:
        filedic = csv.DictReader(csvfile, delimiter=',')

        for line in filedic:
            if comp!='' and line['Composer'] not in comp: continue
            if year1!='':
                if line['Date']=='': continue
                if int(line['Date'])<int(year1): continue
            if year2!='':
                if line['Date']=='': continue
                if int(line['Date'])>int(year2): continue
            if inst!='' and inst!=line['Inst1']: continue
            if genre!='' and genre!=line['Genre']: continue

            c = line['Composer']
            name = c+'/'+c+'_'+line['Filename'].replace(' ', '-')+'.txt'
            whichpieces.append(name)

    return(whichpieces)

import composer
max={}
min= {}
def firstlast10():
    for c in composer.Composers:
        min[c] = 2000
        max[c] = 0
    with open('YCAC-metadata1.csv', encoding='Latin-1') as csvfile:
        filedic = csv.DictReader(csvfile, delimiter=',')
    
    for line in filedic:
        c = line['Composer']
        if c not in composer.Composers: continue
        
        if line['Date']=='':continue
        if int(line['Date'])>max[c]: max[c] = int(line['Date'])
        if int(line['Date'])<min[c]: min[c] = int(line['Date'])

    for c in composer.Composers:
        print('composerlist=[\''+c+'\']')
        print('year1=\''+str(min[c])+'\'')
        print('year2=\''+str(min[c]+10)+'\'')
        print()
        print('composerlist=[\''+c+'\']')
        print('year1=\''+str(max[c]-10)+'\'')
        print('year2=\''+str(max[c])+'\'')
        print()

