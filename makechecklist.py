#!/usr/bin/env python
import os
import sys
import re

# makechecklist.py: a quick parser for a specifically-formatted LaTeX file
# that produces a nice checklist in {longtable} for the entire list.
# The list is, or should be, larger than the number of cells on any one 
# bingo card, so a canonical list of the cells is useful when evaluating any
# one card.
#
# Jesse Hamner, 2016

# Functions:

def make_entry(one_pair, indexval):
    """
    Take a nicely formatted variable (string) and write it into a LaTeX
    [long]table cell
    """
    one_pair[0] = re.sub('\\\\myItems{', "", one_pair[0])
    one_pair[1] = re.sub('\\\\myItems{', "", one_pair[1])
    # choice_menu = str("\\CheckBox[checkboxsymbol=\\ding{53}, ")
    choice_menu = str("\\CheckBox[")
    

    tabline = choice_menu + str("name=checkbox" + str(indexval) + "]{} & " + one_pair[0] + " &")

    if re.search('}', one_pair[1] ):
        tabline += str("\\\\[\\sep]\n")
        return tabline
    iv1 = str(indexval + 1)
    tabline += choice_menu + str(", name=checkbox" + iv1 + "]{} & " + one_pair[1] )
    tabline += str(f"\\\\[\\sep]\n")
    return tabline


def slurp_in_file(fn, theList):
    """
    Open an input file, parse it, ignore some fields, and nicely format the
    remainder of the file into a long text string of LaTeX tabular fields.
    """
    f=open(fn, 'r')
    li=f.read()
    grr = li.split('\n')
    for i in range(0, len(grr), 2):
        mline=['','']
        if( re.search('^%|^\s*$', grr[i]) ):
            mline[0] = '' 
        elif( re.search('^%|^\s*$', grr[i+1]) ):
            mline[1] = ''
        
        try:
            mline[0] = re.sub(';', '', grr[i])
        except:
            pass
#            print (mline)
        try:    
            mline[1] = re.sub(';', '', grr[i+1])
        except:
            pass
        
        theList += make_entry(mline, i)

            #for j in mline:
            #    if re.match('^\s*$', j):
            #        continue
            #    j = re.sub('\\\\myItems{', "", j)
            #    theList = theList + make_entry(mline)
        if (re.match('\s*}\s*$', grr[i]) ):
            return(theList)
        elif (re.match('\s*}\s*$', grr[i+1]) ):
            return(theList)
        else:
            continue


    return 0

# Main loop:

filename="bingoquestions.tex"
nicetable="% Hopefully a nice table\n\n"
nicetable = slurp_in_file(filename, nicetable)

# write out the table to a file:

ofile="checklist.tex"
output=open(ofile, 'w')
output.write(nicetable)
output.close()

# let user know: 

print(f'Wrote output to {ofile}')

# EOF
