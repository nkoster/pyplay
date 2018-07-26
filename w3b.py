# function numToAlpha($num){
#     $return = "";
#     $alpha = "dn6ksvwg8aqht5jmzl7crxe4y9ip2b3o10uf";
# //   $alpha = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
#     $n = floor($num/strlen($alpha));
#     if($n > 0)
#         $return .= numToAlpha($n);
#     $return .= $alpha[$num % strlen($alpha)];
#     return $return;
# }
#
# function alphaToNum($s){
#     $alpha = "dn6ksvwg8aqht5jmzl7crxe4y9ip2b3o10uf";
#     $return = 0;
#     $i = strlen($s);
#     $s = strrev($s);
#     while(isset($s[--$i])){
#         $return += strpos($alpha, $s[$i]) * pow(strlen($alpha), $i);
#     }
#     return $return;
# }

import math

alpha = "dn6ksvwg8aqht5jmzl7crxe4y9ip2b3o10uf"

def numToAlpha(num):
    r = ""
    n = int(math.floor(num / len(alpha)))
    if n > 0:
        r += numToAlpha(n)
    r += alpha[num % len(alpha)]
    return r

def alphaToNum(s):
    r = 0
    i = len(s)
    s = s[::-1]
    while i >= 0:
        i -= 1
        r += alpha.find(s[i]) * pow(len(alpha), i)
    return int(r)

print '103454 = ', numToAlpha(103454)

print '6gbi =', alphaToNum('6gbi')
