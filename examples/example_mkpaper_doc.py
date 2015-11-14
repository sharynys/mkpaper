#   Author: Christopher Bull. 
#   Affiliation: Climate Change Research Centre and ARC Centre of Excellence for Climate System Science.
#                Level 4, Mathews Building
#                University of New South Wales
#                Sydney, NSW, Australia, 2052
#   Contact: z3457920@student.unsw.edu.au
#   www:     christopherbull.com.au
#   Date created: Fri, 13 Nov 2015 14:01:53
#   Machine created on: ccrc165
#

"""
Example script of how to use mkpaper (word doc)

Requires python-docx package.

Things to change (see init box):
    1] path to mkpaper package
    2] path to png plots (pending how you cloned)
    3] path to doc output (pending how you cloned)
"""

###########################################################################
#                INIT -- CHANGE me to make script work....                #
###########################################################################
path_to_mkpaper='/home/nfs/z3457920/hdrive/repos/'

#IF you cloned to a repo NOT called 'mkpaper' you need to change these lines...
path_to_pngplots=path_to_mkpaper+'mkpaper/examples/figs/' 
path_to_doc=path_to_mkpaper+'mkpaper/examples/examplemkpaper/'

###########################################################################
#                                INIT END                                 #
###########################################################################

import sys,os
sys.path.insert(1,path_to_mkpaper)

import mkpaper as mp
import glob

if __name__ == "__main__": 
    #get a list of your figures in PNG format...
    ifiles=sorted(glob.glob(path_to_pngplots + '*.png' ))
    assert(ifiles!=[]),"glob didn't find anything!"

    #alternatively, we could be more explicit
    #ifile[0]=path_to_doc+'penguin1.png'
    #ifile[1]=path_to_doc+'penguin2.png'

    #instantiate WordFigureDoc class:
    #arguments are: path/to/put/figuredocs and name of figure doc..
    figobj=mp.WordFigureDoc(path_to_doc,'penguinfigs')
    figobj.add_figure(ifiles[0],'first penguin')
    figobj.add_figure(ifiles[1],'second penguin')
    #etc

    #insert the tail of the doc
    figobj.end_doc()
