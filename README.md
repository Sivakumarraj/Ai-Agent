# Browser Use WebUI

Control your browser with AI assistance. This project provides a web interface for interacting with browser automation using various AI models.

## Features

- Multiple LLM provider support (OpenAI, Anthropic, Google, etc.)
- Browser automation with AI assistance
- Deep research capabilities
- Recording and trace functionality
- Configurable settings and parameters

## Installation

1. Clone the repository:
```bash
git clone https://github.com/browser-use/web-ui.git
cd web-ui
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -e ".[dev]"
```

4. Install Playwright browsers:
```bash
playwright install
```

## Configuration

Create a `.env` file in the project root with your API keys:

```env
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_key
```

## Usage

Start the WebUI:

```bash
python -m browser_use_webui.webui --ip 127.0.0.1 --port 7788
```

## Development

1. Install development dependencies:
```bash
pip install -e ".[dev]"
```

2. Run tests:
```bash
pytest tests/
```

## License

MIT License - see LICENSE file for details.