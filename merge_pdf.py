import os
import fitz  # PyMuPDF

def merge_pdfs(input_folder, output_pdf_path):
    # Create a new PDF document where the files will be merged
    merged_pdf = fitz.open()

    # Iterate through all PDF files in the input folder
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".pdf"):
            file_path = os.path.join(input_folder, filename)
            # Open each PDF file
            pdf_document = fitz.open(file_path)
            # Insert all the pages of the PDF into the merged document
            merged_pdf.insert_pdf(pdf_document)
            # Close the current PDF file
            pdf_document.close()

    # Save the combined PDF file
    merged_pdf.save(output_pdf_path)
    merged_pdf.close()

if __name__ == "__main__":
    input_pdf_path = "C:/Users/"  # Replace with the path to your PDF files
    output_folder = "C:/Users/merged.pdf"  # Replace with the path where the merged PDF will be saved
    merge_pdfs(input_pdf_path, output_folder)
