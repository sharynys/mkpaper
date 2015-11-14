# MkPaper                                                                                                                            
Python library for compiling a PDF or Word doc of Figures                                                                            
Dependencies
============                                                                                                                         
* python                                                                                                                             
* pdflatex (optional)

Without pdflatex, the package still works (you can create the tex file and not compile). Requires figures to be in pdf format.

Installation
============                     

git clone https://github.com/chrisb13/mkpaper.git

Usage
============
See examples/example_mkpaper_pdf.py

In summary, though:
```
import mkpaper as mp

#get a list of your figures in PDF format...
import glob
ifiles=sorted(glob.glob('/path/to/plots/' + '*.pdf' ))
assert(ifiles!=[]),"glob didn't find anything!"

#instantiate LatexFigureDoc class:
#arguments are: path/to/put/figuredocs and name of figure doc..
figobj=mp.LatexFigureDoc('/home/nfs/username/examplemkpaper/','testname')

#for each figure pass the path and a caption
figobj.add_figure(ifiles[0],'fig1')
figobj.add_figure(ifiles[1],'fig2')
figobj.add_figure(ifiles[2],'fig3')
#etc

#insert the tail of the doc
figobj.end_tex()

#send build command to pdflatex, this step actually requires pdflatex on the machine
figobj.build_tex()
```

Acknowledgements
================

The code was written by Christopher Bull.

Contact
=======

Christopher Bull.                                                               
Affiliation: Climate Change Research Centre and ARC Centre of Excellence for Climate Sys    tem Science.
     Level 4, Mathews Building                                        
     University of New South Wales                                    
     Sydney, NSW, Australia, 2052                                     
Contact: z3457920@student.unsw.edu.au                                         
www:     christopherbull.com.au                                               
twitter: @ChrisBullOceanO                
