#!/usr/bin/env python

from subprocess import call
import shutil,os,argparse,sys


# How it works:
# 1. Create a tex document with necessary configurations
# 2. Compile the tex to create the pdf
# 3. Trim the pdf margins to get only the figure

class CustomParser(argparse.ArgumentParser):

    def error(self, message):
        sys.stderr.write('\033[91mError: %s\n\033[0m' % message)
        self.print_help()
        sys.exit(2)



def createParser():
    #main parser
    parser = CustomParser(prog="onefig",formatter_class=argparse.RawTextHelpFormatter,
                          description="A tool for merging multiple figures into one.")

    #adding options for numerical jobs
    parser.add_argument("--ifile",'-i',nargs='+',type=str,help="Input files",metavar="FILE",required=True)
    parser.add_argument('--ofile','-o',type=str,required=True,help="Output file name",metavar="FILE")
    parser.add_argument('--per_row','-pr',help="Number of figure in one row (default: %(default)s)",metavar='PR',default=2,type=int)
    parser.add_argument('--index-type','-it',nargs='?',choices=['b','t','n'],default='b',help="Where to put the caption (default: %(default)s)",metavar='IT')
    parser.add_argument('--width','-w',help="Width of each figure (default: %(default)s)",default=0.46,metavar='WIDTH',type=float)
    parser.add_argument('--vspace','-v',help="Verticle space between rows in cm (default: %(default)s)",default=0.3,metavar='VSPACE',type=float)
    parser.add_argument('--rotate','-r',help="Rotate figure (default: %(default)s)",default=0,metavar='ROTATE',type=float)

    return parser.parse_args()


def main():
    args = createParser()
    createPdf(args)


def createPdf(args):
    destDir = 'tmp_pdfmerger'
    os.makedirs(destDir,exist_ok=True)

    for file in args.ifile:
        shutil.copy(file, destDir)

    os.chdir(destDir)
    tex = createTeX(args)
    # print(tex)
    with open('test.tex','w') as f:

        f.write(tex)

    with open('tmp.log','a') as f:
        ret = call(['pdflatex','test.tex'],stdout=f)

        call(['pdfcrop','test.pdf','../{}'.format(args.ofile)],stdout=f)

    os.chdir('../')
    shutil.rmtree(destDir)




def createTeX(args):
    figType={
        'b':r'\subfloat[]',
        't':r'\sidesubfloat[]',
        'n':r'\subfloat'
    }
    thisFig = figType[args.index_type]
    inOneRow=args.per_row
    fig = ''
    assert (1.0/inOneRow)>args.width, "Width {} is too large to fit {} figure in one row".format(args.width,inOneRow)

    for ind,elem in enumerate(args.ifile,start=1):
        fig += thisFig+r'{\includegraphics[width=\imsize,angle='+str(args.rotate)+']{'+elem+'}}'
        fig += r'\\\vspace{'+str(args.vspace)+'cm}' if not ind%inOneRow else r"\hfill"
        fig +='\n'
    
    figWidth = r"\newcommand{\imsize}{"+str(args.width)+r"\textwidth}"
    return r'''
    \documentclass[a4,12pt]{article}
    \usepackage[a4paper,margin=0in]{geometry}

    \usepackage{subfig}
    \usepackage{graphicx}
    \usepackage{multirow} 
    \usepackage{floatrow}

    \thispagestyle{empty}
    %\graphicspath{{../}}


    \captionsetup[subfigure]{justification=raggedright,farskip=12pt,captionskip=12pt,position=auto,labelfont=bf}
    \floatsetup[figure]{style=plain,subcapbesideposition=top}

    '''+figWidth+r'''
    \begin{document}

    \begin{figure}[!htp]
    \centering


    '''+fig+r'''\end{figure}\end{document}'''


if __name__ =="__main__":
    main()
