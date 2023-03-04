import argparse
import sys
import logging
from yacg.util.fileUtils import doesFileExist
from yacg.util.outputUtils import printError
from yacg.builder.jsonBuilder import getModelFromJson
from yacg.builder.yamlBuilder import getModelFromYaml
import yacg.model.randomFuncs as randomFuncs
import yacg.model.random_config as randomConfig
from yacg.util.fileUtils import getFileExt


description = """Reads a JSON schema model in JSON our YAML generates random data
for specific annotated types
"""

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(prog='createRandomData', description=description)
parser.add_argument('--model', help='with random generation information annotated model schema')
parser.add_argument('--outputDir', help='name of the directory to store the data with random data')
parser.add_argument('--type', help='type name to generate data for, alternative to specific annotation')
parser.add_argument('--defaultElemCount', help='default number of elements to generate for a type')
parser.add_argument('--defaultTypeDepth', help='default depth to generate complex types')
parser.add_argument('--defaultMinArrayElemCount', help='default minimal array element count')
parser.add_argument('--defaultMaxArrayElemCount', help='default maximal array element count')
parser.add_argument('--defaultMinDate', help='default minimal date for date and timestamp fields')
parser.add_argument('--defaultMaxDate', help='default maximal date for date and timestamp fields')


def __createDefaultConfig(args):
    defaultConfig = randomConfig.RamdonDefaultConfig()
    defaultConfig.defaultElemCount = args.defaultElemCount
    defaultConfig.defaultTypeDepth = args.defaultTypeDepth
    defaultConfig.defaultMinArrayElemCount = args.defaultMinArrayElemCount
    defaultConfig.defaultMaxArrayElemCount = args.defaultMaxArrayElemCount
    defaultConfig.defaultMinDate = args.defaultMinDate
    defaultConfig.defaultMaxDate = args.defaultMaxDate
    return defaultConfig


def _searchForTypesToGenerateAndProcessThem(args, loadedTypes):
    """takes the prepared meta model ..."""
    defaultConfig = __createDefaultConfig(args)
    for t in loadedTypes:
        if t.processing is None and t.procession.randElemCount > 0:
            randomData = randomFuncs.generateRandomData(t, defaultConfig)
            # TODO write generated datak
            pass
    pass


def main():
    args = parser.parse_args()
    if args.model is None:
        printError('\nModel file not given. It can be passed as parameter or over stdin ... cancel')
        sys.exit(1)
    if not doesFileExist(args.model):
        printError('\nModel file not found ... cancel: {}'.format(args.model))
        sys.exit(1)
    yamlExtensions = set(['.yaml', '.yml'])
    fileExt = getFileExt(args.model)
    loadedTypes = []
    if fileExt.lower() in yamlExtensions:
        loadedTypes = getModelFromYaml(args.model, loadedTypes)
    else:
        loadedTypes = getModelFromJson(args.model, loadedTypes)
    randomFuncs.extendMetaModelWithRandomConfigTypes(loadedTypes)
    _searchForTypesToGenerateAndProcessThem(args, loadedTypes)


if __name__ == '__main__':
    main()
