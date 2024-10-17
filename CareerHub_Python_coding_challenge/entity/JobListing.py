class JobListing:
    def __init__(self, job_id, job_title, company_id, job_description, job_location, salary, job_type, company_name=None):
        self.job_id = job_id
        self.job_title = job_title
        self.company_id = company_id
        self.job_description = job_description
        self.job_location = job_location
        self.salary = salary
        self.job_type = job_type
        self.company_name = company_name 
