# Attention, this file is generated. Manual changes get lost with the next
# run of the code generation.
# created by yacg (template: pythonBeans.mako v1.0.0)

from enum import Enum
import yacg.model.model


class OperationBase:
    def __init__(self):

        self.operationId = None

        self.summary = None

        self.description = None

        self.message = None

        self.xToken = []

        self.amqpBinding = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.operationId = dict.get('operationId', None)

        obj.summary = dict.get('summary', None)

        obj.description = dict.get('description', None)

        obj.message = Message.dictToObject(dict.get('message', None))

        arrayXToken = dict.get('xToken', [])
        for elemXToken in arrayXToken:
            obj.xToken.append(
                XTokenContent.dictToObject(elemXToken))

        obj.amqpBinding = AmqpBinding.dictToObject(dict.get('amqpBinding', None))
        return obj


class Message:
    """ Container that describes the messages are sent
    """

    def __init__(self):

        #: Container that describes the messages are sent
        self.xParameters = []

        #: Container that describes the messages are sent
        self.payload = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        arrayXParameters = dict.get('xParameters', [])
        for elemXParameters in arrayXParameters:
            obj.xParameters.append(
                XParameter.dictToObject(elemXParameters))

        obj.payload = PayloadType.dictToObject(dict.get('payload', None))
        return obj


class XTokenContent:
    """ claim that is expected as part of a attached JWT token
    """

    def __init__(self):

        #: claim that is expected as part of a attached JWT token
        self.name = None

        #: claim that is expected as part of a attached JWT token
        self.description = None

        #: claim that is expected as part of a attached JWT token
        self.type = None

        #: claim that is expected as part of a attached JWT token
        self.isArray = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.name = dict.get('name', None)

        obj.description = dict.get('description', None)

        obj.type = yacg.model.model.Type.dictToObject(dict.get('type', None))

        obj.isArray = dict.get('isArray', None)
        return obj


class AmqpBinding:
    """ specific AMQP binding properties
    """

    def __init__(self):

        #: specific AMQP binding properties
        self.exchangeName = None

        #: specific AMQP binding properties
        self.exchangeType = None

        #: specific AMQP binding properties
        self.replyTo = "amq.rabbitmq.reply-to"

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.exchangeName = dict.get('exchangeName', None)

        obj.exchangeType = AmqpBindingExchangeTypeEnum.valueForString(dict.get('exchangeType', None))

        obj.replyTo = dict.get('replyTo', "amq.rabbitmq.reply-to")
        return obj


class AsyncApiType (yacg.model.model.Type):
    """ Base type to identify AsyncApi types
    """

    def __init__(self):
        super(yacg.model.model.Type, self).__init__()
        pass

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()
        return obj


class AsyncApiInfoType (AsyncApiType):
    """ Subset of the info object attribs: https://www.asyncapi.com/docs/specifications/v2.0.0#infoObject
    """

    def __init__(self):
        super(AsyncApiType, self).__init__()

        #: Subset of the info object attribs: https://www.asyncapi.com/docs/specifications/v2.0.0#infoObject
        self.title = None

        #: Subset of the info object attribs: https://www.asyncapi.com/docs/specifications/v2.0.0#infoObject
        self.version = None

        #: Subset of the info object attribs: https://www.asyncapi.com/docs/specifications/v2.0.0#infoObject
        self.description = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.title = dict.get('title', None)

        obj.version = dict.get('version', None)

        obj.description = dict.get('description', None)
        return obj


class AsyncApiServerType (AsyncApiType):
    """ one entry of the servers section
    """

    def __init__(self):
        super(AsyncApiType, self).__init__()

        #: one entry of the servers section
        self.name = None

        #: one entry of the servers section
        self.url = None

        #: one entry of the servers section
        self.description = None

        #: one entry of the servers section
        self.protocol = None

        #: one entry of the servers section
        self.protocolVersion = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.name = dict.get('name', None)

        obj.url = dict.get('url', None)

        obj.description = dict.get('description', None)

        obj.protocol = dict.get('protocol', None)

        obj.protocolVersion = dict.get('protocolVersion', None)
        return obj


class AsyncApiChannelType (AsyncApiType):
    """ one entry of the channels section
    """

    def __init__(self):
        super(AsyncApiType, self).__init__()

        #: one entry of the channels section
        self.key = None

        #: one entry of the channels section
        self.description = None

        #: one entry of the channels section
        self.parameters = []

        #: one entry of the channels section
        self.publish = None

        #: one entry of the channels section
        self.subscribe = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.key = dict.get('key', None)

        obj.description = dict.get('description', None)

        arrayParameters = dict.get('parameters', [])
        for elemParameters in arrayParameters:
            obj.parameters.append(
                Parameter.dictToObject(elemParameters))

        obj.publish = PublishDescription.dictToObject(dict.get('publish', None))

        obj.subscribe = SubscribeDescription.dictToObject(dict.get('subscribe', None))
        return obj


class Parameter:
    """ Parameters contained in the channel key
    """

    def __init__(self):

        #: Parameters contained in the channel key
        self.name = None

        #: Parameters contained in the channel key
        self.description = None

        #: Parameters contained in the channel key
        self.type = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.name = dict.get('name', None)

        obj.description = dict.get('description', None)

        obj.type = yacg.model.model.Type.dictToObject(dict.get('type', None))
        return obj


class PublishDescription (OperationBase):
    """ Configuration parameter needed for publishing
    """

    def __init__(self):
        super(OperationBase, self).__init__()

        #: Configuration parameter needed for publishing
        self.amqpSubscriberImplementation = None

        #: Configuration parameter needed for publishing
        self.responseType = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = OperationBase.dictToObject(dict)
        obj.amqpSubscriberImplementation = AmqpSubscriberImplementation.dictToObject(dict.get('amqpSubscriberImplementation', None))

        obj.responseType = XResponseType.dictToObject(dict.get('responseType', None))
        return obj


class SubscribeDescription (OperationBase):
    """ Configuration parameter needed to subscribe data
    """

    def __init__(self):
        super(OperationBase, self).__init__()
        pass

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()
        return obj


class AmqpSubscriberImplementation:
    """ AMQP specific subscriber settings
    """

    def __init__(self):

        #: AMQP specific subscriber settings
        self.queue = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.queue = AmqpQueue.dictToObject(dict.get('queue', None))
        return obj


class XResponseType:
    """ type that is responded in RPC style communication
    """

    def __init__(self):

        #: type that is responded in RPC style communication
        self.description = None

        #: type that is responded in RPC style communication
        self.isArray = False

        #: type that is responded in RPC style communication
        self.arrayMinItems = None

        #: type that is responded in RPC style communication
        self.arrayMaxItems = None

        #: type that is responded in RPC style communication
        self.arrayUniqueItems = None

        #: type that is responded in RPC style communication
        self.type = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.description = dict.get('description', None)

        obj.isArray = dict.get('isArray', False)

        obj.arrayMinItems = dict.get('arrayMinItems', None)

        obj.arrayMaxItems = dict.get('arrayMaxItems', None)

        obj.arrayUniqueItems = dict.get('arrayUniqueItems', None)

        obj.type = yacg.model.model.Type.dictToObject(dict.get('type', None))
        return obj


class XParameter:
    """ models the custom parameters
    """

    def __init__(self):

        #: models the custom parameters
        self.name = None

        #: models the custom parameters
        self.description = None

        #: models the custom parameters
        self.type = None

        #: models the custom parameters
        self.isArray = False

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.name = dict.get('name', None)

        obj.description = dict.get('description', None)

        obj.type = yacg.model.model.Type.dictToObject(dict.get('type', None))

        obj.isArray = dict.get('isArray', False)
        return obj


class PayloadType:
    def __init__(self):

        self.type = None

        self.isArray = False

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.type = yacg.model.model.Type.dictToObject(dict.get('type', None))

        obj.isArray = dict.get('isArray', False)
        return obj


class AmqpBindingExchangeTypeEnum(Enum):
    TOPIC = 'topic'
    FAN = 'fan'
    DIRECT = 'direct'
    HEADER = 'header'

    @classmethod
    def valueForString(cls, stringValue):
        lowerStringValue = stringValue.lower() if stringValue is not None else None
        if lowerStringValue is None:
            return None
        elif lowerStringValue == 'topic':
            return AmqpBindingExchangeTypeEnum.TOPIC
        elif lowerStringValue == 'fan':
            return AmqpBindingExchangeTypeEnum.FAN
        elif lowerStringValue == 'direct':
            return AmqpBindingExchangeTypeEnum.DIRECT
        elif lowerStringValue == 'header':
            return AmqpBindingExchangeTypeEnum.HEADER
        else:
            return None

    @classmethod
    def valueAsString(cls, enumValue):
        if enumValue is None:
            return ''
        elif enumValue == AmqpBindingExchangeTypeEnum.TOPIC:
            return 'topic'
        elif enumValue == AmqpBindingExchangeTypeEnum.FAN:
            return 'fan'
        elif enumValue == AmqpBindingExchangeTypeEnum.DIRECT:
            return 'direct'
        elif enumValue == AmqpBindingExchangeTypeEnum.HEADER:
            return 'header'
        else:
            return ''



class AmqpQueue:
    """ AMQP specific queue settings
    """

    def __init__(self):

        #: AMQP specific queue settings
        self.name = None

        #: AMQP specific queue settings
        self.type = None

        #: AMQP specific queue settings
        self.durable = None

        #: AMQP specific queue settings
        self.exclusive = None

        #: AMQP specific queue settings
        self.maxLength = None

        #: AMQP specific queue settings
        self.msgTtl = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.name = dict.get('name', None)

        obj.type = AmqpQueueTypeEnum.valueForString(dict.get('type', None))

        obj.durable = dict.get('durable', None)

        obj.exclusive = dict.get('exclusive', None)

        obj.maxLength = dict.get('maxLength', None)

        obj.msgTtl = dict.get('msgTtl', None)
        return obj


class AmqpQueueTypeEnum(Enum):
    QUORUM = 'quorum'
    CLASSIC = 'classic'

    @classmethod
    def valueForString(cls, stringValue):
        lowerStringValue = stringValue.lower() if stringValue is not None else None
        if lowerStringValue is None:
            return None
        elif lowerStringValue == 'quorum':
            return AmqpQueueTypeEnum.QUORUM
        elif lowerStringValue == 'classic':
            return AmqpQueueTypeEnum.CLASSIC
        else:
            return None

    @classmethod
    def valueAsString(cls, enumValue):
        if enumValue is None:
            return ''
        elif enumValue == AmqpQueueTypeEnum.QUORUM:
            return 'quorum'
        elif enumValue == AmqpQueueTypeEnum.CLASSIC:
            return 'classic'
        else:
            return ''



