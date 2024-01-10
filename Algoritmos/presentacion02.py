import docx

# Load the DOCX file
doc_path = "UD6_DisenoDeAlgoritmos.docx"
doc = docx.Document(doc_path)

# Function to check if a paragraph is a section title (assuming titles are bold)
def is_section_title(paragraph):
    if paragraph.runs and paragraph.runs[0].bold:
        return True
    return False

# Initialize the array to store sections
sections = []

# Iterate through the paragraphs to extract section titles and their content
current_section = {}
for para in doc.paragraphs:
    if is_section_title(para):
        # If there is a current section being processed, add it to sections list
        if current_section:
            sections.append(current_section)
            if len(sections) == 19:  # Stop after 19 sections
                break

        # Start a new section
        current_section = {"title": para.text, "context": "", "requirements": "", "instructions": "", "complexity": {"temporal": "", "spatial": ""}}
    else:
        # Continue adding content to the current section
        # For simplicity, all content is added to 'context'; this can be adjusted
        if current_section:
            current_section["context"] += para.text + " "

# Add the last section if it exists
if current_section and len(sections) < 19:
    sections.append(current_section)

print(sections)

