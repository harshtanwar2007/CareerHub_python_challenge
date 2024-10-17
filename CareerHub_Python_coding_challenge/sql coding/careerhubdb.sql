CREATE DATABASE CareerHubDB
USE CareerHubDB


CREATE TABLE Companies (
    CompanyID INT PRIMARY KEY IDENTITY(1,1),
    CompanyName NVARCHAR(255) NOT NULL,
    Location NVARCHAR(255) NOT NULL
);
INSERT INTO Companies (CompanyID, CompanyName, Location) VALUES
(1, 'Tech Innovators Inc.', 'San Francisco, CA'),
(2, 'Health Solutions LLC', 'New York, NY'),
(3, 'Green Energy Corp.', 'Austin, TX'),
(4, 'FinTech Services', 'Chicago, IL'),
(5, 'Creative Designs Studio', 'Los Angeles, CA');


CREATE TABLE Jobs (
    JobID INT PRIMARY KEY IDENTITY(1,1),
    CompanyID INT NOT NULL,
    JobTitle NVARCHAR(255) NOT NULL,
    JobDescription NVARCHAR(MAX) NOT NULL,
    JobLocation NVARCHAR(255) NOT NULL,
    Salary DECIMAL(10, 2) NOT NULL CHECK (Salary >= 0),
    JobType NVARCHAR(50) NOT NULL,
    PostedDate DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID) ON DELETE CASCADE
);
INSERT INTO Jobs (JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)
VALUES
( 'Software Engineer', 'Develop and maintain software applications.', 'New York, NY', 95000.00, 'Full-Time', '2024-10-10'),
( 'Data Analyst', 'Analyze and interpret complex data sets.', 'San Francisco, CA', 70000.00, 'Full-Time', '2024-10-12'),
( 'Marketing Manager', 'Manage and execute marketing strategies.', 'Chicago, IL', 85000.00, 'Full-Time', '2024-10-08'),
( 'Project Manager', 'Oversee project planning and execution.', 'Los Angeles, CA', 90000.00, 'Full-Time', '2024-10-15'),
( 'UI/UX Designer', 'Design user interfaces and user experiences.', 'Austin, TX', 80000.00, 'Part-Time', '2024-10-09');


CREATE TABLE Applicants (
    ApplicantID INT PRIMARY KEY IDENTITY(1,1),
    FirstName NVARCHAR(255) NOT NULL,
    LastName NVARCHAR(255) NOT NULL,
    Email NVARCHAR(255) NOT NULL UNIQUE,
    Phone NVARCHAR(50) NOT NULL,
    Resume NVARCHAR(255) NOT NULL
);
INSERT INTO Applicants (FirstName, LastName, Email, Phone, Resume)
VALUES
('John', 'Doe', 'john.doe@example.com', '555-1234', 'Resume for John Doe...'),
('Jane', 'Smith', 'jane.smith@example.com', '555-5678', 'Resume for Jane Smith...'),
('Mark', 'Johnson', 'mark.johnson@example.com', '555-9101', 'Resume for Mark Johnson...'),
('Emily', 'Clark', 'emily.clark@example.com', '555-1122', 'Resume for Emily Clark...'),
('Robert', 'Brown', 'robert.brown@example.com', '555-3344', 'Resume for Robert Brown...');

CREATE TABLE JobApplications (
    ApplicationID INT PRIMARY KEY IDENTITY(1,1),
    JobID INT NOT NULL,
    ApplicantID INT NOT NULL,
    ApplicationDate DATETIME DEFAULT GETDATE(),
    CoverLetter NVARCHAR(MAX) NOT NULL,
    FOREIGN KEY (JobID) REFERENCES Jobs(JobID) ON DELETE CASCADE,
    FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID) ON DELETE CASCADE
);
INSERT INTO JobApplications ( ApplicantID, ApplicationDate, CoverLetter)
VALUES
( 1, '2024-10-12', 'I am interested in the Software Engineer position because...'),
( 2, '2024-10-13', 'I am excited to apply for the Data Analyst position as...'),
( 3, '2024-10-14', 'The Marketing Manager role aligns with my experience...'),
( 4, '2024-10-15', 'I am eager to join as a Project Manager and contribute...'),
( 5, '2024-10-16', 'The UI/UX Designer position is perfect for my skills...');

select * from jobs
drop table Jobs
