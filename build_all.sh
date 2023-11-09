#! /bin/bash

ROOT=$(pwd)

rm -rf out
mkdir out

document_list=(
    SG200X/TRM/en
    SG200X/TRM/zh
)

build(){
    make -C $1 clean
    
    make -C $1 html
    make -C $1 pdf
    
    mkdir -p out/$1
    mv $1/build/html ${ROOT}/out/$1
    mv $1/build/*.pdf ${ROOT}/out/$1

    make -C $1 clean
}

for dir_name in ${document_list[*]}
do
    build $dir_name
done
