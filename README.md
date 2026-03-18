# DataOps Workbench

A practical and structured environment to work with data, troubleshooting, and legacy systems in a single workflow.

---

## Overview

DataOps Workbench combines:

* Python + VS Code + Jupyter
* Power BI (data modelling + DAX)
* Relational and NoSQL databases
* AI assistants (ChatGPT, Gemini, NotebookLM)
* Legacy systems (Visual FoxPro + AVFP)

This is not a demo project.
It is designed for real-world use: data analysis, troubleshooting, process improvement, and system modernization.

---

## Core Components

### Development

* Python (pandas, numpy)
* VS Code + Jupyter
* Virtual environments (.venv)

### Data & Databases

* MySQL
* PostgreSQL
* SQL Server Express
* MongoDB
* DBeaver / Workbench / SSMS / Compass

### Analytics

* Power BI
* DAX
* DAX Studio

### AI Layer

* ChatGPT
* Gemini
* NotebookLM

### Legacy

* Visual FoxPro (VFP)
* Advanced Visual FoxPro (AVFP)
* DBF integration and migration support

---

## Project Structure

```
dataops-workbench/
│
├── docs/
├── scripts/
├── templates/
├── examples/
├── vfp/
```

---

## Quick Start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r templates/requirements.txt
```

---

## Use Cases

* Data analysis and reporting
* Troubleshooting technical issues
* Root cause analysis
* Data pipeline prototyping
* Legacy system documentation and migration

---

## AI Workflow (Recommended)

Each project should include:

* 1 ChatGPT conversation
* 1 Gemini conversation
* 1 NotebookLM notebook

Used for:

* code explanation
* documentation
* refactoring
* architecture decisions

---

## Maturity Model

* **Basic** → environment working
* **Intermediate** → consistent usage
* **Advanced** → automation and integration

---

## Status

Work in progress — evolving into a complete data and troubleshooting framework.

---

## License

Free to use and adapt.
