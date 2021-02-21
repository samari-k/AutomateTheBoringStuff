##! /usr/bin/env python3

# Description:
#   Simple PDF Merger inspired by the book 'Automate The Boring Stuff' by Al Sweigart.
#   Merges the given two files into a new one, called 'mergedFile.pdf'.
#
# Usage:
#   ./pdfMerger.py {file1.pdf} {file2.pdf}
#
# Author: samari-k
# Version: 1.0

import sys, logging
import PyPDF2

# init logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(message)s')
# (un)comment the next line to disable/enable debug logging messages
# logging.disable(logging.DEBUG)

# check if commandline arguments were passed
if len(sys.argv) > 2:
    logging.debug('Found two or more arguments.')

    # open pdfs
    pdf1 = open(sys.argv[1], 'rb')
    pdf2 = open(sys.argv[2], 'rb')
    logging.debug('opened PDF files.')

    # init readers and writer
    reader1 = PyPDF2.PdfFileReader(pdf1)
    reader2 = PyPDF2.PdfFileReader(pdf2)
    writer = PyPDF2.PdfFileWriter()
    logging.debug('initialised readers and writer.')

    # concatenate all pages
    for pageNum in range(reader1.numPages):
        page = reader1.getPage(pageNum)
        writer.addPage(page)
    for pageNum in range(reader2.numPages):
        page = reader2.getPage(pageNum)
        writer.addPage(page)
    logging.debug('concatenated both files.')

    # write merged PDF to new file
    outputFile = open('mergedFile.pdf', 'wb')
    writer.write(outputFile)
    outputFile.close()
    logging.debug('wrote merged PDFs to output file.')
else:
    logging.error('You need to specify two PDFs to merge!')
