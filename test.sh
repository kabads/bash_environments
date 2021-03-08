#!/bin/bash

home_dir=$1

source ${home_dir}/envs.sh
echo ${home_dir}
echo ${git_username}
echo ${git_pass}
echo ${MetaToExclude[@]}
echo ${MetaNamesToExclude[@]}
echo ${TargetBranch}
echo ${SourceBranch}
echo ${ValidateOnly}
echo ${pr_number}
echo ${conf_account}
echo ${PackageVersion}
echo ${conf_pat}
echo ${conf_url}
echo ${conf_page_id}
echo ${conf_page_title}
echo ${deploy_all}