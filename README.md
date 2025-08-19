# Palantir Data Scientist Project

This project demonstrates Gen-AI and Data Science skills relevant for a Palantir production support role, including:
- Gen-AI pipeline (NLP/LLM)
- Defect triaging and root cause analysis
- Code refactoring utilities
- Production accuracy monitoring

## Structure
- `src/`: Core modules (pipeline, GenAI, triage, refactoring)
- `notebooks/`: Jupyter demo for GenAI
- `tests/`: Unit tests

## Quickstart
1. Install requirements: `pip install -r requirements.txt`
2. Run the pipeline: `python src/data_pipeline.py`
3. Explore the GenAI notebook in `notebooks/`

## Requirements
See `requirements.txt` for dependencies.

## For Recruiters
This repo is a technical demonstration for the Palantir Data Scientist position (Prod Support, Gen-AI, Data Science, RCA, Defect Triaging, Refactoring).

# Running Tests

To run all unit tests and verify the pipeline modules:

```bash
# (Optional) Activate your virtual environment
source .venv/bin/activate

# Run all tests
python -m unittest discover -s tests
```

You should see output like:

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

# Running the Pipeline

To run the main data pipeline and see example outputs:

```bash
# (Optional) Activate your virtual environment
source .venv/bin/activate

# Run the pipeline using the module command
python -m src.data_pipeline
```

You should see output similar to:

```
GenAI Insights: ['Insight for: Defect: Missing HER2 status for breast cancer patient 100301', ...]
Defect Triage: ['Triaged: Defect: Missing HER2 status for breast cancer patient 100301', ...]
Code Quality Report: Checked code quality for src/data_pipeline.py
```

# Project Architecture (Mermaid)

```mermaid
graph TD
    A[Data Input] --> B[GenAI Pipeline]
    B --> C[Defect Triager]
    C --> D[Refactor Utils]
    D --> E[Production Accuracy Report]
```
