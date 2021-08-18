import unittest
import os.path

import yacg.model.modelFuncs as modelFuncs
import yacg.model.config as config

from yacg.builder.jsonBuilder import getModelFromJson


class TestModelFuncs (unittest.TestCase):
    def testGetDomains(self):
        modelFile = 'resources/models/json/yacg_asyncapi.json'
        modelFileExists = os.path.isfile(modelFile)        
        self.assertTrue(modelFileExists)
        model = config.Model()
        model.schema = modelFile
        modelTypes = getModelFromJson(model, [])
        domains = modelFuncs.getDomainsAsList(modelTypes)
        self.assertEqual(2, len(domains))
