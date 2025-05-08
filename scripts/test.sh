#!/bin/bash

# current directory
mtxdir=$(dirname "$0")/../mtx
# bin directory
bindir=$(dirname "$0")/../src
# log directory
logdir=$(dirname "$0")/../log

mtx=$mtxdir/sparse_matrix_2000x2000_s10.mtx
bin=$bindir/test

# test
$bin -d 0 -aat 0 $mtx