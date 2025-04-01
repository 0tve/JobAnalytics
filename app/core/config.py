from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int
    NAME: str
    SCHEMAS: list[str]


    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"


    class Config:
        env_file = "envs/database.env"
        
        
class HHSettings(BaseSettings):
    ACCESS_TOKEN: str
    REFRESH_TOKEN: str
    BASE_URL: str
    USER_AGENT_PATTERN: str
    AUTHORIZATION_PATTERN: str
    APP_NAME: str
    EMAIL: str
    RPS: int
    
    
    @property
    def VACANCIES_URL(self):
        return f"{self.BASE_URL}vacancies/"
    
    
    @property
    def USER_AGENT(self):
        return f"{self.APP_NAME} ({self.EMAIL})"
    
    
    @property
    def AUTHORIZATION(self):
        return f"Bearer {self.ACCESS_TOKEN}"
    
    
    class Config:
        env_file = "envs/hh.env"
        
        
class AppSettings(BaseSettings):
    BASE_URL: str
    
    @property
    def SEARCH_URL(self):
        return f"{self.BASE_URL}hh/public/vacancies/search/"
    
    
    @property
    def VIEW_URL(self):
        return f"{self.BASE_URL}hh/applicant/vacancy/view/"
    
    
    class Config:
        env_file = "envs/app.env"
