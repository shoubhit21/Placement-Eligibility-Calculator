# Placement Eligibility Calculator

A Python-based application that determines student eligibility for campus placements based on academic performance. The calculator evaluates 12th percentage, JEE percentile, and yearly GPAs to provide personalized placement opportunities.

##  Features

- **Academic Evaluation**: Analyzes 12th percentage, JEE percentile, and GPA scores
- **Company Categorization**: Classifies companies into 6 different tiers based on package offers
- **Eligibility Calculation**: Determines which company categories a student qualifies for
- **Detailed Report**: Generates comprehensive placement eligibility performa
- **User-Friendly Interface**: Simple command-line interface with clear prompts

##  Company Categories

| Category | 12th % | JEE %ile | Min GPA | Package | Example Companies |
|----------|--------|----------|---------|---------|-------------------|
| Super Dream (30LPA+) | ≥75 | ≥80 | ≥9.0 | 30 LPA+ | Google, Microsoft, Amazon |
| Super Dream (20LPA+) | ≥75 | ≥75 | ≥8.5 | 20 LPA+ | Adobe, Intel, NVIDIA |
| Dream (15LPA+) | ≥75 | ≥75 | ≥8.0 | 15 LPA+ | Infosys, TCS, Wipro |
| Decent (10LPA+) | ≥75 | ≥75 | ≥7.5 | 10 LPA+ | L&T Infotech, Mindtree |
| General (8LPA+) | ≥70 | ≥75 | ≥7.0 | 8 LPA+ | TCS Ninja, Infosys SE |
| Mass Recruitment (5LPA) | ≥70 | ≥70 | <7.0 | 5 LPA + Training | TCS Ignite, Wipro WILP |

## Installation & Usage 
  1.	Install and run Python 3 and create a project in it
  2.	Navigate to the project directory
  3.	Run the application:
  python placement_calculator.py
## Sample Input :
  Enter your 12th percentage: 85.5
  Enter your JEE percentile: 82.3
  
  Enter your GPA for each year (0-10 scale):
  1st Year GPA: 9.2
  2nd Year GPA: 9.0
  3rd Year GPA: 8.8
  4th Year GPA: 9.1
## Output Example 
  PLACEMENT ELIGIBILITY PERFORMA
  
   STUDENT ACADEMIC DETAILS:
     12th Percentage: 85.5%
     JEE Percentile: 82.3%ile
     1st Year GPA: 9.2
     2nd Year GPA: 9.0
     3rd Year GPA: 8.8
     4th Year GPA: 9.1
     Minimum GPA: 8.8

   ELIGIBILITY STATUS:
      Eligible for 2 category/categories
  
   ELIGIBLE COMPANY CATEGORIES:
   1. Super Dream Companies (20LPA+)
        Package: 20 LPA
        Description: Premium companies with excellent packages
        Companies: Adobe, Intel, NVIDIA...

## Project Structure
  •	Placement_Eligibility_Calculator Class: Main class handling all operations
  •	input_from_user(): Collects student academic data
  •	eligibility_calculation(): Determines eligible company categories
  •	generate_performa(): Creates detailed eligibility report
  •	run_calculator(): Main application loop
## Technical Details
  •	Language: Python 3.x
  •	Dependencies: None (pure Python)
  •	Architecture: Object-oriented with dictionary-based criteria storage
  •	Interface: Command-line with user-friendly prompts
## Use Cases
  •	Students: Understand placement opportunities and improvement areas
  •	Placement Cells: Quick eligibility assessment for counseling
  •	Educational Institutions: Academic planning and placement preparation
## Customization
  Easily modify company criteria and lists by updating the dictionaries in the __init__ method:
  •	company_types: Eligibility criteria for each category
  •	companies_list: Actual company names for each category
## Limitations
  •	Basic input validation only
  •	No data persistence between sessions
  •	Command-line interface only
  •	Fixed criteria 


