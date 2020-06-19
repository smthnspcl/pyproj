from argparse import ArgumentParser
from pyproj import Project


def main():
    ap = ArgumentParser()
    ap.add_argument("-n", "--new", type=str, help="project name", required=True)
    ap.add_argument("--no-mit", action="store_true", help="don't create a license file")
    ap.add_argument("-a", "--author", type=str, help="author name", required=True)
    a = ap.parse_args()

    Project.new(a.new, not a.no_mit, a.author)


if __name__ == '__main__':
    main()
