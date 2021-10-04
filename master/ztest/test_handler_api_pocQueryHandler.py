import unittest
import requests as rq
import json
import pandas as pd
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

class TestHandlerApiIntentTestHandler(unittest.TestCase):  #
    """Test Util Tool"""

    @classmethod
    def setUp(self) -> None:
        self.all_corpus = pd.read_csv(os.path.join('./test_sample','silkB_corpus.tsv'), sep='\t', usecols=['intent', 'utterance', 'slots'])
        self.result_df = pd.DataFrame(columns=('intent', 'ori_intents', 'entities', 'ori_entities', 'utterance'))

    def request_fun(self, row):
        try:
            responses = rq.get('http://10.205.50.2/api/query?q=' + row["utterance"],
                               headers={'token': 'thor_pinyin'}).json()
            ori_responses = rq.get('http://10.205.50.23/api/query?q=' + row["utterance"],
                                   headers={'token': 'thor_pinyin'}).json()
            # intent
            intents = [response["value"] for response in responses["retStr"]["combine_intents"]]
            ori_intents = [response["value"] for response in ori_responses["retStr"]["combine_intents"]]
            self.assertEqual(intents, ori_intents)
            # entitie
            entities = responses["retStr"]["entities"]
            ori_entities = ori_responses["retStr"]["entities"]
            self.assertEqual(entities, ori_entities)
        except:
            try:
                s = pd.Series({'intent': intents, 'ori_intents': ori_intents, 'entities': responses["retStr"]["entities"],
                           'ori_entities': ori_responses["retStr"]["entities"], 'utterance': row["utterance"]})
                return s
            except:
                pass
        return None

    def test_post(self):
        processes = []

        with ThreadPoolExecutor(max_workers=100) as executor:
            for index, row in self.all_corpus.iterrows():
                # try:
                if index == 10000:
                    break
                processes.append(executor.submit(self.request_fun, row))
        for task in as_completed(processes):
            if isinstance(task.result(), pd.Series):
                self.result_df = self.result_df.append(task.result(), ignore_index=True)
        self.result_df.to_csv('./test_sample/thor0429_review.tsv', sep='\t', index=False)
if __name__ == '__main__':
    unittest.main()