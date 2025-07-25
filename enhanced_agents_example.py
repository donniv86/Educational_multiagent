#!/usr/bin/env python3
"""
Enhanced CrewAI Agents Example

This example demonstrates advanced agent configurations with comprehensive
roles, goals, and backstories based on real-world applications and industry best practices.

Author: AI Assistant
Date: 2025
"""

import os
from typing import List, Dict, Any
from crewai import Agent, Task, Crew
from crewai_tools import SerperApiTool, FileReadTool, FileWriteTool


class EnhancedAgentsExample:
    """Example demonstrating enhanced agent configurations for real-world applications."""

    def __init__(self, topic: str = "AI in Healthcare", output_file: str = "enhanced_analysis.md"):
        self.topic = topic
        self.output_file = output_file
        self.tools = self._setup_tools()
        self.agents = self._create_enhanced_agents()
        self.tasks = self._create_enhanced_tasks()
        self.crew = self._create_enhanced_crew()

    def _setup_tools(self) -> Dict[str, Any]:
        """Setup tools for enhanced agents."""
        return {
            'web_search': SerperApiTool(),
            'file_read': FileReadTool(),
            'file_write': FileWriteTool()
        }

    def _create_enhanced_agents(self) -> Dict[str, Agent]:
        """Create enhanced agents with comprehensive roles, goals, and backstories."""

        # Enhanced Research Specialist
        research_specialist = Agent(
            role="Senior Market Research Analyst specializing in healthcare technology and competitive intelligence",
            goal="Conduct comprehensive market research to identify emerging trends, competitive dynamics, and market opportunities in the healthcare technology sector, providing actionable intelligence for strategic decision-making",
            backstory="""You are a senior market research analyst with 12+ years of experience in
            healthcare technology, competitive intelligence, and strategic analysis. You've worked
            with major healthcare companies like Johnson & Johnson, Pfizer, and UnitedHealth Group,
            helping them understand market dynamics and identify billion-dollar opportunities. Your
            expertise includes advanced statistical analysis, competitive benchmarking, and trend
            forecasting. You've successfully predicted major healthcare technology disruptions and
            have helped companies launch products that generated over $500M in revenue. You're known
            for your ability to uncover hidden market insights and for translating complex data into
            clear, actionable strategic recommendations.""",
            tools=[self.tools['web_search'], self.tools['file_read']],
            verbose=True,
            allow_delegation=False
        )

        # Enhanced Content Strategist
        content_strategist = Agent(
            role="Senior Content Strategist specializing in healthcare communications and thought leadership",
            goal="Develop comprehensive content strategies that educate healthcare professionals, engage stakeholders, and position organizations as thought leaders in the healthcare technology space",
            backstory="""You are a senior content strategist with 10+ years of experience in
            healthcare communications, thought leadership, and content marketing. You've worked with
            leading healthcare organizations like Mayo Clinic, Cleveland Clinic, and pharmaceutical
            companies, creating content strategies that reach millions of healthcare professionals.
            Your expertise includes medical writing, regulatory compliance, and audience engagement.
            You've helped organizations increase their thought leadership visibility by 300% and
            have developed content frameworks used by major healthcare institutions. You're known for
            your ability to make complex medical concepts accessible and for creating content that
            drives meaningful engagement with healthcare audiences.""",
            tools=[self.tools['file_read'], self.tools['file_write']],
            verbose=True,
            allow_delegation=False
        )

        # Enhanced Business Analyst
        business_analyst = Agent(
            role="Senior Business Analyst specializing in healthcare technology ROI and strategic planning",
            goal="Analyze business opportunities, assess market potential, and develop strategic recommendations that drive growth and competitive advantage in healthcare technology markets",
            backstory="""You are a senior business analyst with 15+ years of experience in
            healthcare technology, strategic planning, and business development. You've worked with
            Fortune 500 healthcare companies, startups, and consulting firms, helping them evaluate
            market opportunities worth billions of dollars. Your expertise includes financial modeling,
            market sizing, and strategic planning. You've helped companies make investment decisions
            that led to successful product launches and market expansions. You're known for your
            ability to build compelling business cases and for providing strategic insights that
            drive executive decision-making.""",
            tools=[self.tools['file_read'], self.tools['file_write']],
            verbose=True,
            allow_delegation=False
        )

        return {
            'research_specialist': research_specialist,
            'content_strategist': content_strategist,
            'business_analyst': business_analyst
        }

    def _create_enhanced_tasks(self) -> List[Task]:
        """Create enhanced tasks with detailed descriptions and expectations."""

        # Enhanced Research Task
        research_task = Task(
            description=f"""Conduct a comprehensive market research analysis on the topic: {self.topic}

            Your research should include:
            1. **Market Size and Growth**: Quantify the current market size, growth rates, and future projections
            2. **Competitive Landscape**: Analyze key players, market share, and competitive positioning
            3. **Technology Trends**: Identify emerging technologies, innovations, and disruption patterns
            4. **Regulatory Environment**: Assess regulatory frameworks, compliance requirements, and policy impacts
            5. **Customer Insights**: Understand user needs, pain points, and adoption barriers
            6. **Investment Landscape**: Analyze funding trends, M&A activity, and investment patterns
            7. **Geographic Analysis**: Identify regional opportunities and market variations
            8. **Risk Assessment**: Evaluate market risks, challenges, and potential obstacles

            Organize your findings in a structured format and save them to 'comprehensive_research.md'.
            Include specific data points, statistics, and actionable insights.""",
            agent=self.agents['research_specialist'],
            expected_output="A comprehensive market research report with quantitative data, competitive analysis, and strategic insights saved to 'comprehensive_research.md'"
        )

        # Enhanced Content Strategy Task
        content_task = Task(
            description=f"""Based on the research findings, develop a comprehensive content strategy for {self.topic}.

            Your content strategy should include:
            1. **Audience Analysis**: Define target audiences, their needs, and content preferences
            2. **Content Pillars**: Identify key themes and topics that align with business objectives
            3. **Content Types**: Recommend specific content formats (whitepapers, webinars, case studies, etc.)
            4. **Distribution Strategy**: Outline channels, platforms, and publishing schedules
            5. **Thought Leadership Plan**: Develop positioning and messaging for thought leadership
            6. **Engagement Metrics**: Define KPIs and success measures for content performance
            7. **Competitive Analysis**: Assess competitor content strategies and identify opportunities
            8. **Implementation Roadmap**: Create a phased approach for content development and distribution

            Create a detailed content strategy document and save it to 'content_strategy.md'.""",
            agent=self.agents['content_strategist'],
            expected_output="A comprehensive content strategy document with audience analysis, content pillars, and implementation roadmap saved to 'content_strategy.md'",
            context=[research_task]
        )

        # Enhanced Business Analysis Task
        business_analysis_task = Task(
            description=f"""Analyze the business opportunities and develop strategic recommendations for {self.topic}.

            Your business analysis should include:
            1. **Market Opportunity Assessment**: Quantify market potential and revenue opportunities
            2. **Competitive Advantage Analysis**: Identify unique positioning and differentiation strategies
            3. **Business Model Recommendations**: Suggest optimal business models and revenue streams
            4. **Go-to-Market Strategy**: Develop comprehensive market entry and expansion plans
            5. **Resource Requirements**: Estimate investment needs, team requirements, and timeline
            6. **Risk Mitigation**: Identify potential challenges and develop mitigation strategies
            7. **Success Metrics**: Define key performance indicators and success criteria
            8. **Strategic Roadmap**: Create a 3-5 year strategic plan with milestones and objectives

            Develop a comprehensive business analysis and strategic recommendations document.""",
            agent=self.agents['business_analyst'],
            expected_output=f"Comprehensive business analysis with strategic recommendations and implementation roadmap saved to '{self.output_file}'",
            context=[research_task, content_task]
        )

        return [research_task, content_task, business_analysis_task]

    def _create_enhanced_crew(self) -> Crew:
        """Create an enhanced crew with optimized configuration."""
        return Crew(
            agents=list(self.agents.values()),
            tasks=self.tasks,
            process="sequential",
            verbose=True,
            memory=True,
            cache=True
        )

    def execute(self) -> str:
        """Execute the enhanced agents example."""
        print(f"🚀 Starting Enhanced Agents Analysis: {self.topic}")
        print("=" * 60)

        try:
            result = self.crew.kickoff()

            print("\n" + "=" * 60)
            print("✅ Enhanced Agents Analysis Completed Successfully!")
            print(f"\n📄 Final Analysis saved to: {self.output_file}")
            print("\n📊 Analysis Summary:")
            print("-" * 30)
            print(result)

            return result

        except Exception as e:
            print(f"❌ Error in enhanced agents analysis: {str(e)}")
            raise


def main():
    """Main function to run the enhanced agents example."""

    print("🚀 Enhanced CrewAI Agents Example")
    print("=" * 50)

    # Check for API key
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  Warning: OPENAI_API_KEY not set.")
        print("Please set your OpenAI API key in the .env file")
        return

    if not os.getenv('SERPER_API_KEY'):
        print("⚠️  Warning: SERPER_API_KEY not set.")
        print("Please set your Serper API key in the .env file for web search capabilities")
        return

    try:
        # Create and run enhanced agents example
        example = EnhancedAgentsExample(
            topic="Artificial Intelligence in Healthcare: Market Analysis and Strategic Opportunities",
            output_file="healthcare_ai_analysis.md"
        )

        result = example.execute()

        print("\n🎯 Key Benefits of Enhanced Agents:")
        print("-" * 40)
        print("✅ Comprehensive role definitions with real-world expertise")
        print("✅ Detailed goals aligned with business objectives")
        print("✅ Rich backstories that provide context and credibility")
        print("✅ Specialized tools and capabilities")
        print("✅ Professional-grade analysis and recommendations")

    except Exception as e:
        print(f"❌ Error running enhanced agents example: {str(e)}")


if __name__ == "__main__":
    main()