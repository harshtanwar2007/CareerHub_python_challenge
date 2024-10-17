import pyodbc
from entity.JobListing import JobListing
from entity.Company import Company
from entity.Applicant import Applicant
from entity.JobApplication import JobApplication
from dao.JobBoardDAO import JobBoardDAO
from dao.DBConnection import DBConnection
from exception.DatabaseConnectionException import DatabaseConnectionException
from exception.NegativeSalaryException import NegativeSalaryException

class JobBoardDAOImpl(JobBoardDAO):
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect_to_db()
    
    def connect_to_db(self):
        try:
            self.connection = DBConnection.get_connection()
            self.cursor = self.connection.cursor()
            print("Database connection established.")
        except DatabaseConnectionException as e:
            raise DatabaseConnectionException(f"Error connecting to the database: {e}")

    def insert_applicant(self, applicant: Applicant):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Applicants (FirstName, LastName, Email, Phone, Resume) VALUES (?, ?, ?, ?, ?)",
                        (applicant.first_name, applicant.last_name, applicant.email, applicant.phone, applicant.resume))
            self.connection.commit()
            print("Applicant inserted successfully.")
        except Exception as e:
            print(f"Error inserting applicant: {e}")


    def insert_company(self, company: Company):
        try:
            self.cursor.execute("""
                INSERT INTO Companies (CompanyName, Location) 
                VALUES (?, ?)
            """, (company.company_name, company.location))  # Exclude CompanyID
            self.connection.commit()  # Commit the transaction to save changes
            print("Company inserted successfully!")
        except Exception as e:
            print(f"Error inserting company: {e}")


    def insert_job_listing(self, job_title, company_id, job_description, job_location, salary, job_type):
        if salary < 0:
            raise NegativeSalaryException("Salary cannot be negative.")
        try:
            self.cursor.execute("""
                INSERT INTO Jobs (CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType) 
                VALUES (?, ?, ?, ?, ?, ?)
            """, (company_id, job_title, job_description, job_location, salary, job_type))
            self.connection.commit()
            print("Job listing posted successfully!")
        except Exception as e:
            print(f"Error posting job listing: {e}")


    def apply_for_job(self, job_application):
        try:
            sql = """INSERT INTO JobApplications (ApplicantID, JobID, CoverLetter, ApplicationDate)
                    VALUES (?, ?, ?, ?)"""
            self.cursor.execute(sql, (job_application.applicant_id, job_application.job_id, job_application.cover_letter, job_application.application_date))
            self.connection.commit()
        except Exception as e:
            print(f"Error inserting job application: {e}")



    def get_applicants(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Applicants")
            rows = cursor.fetchall()
            return [Applicant(applicant_id=row[0], first_name=row[1], last_name=row[2], email=row[3], phone=row[4], resume=row[5]) for row in rows]
        except Exception as e:
            print(f"Error retrieving applicants: {e}")
            return []

    def get_companies(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Companies")
            rows = cursor.fetchall()
            return [Company(company_id=row[0], company_name=row[1], location=row[2]) for row in rows]
        except Exception as e:
            print(f"Error retrieving companies: {e}")
            return []

    def retrieve_job_listings(self):
        sql = "SELECT JobID, JobTitle, CompanyID, JobDescription, JobLocation, Salary, JobType FROM Jobs"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        
        job_listings = []
        for row in rows:
            job = JobListing(
                job_id=row[0],
                job_title=row[1],
                company_id=row[2],
                job_description=row[3],
                job_location=row[4],
                salary=row[5],
                job_type=row[6]
            )
            job_listings.append(job)
        return job_listings




    def get_job_applications(self):
        try:
            self.cursor.execute("SELECT ApplicationID, ApplicantID, JobID, CoverLetter, ApplicationDate FROM JobApplications")
            job_applications = []
            rows = self.cursor.fetchall()
            
            for row in rows:
                application_id = row[0]
                applicant_id = row[1]
                job_id = row[2]
                cover_letter = row[3]
                application_date = row[4]  # Ensure you are retrieving the application date
                
                # Create a JobApplication object with all the required fields
                job_application = JobApplication(
                    application_id=application_id, 
                    applicant_id=applicant_id, 
                    job_id=job_id, 
                    cover_letter=cover_letter, 
                    application_date=application_date  # Pass the application_date
                )
                
                job_applications.append(job_application)
            
            return job_applications
        
        except Exception as e:
            print(f"Error retrieving job applications: {e}")


    def search_job_listings_by_salary_range(self, min_salary, max_salary):
        try:
            query = "SELECT j.JobID, j.JobTitle, j.CompanyID, j.JobDescription, j.JobLocation, j.Salary, j.JobType, c.CompanyName " \
                    "FROM Jobs j " \
                    "JOIN Companies c ON j.CompanyID = c.CompanyID " \
                    "WHERE j.Salary BETWEEN ? AND ?"
            self.cursor.execute(query, (min_salary, max_salary))
            rows = self.cursor.fetchall()
            
            job_listings = []
            for row in rows:
                job_listing = JobListing(
                    job_id=row.JobID,
                    job_title=row.JobTitle,
                    company_id=row.CompanyID,
                    job_description=row.JobDescription,
                    job_location=row.JobLocation,
                    salary=row.Salary,
                    job_type=row.JobType,
                    company_name=row.CompanyName
                )
                job_listings.append(job_listing)
            return job_listings
        except Exception as e:
            print(f"Error searching job listings: {e}")
            return []



    def close_connection(self):
        try:
            if self.connection:
                self.connection.close()
                print("Database connection closed.")
        except Exception as e:
            print(f"Error closing connection: {e}")
