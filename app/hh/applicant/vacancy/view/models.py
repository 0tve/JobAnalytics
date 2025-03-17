from typing import Optional

from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models.base import Base


class Response(Base):
    __tablename__ = "responses"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    accept_handicapped: Mapped[bool]
    accept_incomplete_resumes: Mapped[bool]
    accept_kids: Mapped[bool]
    accept_temporary: Mapped[Optional[bool]]
    allow_messages: Mapped[bool]
    alternate_url: Mapped[str]
    apply_alternate_url: Mapped[str]
    approved: Mapped[bool]
    archived: Mapped[bool]
    area: Mapped["Area"] = relationship(back_populates="response")
    billing_type: Mapped[Optional["BillingType"]] = relationship(back_populates="response")
    code: Mapped[Optional[str]]
    contacts: Mapped[Optional["Contact"]] = relationship(back_populates="response")
    department: Mapped[Optional["Department"]] = relationship(back_populates="response")
    description: Mapped[str]
    driver_license_types: Mapped[list["DriverLicenseType"]] = relationship(back_populates="response")
    employer: Mapped[Optional["Employer"]] = relationship(back_populates="response")
    employment_form: Mapped[Optional["EmploymentForm"]] = relationship(back_populates="response")
    experience: Mapped[Optional["Experience"]] = relationship(back_populates="response")
    fly_in_fly_out_duration: Mapped[Optional["FlyInFlyOutDuration"]] = relationship(back_populates="response")
    has_test: Mapped[bool]
    id: Mapped[str] = mapped_column(primary_key=True)
    initial_created_at: Mapped[str]
    insider_interview: Mapped[Optional["InsiderInterview"]] = relationship(back_populates="response")
    internship: Mapped[Optional[bool]]
    key_skills: Mapped[list["KeySkill"]] = relationship(back_populates="response")
    languages: Mapped[Optional["Language"]] = relationship(back_populates="response")
    name: Mapped[str]
    negotiations_url: Mapped[Optional[str]]
    night_shifts: Mapped[Optional[bool]]
    premium: Mapped[bool]
    professional_roles: Mapped[list["ProfessionalRole"]] = relationship(back_populates="response")
    published_at: Mapped[str]
    relations: Mapped[Optional[list[str]]] = mapped_column(ARRAY(String))
    response_letter_required: Mapped[bool]
    response_url: Mapped[Optional[str]]
    salary: Mapped[Optional["Salary"]] = relationship(back_populates="response")
    suitable_resumes_url: Mapped[Optional[str]]
    test: Mapped[Optional["Test"]] = relationship(back_populates="response")
    type_: Mapped["Type"] = relationship(back_populates="response")
    vacancy_properties: Mapped[Optional["VacancyProperty"]] = relationship(back_populates="response")
    video_vacancy: Mapped[Optional["VideoVacancy"]] = relationship(back_populates="response")
    work_format: Mapped[Optional[list["WorkFormat"]]] = relationship(back_populates="response")
    work_schedule_by_days: Mapped[Optional[list["WorkScheduleByDays"]]] = relationship(back_populates="response")
    working_hours: Mapped[Optional[list["WorkingHours"]]] = relationship(back_populates="response")
    address: Mapped[Optional["Address"]] = relationship(back_populates="response")
    

class Area(Base):
    __tablename__ = "areas"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    url: Mapped[str]

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="area")
    
    
class BillingType(Base):
    __tablename__ = "billing_types"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="billing_type")
    

class Contact(Base):
    __tablename__ = "contacts"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    call_tracking_enabled: Mapped[Optional[bool]]
    email: Mapped[Optional[str]]
    name: Mapped[Optional[str]]
    phones: Mapped[Optional[list["Phone"]]] = relationship(back_populates="contact")

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="contacts")
    

class Phone(Base):
    __tablename__ = "phones"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city: Mapped[Optional[str]]
    comment: Mapped[Optional[str]]
    country: Mapped[Optional[str]]
    formatted: Mapped[Optional[str]]
    number: Mapped[Optional[str]]

    contact_id: Mapped[int] = mapped_column(ForeignKey("applicant_vacancy_view.contacts.id"))
    
    contact: Mapped["Contact"] = relationship(back_populates="phones")
    

class Department(Base):
    __tablename__ = "departments"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="department")
    

class DriverLicenseType(Base):
    __tablename__ = "driver_license_types"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="driver_license_types")
    

class Employer(Base):
    __tablename__ = "employers"
    __table_args__ = {"schema": "applicant_vacancy_view"}
    
    accredited_it_employer: Mapped[Optional[bool]]
    alternate_url: Mapped[Optional[str]]
    employer_rating: Mapped[Optional["EmployerRating"]] = relationship(back_populates="employer")
    id: Mapped[str] = mapped_column(primary_key=True)
    logo_urls: Mapped[Optional["LogoUrl"]] = relationship(back_populates="employer")
    name: Mapped[str]
    trusted: Mapped[bool]
    url: Mapped[Optional[str]]
    vacancies_url: Mapped[Optional[str]]
    blacklisted: Mapped[Optional[bool]]
    applicant_services: Mapped[Optional["ApplicantService"]] = relationship(back_populates="employer")

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="employer")
    
    
class EmployerRating(Base):
    __tablename__ = "employer_ratings"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    reviews_count: Mapped[int]
    total_rating: Mapped[str]

    employer_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.employers.id"))
    
    employer: Mapped["Employer"] = relationship(back_populates="employer_rating")

    
class LogoUrl(Base):
    __tablename__ = "logo_urls"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    px90: Mapped[Optional[str]]
    px240: Mapped[Optional[str]]
    original: Mapped[str]

    employer_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.employers.id"))
    
    employer: Mapped["Employer"] = relationship(back_populates="logo_urls")


class ApplicantService(Base):
    __tablename__ = "applicant_services"
    __table_args__ = {"schema": "applicant_vacancy_view"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    target_employer: Mapped[Optional["TargetEmployer"]] = relationship(back_populates="applicant_service")

    employer_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.employers.id"))
    
    employer: Mapped["Employer"] = relationship(back_populates="applicant_services")


class TargetEmployer(Base):
    __tablename__ = "target_employers"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    count: Mapped[Optional[float]]

    applicant_service_id: Mapped[int] = mapped_column(ForeignKey("applicant_vacancy_view.applicant_services.id"))
    
    applicant_service: Mapped["ApplicantService"] = relationship(back_populates="target_employer")


class EmploymentForm(Base):
    __tablename__ = "employment_forms"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="employment_form")


class Experience(Base):
    __tablename__ = "experiences"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="experience")
    

class FlyInFlyOutDuration(Base):
    __tablename__ = "fly_in_fly_out_durations"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="fly_in_fly_out_duration")
    
    
class InsiderInterview(Base):
    __tablename__ = "insider_interviews"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    url: Mapped[str]

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="insider_interview")
    
    
class KeySkill(Base):
    __tablename__ = "key_skills"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[Optional[str]]

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="key_skills")


class Language(Base):
    __tablename__ = "languages"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    level: Mapped["Level"] = relationship(back_populates="language")
    name: Mapped[str]

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="languages")


class Level(Base):
    __tablename__ = "levels"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]

    language_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.languages.id"))
    
    language: Mapped["Language"] = relationship(back_populates="level")
    

class ProfessionalRole(Base):
    __tablename__ = "professional_roles"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="professional_roles")
    

class Salary(Base):
    __tablename__ = "salaries"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    currency: Mapped[Optional[str]]
    from_: Mapped[Optional[int]] = mapped_column("from")
    gross: Mapped[Optional[bool]]
    to: Mapped[Optional[int]]

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="salary")


class Test(Base):
    __tablename__ = "tests"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    required: Mapped[Optional[bool]]

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="test")


class Type(Base):
    __tablename__ = "types"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="type_")


class VacancyProperty(Base):
    __tablename__ = "vacancy_properties"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    appearance: Mapped[Optional["Appearance"]] = relationship(back_populates="vacancy_property")
    properties: Mapped[Optional["Properties"]] = relationship(back_populates="vacancy_property")

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="vacancy_properties")


class Appearance(Base):
    __tablename__ = "appearances"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[Optional[str]]
    
    vacancy_property_id: Mapped[int] = mapped_column(ForeignKey("applicant_vacancy_view.vacancy_properties.id"))
    
    vacancy_property: Mapped["VacancyProperty"] = relationship(back_populates="appearance")


class Properties(Base):
    __tablename__ = "properties"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    end_time: Mapped[Optional[str]]
    parameters: Mapped[Optional[list[str]]] = mapped_column(ARRAY(String))
    property_type: Mapped[Optional[str]]
    start_time: Mapped[Optional[str]]
    
    vacancy_property_id: Mapped[int] = mapped_column(ForeignKey("applicant_vacancy_view.vacancy_properties.id"))
    
    vacancy_property: Mapped["VacancyProperty"] = relationship(back_populates="properties")
    
    
class VideoVacancy(Base):
    __tablename__ = "video_vacancies"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cover_picture: Mapped[Optional["CoverPicture"]] = relationship(back_populates="video_vacancy")
    snippet_picture: Mapped[Optional["SnippetPicture"]] = relationship(back_populates="video_vacancy")
    snippet_video: Mapped[Optional["SnippetVideo"]] = relationship(back_populates="video_vacancy")
    video: Mapped[Optional["Video"]] = relationship(back_populates="video_vacancy")

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="video_vacancy")


class SnippetPicture(Base):
    __tablename__ = "snippet_pictures"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    url: Mapped[str]

    video_vacancy_id: Mapped[int] = mapped_column(ForeignKey("applicant_vacancy_view.video_vacancies.id"))
    
    video_vacancy: Mapped["VideoVacancy"] = relationship(back_populates="snippet_picture")


class SnippetVideo(Base):
    __tablename__ = "snippet_videos"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    url: Mapped[str]

    video_vacancy_id: Mapped[int] = mapped_column(ForeignKey("applicant_vacancy_view.video_vacancies.id"))
    
    video_vacancy: Mapped["VideoVacancy"] = relationship(back_populates="snippet_video")


class Video(Base):
    __tablename__ = "videos"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    url: Mapped[str]

    video_vacancy_id: Mapped[int] = mapped_column(ForeignKey("applicant_vacancy_view.video_vacancies.id"))
    
    video_vacancy: Mapped["VideoVacancy"] = relationship(back_populates="video")


class CoverPicture(Base):
    __tablename__ = "cover_pictures"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    resized_height: Mapped[float]
    resized_path: Mapped[str]
    resized_width: Mapped[float]

    video_vacancy_id: Mapped[int] = mapped_column(ForeignKey("applicant_vacancy_view.video_vacancies.id"))
    
    video_vacancy: Mapped["VideoVacancy"] = relationship(back_populates="cover_picture")
    

class WorkFormat(Base):
    __tablename__ = "work_formats"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="work_format")
    

class WorkScheduleByDays(Base):
    __tablename__ = "work_schedule_by_days"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="work_schedule_by_days")
    

class WorkingHours(Base):
    __tablename__ = "working_hours"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="working_hours")
    

class Address(Base):
    __tablename__ = "addresses"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    building: Mapped[Optional[str]]
    city: Mapped[Optional[str]]
    lat: Mapped[Optional[float]]
    lng: Mapped[Optional[float]]
    street: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    metro_stations: Mapped[Optional[list["MetroStation"]]] = relationship(back_populates="address")

    response_id: Mapped[str] = mapped_column(ForeignKey("applicant_vacancy_view.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="address")


class MetroStation(Base):
    __tablename__ = "metro_stations"
    __table_args__ = {"schema": "applicant_vacancy_view"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    lat: Mapped[Optional[float]]
    line_id: Mapped[str]
    line_name: Mapped[str]
    lng: Mapped[Optional[float]]
    station_id: Mapped[str]
    station_name: Mapped[str]

    address_id: Mapped[int] = mapped_column(ForeignKey("applicant_vacancy_view.addresses.id"))
    
    address: Mapped["Address"] = relationship(back_populates="metro_stations")


