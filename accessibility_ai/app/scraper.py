import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class AccessibilityIssue:
    element_type: str
    html_content: str
    issue_description: str
    suggested_fix: str

def extract_html_content(url: str) -> List[AccessibilityIssue]:
    print(f"Descargando: {url}")
    response = requests.get(url, verify=False)

    soup = BeautifulSoup(response.content, 'html.parser')

    issues_found = []
    images = soup.find_all('img')
    links = soup.find_all('a')
    inputs = soup.find_all('input')
    print(f"inputs: {inputs}")

    for image in images:
        alt_attr = image.get('alt')
        if alt_attr is None:
            issue = AccessibilityIssue(
                element_type="Image",
                html_content=str(image),
                issue_description="Non-text content presented to user without a text alternative that serves the equivalent purpose.",
                suggested_fix="Add an alt attribute describing the image content."
            )
            issues_found.append(issue)
        elif alt_attr == "":
            pass

    for link in links:
        link_content = link.get_text()
        if not link_content:
            issue = AccessibilityIssue(
                element_type="Link",
                html_content=link_content,
                issue_description="The purpose of the link cannot be determined from the link text alone.",
                suggested_fix="Avoid having links without text content present"
            )
            issues_found.append(issue)

    for input in inputs:
        input_id = input.get('id')
        input_label = soup.find('label', {'for': input_id})
        if not input_label:
            issue = AccessibilityIssue(
                element_type="Input",
                html_content="",
                issue_description="Content requires user input but no labels or instructions are provided.",
                suggested_fix="All inputs must have a label attribute with defined value present"
            )
            issues_found.append(issue)

    return issues_found