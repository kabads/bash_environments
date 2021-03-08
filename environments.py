#!/usr/bin/env python3 
import argparse

#############################################################
# This file accepts a variety of variables on               #
# the command line and then passes them to a                #
# file envs.sh.                                             #
#                                                           # 
# The format for passing is $environments.py                #
# --gitusername $(git_username)                             #  
# --gitpass $(git_pass)                                     #
# --homedir $(System.DefaultWorkingDirectory)               #
# --targetbranch $(TargetBranch)                            #
# --sourcebranch $(SourceBranch)                            # 
# --includedestructivechanges $(IncludeDestructiveChanges)  #
# --validateonly $(ValidateOnly)                            # 
# --metatoexclude $(meta_to_exclude)                        #
# --metanamestoexclude $(names_to_exclude)                  # 
# --automerge $(auto_merge)                                 #
# --bitbucketprsource $(bitbucket_pr_source)                #
# --bitbucketprtarget $(bitbucket_pr_target)                #
# --bitbucketprnumber $(bitbucket_pr_number)                #
# --packageversion $(PackageVersion)                        #
# --confaccount $(atlassian_account)                        #
# --confpat $(atlassian_pat)                                #
# --confurl $(conf_url)                                     #
# --confpageid $(conf_qa_page_id)                           #
# --confpagetitle $(conf_qa_page_title)                     #
# --deployall $(deploy_all)                                 #
# (these should be on the same line in devops azure.        #
#                                                           #
# After this - all your bash script needs to                #
# do is                                                     #
# source $(System.DefaultWorkingDirectory/envs.sh           #
#############################################################

# Place this in your pipeline (changing any local variable names accordingly: 
# $(System.DefaultWorkingDirectory)/build_scripts/environments.py --gitusername $(git_username) --gitpass $(git_pass) --homedir $(System.DefaultWorkingDirectory) --bitbucketprtarget $(bitbucket_pr_target) --bitbucketprsource $(bitbucket_pr_source) --includedestructivechanges $(IncludeDestructiveChanges) --validateonly $(ValidateOnly) --metatoexclude "$(meta_to_exclude)" --metanamestoexclude "$(names_to_exclude)" --automerge false --bitbucketprnumber $(bitbucket_pr_number) --packageversion $(PackageVersion) --confaccount $(atlassian_account) --confpat $(atlassian_pat) --confurl $(conf_url) --confpageid $(conf_qa_page_id) --confpagetitle $(conf_qa_page_title) --deployall false


BASH_FILE = 'envs.sh'


def open_file(filename, method):
    """Open a file for writing"""
    return open(filename, method)


def close_file(file):
    """Close the file after it is finished with"""
    file.close()


def write_bash_envs(args):
    """We will open the file and append the env vars to it."""
    file = BASH_FILE
    # print(file)
    f = open_file(file, 'w')
    print("Writing environment variables.....")
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
    f.write('IncludeDestructiveChanges="' + args.includedestructivechanges + '"\n')
    f.write('ValidateOnly="' + args.validateonly + '"\n')
    f.write('TargetBranch="' + args.bitbucketprtarget + '"\n')
    f.write('SourceBranch="' + args.bitbucketprsource + '"\n')
    f.write('auto_merge="' + args.automerge + '"\n')
    f.write('pr_number="' + str(args.bitbucketprnumber) + '"\n')
    f.write('PackageVersion="' + str(args.packageversion) + '"\n')
    f.write('conf_account="' + str(args.confaccount) + '"\n')
    f.write('conf_pat="' + str(args.confpat) + '"\n')
    f.write('conf_url="' + str(args.confurl) + '"\n')
    f.write('conf_page_id="' + str(args.confpageid) + '"\n')
    f.write('conf_page_title="' + ' '.join(args.confpagetitle) + '"\n')
    f.write('deploy_all="' + args.deployall + '"\n')
    close_file(f)


def main():
    """This function sets up the parser arguments
    then sends them to the write_bash_envs function."""
    parser = argparse.ArgumentParser(
        description='Manage environment variables')
    parser.add_argument("--gitusername")
    parser.add_argument("--gitpass")
    parser.add_argument("--homedir")
    parser.add_argument("--includedestructivechanges")
    parser.add_argument("--validateonly")
    parser.add_argument("--metatoexclude", nargs='+')
    parser.add_argument("--metanamestoexclude", nargs='+')
    parser.add_argument("--automerge")
    parser.add_argument("--bitbucketprnumber")
    parser.add_argument("--bitbucketprsource")
    parser.add_argument("--bitbucketprtarget")
    parser.add_argument("--packageversion")
    parser.add_argument("--confaccount")
    parser.add_argument("--confpat")
    parser.add_argument("--confurl")
    parser.add_argument("--confpageid")
    parser.add_argument("--confpagetitle", nargs='+')
    parser.add_argument("--deployall")

    args = parser.parse_args()

    write_bash_envs(args)


if __name__ == '__main__':
    main()
