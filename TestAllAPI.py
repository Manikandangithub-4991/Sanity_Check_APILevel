import json
import unittest

from ConfigManager import ConfigManager
from client.RestClient import RestClient


class TestAllAPI(unittest.TestCase):
    restClient = RestClient()
    sop_url = ConfigManager.sop_predict_url
    classifier_url = ConfigManager.classifier_url
    nlu_url = ConfigManager.nlu_url

    sop_data = {"botInstance": "7j6RXz6v4an2sjesD",
                "input": "what is the education allowance as part of WBS?",
                "noOfResults": 10,
                "minConfidence": 0.3}

    classifier_data = {
        "botInstance": "iHJ47TMLcfaJcccTM",
        "input": "desktop won t boot up",
        "noOfResults": "3",
        "additionalInputs": "xxxxx"}

    nlu_data = {
        "inputPath":"/home/rootuser/BotRunENV/NLU_BOT/data/OS.json",
        "botInstance":"OS",
        "inputText":"read and write"}

    def test_sop_api_wbsclaim(self):
        data = json.dumps(self.sop_data)
        actual_response = self.restClient.post(self.sop_url, data)
        response = actual_response["Response"]["RelevantDocuments"][0]["SectionName"]
        self.assertTrue(response.startswith("1.3 Education Allowance as part of WBS"))

    def test_classifier_desktop(self):
        data = json.dumps(self.classifier_data)
        actual_response = self.restClient.post(self.classifier_url, data)
        response = actual_response["result"][1][0]["group"]
        self.assertTrue(response.startswith("Desktop Management Support Services"))

    def test_nlu_api_usb(self):
        data = json.dumps(self.nlu_data)
        actual_response = self.restClient.post(self.nlu_url, data)
        self.assertEquals("OS-USBCONFIG",actual_response["intent"])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestALLAPI)
    unittest.TextTestRunner(verbosity=2).run(suite)
