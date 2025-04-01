from typing import Annotated, Any, Optional

from pydantic import BaseModel, Field
from pydantic.types import StringConstraints

from app.core.config import HHSettings

hh = HHSettings()


class PathParameters(BaseModel):
    vacancy_id: str
    

class QueryParameters(BaseModel):
    locale: str = "RU"
    host: str = "hh.ru"


class HeaderParameters(BaseModel):
    user_agent: Annotated[str, StringConstraints(pattern=hh.USER_AGENT_PATTERN)] = Field(default=hh.USER_AGENT)
    authorization: Annotated[str, StringConstraints(pattern=hh.AUTHORIZATION_PATTERN)] = Field(default=hh.AUTHORIZATION)


class Response(BaseModel):
    accept_handicapped: bool
    accept_incomplete_resumes: bool
    accept_kids: bool
    accept_temporary: bool | None = None
    allow_messages: bool
    alternate_url: str
    apply_alternate_url: str
    approved: bool
    archived: bool
    area: "Area"
    billing_type: Optional["BillingType"]
    code: str | None = None
    contacts: Optional["Contact"] = None
    department: Optional["Department"] = None
    description: str
    driver_license_types: list["DriverLicenseType"]
    employer: Optional["Employer"] = None
    employment_form: Optional["EmploymentForm"] = None
    experience: Optional["Experience"] = None
    
    # TODO: accept list - maybe incorrect
    fly_in_fly_out_duration: Optional["FlyInFlyOutDuration"] | list = None
    has_test: bool
    id: str
    initial_created_at: str
    insider_interview: Optional["InsiderInterview"] = None
    internship: bool | None = None
    key_skills: list["KeySkill"]
    
    # TODO: accept list - maybe incorrect
    languages: Optional["Language"] | list = None
    name: str
    negotiations_url: str | None = None
    night_shifts: bool | None = None
    premium: bool
    professional_roles: list["ProfessionalRole"]
    published_at: str
    relations: list[str] | None = None
    response_letter_required: bool
    response_url: str | None = None
    salary: Optional["Salary"] = None
    suitable_resumes_url: str | None = None
    test: Optional["Test"] = None
    type_: "Type" = Field(alias="type")
    video_vacancy: Optional["VideoVacancy"] = None
    work_format: list["WorkFormat"] | None = None
    work_schedule_by_days: list["WorkScheduleByDays"] | None = None
    working_hours: list["WorkingHours"] | None = None
    address: Optional["Address"] = None
    

class Area(BaseModel):
    id: str
    name: str
    url: str
    

class BillingType(BaseModel):
    id: str
    name: str | None = None
    

class Contact(BaseModel):
    call_tracking_enabled: bool | None = None
    email: str | None = None
    name: str | None = None
    phones: list["Phone"] | None = None


class Phone(BaseModel):
    city: str | None = None
    comment: str | None = None
    country: str | None = None
    formatted: str | None = None
    number: str | None = None


class Department(BaseModel):
    id: str | None = None
    name: str | None = None
    

class DriverLicenseType(BaseModel):
    id: str | None = None
    

class Employer(BaseModel):
    accredited_it_employer: bool | None = None
    alternate_url: str | None = None
    employer_rating: Optional["EmployerRating"] = None
    id: str | None = None
    logo_urls: Optional["LogoUrl"] = None
    name: str
    trusted: bool
    url: str | None = None
    vacancies_url: str | None = None
    blacklisted: bool | None = None
    applicant_services: Optional["ApplicantService"] = None
    

class EmployerRating(BaseModel):
    reviews_count: Any
    total_rating: str
    

class LogoUrl(BaseModel):
    px90: str | None = Field(None, alias="90")
    px240: str | None = Field(None, alias="240")
    original: str
    

class ApplicantService(BaseModel):
    target_employer: Optional["TargetEmployer"] = None
    

class TargetEmployer(BaseModel):
    count: int | float | None = None
    

class EmploymentForm(BaseModel):
    id: str | None = None
    name: str | None = None
    

class Experience(BaseModel):
    id: str | None = None
    name: str | None = None
    

class FlyInFlyOutDuration(BaseModel):
    id: str | None = None
    name: str | None = None
    
    
class InsiderInterview(BaseModel):
    id: str
    url: str
    

class KeySkill(BaseModel):
    name: str | None = None
    

class Language(BaseModel):
    id: str
    level: "Level"
    name: str
    

class Level(BaseModel):
    id: str
    name: str
    

class ProfessionalRole(BaseModel):
    id: str | None = None
    name: str | None = None
    

class Salary(BaseModel):
    currency: str | None = None
    from_: int | None = Field(None, alias="from")
    gross: bool | None = None
    to: int | None = None
    

class Test(BaseModel):
    id: str | None = None
    required: bool | None = None


class Type(BaseModel):
    id: str
    name: str
    

class VacancyProperty(BaseModel):
    appearance: Optional["Appearance"] = None
    properties: list["Properties"] | None = None
    

class Appearance(BaseModel):
    title: str | None = None
    

class Properties(BaseModel):
    end_time: str | None = None
    parameters: list[str] | None = None
    property_type: str | None = None
    start_time: str | None = None


class VideoVacancy(BaseModel):
    cover_picture: Optional["CoverPicture"] = None
    snippet_picture: Optional["SnippetPicture"] = None
    snippet_video: Optional["SnippetVideo"] = None
    video: Optional["Video"] = None
   

class SnippetPicture(BaseModel):
    url: Annotated[str, StringConstraints(min_length=1)]
    

class SnippetVideo(BaseModel):
    id: Annotated[str, StringConstraints(min_length=1)]
    url: Annotated[str, StringConstraints(min_length=1)]
    

class Video(BaseModel):
    id: Annotated[str, StringConstraints(min_length=1)]
    url: Annotated[str, StringConstraints(min_length=1)]
    

class CoverPicture(BaseModel):
    resized_height: int | float
    resized_path: Annotated[str, StringConstraints(min_length=1)]
    resized_width: int | float
    

class WorkFormat(BaseModel):
    id: str | None = None
    name: str | None = None
    

class WorkScheduleByDays(BaseModel):
    id: str | None = None
    name: str | None = None
    

class WorkingHours(BaseModel):
    id: str | None = None
    name: str | None = None
    

class Address(BaseModel):
    building: str | None = None
    city: str | None = None
    lat: int | float | None = None
    lng: int | float | None = None
    street: str | None = None
    description: str | None = None
    metro_stations: list["MetroStation"] | None = None
    
    
class MetroStation(BaseModel):
    lat: int | float | None
    line_id: str
    line_name: str
    lng: int | float | None
    station_id: str
    station_name: str