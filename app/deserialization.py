from app.models import (Address, AddressForApplicant, Appearance,
                        ApplicantService, Area, Argument, BillingType, Cluster,
                        ClusterGroup, ClusterItem, ClusterMetroStation,
                        Contacts, Counters, CoverPicture, Department,
                        DriverLicenseType, Employer, EmployerForApplicant,
                        EmployerRating, EmploymentForm, Experience, Fixes,
                        FlyInFlyOutDuration, Frequency, InsiderInterview,
                        KeySkill, Language, Level, LogoUrls, Metro, MetroLine,
                        MetroStation, Mode, Phone, ProfessionalRole, Property,
                        SalaryRange, Snippet, SnippetPicture, SnippetVideo,
                        Suggests, TargetEmployer, Test, Type, Vacancy,
                        VacancyProperties, VacancySearch, VacancyShort, Video,
                        VideoVacancy, WorkFormat, WorkingHours,
                        WorkScheduleByDays)
from app.schemas import Vacancy as VacancySchema
from app.schemas import VacancySearch as VacancySearchSchema



def vacancy_deserialize(vacancy: dict) -> Vacancy | None:
    
    if not vacancy:
        return
    
    vacancy = VacancySchema(**vacancy).model_dump(exclude_none=True)
    
    if "type" in vacancy:
        vacancy["type_"] = vacancy.pop("type")
        
    if "employer" in vacancy:
        vacancy["employer_for_applicant"] = vacancy.pop("employer")
        
    if "address" in vacancy:
        vacancy["address_for_applicant"] = vacancy.pop("address")

    if "area" in vacancy and vacancy["area"]:
        area = vacancy["area"]
        area = area_deserialize(area)
        vacancy["area"] = area
    
    if "billing_type" in vacancy and vacancy["billing_type"]:
        billing_type = vacancy["billing_type"]
        billing_type = billing_type_deserialize(billing_type)
        vacancy["billing_type"] = billing_type
        
    if "contacts" in vacancy and vacancy["contacts"]:
        contacts = vacancy["contacts"]
        contacts = contacts_deserialize(contacts)
        vacancy["contacts"] = contacts
        
    if "department" in vacancy and vacancy["department"]:
        department = vacancy["department"]
        department = department_deserialize(department)
        vacancy["department"] = department
    
    if "driver_license_types" in vacancy and vacancy["driver_license_types"]:
        driver_license_types = [driver_license_type_deserialize(driver_license_type) for driver_license_type in vacancy["driver_license_types"]]
        vacancy["driver_license_types"] = driver_license_types

    if "employer_for_applicant" in vacancy and vacancy["employer_for_applicant"]:
        employer_for_applicant = vacancy["employer_for_applicant"]
        employer_for_applicant = employer_for_applicant_deserialize(employer_for_applicant)
        vacancy["employer_for_applicant"] = employer_for_applicant
        
    if "employment_form" in vacancy and vacancy["employment_form"]:
        employment_form = vacancy["employment_form"]
        employment_form = employment_form_deserialize(employment_form)
        vacancy["employment_form"] = employment_form
        
    if "experience" in vacancy and vacancy["experience"]:
        experience = vacancy["experience"]
        experience = experience_deserialize(experience)
        vacancy["experience"] = experience
    
    if "fly_in_fly_out_duration" in vacancy and vacancy["fly_in_fly_out_duration"]:
        fly_in_fly_out_duration = [fly_in_fly_out_duration_deserialize(fly_in_fly_out_duration) for fly_in_fly_out_duration in vacancy["fly_in_fly_out_duration"]]
        vacancy["fly_in_fly_out_duration"] = fly_in_fly_out_duration
        
    if "insider_interview" in vacancy and vacancy["insider_interview"]:
        insider_interview = vacancy["insider_interview"]
        insider_interview = insider_interview_deserialize(insider_interview)
        vacancy["insider_interview"] = insider_interview
    
    if "key_skills" in vacancy and vacancy["key_skills"]:
        key_skills = [key_skill_deserialize(key_skill) for key_skill in vacancy["key_skills"]]
        vacancy["key_skills"] = key_skills

    if "languages" in vacancy and vacancy["languages"]:
        languages = [language_deserialize(language) for language in vacancy["languages"]]
        vacancy["languages"] = languages
            
    if "professional_roles" in vacancy and vacancy["professional_roles"]:
        professional_roles = [professional_role_deserialize(professional_role) for professional_role in vacancy["professional_roles"]]
        vacancy["professional_roles"] = professional_roles
    
    if "salary_range" in vacancy and vacancy["salary_range"]:
        salary_range = vacancy["salary_range"]
        salary_range = salary_range_deserialize(salary_range)
        vacancy["salary_range"] = salary_range
        
    if "test" in vacancy and vacancy["test"]:
        test = vacancy["test"]
        test = test_deserialize(test)
        vacancy["test"] = test
        
    if "type_" in vacancy and vacancy["type_"]:
        type_ = vacancy["type_"]
        type_ = type_deserialize(type_)
        vacancy["type_"] = type_
        
    if "vacancy_properties" in vacancy and vacancy["vacancy_properties"]:
        vacancy_properties = vacancy["vacancy_properties"]
        vacancy_properties = vacancy_property_deserialize(vacancy_properties)
        vacancy["vacancy_properties"] = vacancy_properties
        
    if "video_vacancy" in vacancy and vacancy["video_vacancy"]:
        video_vacancy = vacancy["video_vacancy"]
        video_vacancy = video_vacancy_deserialize(video_vacancy)
        vacancy["video_vacancy"] = video_vacancy
    
    if "work_format" in vacancy and vacancy["work_format"]:
        work_format = [work_format_deserialize(work_format) for work_format in vacancy["work_format"]]
        vacancy["work_format"] = work_format

    if "work_schedule_by_days" in vacancy and vacancy["work_schedule_by_days"]:
        work_schedule_by_days = [work_schedule_by_days_deserialize(work_schedule_by_days) for work_schedule_by_days in vacancy["work_schedule_by_days"]]
        vacancy["work_schedule_by_days"] = work_schedule_by_days
        
    if "working_hours" in vacancy and vacancy["working_hours"]:
        working_hours = [working_hours_deserialize(working_hours) for working_hours in vacancy["working_hours"]]
        vacancy["working_hours"] = working_hours
    
    if "address_for_applicant" in vacancy and vacancy["address_for_applicant"]:
        address_for_applicant = vacancy["address_for_applicant"]
        address_for_applicant = address_for_applicant_deserialize(address_for_applicant)
        vacancy["address_for_applicant"] = address_for_applicant

    vacancy = Vacancy(**vacancy)
    return vacancy

def vacancy_search_deserialize(vacancy_search: dict) -> VacancySearch | None:
    
    if not vacancy_search:
        return
    
    vacancy_search = VacancySearchSchema(**vacancy_search).model_dump(exclude_none=True)

    if "items" in vacancy_search:
        vacancy_search["vacancies_short"] = vacancy_search.pop("items")
    
    if "vacancies_short" in vacancy_search and vacancy_search["vacancies_short"]:
        vacancies_short = [vacancy_short_deserialize(vacancy_short) for vacancy_short in vacancy_search["vacancies_short"]]
        vacancy_search["vacancies_short"] = vacancies_short
        
    if "clusters" in vacancy_search and vacancy_search["clusters"]:
        clusters = [cluster_deserialize(cluster) for cluster in vacancy_search["clusters"]]
        vacancy_search["clusters"] = clusters
        
    if "arguments" in vacancy_search and vacancy_search["arguments"]:
        arguments = [argument_deserialize(argument) for argument in vacancy_search["arguments"]]
        vacancy_search["arguments"] = arguments
        
    if "fixes" in vacancy_search and vacancy_search["fixes"]:
        fixes = vacancy_search["fixes"]
        fixes = fixes_deserialize(fixes)
        vacancy_search["fixes"] = fixes
        
    if "suggests" in vacancy_search and vacancy_search["suggests"]:
        suggests = vacancy_search["suggests"]
        suggests = suggests_deserialize(suggests)
        vacancy_search["suggests"] = suggests
    
    vacancy_search = VacancySearch(**vacancy_search)
    return vacancy_search
    
def vacancy_short_deserialize(vacancy_short: dict) -> VacancyShort | None:
    
    if not vacancy_short:
        return
    
    if "type" in vacancy_short:
        vacancy_short["type_"] = vacancy_short.pop("type")
    
    if "address" in vacancy_short and vacancy_short["address"]:
        address = vacancy_short["address"]
        address = address_deserialize(address)
        vacancy_short["address"] = address
        
    if "area" in vacancy_short and vacancy_short["area"]:
        area = vacancy_short["area"]
        area = area_deserialize(area)
        vacancy_short["area"] = area
        
    if "contacts" in vacancy_short and vacancy_short["contacts"]:
        contacts = vacancy_short["contacts"]
        contacts = contacts_deserialize(contacts)
        vacancy_short["contacts"] = contacts

    if "department" in vacancy_short and vacancy_short["department"]:
        department = vacancy_short["department"]
        department = department_deserialize(department)
        vacancy_short["department"] = department

    if "employer" in vacancy_short and vacancy_short["employer"]:
        employer = vacancy_short["employer"]
        employer = employer_deserialize(employer)
        vacancy_short["employer"] = employer

    if "fly_in_fly_out_duration" in vacancy_short and vacancy_short["fly_in_fly_out_duration"]:
        fly_in_fly_out_duration = [fly_in_fly_out_duration_deserialize(fly_in_fly_out_duration) for fly_in_fly_out_duration in vacancy_short["fly_in_fly_out_duration"]]
        vacancy_short["fly_in_fly_out_duration"] = fly_in_fly_out_duration

    if "insider_interview" in vacancy_short and vacancy_short["insider_interview"]:
        insider_interview = vacancy_short["insider_interview"]
        insider_interview = insider_interview_deserialize(insider_interview)
        vacancy_short["insider_interview"] = insider_interview

    if "metro_station" in vacancy_short and vacancy_short["metro_station"]:
        metro_station = [metro_station_deserialize(metro_station) for metro_station in vacancy_short["metro_station"]]
        vacancy_short["metro_station"] = metro_station

    if "professional_roles" in vacancy_short and vacancy_short["professional_roles"]:
        professional_role = [professional_role_deserialize(professional_role) for professional_role in vacancy_short["professional_roles"]]
        vacancy_short["professional_roles"] = professional_role

    if "salary_range" in vacancy_short and vacancy_short["salary_range"]:
        salary_range = vacancy_short["salary_range"]
        salary_range = salary_range_deserialize(salary_range)
        vacancy_short["salary_range"] = salary_range

    if "type_" in vacancy_short and vacancy_short["type_"]:
        type_ = vacancy_short["type_"]
        type_ = type_deserialize(type_)
        vacancy_short["type_"] = type_

    if "work_format" in vacancy_short and vacancy_short["work_format"]:
        work_format = [work_format_deserialize(work_format) for work_format in vacancy_short["work_format"]]
        vacancy_short["work_format"] = work_format

    if "work_schedule_by_days" in vacancy_short and vacancy_short["work_schedule_by_days"]:
        work_schedule_by_days = [work_schedule_by_days_deserialize(work_schedule_by_days) for work_schedule_by_days in vacancy_short["work_schedule_by_days"]]
        vacancy_short["work_schedule_by_days"] = work_schedule_by_days

    if "working_hours" in vacancy_short and vacancy_short["working_hours"]:
        working_hours = [working_hours_deserialize(working_hours) for working_hours in vacancy_short["working_hours"]]
        vacancy_short["working_hours"] = working_hours

    if "counters" in vacancy_short and vacancy_short["counters"]:
        counters = vacancy_short["counters"]
        counters = counters_deserialize(counters)
        vacancy_short["counters"] = counters

    if "employment_form" in vacancy_short and vacancy_short["employment_form"]:
        employment_form = vacancy_short["employment_form"]
        employment_form = employment_form_deserialize(employment_form)
        vacancy_short["employment_form"] = employment_form

    if "experience" in vacancy_short and vacancy_short["experience"]:
        experience = vacancy_short["experience"]
        experience = experience_deserialize(experience)
        vacancy_short["experience"] = experience

    if "snippet" in vacancy_short and vacancy_short["snippet"]:
        snippet = vacancy_short["snippet"]
        snippet = snippet_deserialize(snippet)
        vacancy_short["snippet"] = snippet

    if "video_vacancy" in vacancy_short and vacancy_short["video_vacancy"]:
        video_vacancy = vacancy_short["video_vacancy"]
        video_vacancy = video_vacancy_deserialize(video_vacancy)
        vacancy_short["video_vacancy"] = video_vacancy
        
    vacancy_short = VacancyShort(**vacancy_short)
    return vacancy_short

def fixes_deserialize(fixes: dict) -> Fixes | None:
    
    if not fixes:
        return
    
    fixes = Fixes(**fixes)
    return fixes

def suggests_deserialize(suggests: dict) -> Suggests | None:
    
    if not suggests:
        return
    
    suggests = Suggests(**suggests)
    return suggests

def argument_deserialize(argument: dict) -> Argument | None:
    
    if not argument:
        return
    
    if "cluster_group" in argument and argument["cluster_group"]:
        cluster_group = argument["cluster_group"]
        cluster_group = ClusterGroup(cluster_group)
        argument["cluster_group"] = cluster_group
        
    argument = Argument(**argument)
    return argument

def counters_deserialize(counters: dict) -> Counters | None:
    
    if not counters:
        return
    
    counters = Counters(**counters)
    return counters

def snippet_deserialize(snippet: dict) -> Snippet | None:
    
    if not snippet:
        return
    
    snippet = Snippet(**snippet)
    return snippet

def employer_deserialize(employer: dict) -> Employer | None:
    
    if not employer:
        return
    
    if "employer_rating" in employer and employer["employer_rating"]:
        employer_rating = employer["employer_rating"]
        employer_rating = employer_rating_deserialize(employer_rating)
        employer["employer_rating"] = employer_rating
        
    if "logo_urls" in employer and employer["logo_urls"]:
        logo_urls = employer["logo_urls"]
        logo_urls = logo_urls_deserialize(logo_urls)
        employer["logo_urls"] = logo_urls
        
    employer = Employer(**employer)
    return employer

def address_deserialize(address: dict) -> Address | None:
    
    if not address:
        return
    
    if "metro" in address and address["metro"]:
        metro = address["metro"]
        metro = metro_deserialize(metro)
        address["metro"] = metro
        
    if "metro_stations" in address and address["metro_stations"]:
        metro_stations = [metro_station_deserialize(metro_station) for metro_station in address["metro_stations"]]
        address["metro_stations"] = metro_stations
        
    address = Address(**address)
    return address

def metro_deserialize(metro: dict) -> Metro | None:
    
    if not metro:
        return
    
    metro = Metro(**metro)
    return metro

def cluster_deserialize(cluster: dict) -> Cluster | None:
    
    if not cluster:
        return
    
    if "items" in cluster:
        cluster["cluster_items"] = cluster.pop("items")
        
    if "cluster_items" in cluster and cluster["cluster_items"]:
        cluster_items = [cluster_item_deserialize(cluster_item) for cluster_item in cluster["cluster_items"]]
        cluster["cluster_items"] = cluster_items
        
    cluster = Cluster(**cluster)
    return cluster

def cluster_item_deserialize(cluster_item: dict) -> ClusterItem | None:
    
    if not cluster_item:
        return
    
    if "metro_station" in cluster_item:
        cluster_item["cluster_metro_station"] = cluster_item.pop("metro_station")
    
    if "metro_line" in cluster_item and cluster_item["metro_line"]:
        metro_line = cluster_item["metro_line"]
        metro_line = metro_line_deserialize(metro_line)
        cluster_item["metro_line"] = metro_line
        
    if "cluster_metro_station" in cluster_item and cluster_item["cluster_metro_station"]:
        cluster_metro_station = cluster_item["cluster_metro_station"]
        cluster_metro_station = cluster_metro_station_deserialize(cluster_metro_station)
        cluster_item["cluster_metro_station"] = cluster_metro_station
    
    cluster_item = ClusterItem(**cluster_item)
    return cluster_item

def metro_line_deserialize(metro_line: dict) -> MetroLine | None:
    
    if not metro_line:
        return
    
    if "area" in metro_line and metro_line["area"]:
        area = metro_line["area"]
        area = area_deserialize(area)
        metro_line["area"] = area
    
    metro_line = MetroLine(**metro_line)
    return metro_line

def cluster_metro_station_deserialize(cluster_metro_station: dict) -> ClusterMetroStation | None:
    
    if not cluster_metro_station:
        return
    
    if "area" in cluster_metro_station and cluster_metro_station["area"]:
        area = cluster_metro_station["area"]
        area = area_deserialize(area)
        cluster_metro_station["area"] = area
        
    cluster_metro_station = ClusterMetroStation(**cluster_metro_station)
    return cluster_metro_station
    
def area_deserialize(area: dict) -> Area | None:
    
    if not area:
        return
    
    area = Area(**area)
    return area
    
def billing_type_deserialize(billing_type: dict) -> BillingType | None:
    
    if not billing_type:
        return
    
    billing_type = BillingType(**billing_type)
    return billing_type
    
def contacts_deserialize(contacts: dict) -> Contacts | None:
    
    if not contacts:
        return
    
    if "phones" in contacts and contacts["phones"]:    
        phones = [phone_deserialize(phone) for phone in contacts["phones"]]
        contacts["phones"] = phones
               
    contacts = Contacts(**contacts)
    return contacts
    
def phone_deserialize(phone: dict) -> Phone | None:
    
    if not phone:
        return
    
    phone = Phone(**phone)
    return phone
    
def department_deserialize(department: dict) -> Department | None:
    
    if not department:
        return
    
    department = Department(**department)
    return department
    
def driver_license_type_deserialize(driver_license_type: dict) -> DriverLicenseType | None:
    
    if not driver_license_type:
        return
    
    driver_license_type = DriverLicenseType(**driver_license_type)
    return driver_license_type
    
def employer_for_applicant_deserialize(employer_for_applicant: dict) -> EmployerForApplicant | None:
    
    if not employer_for_applicant:
        return

    if "employer_rating" in employer_for_applicant and employer_for_applicant["employer_rating"]:
        employer_rating = employer_for_applicant["employer_rating"]
        employer_rating = employer_rating_deserialize(employer_rating)
        employer_for_applicant["employer_rating"] = employer_rating
        
    if "logo_urls" in employer_for_applicant and employer_for_applicant["logo_urls"]:
        logo_urls = employer_for_applicant["logo_urls"]
        logo_urls = {f"px{key}": logo_urls[key] for key in ["90", "240"] if key in logo_urls}
        logo_urls = logo_urls_deserialize(logo_urls)
        employer_for_applicant["logo_urls"] = logo_urls
        
    if "applicant_services" in employer_for_applicant and employer_for_applicant["applicant_services"]:
        applicant_services = employer_for_applicant["applicant_services"]
        
        if "target_employer" in applicant_services and applicant_services["target_employer"]:
            target_employer = applicant_services["target_employer"]
            target_employer = target_employer_deserialize(target_employer)
            applicant_services["target_employer"] = target_employer
            
        applicant_services = applicant_service_deserialize(applicant_services)
        employer_for_applicant["applicant_services"] = applicant_services
    
    employer_for_applicant = EmployerForApplicant(**employer_for_applicant)
    return employer_for_applicant
    
def target_employer_deserialize(target_employer: dict) -> TargetEmployer | None:
    
    if not target_employer:
        return
    
    target_employer = TargetEmployer(**target_employer)
    return target_employer

def applicant_service_deserialize(applicant_service: dict) -> ApplicantService | None:
    
    if not applicant_service:
        return
    
    applicant_service = ApplicantService(**applicant_service)
    return applicant_service

def logo_urls_deserialize(logo_urls: dict) -> LogoUrls | None:
    
    if not logo_urls:
        return
    
    logo_urls = LogoUrls(**logo_urls)
    return logo_urls

def employer_rating_deserialize(employer_rating: dict) -> EmployerRating | None:
    
    if not employer_rating:
        return
    
    employer_rating = EmployerRating(**employer_rating)
    return employer_rating

def employment_form_deserialize(employment_form: dict) -> EmploymentForm | None:
    
    if not employment_form:
        return
    
    employment_form = EmploymentForm(**employment_form)
    return employment_form

def experience_deserialize(experience: dict) -> Experience | None:
    
    if not experience:
        return
    
    experience = Experience(**experience)
    return experience

def fly_in_fly_out_duration_deserialize(fly_in_fly_out_duration: dict) -> FlyInFlyOutDuration | None:
    
    if not fly_in_fly_out_duration:
        return
    
    fly_in_fly_out_duration = FlyInFlyOutDuration(**fly_in_fly_out_duration)
    return fly_in_fly_out_duration

def insider_interview_deserialize(insider_interview: dict) -> InsiderInterview | None:
    
    if not insider_interview:
        return
    
    insider_interview = InsiderInterview(**insider_interview)
    return insider_interview

def key_skill_deserialize(key_skill: dict) -> KeySkill | None:
    
    if not key_skill:
        return
    
    key_skill = KeySkill(**key_skill)
    return key_skill

def language_deserialize(language: dict) -> Language | None:
    
    if not language:
        return
    
    if "level" in language and language["level"]:
        level = language["level"]
        level = level_deserialize(level)
        language["level"] = level
        
    language = Language(**language)
    return language
    
def level_deserialize(level: dict) -> Level | None:
    
    if not level:
        return
    
    level = Level(**level)
    return level

def professional_role_deserialize(professional_role: dict) -> ProfessionalRole | None:
    
    if not professional_role:
        return
    
    professional_role = ProfessionalRole(**professional_role)
    return professional_role

def salary_range_deserialize(salary_range: dict) -> SalaryRange | None:
    
    if not salary_range:
        return
    
    if "from" in salary_range:
        salary_range["from_"] = salary_range.pop("from")
    
    if "frequency" in salary_range and salary_range["frequency"]:
        frequency = salary_range["frequency"]
        frequency = frequency_deserialize(frequency)
        salary_range["frequency"] = frequency
        
    if "mode" in salary_range and salary_range["mode"]:
        mode = salary_range["mode"]
        mode = mode_deserialize(mode)
        salary_range["mode"] = mode
    
    salary_range = SalaryRange(**salary_range)
    return salary_range
    
def frequency_deserialize(frequency: dict) -> Frequency | None:
    
    if not frequency:
        return
    
    frequency = Frequency(**frequency)
    return frequency

def mode_deserialize(mode: dict) -> Mode | None:
    
    if not mode:
        return
    
    mode = Mode(**mode)
    return mode

def test_deserialize(test: dict) -> Test | None:
    
    if not test:
        return
    
    test = Test(**test)
    return test

def type_deserialize(type_: dict) -> Type | None:
    
    if not type_:
        return
    
    type_ = Type(**type_)
    return type_

def vacancy_property_deserialize(vacancy_property: dict) -> VacancyProperties | None:
    
    if not vacancy_property:
        return
    
    if "appearance" in vacancy_property and vacancy_property["appearance"]:
        appearance = vacancy_property["appearance"]
        appearance = appearance_deserialize(appearance)
        vacancy_property["appearance"] = appearance

    if "properties" in vacancy_property and vacancy_property["properties"]:
        properties = [property_deserialize(property) for property in vacancy_property["properties"]]
        vacancy_property["properties"] = properties
    
    vacancy_property = VacancyProperties(**vacancy_property)
    return vacancy_property
    
def appearance_deserialize(appearance: dict) -> Appearance | None:
    
    if not appearance:
        return
    
    appearance = Appearance(**appearance)
    return appearance

def property_deserialize(property: dict) -> Property | None:
    
    if not property:
        return
    
    property = Property(**property)
    return property

def video_vacancy_deserialize(video_vacancy: dict) -> VideoVacancy | None:
    
    if not video_vacancy:
        return
    
    if "cover_picture" in video_vacancy and video_vacancy["cover_picture"]:
        cover_picture = video_vacancy["cover_picture"]
        cover_picture = cover_picture_deserialize(cover_picture)
        video_vacancy["cover_picture"] = cover_picture
        
    if "snippet_picture" in video_vacancy and video_vacancy["snippet_picture"]:
        snippet_picture = video_vacancy["snippet_picture"]
        snippet_picture = snippet_picture_deserialize(snippet_picture)
        video_vacancy["snippet_picture"] = snippet_picture
        
    if "snippet_video" in video_vacancy and video_vacancy["snippet_video"]:
        snippet_video = video_vacancy["snippet_video"]
        snippet_video = snippet_video_deserialize(snippet_video)
        video_vacancy["snippet_video"] = snippet_video
        
    if "video" in video_vacancy and video_vacancy["video"]:
        video = video_vacancy["video"]
        video = video_deserialize(video)
        video_vacancy["video"] = video

    video_vacancy = VideoVacancy(**video_vacancy)
    return video_vacancy
    
def video_deserialize(video: dict) -> Video | None:
    
    if not video:
        return
    
    if "upload_id" in video:
        video["id"] = video.pop("upload_id")
        
    video = Video(**video)
    return video

def snippet_video_deserialize(snippet_video: dict) -> SnippetVideo | None:
    
    if not snippet_video: 
        return
    
    if "upload_id" in snippet_video: 
        snippet_video["id"] = snippet_video.pop("upload_id")
    
    snippet_video = SnippetVideo(**snippet_video)
    return snippet_video

def snippet_picture_deserialize(snippet_picture: dict) -> SnippetPicture | None:
    
    if not snippet_picture:
        return
    
    snippet_picture = SnippetPicture(**snippet_picture)
    return snippet_picture

def cover_picture_deserialize(cover_picture: dict) -> CoverPicture | None:
    
    if not cover_picture:
        return
    
    cover_picture = CoverPicture(**cover_picture)
    return cover_picture

def work_format_deserialize(work_format: dict) -> WorkFormat | None:
    
    if not work_format:
        return
    
    work_format = WorkFormat(**work_format)
    return work_format

def work_schedule_by_days_deserialize(work_schedule_by_days: dict) -> WorkScheduleByDays | None:
    
    if not work_schedule_by_days:
        return
    
    work_schedule_by_days = WorkScheduleByDays(**work_schedule_by_days)
    return work_schedule_by_days

def working_hours_deserialize(working_hours: dict) -> WorkingHours:
    
    if not working_hours:
        return
    
    working_hours = WorkingHours(**working_hours)
    return working_hours

def address_for_applicant_deserialize(address_for_applicant: dict) -> AddressForApplicant | None:
    
    if not address_for_applicant:
        return
    
    if "metro_stations" in address_for_applicant and address_for_applicant["metro_stations"]:
        metro_stations = [metro_station_deserialize(metro_station) for metro_station in address_for_applicant["metro_stations"]]
        address_for_applicant["metro_stations"] = metro_stations
    
    address_for_applicant = AddressForApplicant(**address_for_applicant)
    return address_for_applicant
    
def metro_station_deserialize(metro_station: dict) -> MetroStation:
    
    if not metro_station:
        return
    
    metro_station = MetroStation(**metro_station)
    return metro_station
