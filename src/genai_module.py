from typing import List
import spacy
import logging

class GenAIPipeline:
    """GenAI pipeline for analyzing defect reports using spaCy NLP."""
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def analyze(self, texts: List[str]) -> List[str]:
        insights = []
        for t in texts:
            logging.info(f'Analyzing text with GenAI: {t}')
            doc = self.nlp(t)
            ents = [(ent.text, ent.label_) for ent in doc.ents]
            if ents:
                insight = f"Entities found: {ents}"
            else:
                insight = "No entities found."
            insights.append(insight)
        return insights
