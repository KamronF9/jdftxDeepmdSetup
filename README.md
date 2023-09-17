# jdftxDeepmdSetup


## Environment setup:


    deepmd kit and deepmd lammps
    conda create -n deepmd deepmd-kit=*=*cpu libdeepmd=*=*cpu lammps -c https://conda.deepmodeling.com -c defaults


    for converting into deepmd from jdftx output:
    git clone https://github.com/KamronF9/dpdatajdftx
    python -m pip install -e .

    sudo apt-get install libgsl-dev
    sudo apt-get install libfftw3-dev libfftw3-doc
    sudo apt-get install libblas-dev liblapack-dev
    git clone https://github.com/shankar1729/jdftx.git jdftx-git
    [in build dir]cmake ../jdftx-git/jdftx
    make
    export PATH="/home/kamron/DFT/jdftx/build:/home/kamron/DFT/jdftx/jdftx-git/jdftx/scripts:$PATH"

    conda install -c conda-forge octave (for jdftx createxsf)

## To run 1 AIMD

    jdftx_gpu -i md.in -o md.out
    rename .out to .jdftxout
    move to train folder in 2DeePMD

## To run 2 DEEPMD

    setup env variable to Variable parser - see 1parseAIMD....sh
    bash parseAIMD...
    confirm new folders in train folder with content
    match input.json to folders in train
    bash/sbatch 2train.job
    dp freeze -o name.pb

## To run 3 NNMD

    lmp NNmd.in -v pot name.pb
