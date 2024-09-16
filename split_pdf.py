import os
import fitz  # PyMuPDF

def split_pdf(input_pdf_path, output_folder):
    # Ensure that the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Open the PDF
    pdf_document = fitz.open(input_pdf_path)

    # Split the PDF into multiple single-page files
    for page_num in range(len(pdf_document)):
        # Create a new PDF document with a single page
        single_page_pdf = fitz.open()
        single_page_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

        # Generate the name of the output file
        output_pdf_path = os.path.join(output_folder, f"page_{page_num + 1}.pdf")

        # Save the individual page to a new PDF file
        single_page_pdf.save(output_pdf_path)
        single_page_pdf.close()

    # Close the original document
    pdf_document.close()

if __name__ == "__main__":
    input_pdf_path = "C:/Users/"  # Replace with the path to your PDF file
    output_folder = "C:/Users/"  # Replace with the path where the single-page PDFs will be saved
    for filename in os.listdir(input_pdf_path):
        if filename.endswith(".pdf"):
            input_pdf_path = os.path.join(input_pdf_path, filename)
            split_pdf(input_pdf_path, output_folder)
