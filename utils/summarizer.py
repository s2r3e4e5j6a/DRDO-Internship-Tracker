def summarize_opportunity(opportunity):

    summary = f"""
Programme: {opportunity.get('Lab', 'Unknown')}

Organization: {opportunity.get('Source', 'Unknown')}

Deadline: {opportunity.get('Deadline', 'Unknown')}

Eligibility: {opportunity.get('Eligibility', 'Unknown')}

Location: {opportunity.get('Location', 'Unknown')}
"""

    return summary