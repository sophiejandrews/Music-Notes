# count_notes()
#
# input: all pieces for all composers, e.g. Bach/Bach*.txt 
# output:  Bach/Bach_count_notes.csv 
#	   count_notes.csv (comparable to count_1gram.csv, 
#	                    but not sorted by count/freq, but in order of notes in octive)
#	   count_weightednotes.csv
# No cdf for counting notes
#
# compute_entropy(c_list, style_list)
# input: Bach/Bach_count_1gram.csv

import os
import composer
import csv
import math
import numpy

import parse_meta

composerlist = composer.Composers 
year = composer.year
alphabet = composer.Alphabet
map = composer.map

weighted = 0
'''
composerlist=['Mozart']
year1='1739'
year2='1749'
'''

#composerlist=['Bach']
year1=''
year2=''

inst=''
genre=''

total = {}
count = {}

def count_notes():
    for c in composerlist:
        total[c] = 0
        count[c] = {}
        for n in alphabet:
            count[c][n]=0

    if weighted ==0:
        f = 'countnotes_'
    if weighted ==1:
        f = 'countweightednotes_'
    if len(composerlist)==1:
        f += ''+composerlist[0]
    if year1 != '':
        f += 'After'+year1
    if year2 != '':
        f += 'Before'+year2
    if inst != '':
        f += inst
    if genre != '':
        f += genre

    print('--',f)

    # temp: a list of files with composer c
    for c in composerlist:
        if c== composerlist[0]: 
            command = 'ls '+c+'/'+c+'*.txt > temp'
        else:
            command = 'ls '+c+'/'+c+'*.txt >> temp'
        os.system(command)

    allpieces = open('temp', encoding='Latin-1')
    whichpieces = parse_meta.whichpieces(composerlist, year1, year2, inst, genre)
    
    if whichpieces == []:
        print('empty set')
        return


    for ll in allpieces:
        piece = ll.strip()
        if piece not in whichpieces: continue

        c = piece.split('/')[0]
        file = open(piece, 'r')

        for line in file:
            notes = line.split(',')[1].strip().split('.')
            duration = line.split(',')[0].strip()

        if weighted == 0:
            for n in notes:
                if n not in map:
                    print(n, "not in map")
                    continue
                n = map[n]
                count[c][n] += 1
                total[c] += 1
            if weighted == 1:
                if duration!='last':
                    duration = float(duration)
                    for n in notes:
                        if n not in map:
                            print(n, "not in map")
                            continue
                        n = map[n]
                        count[c][n] += duration
                        total[c] += duration

count_notes()

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

def plot_sharpflat_trend():
    fig = plt.figure(figsize = (20,8))

    #y: fraction of flats and sharps  (saved in sharpflat_fraction.xlsx)
    y = [0.073692492,0.195217825,0.224292851,0.228037103,0.253901307,0.275995948,0.283227583,0.288856066,0.293506037,0.300104018,0.301648847,0.315581263,0.344571417,0.34853654,0.357052559,0.419005056,0.441692994,0.453079867]

    x=range(len(y))
    my_xticks = ['Byrd','Telemann','Handel','Vivaldi','Mozart','Bach','Beethoven','Saint-Saens','Haydn','Wagner','Mendelssohn','Schubert','Schumann','Brahms','Tchaikovsky','Liszt','Chopin','Debussy']

    ax = fig.add_subplot(1,1,1)
    ax.set_xticks(x)
    ax.set_xticklabels(my_xticks)
    
    [t.set_color(i) for (t,i) in zip(ax.xaxis.get_ticklabels(), ['m','g','g','g','b','g', 'b','r','b','r','r','r','r','r','r','r','r','k'])]
    
    for tick in ax.xaxis.get_ticklabels():
        tick.set_fontsize('large')


    plt.xticks(x, my_xticks, rotation = '30')
    plt.title('Fraction of sharps and flats')
    plt.plot(x, y)
    
    # Byrd
    plt.plot([0],[y[0]], 'mo', markersize=10) 
    
    # Baroque
    for i in [1,2,3,5]:
        plt.plot([i],[y[i]], 'go', markersize=10) 

    # classic
    for i in [4,6,8]:
        plt.plot([i],[y[i]], 'bo', markersize=10)

    # romantic
    for i in [7,9,10,11,12,13,14,15,16]:
        plt.plot([i], [y[i]], 'ro',markersize=10)
     
    # impressionist
    plt.plot([17],[y[17]], 'ko', markersize=10)

    plt.savefig('sharpflat_fraction.png')
    plt.close()

#plot_sharpflat_trend()
def plot_firstlast10years():
    first10=[0.25851691,0.310137972,0.34555331,0.390382262,0.327930175,0.20818659,0.2757175,0.45137354,0.329666868,0.202136044,0.197866813,0.329384988,0.352718366,0.348125666,0.186695279,0.247231693,0.203429314]

    last10=[0.401719551,0.336717711,0.415298058,0.483327352,0.495316053,0.247400326,0.294952458,0.524822237,0.294966389,0.261805379,0.304556672,0.337233049,0.316159848,0.314431098,0.224324324,0.304093332,0.447300132]
     
    plt.figure(figsize = (20,7))
    x = range(len(first10))
    bar_width = 0.3
    opacity = 0.8
    
    plt.bar([xx+0.25 for xx in x], first10, bar_width,
            alpha=opacity,
            color='b',
            label='first 10 years')
    
    plt.bar([xx + +0.25+bar_width for xx in x], last10, bar_width,
            alpha=opacity,
            color='r',
            label='last 10 years')
    
    plt.title('Fraction of sharps and flats')

    my_xticks = ['Bach', 'Beethoven', 'Brahms', 'Chopin', 'Debussy', 'Handel','Haydn','Liszt','Mendelssohn','Mozart','Saint-Saens','Schubert','Schumann','Tchaikovsky','Telemann','Vivaldi','Wagner']

    plt.xticks([xx+0.5 for xx in x], my_xticks, rotation = 30)
    plt.legend()
    
    plt.tight_layout()
     
    plt.savefig('firstlast10years.png')
    plt.close()

def plots():
    for c in composerlist:
        print('temp', c)
        if total[c] == 0: continue

        t = c 
        if weighted==1:
            t += ' weighted '
        if year1 != '':
            t += ' After '+year1
        if year2 != '':
            t += ' Before '+year2
        if inst != '':
            t += ' '+ inst
        if genre != '':
            t += ' '+ genre

        ab =  alphabet[alphabet.index('C2'):alphabet.index('B6')+1]
        x = range(len(ab))
        y = []
        for n in ab:
            y.append(count[c][n])

        my_xticks = ab
            
        plt.figure(figsize = (20,7))
        plt.xticks(x, my_xticks, rotation = 'vertical')
        plt.title(t)
        plt.plot(x, y)
        
        for i in x:
            if '#' in ab[i] or '-' in ab[i]:
                plt.plot([i],[y[i]], 'ro') 

        plt.savefig('countnotes_'+t.replace(' ','')+'.png')
        plt.close()

        # compute % sharp/flat notes
        all = 0
        sharpflat = 0
        for i in x:
            all += y[i]
            if '#' in ab[i] or '-' in ab[i]:
                sharpflat += y[i]
    print('done plots')
     
plots()    
    
def compute_entropy(c_list,style_list):
    if len(c_list) == 1:
        if weighted == 0:
            file = open(c_list[0]+'_noteentropy.csv', 'w')
        if weighted == 1:
            file = open(c_list[0]+'_weightednoteentropy.csv', 'w')
        style_list = ['']+style_list  # for computing overall entropy
    elif len(style_list) == 1:
        if weighted == 0:
            file = open(style_list[0]+'_noteentropy.csv', 'w')
        if weighted == 1:
            file = open(style_list[0]+'_weightednoteentropy.csv', 'w')
    else:
        print("one composer, or one style")

    for c in c_list:
        for s in style_list:
            total[c] = 0
            count[c] = {}
            for n in alphabet:
                count[c][n] = 0

            count_notes_c_s(c,s)
            entropy = 0
            for n in alphabet:
                if count[c][n]>0:
                    entropy += 1.0*count[c][n]/total[c]*numpy.log2(1.0*count[c][n]/total[c])
            print(c, s, entropy)
               
            file.write(c+','+s+','+str(entropy)+'\n')
	
