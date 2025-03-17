from typing import Annotated, Any, Optional

from pydantic import BaseModel, Field
from pydantic.types import StringConstraints

from app.core.config import HHSettings

hh = HHSettings()


class QueryParameters(BaseModel):
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
    salary: int | float | None = None
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
    

class HeaderParameters(BaseModel):
    user_agent: Annotated[str, StringConstraints(pattern=hh.USER_AGENT_PATTERN)] = Field(default=hh.USER_AGENT)
    authorization: Annotated[str, StringConstraints(pattern=hh.AUTHORIZATION_PATTERN)] = Field(default=hh.AUTHORIZATION)
    

class Response(BaseModel):
    items: list["Item"]
    found: int
    page: int
    pages: int
    per_page: int
    clusters: list["Cluster"] | None = None
    arguments: list["Argument"] | None = None
    alternate_url: str | None = None
    fixes: Optional["Fix"] = None
    suggests: Optional["Suggest"] = None
    

class Item(BaseModel):
    accept_incomplete_resumes: bool
    accept_temporary: bool | None = None
    address: Optional["Address"] = None
    alternate_url: str
    apply_alternate_url: str
    archived: bool | None = None
    area: "Area"
    contacts: Optional["Contact"] = None
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
    salary: Optional["Salary"]
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
    

class Metro(BaseModel):
    lat: int | float | None
    line_id: str
    line_name: str
    lng: int | float | None
    station_id: str
    station_name: str
    
    
class MetroStation(BaseModel):
    lat: int | float | None
    line_id: str
    line_name: str
    lng: int | float | None
    station_id: str
    station_name: str


class Area(BaseModel):
    id: str
    name: str
    url: str
    

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
    

class EmployerRating(BaseModel):
    reviews_count: Any
    total_rating: str
    

class LogoUrl(BaseModel):
    px90: str | None = Field(None, alias="90")
    px240: str | None = Field(None, alias="240")
    original: str
    

class FlyInFlyOutDuration(BaseModel):
    id: str | None = None
    name: str | None = None
    

class InsiderInterview(BaseModel):
    id: str
    url: str
    

class ProfessionalRole(BaseModel):
    id: str | None = None
    name: str | None = None
    

class Salary(BaseModel):
    currency: str | None = None
    from_: int | None = Field(None, alias="from")
    gross: bool | None = None
    to: int | None = None
    

class Type(BaseModel):
    id: str
    name: str | None = None
    

class WorkFormat(BaseModel):
    id: str | None = None
    name: str | None = None
    

class WorkScheduleByDays(BaseModel):
    id: str | None = None
    name: str | None = None
    

class WorkingHours(BaseModel):
    id: str | None = None
    name: str | None = None
    

class Counter(BaseModel):
    responses: int | float | None = None
    total_responses: int | float | None = None
    

class EmploymentForm(BaseModel):
    id: str | None = None
    name: str | None = None
    

class Experience(BaseModel):
    id: str | None = None
    name: str | None = None
    

class Snippet(BaseModel):
    requirement: str | None = None
    responsibility: str | None = None
    

class VideoVacancy(BaseModel):
    cover_picture: Optional["CoverPicture"] = None
    snippet_picture_url: str | None = None
    snippet_video_url: str | None = None
    video_url: Annotated[str, StringConstraints(min_length=1)] | None = None
    

class CoverPicture(BaseModel):
    resized_height: int | float
    resized_path: Annotated[str, StringConstraints(min_length=1)]
    resized_width: int | float
    

class Cluster(BaseModel):
    id: str
    items: list["ClusterItem"]
    name: str
    

class ClusterItem(BaseModel):
    count: int | float
    metro_line: Optional["MetroLine"] = None
    metro_station: Optional["ClusterMetroStation"] = None
    name: str
    type_: str | None = Field(None, alias="type")
    url: str
    

class MetroLine(BaseModel):
    area: "Area"
    hex_color: str
    id: str
    

class ClusterMetroStation(BaseModel):
    area: "Area"
    hex_color: str
    id: str
    lat: int | float
    lng: int | float
    order: int | float
    

class Argument(BaseModel):
    argument: str
    cluster_group: Optional["ClusterGroup"] = None
    disable_url: str
    hex_color: str | None = None
    metro_type: str | None = None
    name: str | None = None
    value: str
    value_description: str | None
    

class ClusterGroup(BaseModel):
    id: str
    name: str
    

class Fix(BaseModel):
    fixed: str | None = None
    original: str | None = None
    

class Suggest(BaseModel):
    found: int | None = None
    value: str | None = None