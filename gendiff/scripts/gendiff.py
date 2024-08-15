from gendiff.cli import pars_arg
from gendiff import generate_diff


def main():
    args = pars_arg()
    diff = generate_diff(args.first_file, args.second_file, args.form)
    print(diff)


if __name__ == '__main__':
    main()
