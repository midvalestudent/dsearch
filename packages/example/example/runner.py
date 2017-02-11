''' example runner function
'''
from example import settings
from example import logger


# example run cmd
def run(args):
    logger.info("running with setting: {}".format(settings.NAME))
    logger.info("input file: {}".format(args.infile))
    logger.info("output file: {}".format(args.outfile))

    for k, line in enumerate(args.infile.readlines()):
        args.outfile.write("Read line number {} as: {}".format(k, line))

    return 0


