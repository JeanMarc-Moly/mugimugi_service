#!/bin/sh

mamba env create\
 --file envs/base/environment.prod.yml\
 --prefix .python_env

mamba env update\
 --file envs/base/environment.dev.yml\
 --prefix .python_env
