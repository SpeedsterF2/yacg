# Attention, this file is generated. Manual changes get lost with the next
# run of the code generation.
# created by yacg (template: pythonBeans.mako v1.0.0)

import unittest

import yacg.model.asyncapi


class TestYacgOpenapiModel (unittest.TestCase):
    def testOperationBase(self):
        x = yacg.model.asyncapi.OperationBase()
        self.assertIsNotNone(x)

    def testParameter(self):
        x = yacg.model.asyncapi.Parameter()
        self.assertIsNotNone(x)

    def testMessage(self):
        x = yacg.model.asyncapi.Message()
        self.assertIsNotNone(x)

    def testAmqpBinding(self):
        x = yacg.model.asyncapi.AmqpBinding()
        self.assertIsNotNone(x)

    def testAmqpSubscriberImplementation(self):
        x = yacg.model.asyncapi.AmqpSubscriberImplementation()
        self.assertIsNotNone(x)

    def testXResponseType(self):
        x = yacg.model.asyncapi.XResponseType()
        self.assertIsNotNone(x)

    def testAsyncApiDefinition(self):
        x = yacg.model.asyncapi.AsyncApiDefinition()
        self.assertIsNotNone(x)

    def testInfo(self):
        x = yacg.model.asyncapi.Info()
        self.assertIsNotNone(x)

    def testServer(self):
        x = yacg.model.asyncapi.Server()
        self.assertIsNotNone(x)

    def testChannel(self):
        x = yacg.model.asyncapi.Channel()
        self.assertIsNotNone(x)

    def testPublishDescription(self):
        x = yacg.model.asyncapi.PublishDescription()
        self.assertIsNotNone(x)

    def testSubscribeDescription(self):
        x = yacg.model.asyncapi.SubscribeDescription()
        self.assertIsNotNone(x)

    def testXParameter(self):
        x = yacg.model.asyncapi.XParameter()
        self.assertIsNotNone(x)

    def testXTokenContent(self):
        x = yacg.model.asyncapi.XTokenContent()
        self.assertIsNotNone(x)

    def testAmqpBindingExchangeTypeEnum(self):
        self.assertIsNotNone(yacg.model.asyncapi.AmqpBindingExchangeTypeEnum.TOPIC)
        self.assertIsNotNone(yacg.model.asyncapi.AmqpBindingExchangeTypeEnum.FAN)
        self.assertIsNotNone(yacg.model.asyncapi.AmqpBindingExchangeTypeEnum.DIRECT)
        self.assertIsNotNone(yacg.model.asyncapi.AmqpBindingExchangeTypeEnum.HEADER)

    def testAmqpQueue(self):
        x = yacg.model.asyncapi.AmqpQueue()
        self.assertIsNotNone(x)

    def testAmqpQueueTypeEnum(self):
        self.assertIsNotNone(yacg.model.asyncapi.AmqpQueueTypeEnum.QUORUM)
        self.assertIsNotNone(yacg.model.asyncapi.AmqpQueueTypeEnum.CLASSIC)


if __name__ == '__main__':
    unittest.main()
