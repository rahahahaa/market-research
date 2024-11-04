# main.py
from agents.industry_research_agent import IndustryResearchAgent


def main():
    # Initialize the agent with an example industry and company
    industry_name = "Automotive"
    company_name = "Tesla"

    # Create an instance of IndustryResearchAgent
    research_agent = IndustryResearchAgent(industry_name, company_name)

    # Perform industry and company research
    industry_info = research_agent.search_industry()
    company_focus = research_agent.search_company_focus()

    # Display the results
    print("\nIndustry Overview:")
    for info in industry_info:
        print(f"- {info}")

    print("\nCompany Focus Areas:")
    for focus in company_focus:
        print(f"- {focus}")


if __name__ == "__main__":
    main()

# main.py
from agents.industry_research_agent import IndustryResearchAgent
from agents.use_case_generation_agent import UseCaseGenerationAgent


def main():
    # Initialize the agent with an example industry and company
    industry_name = "Automotive"
    company_name = "Tesla"

    # Create an instance of IndustryResearchAgent
    research_agent = IndustryResearchAgent(industry_name, company_name)

    # Perform industry and company research
    industry_info = research_agent.search_industry()
    company_focus = research_agent.search_company_focus()

    # Display the results
    print("\nIndustry Overview:")
    for info in industry_info:
        print(f"- {info}")

    print("\nCompany Focus Areas:")
    for focus in company_focus:
        print(f"- {focus}")

    # Create an instance of UseCaseGenerationAgent
    use_case_agent = UseCaseGenerationAgent(industry_info, company_focus)

    # Generate use cases based on the gathered information
    use_cases = use_case_agent.generate_use_cases()

    # Display the generated use cases
    print("\nProposed Use Cases:")
    for case in use_cases:
        print(f"- {case}")


if __name__ == "__main__":
    main()

# main.py
from agents.industry_research_agent import IndustryResearchAgent
from agents.use_case_generation_agent import UseCaseGenerationAgent
from agents.resource_collection_agent import ResourceCollectionAgent


def main():
    # Initialize the agent with an example industry and company
    industry_name = "Automotive"
    company_name = "Tesla"

    # Create an instance of IndustryResearchAgent
    research_agent = IndustryResearchAgent(industry_name, company_name)

    # Perform industry and company research
    industry_info = research_agent.search_industry()
    company_focus = research_agent.search_company_focus()

    # Display the results
    print("\nIndustry Overview:")
    for info in industry_info:
        print(f"- {info}")

    print("\nCompany Focus Areas:")
    for focus in company_focus:
        print(f"- {focus}")

    # Create an instance of UseCaseGenerationAgent
    use_case_agent = UseCaseGenerationAgent(industry_info, company_focus)

    # Generate use cases based on the gathered information
    use_cases = use_case_agent.generate_use_cases()

    # Display the generated use cases
    print("\nProposed Use Cases:")
    for case in use_cases:
        print(f"- {case}")

    # Create an instance of ResourceCollectionAgent
    resource_agent = ResourceCollectionAgent(use_cases)

    # Search for resources based on the use cases
    resource_agent.search_resources()

    # Retrieve the resources collected
    resources = resource_agent.get_resources()

    # Display the collected resources
    print("\nResource Links:")
    for use_case, links in resources.items():
        print(f"\nUse Case: {use_case}")
        for link in links:
            print(f"- {link}")


if __name__ == "__main__":
    main()

# main.py
from agents.industry_research_agent import IndustryResearchAgent
from agents.use_case_generation_agent import UseCaseGenerationAgent
from agents.resource_collection_agent import ResourceCollectionAgent
from agents.final_proposal import FinalProposal


def main():
    # Initialize the agent with an example industry and company
    industry_name = "Automotive"
    company_name = "Tesla"

    # Create an instance of IndustryResearchAgent
    research_agent = IndustryResearchAgent(industry_name, company_name)

    # Perform industry and company research
    industry_info = research_agent.search_industry()
    company_focus = research_agent.search_company_focus()

    # Display the results
    print("\nIndustry Overview:")
    for info in industry_info:
        print(f"- {info}")

    print("\nCompany Focus Areas:")
    for focus in company_focus:
        print(f"- {focus}")

    # Create an instance of UseCaseGenerationAgent
    use_case_agent = UseCaseGenerationAgent(industry_info, company_focus)

    # Generate use cases based on the gathered information
    use_cases = use_case_agent.generate_use_cases()

    # Display the generated use cases
    print("\nProposed Use Cases:")
    for case in use_cases:
        print(f"- {case}")

    # Create an instance of ResourceCollectionAgent
    resource_agent = ResourceCollectionAgent(use_cases)

    # Search for resources based on the use cases
    resource_agent.search_resources()

    # Retrieve the resources collected
    resources = resource_agent.get_resources()

    # Display the collected resources
    print("\nResource Links:")
    for use_case, links in resources.items():
        print(f"\nUse Case: {use_case}")
        for link in links:
            print(f"- {link}")

    # Create an instance of FinalProposal
    proposal = FinalProposal(use_cases, resources)

    # Generate and display the final proposal
    final_proposal = proposal.generate_proposal()
    print("\nFinal Proposal:")
    for entry in final_proposal:
        print(f"\nUse Case: {entry['use_case']}")
        print("Resources:")
        for resource in entry["resources"]:
            print(f"- {resource}")


if __name__ == "__main__":
    main()

# Define your use cases here
use_cases = [
    {
        "title": "Automated Customer Support",
        "description": "Use AI chatbots to handle customer inquiries and complaints 24/7, reducing wait times and improving customer satisfaction.",
        "reference": "McKinsey Report on AI in Customer Experience.",
        "dataset_links": "[Customer Support Dataset](https://www.kaggle.com/datasets/saurabhshri/customer-support-dataset)",
    },
    {
        "title": "Predictive Maintenance",
        "description": "Implement machine learning algorithms to predict equipment failures and optimize maintenance schedules, minimizing downtime in manufacturing operations.",
        "reference": "Deloitte Insights on AI in Manufacturing.",
        "dataset_links": "[Predictive Maintenance Dataset](https://www.kaggle.com/datasets/shubhendra/predictive-maintenance-dataset)",
    },
    {
        "title": "Personalized Marketing Campaigns",
        "description": "Leverage customer data to create targeted marketing campaigns that enhance engagement and conversion rates through personalized recommendations.",
        "reference": "Harvard Business Review on AI in Marketing.",
        "dataset_links": "[Marketing Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)",
    },
    {
        "title": "Fraud Detection",
        "description": "Utilize machine learning models to detect fraudulent transactions in real-time, thereby reducing financial losses for companies in the finance sector.",
        "reference": "PwC Report on AI in Financial Services.",
        "dataset_links": "[Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/dalpozz/creditcard-fraud)",
    },
    {
        "title": "Supply Chain Optimization",
        "description": "Use AI algorithms to analyze supply chain data, optimizing routes and inventory levels to enhance efficiency and reduce costs.",
        "reference": "McKinsey Insights on AI in Supply Chain.",
        "dataset_links": "[Supply Chain Dataset](https://www.kaggle.com/datasets/soumyadip007/supply-chain-data)",
    },
    {
        "title": "Health Monitoring Systems",
        "description": "Implement AI solutions that analyze patient data to provide real-time health monitoring and early detection of potential health issues.",
        "reference": "Deloitte Insights on AI in Healthcare.",
        "dataset_links": "[Health Monitoring Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)",
    },
]


def save_proposal_to_file(use_cases, output_file="final_proposal.md"):
    with open(output_file, "w") as f:
        f.write("# Final Proposal\n\n")
        for use_case in use_cases:
            f.write(f'## {use_case["title"]}\n')
            f.write(f'{use_case["description"]}\n')
            f.write(f'Reference: {use_case["reference"]}\n')
            f.write(f'Dataset Links: {use_case["dataset_links"]}\n\n')
        f.write("---\n")
        f.write("## Resources\n\n")
        # Add any additional resources here if you have them


# Call the function to save the proposal
save_proposal_to_file(use_cases)


def save_proposal_to_file(use_cases, output_file="final_proposal.md"):
    with open(output_file, "w") as f:
        f.write("# Final Proposal\n\n")
        for use_case in use_cases:
            f.write(f'## {use_case["title"]}\n')
            f.write(f'{use_case["description"]}\n')
            f.write(f'Reference: {use_case["reference"]}\n')
            f.write(f'Dataset Links: {use_case["dataset_links"]}\n\n')
        f.write("---\n")
        f.write("## Resources\n\n")
        # Add any additional resources here if you have them


# Call the function to save the proposal
save_proposal_to_file(use_cases)
