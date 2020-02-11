import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvery(unittest.TestCase):

    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survery=AnonymousSurvey(question)
        self.responses=['English','Spanish','Mandarin']


    def test_store_single_response(self):
        self.my_survery.store_response(self.responses[0])

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survery.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survery.responses)

    def test_store_three_response(self):
        question = "What language did you first learn to speak?"
        my_suvery = AnonymousSurvey(question)
        responses=['English','Spanish','Mandarin']
        for response in responses:
            my_suvery.store_response(response)
        for response in responses:
            self.assertIn('English', my_suvery.responses)

unittest.main()