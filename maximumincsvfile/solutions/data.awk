{
    numbers[i++]=$1;
    max=0;
}
END{
    for (i in numbers){
       if (numbers[i] > max) max=numbers[i];
   }
   print max;
}