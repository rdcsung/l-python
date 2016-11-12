import argparse


def main (args):
    print ('start main')

    print (args)
    print (args.data_dir)

    answer = args.x**args.y
    if args.quiet:
        print (answer)
    elif args.verbose:
        print ("{} to the power {} equals {}".format(args.x, args.y, answer))
    else:
        print ("{}^{} == {}".format(args.x, args.y, answer))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="calculate X to the power of Y")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true",
        help="increase output verbosity")
    group.add_argument("-q", "--quiet", action="store_true",
        help="simple output")
    group.add_argument("--data_dir", type=str, default='/tmp/data',
        help='Directory for storing data')
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()
    #print (args)
    print (argv)
    main (args)
