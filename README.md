# ASIS SEO Automation

A comprehensive SEO automation toolkit featuring Python scripts for backlink monitoring, keyword tracking, SEO audits, reporting, and a Streamlit dashboard for data visualization.

## 🚀 Features

- **Backlink Monitor**: Track and analyze backlink profiles
- **Keyword Tracking**: Monitor keyword rankings and performance
- **SEO Audit**: Comprehensive website SEO analysis
- **Reporting**: Generate detailed SEO reports
- **Streamlit Dashboard**: Interactive web dashboard for data visualization
- **n8n Workflow**: Automation workflow for seamless SEO processes

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for version control)

## ⚙️ Setup Instructions

### 1. Clone or Download the Project

If you have Git installed:
```bash
git clone <repository-url>
cd ASIS_SEO_Automation
```

Or download and extract the project files to your local machine.

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Google API Setup (Optional)

If you plan to use Google Search Console or Analytics APIs:

1. Copy the example credentials file:
   ```bash
   cp streamlit_dashboard/google_creds.json.example streamlit_dashboard/google_creds.json
   ```

2. Replace the content with your actual Google service account credentials
3. Enable the required APIs in Google Cloud Console:
   - Google Search Console API
   - Google Analytics API

## 🏃‍♂️ Running the Project

### Run Individual Scripts

```bash
# Backlink monitoring
python python_scripts/backlink_monitor.py

# Keyword tracking
python python_scripts/keyword_tracking.py

# SEO audit
python python_scripts/seo_audit.py

# Generate reports
python python_scripts/reporting.py
```

### Run Streamlit Dashboard

```bash
# Start the dashboard
streamlit run streamlit_dashboard/dashboard_alerts.py
```

The dashboard will be available at `http://localhost:8501`

### n8n Workflow

The n8n workflow file is located at `n8n_workflow/asis_seo_workflow.json`. Import this into your n8n instance to automate the SEO processes.

## 📊 Project Structure

```
ASIS_SEO_Automation/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── python_scripts/                    # Core Python scripts
│   ├── backlink_monitor.py           # Backlink monitoring
│   ├── keyword_tracking.py           # Keyword tracking
│   ├── seo_audit.py                  # SEO audit functionality
│   └── reporting.py                  # Report generation
├── streamlit_dashboard/               # Dashboard components
│   ├── dashboard_alerts.py           # Main dashboard
│   └── google_creds.json.example     # Google API credentials template
└── n8n_workflow/                     # Automation workflows
    └── asis_seo_workflow.json        # n8n workflow configuration
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory for configuration:

```env
# Google API Configuration
GOOGLE_CREDENTIALS_PATH=streamlit_dashboard/google_creds.json

# SEO Tool Configuration
DEFAULT_DOMAIN=example.com
CRAWL_DELAY=1

# Dashboard Configuration
DASHBOARD_PORT=8501
DEBUG_MODE=True
```

### API Keys

Add your API keys to the `.env` file:

```env
# Search Console
GOOGLE_SEARCH_CONSOLE_PROPERTY=https://example.com

# Third-party SEO tools (optional)
AHREFS_API_KEY=your_ahrefs_key
SEMRUSH_API_KEY=your_semrush_key
```

## 🚨 Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Ensure virtual environment is activated and dependencies are installed
2. **Google API Errors**: Check credentials file and API enablement
3. **Port Already in Use**: Change the port in Streamlit configuration

### Getting Help

- Check the error logs in the terminal
- Ensure all dependencies are properly installed
- Verify API credentials and permissions

## 📝 Usage Examples

### Basic SEO Audit
```python
from python_scripts.seo_audit import run_audit
results = run_audit('https://example.com')
print(results)
```

### Keyword Tracking
```python
from python_scripts.keyword_tracking import track_keywords
keywords = ['SEO', 'digital marketing', 'website optimization']
results = track_keywords(keywords, domain='example.com')
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.