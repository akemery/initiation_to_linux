{
    numbers[i++]=$1;
    min=36335;
}
END{
    for (i in numbers){
       if (numbers[i] < min) min=numbers[i];
   }
   print min;
}