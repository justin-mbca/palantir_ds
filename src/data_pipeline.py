
import pandas as pd
import logging
from src.genai_module import GenAIPipeline
from src.defect_triage import DefectTriager
from src.refactor_utils import RefactorUtils


def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    try:
        # Example: Load oncology biomarker defect reports
        data = pd.DataFrame({
            'text': [
                'Defect: Missing HER2 status for breast cancer patient 100301',
                'Defect: EGFR mutation result not recorded for lung cancer patient 100302',
                'Defect: Inconsistent PD-L1 expression values for patient 100303',
                'Defect: Invalid ALK rearrangement result for patient 100304',
                'Defect: BRAF mutation status missing in melanoma patient 100305',
                'Defect: KRAS mutation result duplicated for colorectal cancer patient 100306',
                'Defect: Biomarker panel incomplete for patient 100307',
                'Defect: Unrecognized biomarker code in patient 100308',
                'Defect: ER/PR status not updated after retest for patient 100309',
                'Defect: Biomarker result date precedes sample collection date for patient 100310'
            ]
        })

        # GenAI pipeline: extract insights
        genai = GenAIPipeline()
        insights = genai.analyze(data['text'])
        logging.info(f'GenAI Insights: {insights}')

        # Defect triaging
        triager = DefectTriager()
        triage_results = triager.triage(data['text'])
        logging.info(f'Defect Triage: {triage_results}')

        # Refactoring utility: check code quality
        refactor = RefactorUtils()
        quality_report = refactor.check_code_quality('src/data_pipeline.py')
        logging.info(f'Code Quality Report: {quality_report}')
    except Exception as e:
        logging.error(f'Pipeline failed: {e}', exc_info=True)

if __name__ == '__main__':
    main()
