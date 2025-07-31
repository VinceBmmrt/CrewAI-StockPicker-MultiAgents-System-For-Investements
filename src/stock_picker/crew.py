from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from pydantic import BaseModel, Field
from crewai_tools import SerperDevTool

class TrendingCompany(BaseModel):
    """A Company that is currently trending and has potential for stock picking."""
    name: str = Field(description="Name of the trending company")
    ticker: str = Field(description="Ticker symbol of the company")
    reason: str = Field(description="Reason why the company is trending")

class TrendingCompanyList(BaseModel):
    """A list of trending companies that are in the news."""
    companies: List[TrendingCompany] = Field(description="List of trending companies")

class TrendingCompanyResearch(BaseModel):
    """Research data for a trending company."""
    name: str = Field(description="Name of the company")
    market_position: str = Field(description="Market position of the company and competitive analysis")
    future_outlook: str = Field(description="Future outlook of the company and growth prospects")
    investment_potential: str = Field(description="Investment potential and suitability for investment")

class TrendingCompanyResearchList(BaseModel):
    """A list of research data for trending companies."""
    research_list: List[TrendingCompanyResearch] = Field(description="Comprehensive list of research for trending companies")

@CrewBase
class StockPicker():
    """StockPicker crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def trending_company_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['trending_company_finder'], # type: ignore[index]
            verbose=True,
            tools=[
                SerperDevTool()
            ]
        )
    
    def financial_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_researcher'], # type: ignore[index]
            verbose=True,
            tools=[
                SerperDevTool()
            ]
        )

    @agent
    def stock_picker(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_picker'], # type: ignore[index]
            verbose=True,
        )


    @task
    def find_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config['find_trending_companies'], # type: ignore[index]
            output_pydantic=TrendingCompanyList,
        )

    @task
    def research_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config['research_trending_companies'], # type: ignore[index]
            output_pydantic=TrendingCompanyResearchList,

        )
    
    @task
    def pick_best_company(self) -> Task:
        return Task(
            config=self.tasks_config['pick_best_company'], # type: ignore[index]
        )   

    @crew
    def crew(self) -> Crew:
        """Creates the StockPicker crew"""
        manager = Agent(
            config=self.agents_config['manager'], # type: ignore[index]
            allow_delegation=True
           
        )
        

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.hierarchical,
            verbose=True,
            manager_agent=manager,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
