#!/bin/bash


usage_func()
{
  echo "**********************************************************************"
  echo "*                                                                    *"
  echo "*  Usage:                                                            *"
  echo "*     Param1: -E,set exec Env info                                   *"
  echo "*     Param2: -t,set exec env tag                                    *"
  echo "*     Param3: -s,set exec service cases                              *"
  echo "*  Example:                                                          *"
  echo "*     sh start.sh -E online -t feature-1 -s xxx-api-service          *"
  echo "*  Note:                                                             *"
  echo "*     Available envs: online/test/pre_online                         *"
  echo "*     Available tags: prod/feature-1 ...                             *"
  echo "*     Available service: api-service1/api-service2 ...               *"
  echo "*                                                                    *"
  echo "**********************************************************************"

  exit 0
}

while getopts :E:t:s: OPTION
do
    case $OPTION in
    E)
      test_env=$OPTARG
      ;;
    t)
      test_env_tag=$OPTARG
      ;;
    s)
      test_service=$OPTARG
      ;;
    \?)
      usage_func
      ;;
    esac
done

if [ ! "${test_env}" ]; then
    usage_func
fi
if [ ! "${test_env_tag}" ]; then
    usage_func
fi
if [ ! "${test_service}" ]; then
    usage_func
fi

echo "Run test params: Env is '""${test_env}""', env tag is '""${test_env_tag}""', test service is '""${test_service}""'"
