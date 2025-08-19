import unittest
from src.genai_module import GenAIPipeline
from src.defect_triage import DefectTriager
from src.refactor_utils import RefactorUtils

class TestPipeline(unittest.TestCase):
    def test_genai_analyze(self):
        genai = GenAIPipeline()
        result = genai.analyze(["test defect"])
        self.assertIn("Insight for: test defect", result)

    def test_defect_triage(self):
        triager = DefectTriager()
        result = triager.triage(["test defect"])
        self.assertIn("Triaged: test defect", result)

    def test_refactor_utils(self):
        refactor = RefactorUtils()
        result = refactor.check_code_quality("dummy.py")
        self.assertIn("Checked code quality for dummy.py", result)

if __name__ == "__main__":
    unittest.main()
