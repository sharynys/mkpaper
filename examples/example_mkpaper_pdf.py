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
Example script of how to use mkpaper

Things to change (see init box):
    1] path to mkpaper package
    2] path to pdf plots
    3] path to pdf output
"""

###########################################################################
#                INIT -- CHANGE me to make script work....                #
###########################################################################
path_to_mkpaper='~/hdrive/repos/'
path_to_pdfplots='/srv/ccrc/data42/z3457920/20141202_leeuwincurrent_revision1_001/paper_qual_plots2/'
path_to_pdf='/home/nfs/z3457920/hdrive/repos/examplemkpaper/'

###########################################################################
#                                INIT END                                 #
###########################################################################

import sys,os
sys.path.insert(1,os.path.expanduser(path_to_mkpaper))

import mkpaper as mp
import glob

#import ipdb; ipdb.set_trace()

if __name__ == "__main__": 

    #glob your files...
    ifiles=sorted(glob.glob(path_to_pdfplots + '*.pdf' ))
    assert(ifiles!=[]),"glob didn't find anything!"

    figobj=mp.LatexFigureDoc('/home/nfs/z3457920/hdrive/repos/examplemkpaper/','testname')
    figobj.add_figure(ifiles[0],'fig1')
    figobj.add_figure(ifiles[1],'fig2')
    figobj.add_figure(ifiles[2],'fig3')
    #etc
    figobj.end_tex()
    figobj.build_tex()

