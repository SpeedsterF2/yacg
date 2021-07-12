import argparse
import sys
import os
import yaml
import logging
from yacg.util.fileUtils import doesFileExist
from yacg.util.outputUtils import printError, printInfo
import yacg.builder.impl.dictionaryBuilder as builder


description = """Reads a JSON schema model and converts it to a
yaml file
"""

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(prog='modelToYaml', description=description)
parser.add_argument('--model', help='model schema to convert to yaml')
parser.add_argument('--stdin', help='reads the model content from stdin', action='store_true')
parser.add_argument('--destDir', help='directory to write the yaml versions')
parser.add_argument('--dryRun', help='if set, then no output file is created', action='store_true')


def trimModelFileName(modelFile):
    lastSlash = modelFile.rfind('/')
    modelFileName = modelFile[lastSlash + 1:]
    lastDot = modelFileName.rfind('.')
    return modelFileName[:lastDot]


def _printYaml(parsedSchema, model, destDir):
    modelFileNameWithoutExt = trimModelFileName(model)
    modelFile = "{}/{}.yaml".format(destDir, modelFileNameWithoutExt)
    printInfo('\nWrite yaml: {}'.format(modelFile))
    with open(modelFile, 'w') as outfile:
        yaml.dump(parsedSchema, outfile, indent=4)


def convertModel(model, dryRun, destDir):
    parsedSchema = builder.getParsedSchemaFromJson(model)
    if dryRun:
        print(yaml.dump(parsedSchema))
    else:
        _printYaml(parsedSchema, model, destDir)


def readStdin():
    stdinInput = ''
    for line in sys.stdin:
        stdinInput = stdinInput + line
    return stdinInput


def main():
    args = parser.parse_args()
    if not args.stdin:
        if args.model is None:
            printError('\nModel file not given. It can be passed as parameter or over stdin ... cancel')
            sys.exit(1)
        if not doesFileExist(args.model):
            printError('\nModel file not found ... cancel: {}'.format(args.model))
            sys.exit(1)
        model = args.model
    else:
        model = readStdin()
    if (not args.dryRun) and ((args.destDir is None) or (not os.path.isdir(args.destDir))):
        printError('\nDest dir for yaml output not found ... cancel: {}'.format(args.destDir))
        sys.exit(1)
    convertModel(model, args.dryRun, args.destDir)



if __name__ == '__main__':
    main()
