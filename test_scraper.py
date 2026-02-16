from accessibility_ai.app.scraper import extract_html_content

url = "https://www.w3.org/WAI/demos/bad/before/survey.html"
resultado = extract_html_content(url)

print(f"Resultado del scraping: {resultado}")