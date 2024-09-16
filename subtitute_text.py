import os
import subprocess
import aspose.pdf as ap

def replace_text_in_pdf(input_path, output_path, search_text, replacement_text):
    # Load the PDF document
    document = ap.Document(input_path)
    
    # Instantiate a TextFragmentAbsorber object
    txtAbsorber = ap.text.TextFragmentAbsorber(search_text)
    
    # Search text
    document.pages.accept(txtAbsorber)
    
    # Get reference to the found text fragments
    textFragmentCollection = txtAbsorber.text_fragments
    
    # Parse all the searched text fragments and replace text
    for txtFragment in textFragmentCollection:
        txtFragment.text = replacement_text
    
    # Save the updated PDF
    document.save(output_path)

def process_pdfs_in_folder(folder_path, search_text, replacement_text):
    output_folder = os.path.join(folder_path, "modified_pdfs")
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, filename)
            replace_text_in_pdf(input_path, output_path, search_text, replacement_text)
            run_substitute_script(output_path)

def run_substitute_script(pdf_path):
    search_text = "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2024 Aspose Pty Ltd."
    replacement_text = " "
    output_temp_path = pdf_path.replace(".pdf", "_temp.pdf")
    
    command = [
        "python",
        "delete_text.py",
        "--input", pdf_path,
        "--search", search_text,
        "--replace", replacement_text,
        "--output", output_temp_path
    ]
    
    try:
        subprocess.run(command, check=True)
        os.replace(output_temp_path, pdf_path)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

if __name__ == "__main__":
    folder_path = "C:/Users/"  # Put here your working folder path
    search_text = "Text to find" # Put here the text you want to replace
    replacement_text = "Text to replace" # Put here the text you want to put
    process_pdfs_in_folder(folder_path, search_text, replacement_text)
    print("Document text changed succesfully!")
