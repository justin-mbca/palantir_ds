import unittest
from src.genai_module import GenAIPipeline
from src.defect_triage import DefectTriager
from src.refactor_utils import RefactorUtils


class TestPipeline(unittest.TestCase):
    def test_genai_entity_extraction(self):
        genai = GenAIPipeline()
        # Should find entity '100301' as a number/date
        result = genai.analyze(["Defect: Missing HER2 status for breast cancer patient 100301"])
        self.assertTrue(any("100301" in r for r in result))

    def test_defect_triage_severity(self):
        triager = DefectTriager()
        # High severity
        result_high = triager.triage(["Defect: Missing HER2 status"])
        self.assertTrue(any("High" in r for r in result_high))
        # Medium severity
        result_medium = triager.triage(["Defect: Invalid code"])
        self.assertTrue(any("Medium" in r for r in result_medium))
        # Low severity
        result_low = triager.triage(["Defect: Biomarker panel incomplete"])
        self.assertTrue(any("Low" in r for r in result_low))

    def test_refactor_utils_flake8(self):
        refactor = RefactorUtils()
        # Should handle non-existent file gracefully
        result = refactor.check_code_quality("not_a_real_file.py")
        self.assertTrue("Error running flake8" in result or "No issues found" in result or "flake8 issues" in result)

if __name__ == "__main__":
    unittest.main()
