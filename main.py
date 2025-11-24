class Placement_Eligibility_Calculator:
    def __init__(s):
        s.company_types = {
            "Super Dream Companies (30LPA+)": {"criteria": {"12th_percentage": 75,"jee_percentile": 80,"min_gpa": 9.0,"package": "30 LPA","description": "Top-tier companies with best packages"}},
            "Super Dream Companies (20LPA+)": {"criteria": {"12th_percentage": 75,"jee_percentile": 75,"min_gpa": 8.5,"package": "20 LPA","description": "Premium companies with excellent packages"}},
            "Dream Companies (15LPA+)": {"criteria": {"12th_percentage": 75,"jee_percentile": 75,"min_gpa": 8.0,"package": "15 LPA","description": "Big companies with great opportunities"}},
            "Decent Companies (10LPA+)": {"criteria": {"12th_percentage": 75,"jee_percentile": 75,"min_gpa": 7.5,"package": "10 LPA","description": "Decent companies with considerable packages"}},
            "General Companies (8LPA+)": {"criteria": {"12th_percentage": 70,"jee_percentile": 75,"min_gpa": 7.0,"package": "8 LPA","description": "random recruitment and decent packages "}},
            "Mass Recruitment with Training Companies (5LPA)": {"criteria": {"12th_percentage": 70,"jee_percentile": 70,"min_gpa": 0,"package": "5 LPA + 3 months training","description": "Companies offering training and skill development programs"}}
        }

        s.companies_list = {
            "Super Dream Companies (30LPA+)": ["Google", "Microsoft", "Amazon", "Meta",
                "Goldman Sachs"],
            "Super Dream Companies (20LPA+)": ["Adobe", "Intel", "NVIDIA", "Oracle", "JP Morgan"],
            "Dream Companies (15LPA+)": ["Infosys", "TCS", "Wipro", "HCL", "Tech Mahindra","Accenture", "Cognizant", "Capgemini"],
            "Decent Companies (10LPA+)": ["L&T Infotech", "Mindtree", "Mphasis", "Hexaware","Persistent Systems", "Coforge", "Zensar"],
            "General Companies (8LPA+)": ["TCS Ninja", "Infosys System Engineer", "Wipro Turbo","HCL Tech Bee", "Tech Mahindra GET"],
            "Mass Recruitment with Training Companies (5LPA)": ["TCS Ignite", "Infosys Springboard", "Wipro WILP","HCL Career Development", "Tech Mahindra Elevate"]
        }

    def input_from_user(s):
        print("\nPlacement Eligibility Calculator")
        try:
            twelfth_percentage = float(input("Enter your 12th percentage: "))
            jee_percentile = float(input("Enter your JEE percentile: "))

            print("\nEnter your GPA for each year (0-10 scale):")
            year_1_gpa = float(input("1st Year GPA: "))
            year_2_gpa = float(input("2nd Year GPA: "))
            year_3_gpa = float(input("3rd Year GPA: "))
            year_4_gpa = float(input("4th Year GPA: "))

            return {'twelfth_percentage': twelfth_percentage,'jee_percentile': jee_percentile,'year_gpas': [year_1_gpa, year_2_gpa, year_3_gpa, year_4_gpa]}
        except ValueError:
            print("Please enter valid numerical values!")
            return None

    def eligibility_calculation(s, student_info):
        _12th = student_info['twelfth_percentage']
        JEE = student_info['jee_percentile']
        gpas = student_info['year_gpas']
        min_gpa = min(gpas)

        eligible_categories = []

        if _12th <= 70 or JEE <= 70:
            return []

        for category_name, criteria in s.company_types.items():
            cat_criteria = criteria["criteria"]

            if category_name == "Mass Recruitment with Training Companies (5LPA)":
                if min_gpa < 7.0:
                    eligible_categories.append(category_name)
                continue


            if (_12th >= cat_criteria["12th_percentage"] and
                    JEE >= cat_criteria["jee_percentile"] and
                    min_gpa >= cat_criteria["min_gpa"]):
                eligible_categories.append(category_name)

        return eligible_categories

    def generate_performa(s, student_info, eligible_categories):


        print("PLACEMENT ELIGIBILITY PERFORMA")


        print(f"\n STUDENT ACADEMIC DETAILS:")
        print(f"   12th Percentage: {student_info['twelfth_percentage']}%")
        print(f"   JEE Percentile: {student_info['jee_percentile']}%ile")
        print(f"   1st Year GPA: {student_info['year_gpas'][0]}")
        print(f"   2nd Year GPA: {student_info['year_gpas'][1]}")
        print(f"   3rd Year GPA: {student_info['year_gpas'][2]}")
        print(f"   4th Year GPA: {student_info['year_gpas'][3]}")
        print(f"   Minimum GPA: {min(student_info['year_gpas'])}")


        print(f"\n ELIGIBILITY STATUS:")
        if not eligible_categories:
            print("  Not eligible for campus placements")
            print("  Improvement Areas:")
            if student_info['twelfth_percentage'] < 75:
                print("     - 12th percentage should be ≥ 75%")
            if student_info['jee_percentile'] < 75:
                print("     - JEE percentile should be ≥ 75%")
            return

        print(f"    Eligible for {len(eligible_categories)} category/categories")


        print(f"\n ELIGIBLE COMPANY CATEGORIES:")
        for i, category in enumerate(eligible_categories, 1):
            criteria = s.company_types[category]["criteria"]
            companies = s.companies_list[category]

            print(f"\n   {i}. {category}")
            print(f"      Package: {criteria['package']}")
            print(f"      Description: {criteria['description']}")
            print(f"      Companies: {', '.join(companies[:3])}...")


    def run_calculator(s):
        while True:
            student_data = s.input_from_user()

            if student_data is None:
                continue


            eligible_categories = s.eligibility_calculation(student_data)


            s.generate_performa(student_data, eligible_categories)


            print("\n")
            choice = input("\nDo you want to check another student? (y/n): ").lower()
            if choice != 'y':
                print("Thank you for using Placement Eligibility Calculator! ")
                break



def welcome_message():
    print(" Welcome to the Placement Eligibility Calculator ")
    print("\nThis tool will help you determine:")
    print("• Which company categories you're eligible for")
    print("• Expected salary packages")
    print("• Specific companies in each category")


def main():
    welcome_message()

    calculator = Placement_Eligibility_Calculator()
    calculator.run_calculator()


if __name__ == "__main__":
    main()