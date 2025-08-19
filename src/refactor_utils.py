
import subprocess
import logging

class RefactorUtils:
    """Utilities for code refactoring and quality checks."""
    def check_code_quality(self, filepath: str) -> str:
        """Run flake8 static analysis on the given file and return the results."""
        logging.info(f'Checking code quality for {filepath} using flake8.')
        try:
            result = subprocess.run([
                'flake8', filepath
            ], capture_output=True, text=True)
            if result.returncode == 0:
                logging.info(f'No issues found by flake8 in {filepath}.')
                return f"No issues found by flake8 in {filepath}."
            else:
                logging.warning(f'flake8 issues in {filepath}:\n{result.stdout}')
                return f"flake8 issues in {filepath}:\n{result.stdout}"
        except Exception as e:
            logging.error(f'Error running flake8: {e}', exc_info=True)
            return f"Error running flake8: {e}"
