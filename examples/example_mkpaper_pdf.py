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
Example script of how to use mkpaper (pdflatex)

Things to change (see init box):
    1] path to mkpaper package (it's the folder CONTAINING mkpaper, e.g. should be /folder_containing_mkpaper/ NOT /folder_containing_mkpaper/mkpaper/ )
    2] path to pdf plots  (optional: pending how you cloned)
    3] path to pdf output (optional: pending how you cloned)
"""

###########################################################################
#                INIT -- CHANGE me to make script work....                #
###########################################################################
path_to_mkpaper='/home/nfs/z3457920/hdrive/repos/' #note: it's the folder CONTAINING mkpaper

#IF you cloned to a repo NOT called 'mkpaper' you need to change these lines...
path_to_pdfplots=path_to_mkpaper+'mkpaper/examples/figs/' 
path_to_pdf=path_to_mkpaper+'mkpaper/examples/examplemkpaper/'

###########################################################################
#                                INIT END                                 #
###########################################################################

import sys,os
sys.path.insert(1,path_to_mkpaper)

import mkpaper as mp
import glob

if __name__ == "__main__": 
    #get a list of your figures in PDF format...
    ifiles=sorted(glob.glob(path_to_pdfplots + '*.pdf' ))
    assert(ifiles!=[]),"glob didn't find anything!"

    #alternatively, we could be more explicit
    #ifile[0]=path_to_pdf+'penguin1.pdf'
    #ifile[1]=path_to_pdf+'penguin2.pdf'

    #instantiate LatexFigureDoc class:
    #arguments are: path/to/put/figuredocs and name of figure doc..
    figobj=mp.LatexFigureDoc(path_to_pdf,'penguinfigs')
    figobj.add_figure(ifiles[0],'first penguin')
    figobj.add_figure(ifiles[1],'second penguin')
    #etc

    #insert the tail of the doc
    figobj.end_tex()
    #send build command to pdflatex, this step actually requires pdflatex on the machine
    figobj.build_tex()
