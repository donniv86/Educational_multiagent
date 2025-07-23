#!/usr/bin/env python3
"""
Basic CrewAI Example

This example demonstrates the fundamental concepts of CrewAI:
- Creating agents with roles and goals
- Defining tasks
- Creating and running a crew

Author: AI Assistant
Date: 2025
"""

import os
from crewai import Agent, Task, Crew


def create_basic_crew():
    """
    Create a simple crew with two agents working on a basic task.
    """

    # Create agents
    researcher = Agent(
        role="Research Assistant",
        goal="Gather information and provide accurate data",
        backstory="You are an expert researcher with years of experience in data analysis and information gathering.",
        verbose=True,
        allow_delegation=False
    )

    writer = Agent(
        role="Content Writer",
        goal="Create clear and engaging content based on research",
        backstory="You are a skilled writer who excels at transforming complex information into clear, engaging content.",
        verbose=True,
        allow_delegation=False
    )

    # Create tasks
    research_task = Task(
        description="Research the topic of 'Artificial Intelligence in Healthcare' and provide key insights, trends, and statistics.",
        agent=researcher,
        expected_output="A comprehensive research summary with key findings and data points."
    )

    writing_task = Task(
        description="Using the research findings, create a 500-word article about AI in healthcare that is informative and engaging for a general audience.",
        agent=writer,
        expected_output="A well-written article about AI in healthcare.",
        context=[research_task]
    )

    # Create crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process="sequential",
        verbose=True
    )

    return crew


def main():
    """Main function to run the basic crew example."""

    print("🚀 Starting Basic CrewAI Example")
    print("=" * 50)

    # Check for API key
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  Warning: OPENAI_API_KEY not set.")
        print("Please set your OpenAI API key in the .env file")
        return

    try:
        # Create and run crew
        crew = create_basic_crew()
        result = crew.kickoff()

        print("\n" + "=" * 50)
        print("✅ Basic Crew Example Completed Successfully!")
        print("\n📄 Final Result:")
        print("-" * 30)
        print(result)

    except Exception as e:
        print(f"❌ Error running basic crew: {str(e)}")


if __name__ == "__main__":
    main()