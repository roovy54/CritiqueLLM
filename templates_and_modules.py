# SWOT template
SWOT_template = '''
Given a user task and reasoning modules, adapt them to the specific task, and create a step-by-step reasoning plan with problems that can be faced while implementing the idea, in JSON format. Generate problems that are specific to the user task and action. Return only a simple string with no extra characters or comments.

Give as many valids strenghts, weaknesses, oppurtunities and threats as possible.
Number of strenghts, weaknesses, oppurtunities and threats can be not equal.

<input>
User Task: Given user tasks
Modules: Reasoning modules to solve given user tasks
<\input>

<output>
[
  {{
    "Module": "Module Name 1",
    "Action": "Adapted description 1",
    "Strengths": [
      "Strength 1",
      "Strength 2",
      "..."
    ],
    "Weaknesses": [
      "Weakness 1",
      "Weakness 2",
      "..."
    ],
    "Opportunities": [
      "Opportunity 1",
      "Opportunity 2",
      "..."
    ],
    "Threats": [
      "Threat 1",
      "Threat 2",
      "..."
    ]
  }},
  {{
    "Module": "Module Name 2",
    "Action": "Adapted description 2",
    "Strengths": [
      "Strength 1",
      "Strength 2",
      "..."
    ],
    "Weaknesses": [
      "Weakness 1",
      "Weakness 2",
      "..."
    ],
    "Opportunities": [
      "Opportunity 1",
      "Opportunity 2",
      "..."
    ],
    "Threats": [
      "Threat 1",
      "Threat 2",
      "..."
    ]
  }},
  {{
    "Module": "Module Name 3",
    "Action": "Adapted description 3",
    "Strengths": [
      "Strength 1",
      "Strength 2",
      "..."
    ],
    "Weaknesses": [
      "Weakness 1",
      "Weakness 2",
      "..."
    ],
    "Opportunities": [
      "Opportunity 1",
      "Opportunity 2",
      "..."
    ],
    "Threats": [
      "Threat 1",
      "Threat 2",
      "..."
    ]
  }}
]
<\output>

---

User Task: {}
Modules: {}
Implemented Schema:

---
'''

# Modules
reasoning_modules = {"Real World Relevance and Acuteness Analyzer",
                     "Market and User Base Analyzer",
                     "Resources and Capital Analyzer"}
