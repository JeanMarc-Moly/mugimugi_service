#! /bin/sh

mamba env create\
 --file envs/base/environment.prod.yml\
 --prefix .python_env
