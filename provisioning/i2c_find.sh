#! /bin/bash
i2cdetect -y 1 | awk  '{if (NR > 1) 
                           {for(i=2 ;i<=NF;i++)
                               {if($i != "--")
                                  print  $i
                               }
                           }
                       }