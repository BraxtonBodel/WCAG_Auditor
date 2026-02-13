import requests

# 15 Criterios de éxito reales WCAG 2.2
WCAG_DATA = [
    {"success_criterion": "1.1.1", "level": "A", "description": "Non-text Content: All non-text content that is presented to the user has a text alternative that serves the equivalent purpose."},
    {"success_criterion": "1.3.1", "level": "A", "description": "Info and Relationships: Information, structure, and relationships conveyed through presentation can be programmatically determined or are available in text."},
    {"success_criterion": "1.4.3", "level": "AA", "description": "Contrast (Minimum): The visual presentation of text and images of text has a contrast ratio of at least 4.5:1."},
    {"success_criterion": "1.4.10", "level": "AA", "description": "Reflow: Content can be presented without loss of information or functionality, and without requiring scrolling in two dimensions for vertical scrolling content at a width equivalent to 320 CSS pixels."},
    {"success_criterion": "2.1.1", "level": "A", "description": "Keyboard: All functionality of the content is operable through a keyboard interface without requiring specific timings for individual keystrokes."},
    {"success_criterion": "2.1.2", "level": "A", "description": "No Keyboard Trap: If keyboard focus can be moved to a component of the page using a keyboard interface, then focus can be moved away from that component using only a keyboard interface."},
    {"success_criterion": "2.4.3", "level": "A", "description": "Focus Order: If a Web page can be navigated sequentially and the navigation sequences affect meaning or operation, focusable components receive focus in an order that preserves meaning and operability."},
    {"success_criterion": "2.4.4", "level": "A", "description": "Link Purpose (In Context): The purpose of each link can be determined from the link text alone or from the link text together with its programmatically determined link context."},
    {"success_criterion": "2.4.7", "level": "AA", "description": "Focus Visible: Any keyboard operable user interface has a mode of operation where the keyboard focus indicator is visible."},
    {"success_criterion": "3.1.1", "level": "A", "description": "Language of Page: The default human language of each Web page can be programmatically determined."},
    {"success_criterion": "3.2.2", "level": "A", "description": "On Input: Changing the setting of any user interface component does not automatically cause a change of context unless the user has been advised of the behavior before using the component."},
    {"success_criterion": "3.3.1", "level": "A", "description": "Error Identification: If an input error is automatically detected, the item that is in error is identified and the error is described to the user in text."},
    {"success_criterion": "3.3.2", "level": "A", "description": "Labels or Instructions: Labels or instructions are provided when content requires user input."},
    {"success_criterion": "4.1.1", "level": "A", "description": "Parsing: In content implemented using markup languages, elements have complete start and end tags, elements are nested according to their specifications, and elements do not contain duplicate attributes."},
    {"success_criterion": "4.1.2", "level": "A", "description": "Name, Role, Value: For all user interface components, the name and role can be programmatically determined; states, properties, and values can be programmatically set."}
]

def seed():
    url = "http://localhost:8000/guidelines/"
    print(f"🚀 Iniciando carga masiva de {len(WCAG_DATA)} criterios...")
    
    for item in WCAG_DATA:
        try:
            response = requests.post(url, json=item, timeout=30)
            if response.status_code == 200:
                print(f"✅ {item['success_criterion']} cargado exitosamente.")
            else:
                print(f"⚠️ Error en {item['success_criterion']}: {response.json()}")
        except Exception as e:
            print(f"❌ Fallo de conexión: {e}")

if __name__ == "__main__":
    seed()