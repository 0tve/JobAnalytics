from typing import Annotated, Any, Optional

from pydantic import BaseModel, Field, ConfigDict
from pydantic.types import StringConstraints

from app.config import HHSettings

hh = HHSettings()


class Vacancy(BaseModel):
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
    contacts: Optional["Contacts"] = None
    department: Optional["Department"] = None
    description: str
    driver_license_types: list["DriverLicenseType"]
    employer_for_applicant: Optional["EmployerForApplicant"] = Field(None, alias="employer")
    employment_form: Optional["EmploymentForm"] = None
    experience: Optional["Experience"] = None
    fly_in_fly_out_duration: Optional[list["FlyInFlyOutDuration"]] = None
    has_test: bool
    id: str
    initial_created_at: str
    insider_interview: Optional["InsiderInterview"] = None
    internship: bool | None = None
    key_skills: list["KeySkill"]
    languages: Optional[list["Language"]] = None
    name: str
    negotiations_url: str | None = None
    night_shifts: bool | None = None
    premium: bool
    professional_roles: list["ProfessionalRole"]
    published_at: str
    relations: list[str] | None = None
    response_letter_required: bool
    response_url: str | None = None
    salary_range: Optional["SalaryRange"] = None
    suitable_resumes_url: str | None = None
    test: Optional["Test"] = None
    type_: Optional["Type"] = Field(None, alias="type")
    vacancy_properties: Optional["VacancyProperty"] = None
    video_vacancy: Optional["VideoVacancy"] = None
    work_format: list["WorkFormat"] | None = None
    work_schedule_by_days: list["WorkScheduleByDays"] | None = None
    working_hours: list["WorkingHours"] | None = None
    address_for_applicant: Optional["AddressForApplicant"] = Field(None, alias="address")

    model_config = ConfigDict(validate_by_name=True, from_attributes=True)
    

class VacancySearch(BaseModel):
    vacancies_short: list["VacancyShort"] = Field(alias="items")
    found: int
    page: int
    pages: int
    per_page: int
    clusters: list["Cluster"] | None = None
    arguments: list["Argument"] | None = None
    alternate_url: str | None = None
    fixes: Optional["Fix"] = None
    suggests: Optional["Suggests"] = None
    
    model_config = ConfigDict(from_attributes=True)


class VacancyShort(BaseModel):
    accept_incomplete_resumes: bool
    accept_temporary: bool | None = None
    address: Optional["Address"] = None
    alternate_url: str
    apply_alternate_url: str
    archived: bool | None = None
    area: "Area"
    contacts: Optional["Contacts"] = None
    created_at: str | None = None
    department: Optional["Department"]
    employer: "Employer"
    fly_in_fly_out_duration: list["FlyInFlyOutDuration"] | None = None
    has_test: bool
    id: str
    insider_interview: Optional["InsiderInterview"] = None
    internship: bool | None = None
    metro_stations: Optional["MetroStation"] = None
    name: str
    night_shifts: bool | None = None
    premium: bool | None = None
    professional_roles: list["ProfessionalRole"]
    published_at: str
    relations: list[str] | None
    response_letter_required: bool
    response_url: str | None = None
    salary_range: Optional["SalaryRange"]
    sort_point_distance: int | float | None
    type_: "Type" = Field(alias="type")
    url: str
    work_format: list["WorkFormat"] | None = None
    work_schedule_by_days: list["WorkScheduleByDays"] | None = None
    working_hours: list["WorkingHours"] | None = None
    counters: Optional["Counter"] = None
    employment_form: Optional["EmploymentForm"] = None
    experience: Optional["Experience"] = None
    snippet: "Snippet"
    show_logo_in_search: bool | None = None
    video_vacancy: Optional["VideoVacancy"] = None
    
    model_config = ConfigDict(validate_by_name=True, from_attributes=True)


class VacancyPath(BaseModel):
    vacancy_id: str
    

class VacancyParams(BaseModel):
    locale: str = "RU"
    host: str = "hh.ru"


class VacancyHeaders(BaseModel):
    user_agent: Annotated[str, StringConstraints(pattern=hh.USER_AGENT_PATTERN)] = Field(default=hh.USER_AGENT)
    authorization: Annotated[str, StringConstraints(pattern=hh.AUTHORIZATION_PATTERN)] = Field(default=hh.AUTHORIZATION)


class VacancySearchParams(BaseModel):
    page: int | float | None = 0
    per_page: Annotated[int | float, Field(le=100)] | None = 10
    text: str | None = None
    search_field: str | None = None
    experience: str | None = None
    employment: str | None = None
    schedule: str | None = None
    area: str | None = None
    metro: str | None = None
    professional_role: str | None = None
    industry: str | None = None
    employer_id: str | None = None
    currency: str | None = None
    salary_range: int | float | None = None
    label: str | None = None
    only_with_salary: bool = False
    period: int | float | None = None
    date_from: str | None = None
    date_to: str | None = None
    top_lat: int | float | None = None
    bottom_lat: int | float | None = None
    left_lng: int | float | None = None
    right_lng: int | float | None = None
    order_by: str | None = None
    sort_point_lat: int | float | None = None
    sort_point_lng: int | float | None = None
    clusters: bool = False
    describe_arguments: bool = False
    no_magic: bool = False
    premium: bool = False
    responses_count_enabled: bool = False
    part_time: str | None = None
    accept_temporary: bool = False
    locale: str = "RU"
    host: str = "hh.ru"
    

class VacancySearchHeaders(BaseModel):
    user_agent: Annotated[str, StringConstraints(pattern=hh.USER_AGENT_PATTERN)] = Field(default=hh.USER_AGENT)
    authorization: Annotated[str, StringConstraints(pattern=hh.AUTHORIZATION_PATTERN)] = Field(default=hh.AUTHORIZATION)


class BillingType(BaseModel):
    id: str
    name: str | None = None
    
    model_config = ConfigDict(from_attributes=True)


class Area(BaseModel):
    id: str
    name: str
    url: str
    
    model_config = ConfigDict(from_attributes=True)
    
    
class Department(BaseModel):
    id: str | None = None
    name: str | None = None
    
    model_config = ConfigDict(from_attributes=True)


class DriverLicenseType(BaseModel):
    id: str | None = None
    
    model_config = ConfigDict(from_attributes=True)


class EmployerRating(BaseModel):
    reviews_count: Any
    total_rating: str
    
    model_config = ConfigDict(from_attributes=True)
    

class LogoUrl(BaseModel):
    px90: str | None = Field(None, alias="90")
    px240: str | None = Field(None, alias="240")
    original: str
    
    model_config = ConfigDict(from_attributes=True)
    

class FlyInFlyOutDuration(BaseModel):
    id: str | None = None
    name: str | None = None
    
    model_config = ConfigDict(from_attributes=True)


class InsiderInterview(BaseModel):
    id: str
    url: str
    
    model_config = ConfigDict(from_attributes=True)
    

class ProfessionalRole(BaseModel):
    id: str | None = None
    name: str | None = None
    
    model_config = ConfigDict(from_attributes=True)
    

class KeySkill(BaseModel):
    name: str | None = None
    
    model_config = ConfigDict(from_attributes=True)
    

class Language(BaseModel):
    id: str
    level: "Level"
    name: str
    
    model_config = ConfigDict(from_attributes=True)
    

class Level(BaseModel):
    id: str
    name: str
    
    model_config = ConfigDict(from_attributes=True)
    

class SalaryRange(BaseModel):
    currency: str | None = None
    frequency: Optional["Frequency"] = None
    from_: int | None = Field(None, alias="from")
    gross: bool | None = None
    mode: "Mode"
    to: int | None = None
    
    model_config = ConfigDict(validate_by_name=True, from_attributes=True)
    

class Frequency(BaseModel):
    id: str
    name: str | None
    
    model_config = ConfigDict(from_attributes=True)
    

class Mode(BaseModel):
    id: str
    name: str | None
    
    model_config = ConfigDict(from_attributes=True)


class VacancyProperty(BaseModel):
    appearance: Optional["Appearance"] = None
    properties: list["Properties"] | None = None
    

class Appearance(BaseModel):
    title: str | None = None
    
    model_config = ConfigDict(from_attributes=True)
    

class Properties(BaseModel):
    end_time: str | None = None
    parameters: list[str] | None = None
    property_type: str | None = None
    start_time: str | None = None
    
    model_config = ConfigDict(from_attributes=True)


class Test(BaseModel):
    id: str | None = None
    required: bool | None = None
    
    model_config = ConfigDict(from_attributes=True)


class Type(BaseModel):
    id: str
    name: str
    
    model_config = ConfigDict(from_attributes=True)


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
    
    model_config = ConfigDict(from_attributes=True)
    

class EmployerForApplicant(BaseModel):
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
    
    model_config = ConfigDict(from_attributes=True)


class ApplicantService(BaseModel):
    target_employer: Optional["TargetEmployer"] = None
    
    model_config = ConfigDict(from_attributes=True)
    

class TargetEmployer(BaseModel):
    count: int | float | None = None
    
    model_config = ConfigDict(from_attributes=True)


class Counter(BaseModel):
    responses: int | float | None = None
    total_responses: int | float | None = None
    
    model_config = ConfigDict(from_attributes=True)


class Snippet(BaseModel):
    requirement: str | None = None
    responsibility: str | None = None
    
    model_config = ConfigDict(from_attributes=True)


class Contacts(BaseModel):
    call_tracking_enabled: bool | None = None
    email: str | None = None
    name: str | None = None
    phones: list["Phone"] | None = None
    
    model_config = ConfigDict(from_attributes=True)
    

class Phone(BaseModel):
    city: str | None = None
    comment: str | None = None
    country: str | None = None
    formatted: str | None = None
    number: str | None = None
    
    model_config = ConfigDict(from_attributes=True)


class Experience(BaseModel):
    id: str | None = None
    name: str | None = None
    
    model_config = ConfigDict(from_attributes=True)


class Address(BaseModel):
    building: str | None = None
    city: str | None = None
    description: str | None = None
    id: str | None = None
    lat: int | float | None = None
    lng: int | float | None = None
    metro: Optional["Metro"] = None
    metro_stations: list["MetroStation"] | None = None
    raw: str | None = None
    street: str | None = None
    
    model_config = ConfigDict(from_attributes=True)


class Metro(BaseModel):
    lat: int | float | None
    line_id: str
    line_name: str
    lng: int | float | None
    station_id: str
    station_name: str
    
    model_config = ConfigDict(from_attributes=True)
    

class MetroStation(BaseModel):
    lat: int | float | None
    line_id: str
    line_name: str
    lng: int | float | None
    station_id: str
    station_name: str
    
    model_config = ConfigDict(from_attributes=True)
    

class WorkFormat(BaseModel):
    id: str | None = None
    name: str | None = None
    
    model_config = ConfigDict(from_attributes=True)
    

class WorkScheduleByDays(BaseModel):
    id: str | None = None
    name: str | None = None
    
    model_config = ConfigDict(from_attributes=True)
    

class WorkingHours(BaseModel):
    id: str | None = None
    name: str | None = None
    
    model_config = ConfigDict(from_attributes=True)
    

class AddressForApplicant(BaseModel):
    building: str | None = None
    city: str | None = None
    lat: int | float | None = None
    lng: int | float | None = None
    street: str | None = None
    description: str | None = None
    metro_stations: list["MetroStation"] | None = None
    
    model_config = ConfigDict(from_attributes=True)
    

class EmploymentForm(BaseModel):
    id: str | None = None
    name: str | None = None
    
    model_config = ConfigDict(from_attributes=True)


class VideoVacancy(BaseModel):
    cover_picture: Optional["CoverPicture"] = None
    snippet_picture: Optional["SnippetPicture"] = None
    snippet_video: Optional["SnippetVideo"] = None
    video: Optional["Video"] = None
    
    model_config = ConfigDict(from_attributes=True)
   

class SnippetPicture(BaseModel):
    url: Annotated[str, StringConstraints(min_length=1)]
    
    model_config = ConfigDict(from_attributes=True)
    

class SnippetVideo(BaseModel):
    upload_id: Annotated[str, StringConstraints(min_length=1)]
    url: Annotated[str, StringConstraints(min_length=1)]
    
    model_config = ConfigDict(from_attributes=True)
    

class Video(BaseModel):
    upload_id: Annotated[str, StringConstraints(min_length=1)]
    url: Annotated[str, StringConstraints(min_length=1)]
    
    model_config = ConfigDict(from_attributes=True)
    

class CoverPicture(BaseModel):
    resized_height: int | float
    resized_path: Annotated[str, StringConstraints(min_length=1)]
    resized_width: int | float
    
    model_config = ConfigDict(from_attributes=True)
    

class Cluster(BaseModel):
    id: str
    items: list["ClusterItem"]
    name: str
    
    model_config = ConfigDict(from_attributes=True)
    

class ClusterItem(BaseModel):
    count: int | float
    metro_line: Optional["MetroLine"] = None
    metro_station: Optional["ClusterMetroStation"] = None
    name: str
    type_: str | None = Field(None, alias="type")
    url: str
    
    model_config = ConfigDict(validate_by_name=True, from_attributes=True)
    

class MetroLine(BaseModel):
    area: "Area"
    hex_color: str
    id: str
    
    model_config = ConfigDict(from_attributes=True)
    

class ClusterMetroStation(BaseModel):
    area: "Area"
    hex_color: str
    id: str
    lat: int | float
    lng: int | float
    order: int | float
    
    model_config = ConfigDict(from_attributes=True)
    

class Argument(BaseModel):
    argument: str
    cluster_group: Optional["ClusterGroup"] = None
    disable_url: str
    hex_color: str | None = None
    metro_type: str | None = None
    name: str | None = None
    value: str
    value_description: str | None
    
    model_config = ConfigDict(from_attributes=True)
    

class ClusterGroup(BaseModel):
    id: str
    name: str
    
    model_config = ConfigDict(from_attributes=True)
    

class Fix(BaseModel):
    fixed: str | None = None
    original: str | None = None
    
    model_config = ConfigDict(from_attributes=True)
    

class Suggests(BaseModel):
    found: int | None = None
    value: str | None = None
    
    model_config = ConfigDict(from_attributes=True)