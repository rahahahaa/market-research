# agents/industry_research_agent.py
import requests
from bs4 import BeautifulSoup

class IndustryResearchAgent:
    def __init__(self, industry_name, company_name):
        self.industry_name = industry_name
        self.company_name = company_name
        self.research_results = []

    def search_industry(self):
        search_query = f"{self.industry_name} industry overview"
        print(f"Searching for {search_query}...")

        # Perform web scraping or API calls for industry research
        response = requests.get(f"https://www.google.com/search?q={search_query}")
        soup = BeautifulSoup(response.text, 'html.parser')

        # Parse results
        for item in soup.select('.BNeawe'):
            self.research_results.append(item.get_text())

        return self.research_results

    def search_company_focus(self):
        search_query = f"{self.company_name} company focus areas"
        print(f"Searching for {search_query}...")

        # Perform web scraping or API calls for company research
        response = requests.get(f"https://www.google.com/search?q={search_query}")
        soup = BeautifulSoup(response.text, 'html.parser')

        for item in soup.select('.BNeawe'):
            self.research_results.append(item.get_text())

        return self.research_results
