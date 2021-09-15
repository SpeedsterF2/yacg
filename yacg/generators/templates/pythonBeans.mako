## Template to create a Python file with type beans of the model types
<%
    import yacg.templateHelper as templateHelper
    import yacg.model.modelFuncs as modelFuncs
    import yacg.model.model as model
    import yacg.util.stringUtils as stringUtils
    import yacg.generators.helper.pythonFuncs as pythonFuncs

    templateFile = 'pythonBeans.mako'
    templateVersion = '1.0.0'

    baseModelDomain = templateParameters.get('baseModelDomain',None)
    domainList = modelFuncs.getDomainsAsList(modelTypes)

    def printDefaultValue(property):
        if hasattr(property.type,'default'):
            ret = property.type.default
            if ret is None:
                return None
            elif isinstance(property.type, model.StringType):
                return '"{}"'.format(ret)
            elif isinstance(property.type, model.UuidType):
                return '"{}"'.format(ret)
            else:
                return ret
        else:
            return 'None'

%># Attention, this file is generated. Manual changes get lost with the next
# run of the code generation.
# created by yacg (template: ${templateFile} v${templateVersion})

% if modelFuncs.hasEnumTypes(modelTypes):
from enum import Enum
% endif
% for domain in domainList:
    % if baseModelDomain != domain:
import ${domain}
    % endif
% endfor


% for type in modelTypes:
    % if modelFuncs.isEnumType(type):    
class ${type.name}(Enum):
        % for value in type.values:
    ${stringUtils.toUpperCaseName(value)} = '${value}'
        % endfor

    @classmethod
    def valueForString(cls, stringValue):
        lowerStringValue = stringValue.lower() if stringValue is not None else None
        if lowerStringValue is None:
            return None
        % for value in type.values:
        elif lowerStringValue == '${value.lower()}':
            return ${type.name}.${stringUtils.toUpperCaseName(value)}
        % endfor
        else:
            return None

    @classmethod
    def valueAsString(cls, enumValue):
        if enumValue is None:
            return ''
        % for value in type.values:
        elif enumValue == ${type.name}.${stringUtils.toUpperCaseName(value)}:
            return '${value}'
        % endfor
        else:
            return ''


    % else:
class ${type.name}${ ' ({})'.format(pythonFuncs.getExtendsType(type, modelTypes, baseModelDomain)) if type.extendsType is not None else ''}:
        % if type.description != None:
    """${templateHelper.addLineBreakToDescription(type.description,4)}
    """

        % endif
    def __init__(self):
        % if type.extendsType is not None:
        super(${type.name}, self).__init__()
        % endif
        % if len(type.properties) == 0:
        pass
        % else:
            % for property in type.properties:

                % if type.description != None:
        #: ${type.description}
                % endif
        self.${property.name} = ${pythonFuncs.getDefaultPythonValue(property)}
            % endfor
        % endif

    @classmethod
    def dictToObject(cls, dict):
        if dict is None:
            return None
        % if type.extendsType is not None:
        obj = ${type.extendsType.name}.dictToObject(dict)
        % else:
        obj = cls()
        % endif
        % for property in type.properties:
            % if modelFuncs.isBaseType(property.type):
                % if not property.isArray:

        obj.${property.name} = dict.get('${property.name}', ${printDefaultValue(property)})
                % else:

        array${stringUtils.toUpperCamelCase(property.name)} = dict.get('${property.name}', [])
        for elem${stringUtils.toUpperCamelCase(property.name)} in array${stringUtils.toUpperCamelCase(property.name)}:
            obj.${property.name}.append(elem${stringUtils.toUpperCamelCase(property.name)})
                % endif
            % elif modelFuncs.isEnumType(property.type):
                % if not property.isArray:

        obj.${property.name} = ${property.type.name}.valueForString(dict.get('${property.name}', None))
                % else:

        array${stringUtils.toUpperCamelCase(property.name)} = dict.get('${property.name}', [])
        for elem${stringUtils.toUpperCamelCase(property.name)} in array${stringUtils.toUpperCamelCase(property.name)}:
            obj.${property.name}.append(
                ${property.type.name}.valueForString(elem${stringUtils.toUpperCamelCase(property.name)}))
                % endif
            % else:
                % if not property.isArray:

        obj.${property.name} = ${pythonFuncs.getTypeWithPackage(property.type, modelTypes, baseModelDomain)}.dictToObject(dict.get('${property.name}', ${printDefaultValue(property)}))
                % else:

        array${stringUtils.toUpperCamelCase(property.name)} = dict.get('${property.name}', [])
        for elem${stringUtils.toUpperCamelCase(property.name)} in array${stringUtils.toUpperCamelCase(property.name)}:
            obj.${property.name}.append(
                ${pythonFuncs.getTypeWithPackage(property.type, modelTypes, baseModelDomain)}.dictToObject(elem${stringUtils.toUpperCamelCase(property.name)}))
                % endif
            % endif
        % endfor
        return obj

    % endif

% endfor