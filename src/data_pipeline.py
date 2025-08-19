import pandas as pd
from src.genai_module import GenAIPipeline
from src.defect_triage import DefectTriager
from src.refactor_utils import RefactorUtils


def main():
    # Example: Load data
    data = pd.DataFrame({'text': ['Example defect report', 'Another issue found']})

    # GenAI pipeline: extract insights
    genai = GenAIPipeline()
    insights = genai.analyze(data['text'])
    print('GenAI Insights:', insights)

    # Defect triaging
    triager = DefectTriager()
    triage_results = triager.triage(data['text'])
    print('Defect Triage:', triage_results)

    # Refactoring utility: check code quality
    refactor = RefactorUtils()
    quality_report = refactor.check_code_quality('src/data_pipeline.py')
    print('Code Quality Report:', quality_report)

if __name__ == '__main__':
    main()
