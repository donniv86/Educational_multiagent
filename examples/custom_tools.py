#!/usr/bin/env python3
"""
Custom Tools Example

This example demonstrates how to create and use custom tools in CrewAI:
- Creating custom tools by subclassing BaseTool
- Using the @tool decorator
- Integrating custom tools with agents

Author: AI Assistant
Date: 2025
"""

import os
import json
from datetime import datetime
from crewai import Agent, Task, Crew, tool
from crewai.tools import BaseTool


class CalculatorTool(BaseTool):
    """Custom tool for performing mathematical calculations."""

    name: str = "Calculator"
    description: str = "Performs basic mathematical calculations (add, subtract, multiply, divide)"

    def _run(self, operation: str, a: float, b: float) -> str:
        """Perform mathematical operations."""
        try:
            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b
            elif operation == "multiply":
                result = a * b
            elif operation == "divide":
                if b == 0:
                    return "Error: Division by zero"
                result = a / b
            else:
                return f"Error: Unknown operation '{operation}'. Use add, subtract, multiply, or divide."

            return f"{operation}({a}, {b}) = {result}"
        except Exception as e:
            return f"Error: {str(e)}"


class DataLoggerTool(BaseTool):
    """Custom tool for logging data to a file."""

    name: str = "Data Logger"
    description: str = "Logs data to a JSON file with timestamps"

    def _run(self, data: str, filename: str = "crewai_log.json") -> str:
        """Log data to a JSON file."""
        try:
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "data": data
            }

            # Load existing logs or create new list
            try:
                with open(filename, 'r') as f:
                    logs = json.load(f)
            except FileNotFoundError:
                logs = []

            logs.append(log_entry)

            # Save updated logs
            with open(filename, 'w') as f:
                json.dump(logs, f, indent=2)

            return f"Data logged successfully to {filename}"
        except Exception as e:
            return f"Error logging data: {str(e)}"


@tool("Quick Calculator")
def quick_calc(expression: str) -> str:
    """
    Quick calculator that evaluates mathematical expressions.

    Args:
        expression: Mathematical expression as string (e.g., "2 + 3 * 4")

    Returns:
        Result of the calculation
    """
    try:
        # Note: eval() should be used carefully in production
        result = eval(expression)
        return f"{expression} = {result}"
    except Exception as e:
        return f"Error calculating {expression}: {str(e)}"


@tool("Text Analyzer")
def analyze_text(text: str) -> str:
    """
    Analyzes text and provides basic statistics.

    Args:
        text: Text to analyze

    Returns:
        Analysis results
    """
    try:
        words = text.split()
        characters = len(text)
        word_count = len(words)
        avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0

        analysis = {
            "character_count": characters,
            "word_count": word_count,
            "average_word_length": round(avg_word_length, 2),
            "unique_words": len(set(words))
        }

        return f"Text Analysis: {json.dumps(analysis, indent=2)}"
    except Exception as e:
        return f"Error analyzing text: {str(e)}"


def create_custom_tools_crew():
    """Create a crew that demonstrates custom tools."""

    # Create agents with custom tools
    analyst = Agent(
        role="Data Analyst",
        goal="Analyze data and perform calculations",
        backstory="You are a skilled data analyst who loves working with numbers and data.",
        tools=[CalculatorTool(), DataLoggerTool(), quick_calc, analyze_text],
        verbose=True,
        allow_delegation=False
    )

    reporter = Agent(
        role="Report Writer",
        goal="Create reports based on analysis results",
        backstory="You are a report writer who creates clear summaries of data analysis.",
        verbose=True,
        allow_delegation=False
    )

    # Create tasks
    analysis_task = Task(
        description="""
        Perform the following analysis:
        1. Calculate: (15 * 3) + (20 / 4)
        2. Analyze the text: "CrewAI is a powerful framework for creating collaborative AI agents that work together to solve complex problems."
        3. Log the results of your analysis

        Use the available tools to complete this task.
        """,
        agent=analyst,
        expected_output="Complete analysis with calculations, text analysis, and logged results."
    )

    reporting_task = Task(
        description="Create a summary report of the analysis results in a clear, professional format.",
        agent=reporter,
        expected_output="A professional summary report of the analysis.",
        context=[analysis_task]
    )

    # Create crew
    crew = Crew(
        agents=[analyst, reporter],
        tasks=[analysis_task, reporting_task],
        process="sequential",
        verbose=True
    )

    return crew


def main():
    """Main function to run the custom tools example."""

    print("🚀 Starting Custom Tools Example")
    print("=" * 50)

    # Check for API key
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  Warning: OPENAI_API_KEY not set.")
        print("Please set your OpenAI API key in the .env file")
        return

    try:
        # Create and run crew
        crew = create_custom_tools_crew()
        result = crew.kickoff()

        print("\n" + "=" * 50)
        print("✅ Custom Tools Example Completed Successfully!")
        print("\n📄 Final Result:")
        print("-" * 30)
        print(result)

        # Show the log file if it was created
        if os.path.exists("crewai_log.json"):
            print("\n📊 Log File Created:")
            with open("crewai_log.json", 'r') as f:
                print(json.dumps(json.load(f), indent=2))

    except Exception as e:
        print(f"❌ Error running custom tools example: {str(e)}")


if __name__ == "__main__":
    main()