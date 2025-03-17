from typing import Optional

from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models.base import Base


class Response(Base):
    __tablename__ = "responses"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    items: Mapped[list["Item"]] = relationship(back_populates="response")
    found: Mapped[int]
    page: Mapped[int]
    pages: Mapped[int]
    per_page: Mapped[int]
    clusters: Mapped[Optional[list["Cluster"]]] = relationship(back_populates="response")
    arguments: Mapped[Optional[list["Argument"]]] = relationship(back_populates="response")
    alternate_url: Mapped[Optional[str]]
    fixes: Mapped[Optional["Fix"]] = relationship(back_populates="response")
    suggests: Mapped[Optional["Suggest"]] = relationship(back_populates="response")


class Item(Base):
    __tablename__ = "items"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    accept_incomplete_resumes: Mapped[bool]
    accept_temporary: Mapped[Optional[bool]]
    address: Mapped[Optional["Address"]] = relationship(back_populates="item")
    alternate_url: Mapped[str]
    apply_alternate_url: Mapped[str]
    archived: Mapped[Optional[bool]]
    area: Mapped["Area"] = relationship(back_populates="item")
    contacts: Mapped[Optional["Contact"]] = relationship(back_populates="item")
    created_at: Mapped[Optional[str]]
    department: Mapped["Department"] = relationship(back_populates="item")
    employer: Mapped["Employer"] = relationship(back_populates="item")
    fly_in_fly_out_duration: Mapped[Optional[list["FlyInFlyOutDuration"]]] = relationship(back_populates="item")
    has_test: Mapped[bool]
    id: Mapped[str] = mapped_column(primary_key=True)
    insider_interview: Mapped[Optional["InsiderInterview"]] = relationship(back_populates="item")
    internship: Mapped[Optional[bool]]
    metro_stations: Mapped[Optional[list["MetroStation"]]] = relationship(back_populates="item")
    name: Mapped[str]
    night_shifts: Mapped[Optional[bool]]
    premium: Mapped[Optional[bool]]
    professional_roles: Mapped[list["ProfessionalRole"]] = relationship(back_populates="item")
    published_at: Mapped[str]
    relations: Mapped[Optional[list[str]]] = mapped_column(ARRAY(String))
    response_letter_required: Mapped[bool]
    response_url: Mapped[Optional[str]]
    salary: Mapped["Salary"] = relationship(back_populates="item")
    sort_point_distance: Mapped[Optional[int]]
    type_: Mapped["Type"] = relationship(back_populates="item")
    url: Mapped[str]
    work_format: Mapped[list["WorkFormat"]] = relationship(back_populates="item")
    work_schedule_by_days: Mapped[list["WorkScheduleByDays"]] = relationship(back_populates="item")
    working_hours: Mapped[list["WorkingHours"]] = relationship(back_populates="item")
    counters: Mapped["Counter"] = relationship(back_populates="item")
    employment_form: Mapped["EmploymentForm"] = relationship(back_populates="item")
    experience: Mapped["Experience"] = relationship(back_populates="item")
    snippet: Mapped["Snippet"] = relationship(back_populates="item")
    show_logo_in_search: Mapped[Optional[bool]]
    video_vacancy: Mapped[Optional["VideoVacancy"]] = relationship(back_populates="item")
    
    response_id: Mapped[int] = mapped_column(ForeignKey("public_vacancies_search.responses.id"))

    response: Mapped["Response"] = relationship(back_populates="items")
    
    
class Address(Base):
    __tablename__ = "addresses"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    building: Mapped[Optional[str]]
    city: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    id: Mapped[str] = mapped_column(primary_key=True)
    lat: Mapped[Optional[float]]
    lng: Mapped[Optional[float]]
    metro: Mapped[Optional["Metro"]] = relationship(back_populates="address")
    metro_stations: Mapped[Optional[list["MetroStation"]]] = relationship(back_populates="address")
    raw: Mapped[Optional[str]]
    street: Mapped[Optional[str]]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))
    
    item: Mapped["Item"] = relationship(back_populates="address")
    
    
class Metro(Base):
    __tablename__ = "metros"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    lat: Mapped[Optional[float]]
    line_id: Mapped[str]
    line_name: Mapped[str]
    lng: Mapped[Optional[float]]
    station_id: Mapped[str]
    station_name: Mapped[str]
    
    address_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.addresses.id"))
    
    address: Mapped["Address"] = relationship(back_populates="metro")
    
    
class MetroStation(Base):
    __tablename__ = "metro_stations"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    lat: Mapped[Optional[float]]
    line_id: Mapped[str]
    line_name: Mapped[str]
    lng: Mapped[Optional[float]]
    station_id: Mapped[str]
    station_name: Mapped[str]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))
    address_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.addresses.id"))
        
    item: Mapped["Item"] = relationship(back_populates="metro_stations")
    address: Mapped["Address"] = relationship(back_populates="metro_stations")

class Area(Base):
    __tablename__ = "areas"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    url: Mapped[str]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))
    metro_line_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.metro_lines.id"))
    cluster_metro_station_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.cluster_metro_stations.id"))
    
    item: Mapped["Item"] = relationship(back_populates="area")
    metro_line: Mapped["MetroLine"] = relationship(back_populates="area")
    cluster_metro_station: Mapped["ClusterMetroStation"] = relationship(back_populates="area")

class Contact(Base):
    __tablename__ = "contacts"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    call_tracking_enabled: Mapped[Optional[bool]]
    email: Mapped[Optional[str]]
    name: Mapped[Optional[str]]
    phones: Mapped[Optional[list["Phone"]]] = relationship(back_populates="contact")
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))
    
    item: Mapped["Item"] = relationship(back_populates="contact")
    
class Phone(Base):
    __tablename__ = "phones"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city: Mapped[Optional[str]]
    comment: Mapped[Optional[str]]
    country: Mapped[Optional[str]]
    formatted: Mapped[Optional[str]]
    number: Mapped[Optional[str]]
    
    contact_id: Mapped[int] = mapped_column(ForeignKey("public_vacancies_search.contacts.id"))
    
    contact: Mapped["Contact"] = relationship(back_populates="phones")
    
    
class Department(Base):
    __tablename__ = "departments"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))
    
    item: Mapped["Item"] = relationship(back_populates="department")
    
    
class Employer(Base):
    __tablename__ = "employers"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    accredited_it_employer: Mapped[Optional[bool]]
    alternate_url: Mapped[Optional[str]]
    employer_rating: Mapped["EmployerRating"] = relationship(back_populates="employer")
    id: Mapped[str] = mapped_column(primary_key=True)
    logo_urls: Mapped["LogoUrl"] = relationship(back_populates="employer")
    name: Mapped[str]
    trusted: Mapped[bool]
    url: Mapped[Optional[str]]
    vacancies_url: Mapped[Optional[str]]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))
    
    item: Mapped["Item"] = relationship(back_populates="employer")


class EmployerRating(Base):
    __tablename__ = "employer_ratings"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    reviews_count: Mapped[int]
    total_rating: Mapped[str]
    
    employer_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.employers.id"))
    
    employer: Mapped["Employer"] = relationship(back_populates="employer_rating")


class LogoUrl(Base):
    __tablename__ = "logo_urls"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    px90: Mapped[Optional[str]]
    px240: Mapped[Optional[str]]
    original: Mapped[str]
    
    employer_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.employers.id"))
    
    employer: Mapped["Employer"] = relationship(back_populates="logo_urls")


class FlyInFlyOutDuration(Base):
    __tablename__ = "fly_in_fly_out_durations"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))

    item: Mapped["Item"] = relationship(back_populates="fly_in_fly_out_duration")


class InsiderInterview(Base):
    __tablename__ = "insider_interviews"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[str] = mapped_column(primary_key=True)
    url: Mapped[str]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))
    
    item: Mapped["Item"] = relationship(back_populates="insider_interview")
    

class ProfessionalRole(Base):
    __tablename__ = "professional_roles"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))
    
    item: Mapped["Item"] = relationship(back_populates="professional_role")


class Salary(Base):
    __tablename__ = "salaries"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    currency: Mapped[Optional[str]]
    from_: Mapped[Optional[int]] = mapped_column("from")
    gross: Mapped[Optional[bool]]
    to: Mapped[Optional[int]]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))
    
    item: Mapped["Item"] = relationship(back_populates="salary")


class Type(Base):
    __tablename__ = "types"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))
    
    item: Mapped["Item"] = relationship(back_populates="type")


class WorkFormat(Base):
    __tablename__ = "work_formats"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))
        
    item: Mapped["Item"] = relationship(back_populates="work_format")


class WorkScheduleByDays(Base):
    __tablename__ = "work_schedule_by_days"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))
    
    item: Mapped["Item"] = relationship(back_populates="work_schedule_by_days")
    

class WorkingHours(Base):
    __tablename__ = "working_hours"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))

    item: Mapped["Item"] = relationship(back_populates="working_hours")


class Counter(Base):
    __tablename__ = "counters"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    responses: Mapped[Optional[int]]
    total_responses: Mapped[Optional[int]]

    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))

    item: Mapped["Item"] = relationship(back_populates="counter")


class EmploymentForm(Base):
    __tablename__ = "employment_forms"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))

    item: Mapped["Item"] = relationship(back_populates="employment_form")


class Experience(Base):
    __tablename__ = "experiences"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))

    item: Mapped["Item"] = relationship(back_populates="experience")


class Snippet(Base):
    __tablename__ = "snippets"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    requirement: Mapped[Optional[str]]
    responsibility: Mapped[Optional[str]]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))

    item: Mapped["Item"] = relationship(back_populates="snippet")


class VideoVacancy(Base):
    __tablename__ = "video_vacancies"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cover_picture: Mapped[Optional["CoverPicture"]] = relationship(back_populates="video_vacancy")
    snippet_picture_url: Mapped[Optional[str]]
    snippet_video_url: Mapped[Optional[str]]
    video_url: Mapped[Optional[str]]
    
    item_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.items.id"))

    item: Mapped["Item"] = relationship(back_populates="video_vacancy")


class CoverPicture(Base):
    __tablename__ = "cover_pictures"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    resized_height: Mapped[int]
    resized_path: Mapped[str]
    resized_width: Mapped[int]
    
    video_vacancy_id: Mapped[int] = mapped_column(ForeignKey("public_vacancies_search.video_vacancies.id"))

    video_vacancy: Mapped["VideoVacancy"] = relationship(back_populates="cover_picture")
    

class Cluster(Base):
    __tablename__ = "clusters"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[str] = mapped_column(primary_key=True)
    items: Mapped[list["ClusterItem"]] = relationship(back_populates="cluster")
    name: Mapped[str]
    
    response_id: Mapped[int] = mapped_column(ForeignKey("public_vacancies_search.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="clusters")
    

class ClusterItem(Base):
    __tablename__ = "cluster_items"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    count: Mapped[int]
    metro_line: Mapped["MetroLine"] = relationship(back_populates="cluster_item")
    metro_station: Mapped["ClusterMetroStation"] = relationship(back_populates="cluster_item")
    name: Mapped[str]
    type_: Mapped[Optional[str]] = mapped_column("type")
    url: Mapped[str]
    
    cluster_id: Mapped[str] = mapped_column(ForeignKey("public_vacancies_search.clusters.id"))
    
    cluster: Mapped["Cluster"] = relationship(back_populates="items")
    
    
class MetroLine(Base):
    __tablename__ = "metro_lines"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    area: Mapped["Area"] = relationship(back_populates="metro_line")
    hex_color: Mapped[str]
    id: Mapped[str] = mapped_column(primary_key=True)
    
    cluster_item_id: Mapped[int] = mapped_column(ForeignKey("public_vacancies_search.cluster_items.id"))
    
    cluster_item: Mapped["ClusterItem"] = relationship(back_populates="metro_line")
    
    
class ClusterMetroStation(Base):
    __tablename__ = "cluster_metro_stations"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    area: Mapped["Area"] = relationship(back_populates="cluster_metro_station")
    hex_color: Mapped[str]
    id: Mapped[str] = mapped_column(primary_key=True)
    lat: Mapped[float]
    lng: Mapped[float]
    order: Mapped[float]
    
    cluster_item_id: Mapped[int] = mapped_column(ForeignKey("public_vacancies_search.cluster_items.id"))
    
    cluster_item: Mapped["ClusterItem"] = relationship(back_populates="metro_station")


class Argument(Base):
    __tablename__ = "arguments"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    argument: Mapped[str]
    cluster_group: Mapped["ClusterGroup"] = relationship(back_populates="argument")
    hex_color: Mapped[Optional[str]]
    metro_type: Mapped[Optional[str]]
    name: Mapped[Optional[str]]
    value: Mapped[str]
    value_description: Mapped[Optional[str]]
    
    response_id: Mapped[int] = mapped_column(ForeignKey("public_vacancies_search.responses.id"))
    
    response: Mapped["Response"] = relationship(back_populates="arguments")
    

class ClusterGroup(Base):
    __tablename__ = "cluster_groups"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    
    argument_id: Mapped[int] = mapped_column(ForeignKey("public_vacancies_search.arguments.id"))

    argument: Mapped["Argument"] = relationship(back_populates="cluster_group")


class Fix(Base):
    __tablename__ = "fixes"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fixed: Mapped[Optional[str]]
    original: Mapped[Optional[str]]

    response_id: Mapped[int] = mapped_column(ForeignKey("public_vacancies_search.responses.id"))

    response: Mapped["Response"] = relationship(back_populates="fixes")


class Suggest(Base):
    __tablename__ = "suggests"
    __table_args__ = {"schema": "public_vacancies_search"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    found: Mapped[Optional[int]]
    value: Mapped[Optional[str]]

    response_id: Mapped[int] = mapped_column(ForeignKey("public_vacancies_search.responses.id"))

    response: Mapped["Response"] = relationship(back_populates="suggests")