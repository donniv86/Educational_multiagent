# CrewAI Learning Project

This repository contains comprehensive resources for learning and implementing CrewAI, a powerful Python framework for creating collaborative AI agent teams.

## 📚 What is CrewAI?

CrewAI is a lean, lightning-fast Python framework built entirely from scratch—completely independent of LangChain or other agent frameworks. It empowers developers with both high-level simplicity and precise low-level control, ideal for creating autonomous AI agents tailored to any scenario.

### Key Features
- **Multi-Agent Collaboration**: Orchestrate teams of AI agents with specific roles
- **Role-Based Architecture**: Each agent has defined responsibilities and expertise
- **Tool Integration**: Extensive ecosystem of built-in and custom tools
- **Enterprise-Ready**: Production-ready with monitoring and observability
- **Independent Framework**: Built from scratch, not dependent on other frameworks

## 🗂️ Repository Contents

### 📖 Documentation
- **[CrewAI_Comprehensive_Guide.md](CrewAI_Comprehensive_Guide.md)** - Complete guide covering all aspects of CrewAI
- **[README.md](README.md)** - This file with project overview and setup instructions

### 💻 Code Examples
- **[crewai_example.py](crewai_example.py)** - Practical example of a content creation crew
- **[setup_crewai.py](setup_crewai.py)** - Automated setup script for CrewAI projects

### ⚙️ Configuration
- **[requirements.txt](requirements.txt)** - Python dependencies for the project

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd CrewAI
   ```

2. **Run the automated setup script**
   ```bash
   python setup_crewai.py
   ```

3. **Follow the prompts** to create your first CrewAI project

### Option 2: Manual Setup

1. **Install UV package manager**
   ```bash
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. **Install CrewAI CLI**
   ```bash
   uv tool install crewai
   ```

3. **Create a new project**
   ```bash
   crewai create crew my_project
   cd my_project
   ```

4. **Install dependencies**
   ```bash
   crewai install
   ```

5. **Set up environment variables**
   ```bash
   # Edit .env file with your API keys
   cp .env.example .env
   # Add your OpenAI API key and other required keys
   ```

6. **Run your first crew**
   ```bash
   crewai run
   ```

## 📋 Prerequisites

- **Python 3.10 to 3.13** (CrewAI requirement)
- **API Keys** for LLM providers:
  - OpenAI API key (required)
  - Serper API key (for web search tools)
  - Anthropic API key (alternative to OpenAI)

## 🎯 Example: Content Creation Crew

The included `crewai_example.py` demonstrates a complete content creation workflow with three specialized agents:

1. **Researcher Agent** - Gathers comprehensive information on topics
2. **Writer Agent** - Creates engaging content based on research
3. **Editor Agent** - Reviews and polishes the final content

### Running the Example

```bash
# Set your API keys
export OPENAI_API_KEY="your_openai_api_key"
export SERPER_API_KEY="your_serper_api_key"

# Run the example
python crewai_example.py
```

## 🏗️ Project Structure

When you create a CrewAI project, you'll get this structure:

```
my_project/
├── .gitignore
├── pyproject.toml
├── README.md
├── .env
└── src/
    └── my_project/
        ├── __init__.py
        ├── main.py
        ├── crew.py
        ├── tools/
        │   ├── custom_tool.py
        │   └── __init__.py
        └── config/
            ├── agents.yaml
            └── tasks.yaml
```

## 🔧 Configuration

### Agents Configuration (`config/agents.yaml`)
Define your AI agents with roles, goals, and backstories:

```yaml
researcher:
  role: "Research Specialist"
  goal: "Gather comprehensive information on given topics"
  backstory: "Expert researcher with years of experience in data analysis"
  tools: ["web_search", "file_reader"]
```

### Tasks Configuration (`config/tasks.yaml`)
Define the tasks your agents will perform:

```yaml
research_task:
  description: "Conduct thorough research on the specified topic"
  agent: "researcher"
  expected_output: "Comprehensive research report"
```

## 🛠️ Customization

### Creating Custom Tools

```python
from crewai.tools import BaseTool

class CustomTool(BaseTool):
    name: str = "Custom Tool"
    description: str = "A custom tool for specific tasks"

    def _run(self, *args, **kwargs):
        # Your tool logic here
        return "Tool result"
```

### Using Decorators

```python
from crewai import tool

@tool("Quick Tool")
def quick_function(input_data):
    # Tool logic
    return processed_result
```

## 🔍 CrewAI vs LangChain

| Aspect | CrewAI | LangChain |
|--------|--------|-----------|
| **Focus** | Multi-agent collaboration | LLM application framework |
| **Architecture** | Role-based agent teams | Modular component system |
| **Dependency** | Independent framework | Base framework for CrewAI |
| **Complexity** | High-level orchestration | Low-level granular control |
| **Use Case** | Collaborative AI teams | General LLM applications |

## 📚 Learning Resources

### Official Resources
- **[CrewAI Website](https://crewai.com)** - Official website
- **[Documentation](https://docs.crewai.com)** - Comprehensive documentation
- **[GitHub Repository](https://github.com/crewAIInc/crewAI)** - Source code
- **[Examples Repository](https://github.com/crewAIInc/crewAI-examples)** - Official examples
- **[Community Forum](https://community.crewai.com)** - Community discussions

### Learning Materials
- **[CrewAI Courses](https://learn.crewai.com)** - Official learning platform
- **[Blog](https://blog.crewai.com)** - Latest updates and tutorials
- **[YouTube Channel](https://www.youtube.com/@CrewAI)** - Video tutorials
- **[Quickstart Guide](https://github.com/alexfazio/crewAI-quickstart)** - Community quickstart

## 🏢 Enterprise Features

CrewAI offers enterprise-grade features through the CrewAI Enterprise Suite:

- **Crew Control Plane** - Centralized management platform
- **Tracing & Observability** - Real-time monitoring and analytics
- **Advanced Security** - Enterprise-grade security features
- **24/7 Support** - Dedicated enterprise support
- **On-premise Deployment** - Deploy in your own infrastructure

## 🤝 Contributing

This is a learning project, but you can contribute to the official CrewAI project:

1. Fork the [official repository](https://github.com/crewAIInc/crewAI)
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is for educational purposes. CrewAI itself is open source and available under its own license.

## 🆘 Support

- **Community Forum**: [community.crewai.com](https://community.crewai.com)
- **GitHub Issues**: [github.com/crewAIInc/crewAI/issues](https://github.com/crewAIInc/crewAI/issues)
- **Documentation**: [docs.crewai.com](https://docs.crewai.com)

## 🎉 Getting Help

If you're stuck or have questions:

1. Check the [comprehensive guide](CrewAI_Comprehensive_Guide.md)
2. Review the [official documentation](https://docs.crewai.com)
3. Join the [community forum](https://community.crewai.com)
4. Look at the [examples repository](https://github.com/crewAIInc/crewAI-examples)

---

**Happy building with CrewAI! 🚀**