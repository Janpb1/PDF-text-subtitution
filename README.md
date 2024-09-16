# PDF Text Substituter, Splitter, and Merger

This project provides three main functionalities for working with PDF files:
1. **PDF Text Substitution**: Replace specific text within PDF files.
2. **PDF Splitter**: Split a multi-page PDF into individual single-page PDF files.
3. **PDF Merger**: Merge multiple PDF files into one single PDF.

## Features

### 1. PDF Text Substitution
- Replace specified text in a PDF file with a new string of text. This functionality is especially useful for updating specific phrases or headers in multiple PDFs at once.

### 2. PDF Splitter
- Splits a multi-page PDF file into multiple single-page PDFs. Each page will be saved as a separate PDF file, making it easier to manage or extract individual pages.

### 3. PDF Merger
- Combines multiple PDF files from a folder into a single PDF document. This is useful when you want to merge multiple reports, pages, or sections into one file.

## Dependencies

This project requires the following dependencies:
- **Python 3.6+**
- **[PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)** (`fitz`) for working with PDFs.

### Install Dependencies
To install the required dependencies, run:
```bash
pip install PyMuPDF
