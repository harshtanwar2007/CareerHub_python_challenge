from dao.JobBoardDAOImpl import JobBoardDAOImpl
from entity.Applicant import Applicant
from entity.Company import Company
from entity.JobListing import JobListing
from entity.JobApplication import JobApplication
from exception.DatabaseConnectionException import DatabaseConnectionException
from exception.NegativeSalaryException import NegativeSalaryException

def display_menu():
    print("Job Board Application")
    print("1. Insert Applicant")
    print("2. Insert Company")
    print("3. Insert Job Listing")
    print("4. Insert Job Application")
    print("5. View All Applicants")
    print("6. View All Job Listings")
    print("7. View All Job Applications")
    print("8. View All Companies")
    print("9. Search Job Listings by Salary Range")
    print("10. Exit")

def main():
    dao = JobBoardDAOImpl()
    
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            # Insert Applicant
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            resume = input("Enter resume: ")

            applicant = Applicant(applicant_id=None, first_name=first_name, last_name=last_name, email=email, phone=phone, resume=resume)
            try:
                dao.insert_applicant(applicant)  # Insert the applicant into the database
            except Exception as e:
                print(f"Error inserting applicant: {e}")

        elif choice == "2":
            company_name = input("Enter company name: ")
            location = input("Enter company location: ")
            company = Company(company_id=None, company_name=company_name, location=location)  # Use None for new companies
            try:
                dao.insert_company(company)  # Insert the company into the database
            except Exception as e:
                print(f"Error inserting company: {e}")

        elif choice == "3":
            # Insert Job Listing
            job_title = input("Enter job title: ")
            while True:
                try:
                    company_id = int(input("Enter company ID: "))
                    if company_id < 0:
                        raise ValueError("Company ID cannot be negative.")
                    break
                except ValueError as e:
                    print(e)

            job_description = input("Enter job description: ")
            job_location = input("Enter job location: ")
            
            while True:
                try:
                    salary = float(input("Enter salary: "))
                    if salary < 0:
                        raise ValueError("Salary cannot be negative.")
                    break
                except ValueError as e:
                    print(e)

            job_type = input("Enter job type: ")
            try:
                dao.insert_job_listing(job_title, company_id, job_description, job_location, salary, job_type)
            except Exception as e:
                print(f"Error posting job listing: {e}")

        elif choice == "4":
            # Insert Job Application
            while True:
                try:
                    applicant_id = int(input("Enter applicant ID: "))
                    if applicant_id < 0:
                        raise ValueError("Applicant ID cannot be negative.")
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    job_id = int(input("Enter job ID: "))
                    if job_id < 0:
                        raise ValueError("Job ID cannot be negative.")
                    break
                except ValueError as e:
                    print(e)

            cover_letter = input("Enter cover letter: ")

            # Get the application date
            application_date = input("Enter application date (YYYY-MM-DD): ")

            # Create the JobApplication object with the application_date
            job_application = JobApplication(
                application_id=None, 
                applicant_id=applicant_id, 
                job_id=job_id, 
                cover_letter=cover_letter, 
                application_date=application_date
            )

            try:
                dao.apply_for_job(job_application)  # Apply for the job
                print("Application added successfully.")  # Success message
            except Exception as e:
                print(f"Error applying for job: {e}")



        elif choice == "5":
            # View All Applicants
            try:
                applicants = dao.get_applicants()
                if applicants:
                    for applicant in applicants:
                        print(f"ID: {applicant.applicant_id}, Name: {applicant.first_name} {applicant.last_name}, Email: {applicant.email}")
                else:
                    print("No applicants found.")
            except Exception as e:
                print(f"Error retrieving applicants: {e}")

        elif choice == "6":
            # View All Job Listings
            try:
                job_listings = dao.retrieve_job_listings()
                if job_listings:
                    for job in job_listings:
                        print(f"Job ID: {job.job_id}, CompanyID: {job.company_id} Title: {job.job_title}, Salary: {job.salary}")
                else:
                    print("No job listings found.")
            except Exception as e:
                print(f"Error retrieving job listings: {e}")

        elif choice == "7":
            # View All Job Applications
            try:
                applications = dao.get_job_applications()
                if applications:
                    for application in applications:
                        print(f"Application ID: {application.application_id}, Job ID: {application.job_id}, Applicant ID: {application.applicant_id}")
                else:
                    print("No job applications found.")
            except Exception as e:
                print(f"Error retrieving job applications: {e}")

        elif choice == "8":
            # View All Companies
            try:
                companies = dao.get_companies()
                if companies:
                    for company in companies:
                        print(f"Company ID: {company.company_id}, Name: {company.company_name}, Location: {company.location}")
                else:
                    print("No companies found.")
            except Exception as e:
                print(f"Error retrieving companies: {e}")

        elif choice == "9":
            # Search Job Listings by Salary Range
            while True:
                try:
                    min_salary = float(input("Enter minimum salary: "))
                    if min_salary < 0:
                        raise ValueError("Minimum salary cannot be negative.")
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    max_salary = float(input("Enter maximum salary: "))
                    if max_salary < 0:
                        raise ValueError("Maximum salary cannot be negative.")
                    break
                except ValueError as e:
                    print(e)

            try:
                job_listings = dao.search_job_listings_by_salary_range(min_salary, max_salary)
                if job_listings:
                    for job in job_listings:
                        print(f"Job ID: {job.job_id}, Title: {job.job_title}, Company: {job.company_name}, Salary: {job.salary}")
                else:
                    print("No job listings found in this salary range.")
            except Exception as e:
                print(f"Error searching job listings: {e}")

        elif choice == "10":
            if input("Are you sure you want to exit? (y/n): ").lower() == 'y':
                print("Exiting the application.")
                break

        else:
            print("Invalid choice. Please try again.")

    dao.close_connection()

if __name__ == "__main__":
    main()
