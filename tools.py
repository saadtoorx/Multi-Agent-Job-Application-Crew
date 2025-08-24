# Tools for CrewAI agents with fallback for missing packages
import warnings
import os
warnings.filterwarnings("ignore")

def agent_tools():

    try:
        from crewai_tools import (
        FileReadTool,
        ScrapeWebsiteTool,
        MDXSearchTool,
        SerperDevTool)
        
        # Check if required environment variables are set
        if not os.getenv("OPENAI_API_KEY"):
            print("OPENAI_API_KEY not set, using fallback tools")
            return None, None, None, None
            
        search_tool = SerperDevTool()
        scrape_tool = ScrapeWebsiteTool()
        read_resume_tool = FileReadTool()
        semantic_search_resume_tool = MDXSearchTool()

        return search_tool, scrape_tool, read_resume_tool, semantic_search_resume_tool

    except ImportError as e:
        print(f"Error importing tools: {e}")
        return None, None, None, None
    except Exception as e:
        print(f"Error initializing tools: {e}")
        return None, None, None, None
