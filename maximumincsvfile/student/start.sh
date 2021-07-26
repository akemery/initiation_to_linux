#!/bin/bash
for i in {1..1000}
do
   number=$RANDOM
   echo $number >> $1
done