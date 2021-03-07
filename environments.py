import argparse

ENVIRONMENT_FILE = 'envs.json'
BASH_FILE = 'envs.sh'


def open_file(filename, method):
    """Open a file for writing"""
    return open(filename, method)


def close_file(file):
    """Close the file after it is finished with"""
    file.close()


def write_bash_envs(args):
    """We will open the file and append the env vars to it."""
    file = args.homedir + BASH_FILE
    print(file)
    f = open_file(file, 'w')
    print("Writing")
    f.write('git_username="' + args.gitusername + '"\n')
    f.write('home_dir="' + args.homedir + '"\n')
    f.write('git_pass="' + args.gitpass + '"\n')
    f.write('MetaToExclude=(')
    for meta in args.metatoexclude:
        f.write('"' + meta + '" ')
    f.write(')\n')
    f.write('MetaNamesToExclude=(')
    for metaname in args.metanamestoexclude:
        f.write('"'+ metaname + '" ')
    f.write(')\n')
    close_file(f)


def main():
    """This function takes a json file and passes it to a json reader"""
    parser = argparse.ArgumentParser(
        description='Manage environment variables')
    parser.add_argument("--gitusername")
    parser.add_argument("--gitpass")
    parser.add_argument("--homedir")
    parser.add_argument("--targetbranch")
    parser.add_argument("--sourcebranch")
    parser.add_argument("--includeestructivechanges")
    parser.add_argument("--validateonly")
    parser.add_argument("--metatoexclude", nargs='+')
    parser.add_argument("--metanamestoexclude", nargs='+')
    args = parser.parse_args()

    write_bash_envs(args)


if __name__ == '__main__':
    main()