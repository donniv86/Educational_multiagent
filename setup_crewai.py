#!/usr/bin/env python3
"""
CrewAI Setup Script

This script helps you set up a CrewAI environment and create your first project.
It handles installation, environment setup, and project initialization.

Author: AI Assistant
Date: 2025
"""

import os
import sys
import subprocess
import platform
from pathlib import Path


class CrewAISetup:
    """Helper class for setting up CrewAI environment."""

    def __init__(self):
        self.python_version = sys.version_info
        self.platform = platform.system().lower()
        self.project_dir = Path.cwd()

    def check_python_version(self) -> bool:
        """Check if Python version is compatible with CrewAI."""
        if self.python_version.major == 3 and 10 <= self.python_version.minor <= 13:
            print(f"✅ Python {self.python_version.major}.{self.python_version.minor} is compatible")
            return True
        else:
            print(f"❌ Python {self.python_version.major}.{self.python_version.minor} is not compatible")
            print("CrewAI requires Python 3.10 to 3.13")
            return False

    def install_uv(self) -> bool:
        """Install UV package manager if not already installed."""
        try:
            result = subprocess.run(['uv', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ UV is already installed")
                return True
        except FileNotFoundError:
            pass

        print("📦 Installing UV package manager...")

        if self.platform == "windows":
            cmd = "powershell -c \"irm https://astral.sh/uv/install.ps1 | iex\""
        else:
            cmd = "curl -LsSf https://astral.sh/uv/install.sh | sh"

        try:
            subprocess.run(cmd, shell=True, check=True)
            print("✅ UV installed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install UV: {e}")
            return False

    def install_crewai_cli(self) -> bool:
        """Install CrewAI CLI using UV."""
        print("🔧 Installing CrewAI CLI...")

        try:
            subprocess.run(['uv', 'tool', 'install', 'crewai'], check=True)
            print("✅ CrewAI CLI installed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install CrewAI CLI: {e}")
            return False

    def create_project(self, project_name: str) -> bool:
        """Create a new CrewAI project."""
        print(f"🚀 Creating CrewAI project: {project_name}")

        try:
            subprocess.run(['crewai', 'create', 'crew', project_name], check=True)
            print(f"✅ Project '{project_name}' created successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to create project: {e}")
            return False

    def install_dependencies(self, project_path: Path) -> bool:
        """Install project dependencies."""
        print("📦 Installing project dependencies...")

        try:
            subprocess.run(['crewai', 'install'], cwd=project_path, check=True)
            print("✅ Dependencies installed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install dependencies: {e}")
            return False

    def create_env_file(self, project_path: Path) -> bool:
        """Create a .env file template."""
        env_file = project_path / '.env'

        if env_file.exists():
            print("✅ .env file already exists")
            return True

        env_content = """# CrewAI Environment Variables
# Add your API keys here

# OpenAI API Key (required)
OPENAI_API_KEY=your_openai_api_key_here

# Serper API Key (for web search tools)
SERPER_API_KEY=your_serper_api_key_here

# Anthropic API Key (alternative to OpenAI)
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Other optional API keys
GOOGLE_API_KEY=your_google_api_key_here
SERPER_API_KEY=your_serper_api_key_here

# CrewAI Configuration
CREWAI_VERBOSE=true
CREWAI_DEBUG=false
"""

        try:
            with open(env_file, 'w') as f:
                f.write(env_content)
            print("✅ .env file created with template")
            return True
        except Exception as e:
            print(f"❌ Failed to create .env file: {e}")
            return False

    def run_example(self, project_path: Path) -> bool:
        """Run the example script."""
        print("🎯 Running example...")

        try:
            subprocess.run(['crewai', 'run'], cwd=project_path, check=True)
            print("✅ Example completed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to run example: {e}")
            return False

    def setup(self, project_name: str = "my_crewai_project"):
        """Complete setup process."""
        print("🚀 CrewAI Setup Wizard")
        print("=" * 50)

        # Check Python version
        if not self.check_python_version():
            return False

        # Install UV
        if not self.install_uv():
            return False

        # Install CrewAI CLI
        if not self.install_crewai_cli():
            return False

        # Create project
        if not self.create_project(project_name):
            return False

        project_path = self.project_dir / project_name

        # Install dependencies
        if not self.install_dependencies(project_path):
            return False

        # Create .env file
        if not self.create_env_file(project_path):
            return False

        print("\n" + "=" * 50)
        print("🎉 Setup completed successfully!")
        print(f"📁 Project created at: {project_path}")
        print("\n📝 Next steps:")
        print("1. Edit the .env file with your API keys")
        print("2. Customize agents and tasks in config/")
        print("3. Run 'crewai run' to test your crew")
        print("4. Check out the documentation at https://docs.crewai.com")

        return True


def main():
    """Main function for the setup script."""
    setup = CrewAISetup()

    # Get project name from user or use default
    if len(sys.argv) > 1:
        project_name = sys.argv[1]
    else:
        project_name = input("Enter project name (or press Enter for default): ").strip()
        if not project_name:
            project_name = "my_crewai_project"

    success = setup.setup(project_name)

    if success:
        print("\n🌟 You're all set to start building with CrewAI!")
    else:
        print("\n❌ Setup failed. Please check the error messages above.")
        sys.exit(1)


if __name__ == "__main__":
    main()