# Attention, this file is generated. Manual changes get lost with the next
# run of the code generation.
# created by yacg (template: pythonBeans.mako v1.0.0)

import unittest

import yacg.model.asyncapi
import yacg.model.model


class TestYacgOpenapiModel (unittest.TestCase):
    def testOperationBase(self):
        x = yacg.model.asyncapi.OperationBase()
        self.assertIsNotNone(x)

    def testMessage(self):
        x = yacg.model.asyncapi.Message()
        self.assertIsNotNone(x)

    def testAmqpBinding(self):
        x = yacg.model.asyncapi.AmqpBinding()
        self.assertIsNotNone(x)

    def testAsyncApiType(self):
        x = yacg.model.asyncapi.AsyncApiType()
        self.assertIsNotNone(x)

    def testAsyncApiInfoType(self):
        x = yacg.model.asyncapi.AsyncApiInfoType()
        self.assertIsNotNone(x)

    def testAsyncApiServerType(self):
        x = yacg.model.asyncapi.AsyncApiServerType()
        self.assertIsNotNone(x)

    def testAsyncApiChannelType(self):
        x = yacg.model.asyncapi.AsyncApiChannelType()
        self.assertIsNotNone(x)

    def testParameter(self):
        x = yacg.model.asyncapi.Parameter()
        self.assertIsNotNone(x)

    def testPublishDescription(self):
        x = yacg.model.asyncapi.PublishDescription()
        self.assertIsNotNone(x)

    def testSubscribeDescription(self):
        x = yacg.model.asyncapi.SubscribeDescription()
        self.assertIsNotNone(x)

    def testAmqpSubscriberImplementation(self):
        x = yacg.model.asyncapi.AmqpSubscriberImplementation()
        self.assertIsNotNone(x)

    def testXResponseType(self):
        x = yacg.model.asyncapi.XResponseType()
        self.assertIsNotNone(x)

    def testXParameter(self):
        x = yacg.model.asyncapi.XParameter()
        self.assertIsNotNone(x)

    def testPayloadType(self):
        x = yacg.model.asyncapi.PayloadType()
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
