# Attention, this file is generated. Manual changes get lost with the next
# run of the code generation.
# created by yacg (template: pythonBeans.mako v1.0.0)

from enum import Enum


class OperationBase:
    def __init__(self):

        self.operationId = None

        self.summary = None

        self.description = None

        self.parameters = []

        self.message = None

        self.amqpBinding = None

        self.amqpSubscriberImplementation = None

        self.responseType = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.operationId = dict.get('operationId', None)

        obj.summary = dict.get('summary', None)

        obj.description = dict.get('description', None)

        arrayParameters = dict.get('parameters', [])
        for elemParameters in arrayParameters:
            obj.parameters.append(
                Parameter.dictToObject(elemParameters))

        obj.message = Message.dictToObject(dict.get('message', None))

        obj.amqpBinding = AmqpBinding.dictToObject(dict.get('amqpBinding', None))

        obj.amqpSubscriberImplementation = AmqpSubscriberImplementation.dictToObject(dict.get('amqpSubscriberImplementation', None))

        obj.responseType = XResponseType.dictToObject(dict.get('responseType', None))
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


class Message:
    """ Container that describes the messages are sent
    """

    def __init__(self):

        #: Container that describes the messages are sent
        self.xParameters = []

        #: Container that describes the messages are sent
        self.payload = None

        #: Container that describes the messages are sent
        self.xToken = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        arrayXParameters = dict.get('xParameters', [])
        for elemXParameters in arrayXParameters:
            obj.xParameters.append(
                XParameter.dictToObject(elemXParameters))

        obj.payload = yacg.model.model.Type.dictToObject(dict.get('payload', None))

        obj.xToken = XTokenContent.dictToObject(dict.get('xToken', None))
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

        obj.replyTo = dict.get('replyTo', amq.rabbitmq.reply-to)
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


class AsyncApiDefinition:
    """ subset of attribs, https://www.asyncapi.com/docs/specifications/v2.0.0#A2SObject
    """

    def __init__(self):

        #: subset of attribs, https://www.asyncapi.com/docs/specifications/v2.0.0#A2SObject
        self.info = None

        #: subset of attribs, https://www.asyncapi.com/docs/specifications/v2.0.0#A2SObject
        self.servers = []

        #: subset of attribs, https://www.asyncapi.com/docs/specifications/v2.0.0#A2SObject
        self.channels = []

        #: subset of attribs, https://www.asyncapi.com/docs/specifications/v2.0.0#A2SObject
        self.components = []

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.info = Info.dictToObject(dict.get('info', None))

        arrayServers = dict.get('servers', [])
        for elemServers in arrayServers:
            obj.servers.append(
                Server.dictToObject(elemServers))

        arrayChannels = dict.get('channels', [])
        for elemChannels in arrayChannels:
            obj.channels.append(
                Channel.dictToObject(elemChannels))

        arrayComponents = dict.get('components', [])
        for elemComponents in arrayComponents:
            obj.components.append(
                Server.dictToObject(elemComponents))
        return obj


class Info:
    """ Subset of the info object attribs: https://www.asyncapi.com/docs/specifications/v2.0.0#infoObject
    """

    def __init__(self):

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


class Server:
    """ one entry of the servers section
    """

    def __init__(self):

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


class Channel:
    """ one entry of the channels section
    """

    def __init__(self):

        #: one entry of the channels section
        self.key = None

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

        obj.publish = PublishDescription.dictToObject(dict.get('publish', None))

        obj.subscribe = SubscribeDescription.dictToObject(dict.get('subscribe', None))
        return obj


class PublishDescription (OperationBase):
    """ Configuration parameter needed for publishing
    """

    def __init__(self):
        super(OperationBase, self).__init__()

        #: Configuration parameter needed for publishing
        self.responseType = None

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.responseType = yacg.model.model.Type.dictToObject(dict.get('responseType', None))
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

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.name = dict.get('name', None)

        obj.description = dict.get('description', None)

        obj.type = yacg.model.model.Type.dictToObject(dict.get('type', None))
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

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        obj = cls()

        obj.name = dict.get('name', None)

        obj.description = dict.get('description', None)

        obj.type = yacg.model.model.Type.dictToObject(dict.get('type', None))
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



