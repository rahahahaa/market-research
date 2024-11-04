# agents/final_proposal.py


class FinalProposal:
    def __init__(self, use_cases, resources):
        self.use_cases = use_cases
        self.resources = resources

    def generate_proposal(self):
        proposal = []
        for use_case in self.use_cases:
            proposal_entry = {
                "use_case": use_case,
                "resources": self.resources.get(use_case, []),
            }
            proposal.append(proposal_entry)
        return proposal
