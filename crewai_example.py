#!/usr/bin/env python3
"""
CrewAI Content Creation Example

This example demonstrates how to create a multi-agent crew for content creation,
including research, writing, and editing phases.

Author: AI Assistant
Date: 2025
"""

import os
from typing import List, Dict, Any
from crewai import Agent, Task, Crew
from crewai_tools import SerperApiTool, FileReadTool, FileWriteTool


class ContentCreationCrew:
    """
    A CrewAI implementation for automated content creation.

    This crew consists of three specialized agents:
    1. Researcher - Gathers information and data
    2. Writer - Creates content based on research
    3. Editor - Reviews and improves the content
    """

    def __init__(self, topic: str, output_file: str = "output.md"):
        """
        Initialize the content creation crew.

        Args:
            topic: The topic to research and write about
            output_file: File path for the final output
        """
        self.topic = topic
        self.output_file = output_file
        self.tools = self._setup_tools()
        self.agents = self._create_agents()
        self.tasks = self._create_tasks()
        self.crew = self._create_crew()

    def _setup_tools(self) -> Dict[str, Any]:
        """Set up tools for the agents."""
        return {
            'web_search': SerperApiTool(),
            'file_read': FileReadTool(),
            'file_write': FileWriteTool()
        }

    def _create_agents(self) -> Dict[str, Agent]:
        """Create specialized agents for the content creation process."""

        # Research Agent
        researcher = Agent(
            role="Research Specialist",
            goal="Gather comprehensive, accurate, and up-to-date information on the given topic",
            backstory="""You are an expert research specialist with over 10 years of experience
            in data analysis and information gathering. You have a keen eye for credible sources
            and can quickly identify the most relevant information from vast amounts of data.
            You specialize in academic research, market analysis, and trend identification.""",
            tools=[self.tools['web_search'], self.tools['file_read']],
            verbose=True,
            allow_delegation=False
        )

        # Writer Agent
        writer = Agent(
            role="Content Writer",
            goal="Create engaging, informative, and well-structured content based on research findings",
            backstory="""You are a seasoned content writer with expertise in multiple domains.
            You have a talent for transforming complex information into clear, engaging content
            that resonates with various audiences. You excel at storytelling, technical writing,
            and creating content that both educates and entertains.""",
            tools=[self.tools['file_read'], self.tools['file_write']],
            verbose=True,
            allow_delegation=False
        )

        # Editor Agent
        editor = Agent(
            role="Content Editor",
            goal="Review, refine, and polish content to ensure high quality, accuracy, and readability",
            backstory="""You are a meticulous content editor with years of experience in
            publishing and content management. You have an excellent command of grammar,
            style, and tone. You can spot inconsistencies, improve flow, and ensure content
            meets professional standards while maintaining the author's voice.""",
            tools=[self.tools['file_read'], self.tools['file_write']],
            verbose=True,
            allow_delegation=False
        )

        return {
            'researcher': researcher,
            'writer': writer,
            'editor': editor
        }

    def _create_tasks(self) -> List[Task]:
        """Create tasks for the content creation workflow."""

        # Research Task
        research_task = Task(
            description=f"""Conduct comprehensive research on the topic: {self.topic}

            Your research should include:
            1. Current trends and developments
            2. Key statistics and data points
            3. Expert opinions and insights
            4. Relevant case studies or examples
            5. Potential challenges or controversies

            Organize your findings in a structured format and save them to a file
            named 'research_findings.md' for the writer to use.""",
            agent=self.agents['researcher'],
            expected_output="A comprehensive research report saved to 'research_findings.md'"
        )

        # Writing Task
        writing_task = Task(
            description=f"""Using the research findings, create a comprehensive article about {self.topic}.

            The article should:
            1. Have a compelling introduction that hooks the reader
            2. Include relevant statistics and data from the research
            3. Provide valuable insights and actionable information
            4. Be well-structured with clear headings and sections
            5. Be between 1500-2000 words
            6. Include a conclusion that summarizes key points

            Save the article as 'draft_article.md' for the editor to review.""",
            agent=self.agents['writer'],
            expected_output="A well-written article saved to 'draft_article.md'",
            context=[research_task]
        )

        # Editing Task
        editing_task = Task(
            description=f"""Review and edit the draft article to ensure it meets professional standards.

            Your editing should focus on:
            1. Grammar, spelling, and punctuation
            2. Clarity and readability
            3. Logical flow and structure
            4. Consistency in tone and style
            5. Fact-checking and accuracy
            6. SEO optimization (if applicable)

            Make necessary improvements and save the final version to '{self.output_file}'.
            Provide a brief summary of the changes made.""",
            agent=self.agents['editor'],
            expected_output=f"Final polished article saved to '{self.output_file}'",
            context=[writing_task]
        )

        return [research_task, writing_task, editing_task]

    def _create_crew(self) -> Crew:
        """Create the crew with all agents and tasks."""
        return Crew(
            agents=list(self.agents.values()),
            tasks=self.tasks,
            process="sequential",
            verbose=True
        )

    def execute(self) -> str:
        """
        Execute the content creation workflow.

        Returns:
            str: Path to the final output file
        """
        print(f"🚀 Starting content creation for topic: {self.topic}")
        print("=" * 60)

        try:
            result = self.crew.kickoff()
            print("\n" + "=" * 60)
            print(f"✅ Content creation completed successfully!")
            print(f"📄 Final output saved to: {self.output_file}")
            return self.output_file

        except Exception as e:
            print(f"❌ Error during content creation: {str(e)}")
            raise


def main():
    """Main function to demonstrate the CrewAI content creation workflow."""

    # Set up environment variables (you'll need to set these)
    if not os.getenv('SERPER_API_KEY'):
        print("⚠️  Warning: SERPER_API_KEY not set. Web search functionality may be limited.")

    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  Warning: OPENAI_API_KEY not set. Please set your OpenAI API key.")
        return

    # Example usage
    topic = "The Future of Artificial Intelligence in Healthcare"
    output_file = "ai_healthcare_article.md"

    # Create and execute the crew
    crew = ContentCreationCrew(topic=topic, output_file=output_file)

    try:
        result_file = crew.execute()
        print(f"\n🎉 Success! Check out your article at: {result_file}")

    except Exception as e:
        print(f"❌ Failed to create content: {str(e)}")


if __name__ == "__main__":
    main()