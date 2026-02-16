import pytest
from pytest_mock import MockerFixture
from accessibility_ai.app.scraper import extract_html_content

HTML_SIMULADO = """
<html>
    <body>
        <h1>Prueba de Accesibilidad</h1>
        
        <!-- Caso 1: Imagen sin alt (Debe fallar) -->
        <img src="logo.png" />
        
        <!-- Caso 2: Imagen correcta (No debe fallar) -->
        <img src="foto.jpg" alt="Foto de vacaciones" />
        
        <!-- Caso 3: Link vacío (Debe fallar) -->
        <a href="#"></a>
        
        <!-- Caso 4: Input sin label (Debe fallar) -->
        <input type="text" name="email" id="email" />
    </body>
</html>
"""

def test_extract_html_content_logic(mocker: MockerFixture):

    mock_response = mocker.Mock()
    mock_response.content = HTML_SIMULADO.encode('utf-8')
    mocker.patch("requests.get", return_value=mock_response)

    issues = extract_html_content("http://fake-url.com")

    assert len(issues) == 3

    assert issues[0].element_type == "Image"
    assert "missing alt attribute" in issues[0].issue_description or "Non-text content" in issues[0].issue_description

    # Verificamos que detectó el link vacío
    assert issues[1].element_type == "Link"
    assert "purpose of the link" in issues[1].issue_description
    # Verificamos que detectó el input
    assert issues[2].element_type == "Input"
    assert "requires user input" in issues[2].issue_description

    print("\n✅ ¡Test Unitario del Scraper Pasó Correctamente!")