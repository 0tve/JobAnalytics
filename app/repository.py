from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import (Area, EmployerForApplicant, Experience, Frequency,
                        KeySkill, Mode, ProfessionalRole, SalaryRange,
                        SalaryRangeFrequency, SalaryRangeMode, Vacancy,
                        VacancyArea, VacancyEmployerForApplicant,
                        VacancyExperience, VacancyKeySkill,
                        VacancyProfessionalRole, VacancySalaryRange)
from app.schemas import Vacancy as VacancySchema

    
async def vacancy_insert(session: AsyncSession, vacancy: dict):

    if not vacancy or await exists(session, Vacancy, vacancy["id"]):
        return
    
    vacancy = VacancySchema(**vacancy).model_dump(exclude_none=True)
    
    if "employer" in vacancy:
        vacancy["employer_for_applicant"] = vacancy.pop("employer")

    vacancy_id = vacancy.get("id")

    vacancy_clean = get_clean(vacancy)
    await upsert(session, Vacancy.__table__, vacancy_clean)
    
    if "area" in vacancy and vacancy["area"]:
        area = vacancy["area"]
        await upsert(session, Area.__table__, area)
        vacancy_area = (vacancy_id, area["id"])
        await upsert(session, VacancyArea.__table__, vacancy_area)
    
    if "experience" in vacancy and vacancy["experience"]:
        experience = vacancy["experience"]
        await upsert(session, Experience.__table__, experience)
        vacancy_experience = (vacancy_id, experience["id"])
        await upsert(session, VacancyExperience.__table__, vacancy_experience)
        
    if "key_skills" in vacancy and vacancy["key_skills"]:
        key_skills = vacancy["key_skills"]
        await upsert(session, KeySkill.__table__, key_skills)
        vacancy_key_skills = [(vacancy_id, key_skill["name"]) for key_skill in key_skills]
        await upsert(session, VacancyKeySkill.__table__, vacancy_key_skills)
        
    if "professional_roles" in vacancy and vacancy["professional_roles"]:
        professional_roles = vacancy["professional_roles"]
        await upsert(session, ProfessionalRole.__table__, professional_roles)
        vacancy_professional_roles = [(vacancy_id, professional_role["id"]) for professional_role in professional_roles]
        await upsert(session, VacancyProfessionalRole.__table__, vacancy_professional_roles)

    if "salary_range" in vacancy and vacancy["salary_range"]:
        salary_range = vacancy["salary_range"]
        
        if "from_" in salary_range:
            salary_range["from"] = salary_range.pop("from_")
        
        salary_range_clean = get_clean(salary_range)
        salary_range_id = (await upsert(session, SalaryRange.__table__, salary_range_clean))[0]
        vacancy_salary_range = (vacancy_id, salary_range_id)  
        await upsert(session, VacancySalaryRange.__table__, vacancy_salary_range)
        
        if "frequency" in salary_range and salary_range["frequency"]:
            frequency = salary_range["frequency"]
            await upsert(session, Frequency.__table__, frequency)
            salary_range_frequency = (salary_range_id, frequency["id"])
            await upsert(session, SalaryRangeFrequency.__table__, salary_range_frequency)
        
        if "mode" in salary_range and salary_range["mode"]:
            mode = salary_range["mode"]
            await upsert(session, Mode.__table__, mode)
            salary_range_mode = (salary_range_id, mode["id"])
            await upsert(session, SalaryRangeMode.__table__, salary_range_mode)
        
    if "employer_for_applicant" in vacancy and vacancy["employer_for_applicant"]:
        employer_for_applicant = vacancy["employer_for_applicant"]
        employer_for_applicant_clean = get_clean(employer_for_applicant)
        await upsert(session, EmployerForApplicant.__table__, employer_for_applicant_clean)
        vacancy_employer_for_applicant = (vacancy_id, employer_for_applicant["name"])
        await upsert(session, VacancyEmployerForApplicant.__table__, vacancy_employer_for_applicant)
        
        if "employer_rating" in employer_for_applicant and employer_for_applicant["employer_rating"]:
            ...
        
        if "logo_urls" in employer_for_applicant and employer_for_applicant["logo_urls"]:
            ...
            
async def upsert(session: AsyncSession, table: object, values: dict | list) -> list:
    pk = list(table.primary_key.columns)[0]
    stmt = insert(table).values(values).on_conflict_do_nothing().returning(pk)
    result = await session.execute(stmt)
    return result.scalars().all()

async def exists(session: AsyncSession, model: object, pk_val):
    pk_col = list(model.__table__.primary_key.columns)[0]
    stmt = select(model).where(pk_col == pk_val)
    result = await session.execute(stmt)
    instance = result.scalar_one_or_none()
    return instance is not None

def get_clean(d: dict) -> dict:
    clean = {}
    
    for k, v in d.items():
        
        if not isinstance(v, (dict, list)):
            clean[k] = v
    
    return clean