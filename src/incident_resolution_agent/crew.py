from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class IncidentResolutionAgent():
    """IncidentResolutionAgent crew"""

    agents: list[BaseAgent]
    tasks: list[Task]
    tracing_enabled: bool = True
    @agent
    def incident_triage_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['incident_triage_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def log_analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['log_analysis_agent'], # type: ignore[index]
            verbose=True
        )
        
    @agent
    def root_cause_analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['root_cause_analysis_agent'], # type: ignore[index]
            verbose=True
        )    

    @agent
    def Resolution_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['Resolution_agent'], # type: ignore[index]
            verbose=True
        )
        
    @task
    def log_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['log_analysis_task'], # type: ignore[index]
            output_file='output/log_analysis.json'
        )

    @task
    def triage_task(self) -> Task:
        return Task(
            config=self.tasks_config['triage_task'], # type: ignore[index]
            output_file='output/triage_report.json'
        )
        
    @task
    def root_cause_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['root_cause_analysis_task'], # type: ignore[index]
            output_file='output/root_cause_analysis_report.json'
        )    
        
    @task
    def Resolution_task(self) -> Task:
        return Task(
            config=self.tasks_config['Resolution_task'], # type: ignore[index]
            output_file='output/resolution_report.json'
        )    

    @crew
    def crew(self) -> Crew:
        """Creates the IncidentResolutionAgent crew"""
        ordered_tasks = [
            self.log_analysis_task(),
            self.triage_task(),
            self.root_cause_analysis_task(),
            self.Resolution_task(),
        ]
          
        return Crew(
            agents=self.agents,
            tasks=ordered_tasks,
            process=Process.sequential,
            verbose=True,
        )
