import argparse


def generate_parser():
    argument_parser = argparse.ArgumentParser("CheckVis", 
                                              description="Creates graphical checklist")
    return argument_parser


if (__name__ == "__main__"):
    parser = generate_parser()
    parser.parse_args()
    print("Hello Checklists")
    exit(0)