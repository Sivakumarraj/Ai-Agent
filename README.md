Step 1: Clone the Repository
git clone https://github.com/browser-use/web-ui.git
cd web-ui
Step 2: Install uv (Python package manager)
For PowerShell (Windows)
powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
Step 3: Create and Activate Virtual Environment
Using uv (Recommended)
uv venv --python 3.11
Activate the Virtual Environment
For Windows (Command Prompt)
.venv\Scripts\activate
For Windows (PowerShell)
powershell
.\.venv\Scripts\Activate.ps1
Step 4: Install Dependencies
Install Python Packages
uv pip install -r requirements.txt
Install Playwright
playwright install
Step 5: Run the WebUI Locally
python webui.py --ip 127.0.0.1 --port 7788
