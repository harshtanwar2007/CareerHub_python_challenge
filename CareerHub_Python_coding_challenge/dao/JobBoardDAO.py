from abc import ABC, abstractmethod
from entity.Applicant import Applicant
from entity.Company import Company
from entity.JobListing import JobListing
from entity.JobApplication import JobApplication

class JobBoardDAO(ABC):

    @abstractmethod
    def insert_applicant(self, applicant: Applicant):
        pass

    @abstractmethod
    def insert_company(self, company: Company):
        pass

    @abstractmethod
    def insert_job_listing(self, job_listing: JobListing):
        pass

    @abstractmethod
    def apply_for_job(self, applicant_id: int, job_id: int, cover_letter: str):
        pass

    @abstractmethod
    def get_applicants(self):
        pass

    @abstractmethod
    def get_companies(self):
        pass

    @abstractmethod
    def retrieve_job_listings(self):
        pass

    @abstractmethod
    def get_job_applications(self):
        pass

    @abstractmethod
    def search_job_listings_by_salary_range(self, min_salary: float, max_salary: float):
        pass

    @abstractmethod
    def close_connection(self):
        pass

    def apply_for_job(self, job_application):
        pass