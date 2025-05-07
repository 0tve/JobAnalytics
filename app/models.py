from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Vacancy(Base):
    __tablename__ = "vacancies"

    accept_handicapped: Mapped[bool]
    accept_incomplete_resumes: Mapped[bool]
    accept_kids: Mapped[bool]
    accept_temporary: Mapped[Optional[bool]]
    allow_messages: Mapped[bool]
    alternate_url: Mapped[str]
    apply_alternate_url: Mapped[str]
    approved: Mapped[bool]
    archived: Mapped[bool]
    area: Mapped["Area"] = relationship(secondary="vacancies_areas", back_populates="vacancy")
    billing_type: Mapped[Optional["BillingType"]] = relationship(secondary="vacancies_billing_types", back_populates="vacancy")
    code: Mapped[Optional[str]]
    contacts: Mapped[Optional["Contacts"]] = relationship(secondary="vacancies_contacts", back_populates="vacancy")
    department: Mapped[Optional["Department"]] = relationship(secondary="vacancies_departments", back_populates="vacancy")
    description: Mapped[str]
    driver_license_types: Mapped[list["DriverLicenseType"]] = relationship(secondary="vacancies_driver_license_types", back_populates="vacancy")
    employer_for_applicant: Mapped[Optional["EmployerForApplicant"]] = relationship(secondary="vacancies_employers_for_applicant", back_populates="vacancy")
    employment_form: Mapped[Optional["EmploymentForm"]] = relationship(secondary="vacancies_employment_forms", back_populates="vacancy")
    experience: Mapped[Optional["Experience"]] = relationship(secondary="vacancies_experiences", back_populates="vacancy")
    fly_in_fly_out_duration: Mapped[Optional[list["FlyInFlyOutDuration"]]] = relationship(secondary="vacancies_fly_in_fly_out_durations", back_populates="vacancy")
    has_test: Mapped[bool]
    id: Mapped[str] = mapped_column(primary_key=True)
    initial_created_at: Mapped[str]
    insider_interview: Mapped[Optional["InsiderInterview"]] = relationship(secondary="vacancies_insider_interviews", back_populates="vacancy")
    internship: Mapped[Optional[bool]]
    key_skills: Mapped[list["KeySkill"]] = relationship(secondary="vacancies_key_skills", back_populates="vacancy")
    languages: Mapped[Optional[list["Language"]]] = relationship(secondary="vacancies_languages", back_populates="vacancy")
    name: Mapped[str]
    negotiations_url: Mapped[Optional[str]]
    night_shifts: Mapped[Optional[bool]]
    premium: Mapped[bool]
    professional_roles: Mapped[list["ProfessionalRole"]] = relationship(secondary="vacancies_professional_roles", back_populates="vacancy")
    published_at: Mapped[str]
    relations: Mapped[Optional[list[str]]] = mapped_column(ARRAY(String))
    response_letter_required: Mapped[bool]
    response_url: Mapped[Optional[str]]
    salary_range: Mapped[Optional["SalaryRange"]] = relationship(secondary="vacancies_salary_ranges", back_populates="vacancy")
    suitable_resumes_url: Mapped[Optional[str]]
    test: Mapped[Optional["Test"]] = relationship(secondary="vacancies_tests", back_populates="vacancy")
    type_: Mapped["Type"] = relationship(secondary="vacancies_types", back_populates="vacancy")
    vacancy_properties: Mapped[Optional["VacancyProperties"]] = relationship(secondary="vacancies_vacancy_properties", back_populates="vacancy")
    video_vacancy: Mapped[Optional["VideoVacancy"]] = relationship(secondary="vacancies_video_vacancies", back_populates="vacancy")
    work_format: Mapped[Optional[list["WorkFormat"]]] = relationship(secondary="vacancies_work_formats", back_populates="vacancy")
    work_schedule_by_days: Mapped[Optional[list["WorkScheduleByDays"]]] = relationship(secondary="vacancies_work_schedules_by_days", back_populates="vacancy")
    working_hours: Mapped[Optional[list["WorkingHours"]]] = relationship(secondary="vacancies_working_hours", back_populates="vacancy")
    address_for_applicant: Mapped[Optional["AddressForApplicant"]] = relationship(secondary="vacancies_addresses_for_applicant", back_populates="vacancy")


class VacancySearch(Base):
    __tablename__ = "vacancy_searches"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    vacancies_short: Mapped[list["VacancyShort"]] = relationship(secondary="vacancy_searches_vacancies_short", back_populates="vacancy_search")
    found: Mapped[int]
    page: Mapped[int]
    pages: Mapped[int]
    per_page: Mapped[int]
    clusters: Mapped[Optional[list["Cluster"]]] = relationship(secondary="vacancy_searches_clusters", back_populates="vacancy_search")
    arguments: Mapped[Optional[list["Argument"]]] = relationship(secondary="vacancy_searches_arguments", back_populates="vacancy_search")
    alternate_url: Mapped[Optional[str]]
    fixes: Mapped[Optional["Fixes"]] = relationship(secondary="vacancy_searches_fixes", back_populates="vacancy_search")
    suggests: Mapped[Optional["Suggests"]] = relationship(secondary="vacancy_searches_suggests", back_populates="vacancy_search")


class VacancyShort(Base):
    __tablename__ = "vacancies_short"
    
    accept_incomplete_resumes: Mapped[bool]
    accept_temporary: Mapped[Optional[bool]]
    address: Mapped[Optional["Address"]] = relationship(secondary="vacancies_short_addresses", back_populates="vacancy_short")
    alternate_url: Mapped[str]
    apply_alternate_url: Mapped[str]
    archived: Mapped[Optional[bool]]
    area: Mapped["Area"] = relationship(secondary="vacancies_short_areas", back_populates="vacancy_short")
    contacts: Mapped[Optional["Contacts"]] = relationship(secondary="vacancies_short_contacts", back_populates="vacancy_short")
    created_at: Mapped[Optional[str]]
    department: Mapped["Department"] = relationship(secondary="vacancies_short_departments", back_populates="vacancy_short")
    employer: Mapped["Employer"] = relationship(secondary="vacancies_short_employers", back_populates="vacancy_short")
    fly_in_fly_out_duration: Mapped[Optional[list["FlyInFlyOutDuration"]]] = relationship(secondary="vacancies_short_fly_in_fly_out_durations", back_populates="vacancy_short")
    has_test: Mapped[bool]
    id: Mapped[str] = mapped_column(primary_key=True)
    insider_interview: Mapped[Optional["InsiderInterview"]] = relationship(secondary="vacancies_short_insider_interviews", back_populates="vacancy_short")
    internship: Mapped[Optional[bool]]
    metro_stations: Mapped[Optional[list["MetroStation"]]] = relationship(secondary="vacancies_short_metro_stations", back_populates="vacancy_short")
    name: Mapped[str]
    night_shifts: Mapped[Optional[bool]]
    premium: Mapped[Optional[bool]]
    professional_roles: Mapped[list["ProfessionalRole"]] = relationship(secondary="vacancies_short_professional_roles", back_populates="vacancy_short")
    published_at: Mapped[str]
    relations: Mapped[Optional[list[str]]] = mapped_column(ARRAY(String))
    response_letter_required: Mapped[bool]
    response_url: Mapped[Optional[str]]
    salary_range: Mapped["SalaryRange"] = relationship(secondary="vacancies_short_salary_ranges", back_populates="vacancy_short")
    sort_point_distance: Mapped[Optional[int]]
    type_: Mapped["Type"] = relationship(secondary="vacancies_short_types", back_populates="vacancy_short")
    url: Mapped[str]
    work_format: Mapped[list["WorkFormat"]] = relationship(secondary="vacancies_short_work_formats", back_populates="vacancy_short")
    work_schedule_by_days: Mapped[list["WorkScheduleByDays"]] = relationship(secondary="vacancies_short_work_schedules_by_days", back_populates="vacancy_short")
    working_hours: Mapped[list["WorkingHours"]] = relationship(secondary="vacancies_short_working_hours", back_populates="vacancy_short")
    counters: Mapped["Counters"] = relationship(secondary="vacancies_short_counters", back_populates="vacancy_short")
    employment_form: Mapped["EmploymentForm"] = relationship(secondary="vacancies_short_employment_forms", back_populates="vacancy_short")
    experience: Mapped["Experience"] = relationship(secondary="vacancies_short_experiences", back_populates="vacancy_short")
    snippet: Mapped["Snippet"] = relationship(secondary="vacancies_short_snippets", back_populates="vacancy_short")
    show_logo_in_search: Mapped[Optional[bool]]
    video_vacancy: Mapped[Optional["VideoVacancy"]] = relationship(secondary="vacancies_short_video_vacancies", back_populates="vacancy_short")

    vacancy_search: Mapped["VacancySearch"] = relationship(secondary="vacancy_searches_vacancies_short", back_populates="vacancies_short")


class VacancySearchVacancyShort(Base):
    __tablename__ = "vacancy_searches_vacancies_short"
    
    vacancy_search_id: Mapped[int] = mapped_column(ForeignKey("vacancy_searches.id"), primary_key=True)
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)


class Area(Base):
    __tablename__ = "areas"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    url: Mapped[str]
    
    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_areas", back_populates="area")
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_areas", back_populates="area")
    metro_line: Mapped["MetroLine"] = relationship(secondary="metro_lines_areas", back_populates="area")
    cluster_metro_station: Mapped["ClusterMetroStation"] = relationship(secondary="cluster_metro_stations_areas", back_populates="area")


class VacancyArea(Base):
    __tablename__ = "vacancies_areas"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    area_id: Mapped[str] = mapped_column(ForeignKey("areas.id"), primary_key=True)
    
    
class MetroLineArea(Base):
    __tablename__ = "metro_lines_areas"
    
    metro_line_id: Mapped[str] = mapped_column(ForeignKey("metro_lines.id"), primary_key=True)
    area_id: Mapped[str] = mapped_column(ForeignKey("areas.id"), primary_key=True)
    

class ClusterMetroStationArea(Base):
    __tablename__ = "cluster_metro_stations_areas"
    
    cluster_metro_station_id: Mapped[str] = mapped_column(ForeignKey("cluster_metro_stations.id"), primary_key=True)
    area_id: Mapped[str] = mapped_column(ForeignKey("areas.id"), primary_key=True)
        

class VacancyShortArea(Base):
    __tablename__ = "vacancies_short_areas"
    
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)  
    area_id: Mapped[str] = mapped_column(ForeignKey("areas.id"), primary_key=True)


class BillingType(Base):
    __tablename__ = "billing_types"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]

    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_billing_types", back_populates="billing_type")


class VacancyBillingType(Base):
    __tablename__ = "vacancies_billing_types"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    billing_type_id: Mapped[str] = mapped_column(ForeignKey("billing_types.id"), primary_key=True)
    

class Contacts(Base):
    __tablename__ = "contacts"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    call_tracking_enabled: Mapped[Optional[bool]]
    email: Mapped[Optional[str]]
    name: Mapped[Optional[str]]
    phones: Mapped[Optional[list["Phone"]]] = relationship(secondary="contacts_phones", back_populates="contacts")
    
    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_contacts", back_populates="contacts")
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_contacts", back_populates="contacts")


class VacancyContacts(Base):
    __tablename__ = "vacancies_contacts"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    contacts_id: Mapped[int] = mapped_column(ForeignKey("contacts.id"), primary_key=True)


class VacancyShortContacts(Base):
    __tablename__ = "vacancies_short_contacts"
    
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    contacts_id: Mapped[int] = mapped_column(ForeignKey("contacts.id"), primary_key=True)   


class Phone(Base):
    __tablename__ = "phones"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city: Mapped[Optional[str]]
    comment: Mapped[Optional[str]]
    country: Mapped[Optional[str]]
    formatted: Mapped[Optional[str]]
    number: Mapped[Optional[str]]
    
    contacts: Mapped["Contacts"] = relationship(secondary="contacts_phones", back_populates="phones")


class ContactsPhone(Base):
    __tablename__ = "contacts_phones"
    
    contacts_id: Mapped[int] = mapped_column(ForeignKey("contacts.id"), primary_key=True)
    phone_id: Mapped[int] = mapped_column(ForeignKey("phones.id"), primary_key=True)


class Department(Base):
    __tablename__ = "departments"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]

    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_departments", back_populates="department")
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_departments", back_populates="department")   


class VacancyDepartment(Base):
    __tablename__ = "vacancies_departments"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    department_id: Mapped[str] = mapped_column(ForeignKey("departments.id"), primary_key=True)
    

class VacancyShortDepartment(Base):
    __tablename__ = "vacancies_short_departments"
    
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    department_id: Mapped[str] = mapped_column(ForeignKey("departments.id"), primary_key=True)
    

class DriverLicenseType(Base):
    __tablename__ = "driver_license_types"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    
    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_driver_license_types", back_populates="driver_license_types")


class VacancyDriverLicenseType(Base):
    __tablename__ = "vacancies_driver_license_types"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    driver_license_type_id: Mapped[str] = mapped_column(ForeignKey("driver_license_types.id"), primary_key=True)


class Employer(Base):
    __tablename__ = "employers"
        
    accredited_it_employer: Mapped[Optional[bool]]
    alternate_url: Mapped[Optional[str]]
    employer_rating: Mapped["EmployerRating"] = relationship(secondary="employers_employer_ratings", back_populates="employer")
    id: Mapped[str] = mapped_column(primary_key=True)
    logo_urls: Mapped["LogoUrls"] = relationship(secondary="employers_logo_urls", back_populates="employer")
    name: Mapped[str]
    trusted: Mapped[bool]
    url: Mapped[Optional[str]]
    vacancies_url: Mapped[Optional[str]]
    
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_employers", back_populates="employer")


class VacancyShortEmployer(Base):
    __tablename__ = "vacancies_short_employers"
    
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    employer_id: Mapped[str] = mapped_column(ForeignKey("employers.id"), primary_key=True)


class EmployerForApplicant(Base):
    __tablename__ = "employers_for_applicant"
    
    accredited_it_employer: Mapped[Optional[bool]]
    alternate_url: Mapped[Optional[str]]
    employer_rating: Mapped["EmployerRating"] = relationship(secondary="employers_for_applicant_employer_ratings", back_populates="employer_for_applicant")
    id: Mapped[Optional[str]] 
    logo_urls: Mapped["LogoUrls"] = relationship(secondary="employers_for_applicant_logo_urls", back_populates="employer_for_applicant")
    name: Mapped[str] = mapped_column(primary_key=True)
    trusted: Mapped[bool]
    url: Mapped[Optional[str]]
    vacancies_url: Mapped[Optional[str]]
    blacklisted: Mapped[Optional[bool]]
    applicant_services: Mapped[Optional["ApplicantService"]] = relationship(secondary="employers_for_applicant_applicant_services", back_populates="employer_for_applicant")
    
    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_employers_for_applicant", back_populates="employer_for_applicant")


class VacancyEmployerForApplicant(Base):
    __tablename__ = "vacancies_employers_for_applicant"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    employer_for_applicant_name: Mapped[str] = mapped_column(ForeignKey("employers_for_applicant.name"), primary_key=True)

    
class EmployerRating(Base):
    __tablename__ = "employer_ratings"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    reviews_count: Mapped[int]
    total_rating: Mapped[str]

    employer: Mapped["Employer"] = relationship(secondary="employers_employer_ratings", back_populates="employer_rating")
    employer_for_applicant: Mapped["EmployerForApplicant"] = relationship(secondary="employers_for_applicant_employer_ratings", back_populates="employer_rating")
    

class EmployerEmployerRating(Base):
    __tablename__ = "employers_employer_ratings"

    employer_id: Mapped[str] = mapped_column(ForeignKey("employers.id"), primary_key=True)
    employer_rating_id: Mapped[int] = mapped_column(ForeignKey("employer_ratings.id"), primary_key=True)


class EmployerForApplicantEmployerRating(Base):
    __tablename__ = "employers_for_applicant_employer_ratings"
    
    employer_for_applicant_name: Mapped[str] = mapped_column(ForeignKey("employers_for_applicant.name"), primary_key=True)
    employer_rating_id: Mapped[int] = mapped_column(ForeignKey("employer_ratings.id"), primary_key=True)


class LogoUrls(Base):
    __tablename__ = "logo_urls"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    px90: Mapped[Optional[str]]
    px240: Mapped[Optional[str]]
    original: Mapped[str]
    
    employer: Mapped["Employer"] = relationship(secondary="employers_logo_urls", back_populates="logo_urls")
    employer_for_applicant: Mapped["EmployerForApplicant"] = relationship(secondary="employers_for_applicant_logo_urls", back_populates="logo_urls")
    

class EmployerLogoUrls(Base):
    __tablename__ = "employers_logo_urls"

    employer_id: Mapped[str] = mapped_column(ForeignKey("employers.id"), primary_key=True)
    logo_urls_id: Mapped[int] = mapped_column(ForeignKey("logo_urls.id"), primary_key=True)
    
    
class EmployerForApplicantLogoUrls(Base):
    __tablename__ = "employers_for_applicant_logo_urls"

    employer_for_applicant_name: Mapped[str] = mapped_column(ForeignKey("employers_for_applicant.name"), primary_key=True)
    logo_urls_id: Mapped[int] = mapped_column(ForeignKey("logo_urls.id"), primary_key=True)
    

class ApplicantService(Base):
    __tablename__ = "applicant_services"
        
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    target_employer: Mapped[Optional["TargetEmployer"]] = relationship(secondary="applicant_services_target_employers", back_populates="applicant_service")
    
    employer_for_applicant: Mapped["EmployerForApplicant"] = relationship(secondary="employers_for_applicant_applicant_services", back_populates="applicant_services")


class EmployerForApplicantApplicantService(Base):
    __tablename__ = "employers_for_applicant_applicant_services"

    employer_for_applicant_name: Mapped[str] = mapped_column(ForeignKey("employers_for_applicant.name"), primary_key=True)
    applicant_service_id: Mapped[int] = mapped_column(ForeignKey("applicant_services.id"), primary_key=True)
    

class TargetEmployer(Base):
    __tablename__ = "target_employers"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    count: Mapped[Optional[float]]
    
    applicant_service: Mapped["ApplicantService"] = relationship(secondary="applicant_services_target_employers", back_populates="target_employer")


class ApplicantServiceTargetEmployer(Base):
    __tablename__ = "applicant_services_target_employers"

    applicant_service_id: Mapped[int] = mapped_column(ForeignKey("applicant_services.id"), primary_key=True)
    target_employer_id: Mapped[int] = mapped_column(ForeignKey("target_employers.id"), primary_key=True)


class EmploymentForm(Base):
    __tablename__ = "employment_forms"
        
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]

    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_employment_forms", back_populates="employment_form")
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_employment_forms", back_populates="employment_form")


class VacancyEmploymentForm(Base):
    __tablename__ = "vacancies_employment_forms"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    employment_form_id: Mapped[str] = mapped_column(ForeignKey("employment_forms.id"), primary_key=True)


class VacancyShortEmploymentForm(Base):
    __tablename__ = "vacancies_short_employment_forms"
    
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    employment_form_id: Mapped[str] = mapped_column(ForeignKey("employment_forms.id"), primary_key=True)

    
class Experience(Base):
    __tablename__ = "experiences"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    
    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_experiences", back_populates="experience")
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_experiences", back_populates="experience")
    

class VacancyExperience(Base):
    __tablename__ = "vacancies_experiences"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    experience_id: Mapped[str] = mapped_column(ForeignKey("experiences.id"), primary_key=True)


class VacancyShortExperience(Base):
    __tablename__ = "vacancies_short_experiences"
    
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    experience_id: Mapped[str] = mapped_column(ForeignKey("experiences.id"), primary_key=True)


class FlyInFlyOutDuration(Base):
    __tablename__ = "fly_in_fly_out_durations"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    
    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_fly_in_fly_out_durations", back_populates="fly_in_fly_out_duration")
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_fly_in_fly_out_durations", back_populates="fly_in_fly_out_duration")
    

class VacancyFlyInFlyOutDuration(Base):
    __tablename__ = "vacancies_fly_in_fly_out_durations"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    fly_in_fly_out_duration_id: Mapped[str] = mapped_column(ForeignKey("fly_in_fly_out_durations.id"), primary_key=True)
    

class VacancyShortFlyInFlyOutDuration(Base):
    __tablename__ = "vacancies_short_fly_in_fly_out_durations"
    
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    fly_in_fly_out_duration_id: Mapped[str] = mapped_column(ForeignKey("fly_in_fly_out_durations.id"), primary_key=True)

    
class InsiderInterview(Base):
    __tablename__ = "insider_interviews"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    url: Mapped[str]
    
    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_insider_interviews", back_populates="insider_interview")
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_insider_interviews", back_populates="insider_interview")
    

class VacancyInsiderInterview(Base):
    __tablename__ = "vacancies_insider_interviews"

    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    insider_interview_id: Mapped[str] = mapped_column(ForeignKey("insider_interviews.id"), primary_key=True)
    

class VacancyShortInsiderInterview(Base):
    __tablename__ = "vacancies_short_insider_interviews"

    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    insider_interview_id: Mapped[str] = mapped_column(ForeignKey("insider_interviews.id"), primary_key=True)


class KeySkill(Base):
    __tablename__ = "key_skills"
    
    name: Mapped[Optional[str]] = mapped_column(primary_key=True)
    
    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_key_skills", back_populates="key_skills")


class VacancyKeySkill(Base):
    __tablename__ = "vacancies_key_skills"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    key_skill_name: Mapped[str] = mapped_column(ForeignKey("key_skills.name"), primary_key=True)


class Language(Base):
    __tablename__ = "languages"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    level: Mapped["Level"] = relationship(secondary="languages_levels", back_populates="language")
    name: Mapped[str]

    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_languages", back_populates="languages")


class VacancyLanguage(Base):
    __tablename__ = "vacancies_languages"

    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    languages: Mapped[str] = mapped_column(ForeignKey("languages.id"), primary_key=True)
    

class Level(Base):
    __tablename__ = "levels"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]

    language: Mapped["Language"] = relationship(secondary="languages_levels", back_populates="level")
    
 
class LanguageLevel(Base):
    __tablename__ = "languages_levels"
    
    language_id: Mapped[str] = mapped_column(ForeignKey("languages.id"), primary_key=True)
    level_id: Mapped[str] = mapped_column(ForeignKey("levels.id"), primary_key=True)


class ProfessionalRole(Base):
    __tablename__ = "professional_roles"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    
    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_professional_roles", back_populates="professional_roles")
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_professional_roles", back_populates="professional_roles")


class VacancyProfessionalRole(Base):
    __tablename__ = "vacancies_professional_roles"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    professional_role_id: Mapped[str] = mapped_column(ForeignKey("professional_roles.id"), primary_key=True)
    
    
class VacancyShortProfessionalRole(Base):
    __tablename__ = "vacancies_short_professional_roles"
    
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    professional_role_id: Mapped[str] = mapped_column(ForeignKey("professional_roles.id"), primary_key=True)


class SalaryRange(Base):
    __tablename__ = "salary_ranges"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    currency: Mapped[str]
    frequency: Mapped[Optional["Frequency"]] = relationship(secondary="salary_ranges_frequencies", back_populates="salary_range")
    from_: Mapped[Optional[int]] = mapped_column("from")
    gross: Mapped[bool]
    mode: Mapped["Mode"] = relationship(secondary="salary_ranges_modes", back_populates="salary_range")
    to: Mapped[Optional[int]]
    
    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_salary_ranges", back_populates="salary_range")
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_salary_ranges", back_populates="salary_range")


class VacancySalaryRange(Base):
    __tablename__ = "vacancies_salary_ranges"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    salary_range_id: Mapped[int] = mapped_column(ForeignKey("salary_ranges.id"), primary_key=True)
    
    
class VacancyShortSalaryRange(Base):
    __tablename__ = "vacancies_short_salary_ranges"
    
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    salary_range_id: Mapped[int] = mapped_column(ForeignKey("salary_ranges.id"), primary_key=True)


class Frequency(Base):
    __tablename__ = "frequencies"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    
    salary_range: Mapped["SalaryRange"] = relationship(secondary="salary_ranges_frequencies", back_populates="frequency")
    

class SalaryRangeFrequency(Base):
    __tablename__ = "salary_ranges_frequencies"
    
    salary_range_id: Mapped[int] = mapped_column(ForeignKey("salary_ranges.id"), primary_key=True)
    frequency_id: Mapped[str] = mapped_column(ForeignKey("frequencies.id"), primary_key=True)


class Mode(Base):
    __tablename__ = "modes"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    
    salary_range: Mapped["SalaryRange"] = relationship(secondary="salary_ranges_modes", back_populates="mode")


class SalaryRangeMode(Base):
    __tablename__ = "salary_ranges_modes"

    salary_range_id: Mapped[int] = mapped_column(ForeignKey("salary_ranges.id"), primary_key=True)
    mode_id: Mapped[str] = mapped_column(ForeignKey("modes.id"), primary_key=True)
    

class Type(Base):
    __tablename__ = "types"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    
    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_types", back_populates="type_")
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_types", back_populates="type_")
   

class VacancyType(Base):
    __tablename__ = "vacancies_types"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    type_id: Mapped[str] = mapped_column(ForeignKey("types.id"), primary_key=True)
    
    
class VacancyShortType(Base):
    __tablename__ = "vacancies_short_types"
    
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    type_id: Mapped[str] = mapped_column(ForeignKey("types.id"), primary_key=True)
 

class Test(Base):
    __tablename__ = "tests"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    required: Mapped[Optional[bool]]

    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_tests", back_populates="test")
    
 
class VacancyTest(Base):
    __tablename__ = "vacancies_tests"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    test_id: Mapped[str] = mapped_column(ForeignKey("tests.id"), primary_key=True)


class VacancyProperties(Base):
    __tablename__ = "vacancy_properties"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    appearance: Mapped[Optional["Appearance"]] = relationship(secondary="vacancy_properties_appearances", back_populates="vacancy_properties")
    properties: Mapped[Optional[list["Property"]]] = relationship(secondary="vacancy_properties_properties", back_populates="vacancy_properties")

    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_vacancy_properties", back_populates="vacancy_properties")


class VacancyVacancyProperties(Base):
    __tablename__ = "vacancies_vacancy_properties"

    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    vacancy_properties_id: Mapped[int] = mapped_column(ForeignKey("vacancy_properties.id"), primary_key=True)

    
class Appearance(Base):
    __tablename__ = "appearances"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[Optional[str]]
    
    vacancy_properties: Mapped["VacancyProperties"] = relationship(secondary="vacancy_properties_appearances", back_populates="appearance")


class VacancyPropertiesAppearance(Base):
    __tablename__ = "vacancy_properties_appearances"
    
    vacancy_properties_id: Mapped[int] = mapped_column(ForeignKey("vacancy_properties.id"), primary_key=True)
    appearance_id: Mapped[int] = mapped_column(ForeignKey("appearances.id"), primary_key=True)


class Property(Base):
    __tablename__ = "properties"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    end_time: Mapped[Optional[str]]
    parameters: Mapped[Optional[list[str]]] = mapped_column(ARRAY(String))
    property_type: Mapped[Optional[str]]
    start_time: Mapped[Optional[str]]
    
    vacancy_properties: Mapped["VacancyProperties"] = relationship(secondary="vacancy_properties_properties", back_populates="properties")
   

class VacancyPropertiesProperty(Base):
    __tablename__ = "vacancy_properties_properties"

    vacancy_properties_id: Mapped[int] = mapped_column(ForeignKey("vacancy_properties.id"), primary_key=True)
    property_id: Mapped[int] = mapped_column(ForeignKey("properties.id"), primary_key=True)
    
    
class VideoVacancy(Base):
    __tablename__ = "video_vacancies"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cover_picture: Mapped[Optional["CoverPicture"]] = relationship(secondary="video_vacancies_cover_pictures", back_populates="video_vacancy")
    snippet_picture: Mapped[Optional["SnippetPicture"]] = relationship(secondary="video_vacancies_snippet_pictures", back_populates="video_vacancy")
    snippet_video: Mapped[Optional["SnippetVideo"]] = relationship(secondary="video_vacancies_snippet_videos", back_populates="video_vacancy")
    video: Mapped[Optional["Video"]] = relationship(secondary="video_vacancies_videos", back_populates="video_vacancy")

    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_video_vacancies", back_populates="video_vacancy")
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_video_vacancies", back_populates="video_vacancy")


class VacancyVideoVacancy(Base):
    __tablename__ = "vacancies_video_vacancies"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    video_vacancy_id: Mapped[int] = mapped_column(ForeignKey("video_vacancies.id"), primary_key=True)
    
    
class VacancyShortVideoVacancy(Base):
    __tablename__ = "vacancies_short_video_vacancies"
    
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    video_vacancy_id: Mapped[int] = mapped_column(ForeignKey("video_vacancies.id"), primary_key=True)


class SnippetPicture(Base):
    __tablename__ = "snippet_pictures"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    url: Mapped[str]
    
    video_vacancy: Mapped["VideoVacancy"] = relationship(secondary="video_vacancies_snippet_pictures", back_populates="snippet_picture")


class VideoVacancySnippetPicture(Base):
    __tablename__ = "video_vacancies_snippet_pictures"

    video_vacancy_id: Mapped[int] = mapped_column(ForeignKey("video_vacancies.id"), primary_key=True)
    snippet_picture_id: Mapped[int] = mapped_column(ForeignKey("snippet_pictures.id"), primary_key=True)
    

class SnippetVideo(Base):
    __tablename__ = "snippet_videos"
    
    upload_id: Mapped[str] = mapped_column(primary_key=True)
    url: Mapped[str]
    
    video_vacancy: Mapped["VideoVacancy"] = relationship(secondary="video_vacancies_snippet_videos", back_populates="snippet_video")


class VideoVacancySnippetVideo(Base):
    __tablename__ = "video_vacancies_snippet_videos"

    video_vacancy_id: Mapped[int] = mapped_column(ForeignKey("video_vacancies.id"), primary_key=True)
    snippet_video_upload_id: Mapped[int] = mapped_column(ForeignKey("snippet_videos.upload_id"), primary_key=True)
    

class Video(Base):
    __tablename__ = "videos"
    
    upload_id: Mapped[str] = mapped_column(primary_key=True)
    url: Mapped[str]
    
    video_vacancy: Mapped["VideoVacancy"] = relationship(secondary="video_vacancies_videos", back_populates="video")


class VideoVacancyVideo(Base):
    __tablename__ = "video_vacancies_videos"

    video_vacancy_id: Mapped[int] = mapped_column(ForeignKey("video_vacancies.id"), primary_key=True)
    video_upload_id: Mapped[str] = mapped_column(ForeignKey("videos.upload_id"), primary_key=True)
    

class CoverPicture(Base):
    __tablename__ = "cover_pictures"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    resized_height: Mapped[float]
    resized_path: Mapped[str]
    resized_width: Mapped[float]
    
    video_vacancy: Mapped["VideoVacancy"] = relationship(secondary="video_vacancies_cover_pictures", back_populates="cover_picture")


class VideoVacancyCoverPicture(Base):
    __tablename__ = "video_vacancies_cover_pictures"
    
    video_vacancy_id: Mapped[int] = mapped_column(ForeignKey("video_vacancies.id"), primary_key=True)
    cover_picture_id: Mapped[int] = mapped_column(ForeignKey("cover_pictures.id"), primary_key=True)


class Snippet(Base):
    __tablename__ = "snippets"
        
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    requirement: Mapped[Optional[str]]
    responsibility: Mapped[Optional[str]]
    
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_snippets", back_populates="snippet")


class VacancyShortSnippet(Base):
    __tablename__ = "vacancies_short_snippets"

    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    snippet_id: Mapped[int] = mapped_column(ForeignKey("snippets.id"), primary_key=True)


class WorkFormat(Base):
    __tablename__ = "work_formats"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    
    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_work_formats", back_populates="work_format")
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_work_formats", back_populates="work_format")


class VacancyWorkFormat(Base):
    __tablename__ = "vacancies_work_formats"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    work_format_id: Mapped[str] = mapped_column(ForeignKey("work_formats.id"), primary_key=True)
    

class VacancyShortWorkFormat(Base):
    __tablename__ = "vacancies_short_work_formats"
    
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    work_format_id: Mapped[str] = mapped_column(ForeignKey("work_formats.id"), primary_key=True)


class WorkScheduleByDays(Base):
    __tablename__ = "work_schedules_by_days"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]

    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_work_schedules_by_days", back_populates="work_schedule_by_days")
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_work_schedules_by_days", back_populates="work_schedule_by_days")


class VacancyWorkScheduleByDays(Base):
    __tablename__ = "vacancies_work_schedules_by_days"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    work_schedule_by_days: Mapped[str] = mapped_column(ForeignKey("work_schedules_by_days.id"), primary_key=True)
    
    
class VacancyShortWorkScheduleByDays(Base):
    __tablename__ = "vacancies_short_work_schedules_by_days"
    
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    work_schedule_by_days: Mapped[str] = mapped_column(ForeignKey("work_schedules_by_days.id"), primary_key=True)


class WorkingHours(Base):
    __tablename__ = "working_hours"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    
    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_working_hours", back_populates="working_hours")
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_working_hours", back_populates="working_hours")


class VacancyWorkingHours(Base):
    __tablename__ = "vacancies_working_hours"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    working_hours_id: Mapped[str] = mapped_column(ForeignKey("working_hours.id"), primary_key=True)


class VacancyShortWorkingHours(Base):
    __tablename__ = "vacancies_short_working_hours"
    
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    working_hours_id: Mapped[str] = mapped_column(ForeignKey("working_hours.id"), primary_key=True)
    
    
class Address(Base):
    __tablename__ = "addresses"
        
    building: Mapped[Optional[str]]
    city: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    id: Mapped[str] = mapped_column(primary_key=True)
    lat: Mapped[Optional[float]]
    lng: Mapped[Optional[float]]
    metro: Mapped[Optional["Metro"]] = relationship(secondary="addresses_metros", back_populates="address")
    metro_stations: Mapped[Optional[list["MetroStation"]]] = relationship(secondary="addresses_metro_stations", back_populates="address")
    raw: Mapped[Optional[str]]
    street: Mapped[Optional[str]]
    
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_addresses", back_populates="address")


class VacancyShortAddress(Base):
    __tablename__ = "vacancies_short_addresses"
    
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    address_id: Mapped[str] = mapped_column(ForeignKey("addresses.id"), primary_key=True)


class AddressForApplicant(Base):
    __tablename__ = "addresses_for_applicant"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    building: Mapped[Optional[str]]
    city: Mapped[Optional[str]]
    lat: Mapped[Optional[float]]
    lng: Mapped[Optional[float]]
    street: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    metro_stations: Mapped[Optional[list["MetroStation"]]] = relationship(secondary="addresses_for_applicant_metro_stations", back_populates="address_for_applicant")

    vacancy: Mapped["Vacancy"] = relationship(secondary="vacancies_addresses_for_applicant", back_populates="address_for_applicant")


class VacancyAddressForApplicant(Base):
    __tablename__ = "vacancies_addresses_for_applicant"
    
    vacancy_id: Mapped[str] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    address_for_applicant_id: Mapped[int] = mapped_column(ForeignKey("addresses_for_applicant.id"), primary_key=True)


class MetroStation(Base):
    __tablename__ = "metro_stations"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    lat: Mapped[Optional[float]]
    line_id: Mapped[str]
    line_name: Mapped[str]
    lng: Mapped[Optional[float]]
    station_id: Mapped[str]
    station_name: Mapped[str]
    
    address: Mapped["Address"] = relationship(secondary="addresses_metro_stations", back_populates="metro_stations")
    address_for_applicant: Mapped["AddressForApplicant"] = relationship(secondary="addresses_for_applicant_metro_stations", back_populates="metro_stations")
    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_metro_stations", back_populates="metro_stations")


class AddressMetroStation(Base):
    __tablename__ = "addresses_metro_stations"
    
    address_id: Mapped[str] = mapped_column(ForeignKey("addresses.id"), primary_key=True)
    metro_station: Mapped[int] = mapped_column(ForeignKey("metro_stations.id"), primary_key=True)


class AddressForApplicantMetroStation(Base):
    __tablename__ = "addresses_for_applicant_metro_stations"
    
    address_for_applicant_id: Mapped[int] = mapped_column(ForeignKey("addresses_for_applicant.id"), primary_key=True)
    metro_station: Mapped[int] = mapped_column(ForeignKey("metro_stations.id"), primary_key=True)
    
    
class VacancyShortMetroStation(Base):
    __tablename__ = "vacancies_short_metro_stations"
     
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    metro_station_id: Mapped[int] = mapped_column(ForeignKey("metro_stations.id"), primary_key=True)


class Counters(Base):
    __tablename__ = "counters"
        
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    vacancy_searches: Mapped[Optional[int]]
    total_responses: Mapped[Optional[int]]

    vacancy_short: Mapped["VacancyShort"] = relationship(secondary="vacancies_short_counters", back_populates="counters")


class VacancyShortCounters(Base):
    __tablename__ = "vacancies_short_counters"
    
    vacancy_short_id: Mapped[str] = mapped_column(ForeignKey("vacancies_short.id"), primary_key=True)
    counters_id: Mapped[int] = mapped_column(ForeignKey("counters.id"), primary_key=True)

    
class Metro(Base):
    __tablename__ = "metros"
        
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    lat: Mapped[Optional[float]]
    line_id: Mapped[str]
    line_name: Mapped[str]
    lng: Mapped[Optional[float]]
    station_id: Mapped[str]
    station_name: Mapped[str] 
    
    address: Mapped["Address"] = relationship(secondary="addresses_metros", back_populates="metro")


class AddressMetro(Base):
    __tablename__ = "addresses_metros"

    address_id: Mapped[str] = mapped_column(ForeignKey("addresses.id"), primary_key=True)
    metro_id: Mapped[int] = mapped_column(ForeignKey("metros.id"), primary_key=True)
    
    
class Cluster(Base):
    __tablename__ = "clusters"
        
    id: Mapped[str] = mapped_column(primary_key=True)
    cluster_items: Mapped[list["ClusterItem"]] = relationship(secondary="clusters_cluster_items", back_populates="cluster")
    name: Mapped[str]
    
    vacancy_search: Mapped["VacancySearch"] = relationship(secondary="vacancy_searches_clusters", back_populates="clusters")


class VacancySearchCluster(Base):
    __tablename__ = "vacancy_searches_clusters"

    vacancy_search_id: Mapped[int] = mapped_column(ForeignKey("vacancy_searches.id"), primary_key=True)
    cluster_id: Mapped[str] = mapped_column(ForeignKey("clusters.id"), primary_key=True)


class ClusterItem(Base):
    __tablename__ = "cluster_items"
        
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    count: Mapped[int]
    metro_line: Mapped["MetroLine"] = relationship(secondary="cluster_items_metro_lines", back_populates="cluster_item")
    cluster_metro_station: Mapped["ClusterMetroStation"] = relationship(secondary="cluster_items_cluster_metro_stations", back_populates="cluster_item")
    name: Mapped[str]
    type_: Mapped[Optional[str]] = mapped_column("type")
    url: Mapped[str]
    
    cluster: Mapped["Cluster"] = relationship(secondary="clusters_cluster_items", back_populates="cluster_items")


class ClusterClusterItem(Base):
    __tablename__ = "clusters_cluster_items"

    cluster_id: Mapped[str] = mapped_column(ForeignKey("clusters.id"), primary_key=True)
    cluster_item_id: Mapped[int] = mapped_column(ForeignKey("cluster_items.id"), primary_key=True)
    
    
class MetroLine(Base):
    __tablename__ = "metro_lines"
        
    area: Mapped["Area"] = relationship(secondary="metro_lines_areas", back_populates="metro_line")
    hex_color: Mapped[str]
    id: Mapped[str] = mapped_column(primary_key=True)
    
    cluster_item: Mapped["ClusterItem"] = relationship(secondary="cluster_items_metro_lines", back_populates="metro_line")


class ClusterItemMetroLine(Base):
    __tablename__ = "cluster_items_metro_lines"
    
    cluster_item_id: Mapped[int] = mapped_column(ForeignKey("cluster_items.id"), primary_key=True)
    metro_line_id: Mapped[str] = mapped_column(ForeignKey("metro_lines.id"), primary_key=True)

    
class ClusterMetroStation(Base):
    __tablename__ = "cluster_metro_stations"
        
    area: Mapped["Area"] = relationship(secondary="cluster_metro_stations_areas", back_populates="cluster_metro_station")
    hex_color: Mapped[str]
    id: Mapped[str] = mapped_column(primary_key=True)
    lat: Mapped[float]
    lng: Mapped[float]
    order: Mapped[float]
    
    cluster_item: Mapped["ClusterItem"] = relationship(secondary="cluster_items_cluster_metro_stations", back_populates="cluster_metro_station")


class ClusterItemClusterMetroStation(Base):
    __tablename__ = "cluster_items_cluster_metro_stations"

    cluster_item_id: Mapped[int] = mapped_column(ForeignKey("cluster_items.id"), primary_key=True)
    cluster_metro_station_id: Mapped[str] = mapped_column(ForeignKey("cluster_metro_stations.id"), primary_key=True)


class Argument(Base):
    __tablename__ = "arguments"
        
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    argument: Mapped[str]
    cluster_group: Mapped["ClusterGroup"] = relationship(secondary="arguments_cluster_groups", back_populates="argument")
    hex_color: Mapped[Optional[str]]
    metro_type: Mapped[Optional[str]]
    name: Mapped[Optional[str]]
    value: Mapped[str]
    value_description: Mapped[Optional[str]]
    
    vacancy_search: Mapped["VacancySearch"] = relationship(secondary="vacancy_searches_arguments", back_populates="arguments")


class VacancySearchArgument(Base):
    __tablename__ = "vacancy_searches_arguments"

    vacancy_search_id: Mapped[int] = mapped_column(ForeignKey("vacancy_searches.id"), primary_key=True)
    argument_id: Mapped[int] = mapped_column(ForeignKey("arguments.id"), primary_key=True)
    

class ClusterGroup(Base):
    __tablename__ = "cluster_groups"
        
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    
    argument: Mapped["Argument"] = relationship(secondary="arguments_cluster_groups", back_populates="cluster_group")


class ArgumentClusterGroup(Base):
    __tablename__ = "arguments_cluster_groups"

    argument_id: Mapped[int] = mapped_column(ForeignKey("arguments.id"), primary_key=True)
    cluster_group_id: Mapped[str] = mapped_column(ForeignKey("cluster_groups.id"), primary_key=True)
    

class Fixes(Base):
    __tablename__ = "fixes"
        
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fixed: Mapped[Optional[str]]
    original: Mapped[Optional[str]]

    vacancy_search: Mapped["VacancySearch"] = relationship(secondary="vacancy_searches_fixes", back_populates="fixes")


class VacancySearchFixes(Base):
    __tablename__ = "vacancy_searches_fixes"

    vacancy_search_id: Mapped[int] = mapped_column(ForeignKey("vacancy_searches.id"), primary_key=True)
    fixes_id: Mapped[int] = mapped_column(ForeignKey("fixes.id"), primary_key=True)
    

class Suggests(Base):
    __tablename__ = "suggests"
        
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    found: Mapped[Optional[int]]
    value: Mapped[Optional[str]]

    vacancy_search: Mapped["VacancySearch"] = relationship(secondary="vacancy_searches_suggests", back_populates="suggests")
    

class VacancySearchSuggests(Base):
    __tablename__ = "vacancy_searches_suggests"
    
    vacancy_search_id: Mapped[int] = mapped_column(ForeignKey("vacancy_searches.id"), primary_key=True)
    suggests_id: Mapped[int] = mapped_column(ForeignKey("suggests.id"), primary_key=True)
    