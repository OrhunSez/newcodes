from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Title with user name
        self.set_font('Arial', 'B', 18)
        self.set_text_color(0, 51, 102)  # Dark blue
        self.cell(0, 10, "Orhun Sezgin", ln=True, align='L')
        self.set_font('Arial', 'I', 12)
        self.cell(0, 10, "Computer Engineering Student - A learner who enjoys life", ln=True, align='L')
        self.ln(10)
        
    def footer(self):
        # Footer with page number
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        # Create section title
        self.set_font('Arial', 'B', 14)
        self.set_text_color(0, 51, 102)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, text):
        # Body of each section
        self.set_font('Arial', '', 12)
        self.set_text_color(0)
        self.multi_cell(0, 10, text)
        self.ln()

# Instantiate the PDF
pdf = PDF()

# Add the first page
pdf.add_page()

# Contact information (on the left, as per the template)
pdf.set_font("Arial", 'B', 12)
pdf.set_text_color(255, 255, 255)
pdf.set_fill_color(0, 51, 102)  # Dark blue
pdf.cell(0, 10, "Contact Information", ln=True, fill=True)

# Insert the contact information below the title
pdf.set_text_color(0)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, "Izmir, Turkey 35040\nPhone: +90 551 971 8206\nE-mail: orhunsez@gmail.com\n\n")

# Links section
pdf.set_text_color(255, 255, 255)
pdf.set_fill_color(0, 51, 102)
pdf.cell(0, 10, "Links", ln=True, fill=True)
pdf.set_text_color(0)
pdf.multi_cell(0, 10, "LinkedIn: www.linkedin.com/in/orhun-sezgin\nGitHub: https://github.com/OrhunSez\n\n")

# Skills section
pdf.set_text_color(255, 255, 255)
pdf.set_fill_color(0, 51, 102)
pdf.cell(0, 10, "Skills", ln=True, fill=True)
pdf.set_text_color(0)
skills = [
    "C1 English & A1 German", "Computer Science & Calculus & Physics", "Algorithm Design & Problem-Solving", "Fast Learner",
    "Self-Motivation", "Project Coordination & Team Collaboration", " "
]
pdf.multi_cell(0, 10, "\n".join(skills))

# Work history section
pdf.chapter_title("Work History")
pdf.chapter_body(
    "Freelance Coding (TradingBot) | Freelance, Izmir (Remote) | Nov 2023 - Mar 2024\n"
    "- Enhanced client satisfaction by delivering high-quality work within deadlines.\n"
    "- Adapted quickly to changing project requirements, demonstrating flexibility under pressure.\n"
    "- Collaborated with a group while coding.\n"
    "\n"
    "Host | Random Employers, Izmir, Turkey | Jun 2024 - Oct 2024\n"
    "- Provided exceptional customer service by addressing guest needs and concerns.\n"
    "- Solved unexpected problems efficiently.\n"
    "\n"
    "Ticket Reader | Inka Agency, Izmir, Turkey | Jun 2024 - Sept 2024\n"
    "- Professionally welcomed VIP guests and managed high-pressure situations.\n"
    "- Kept a calm demeanor while addressing guest inquiries."
)

# Education section
pdf.chapter_title("Education")
pdf.chapter_body(
    "Computer Engineering (No Degree) | Ege University, Izmir, Turkey | Expected Graduation: July 2027\n"
    "- 3.3 Current GPA\n- Completed coursework: FreeCodeCamp, Udemy, YouTube (Coding) Courses since 2019\n"
    "\n"
    "High School Diploma | Buca Science High School, Izmir, Turkey | Graduated: June 2023\n"
    "- 98.7% Average\n- Played for class volleyball & basketball teams\n- Class President (9th & 10th grade)"
)

# Hobbies section
pdf.chapter_title("Hobbies")
hobbies = [
    "Guitar and basketball since 6th grade",
    "Table tennis since high school",
    "Bodybuilding since 2 years"
]
pdf.chapter_body("\n".join(hobbies))

# Save the redesigned PDF to your system
pdf_output_path_v2 = "Orhun_Sezgin_Resume_Improved.pdf"
pdf.output(pdf_output_path_v2)

# Confirm the output path
pdf_output_path_v2
