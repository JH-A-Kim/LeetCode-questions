/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 * Using Euclids algorithm makes this far easier to solve when i know Data structures and algorithms.
 */
var gcdOfStrings = function(str1, str2) {
    var shortString = str1;
    var longString = str2;
    var shortStringC;
    var isDiv = false;

    if (str1+str2!=str2+str1){
        return "";
    }
    if (shortString.length>str2.length){
        shortString=str2;
        longString=str1;
    }

    shortStringC=shortString;
    while(isDiv==false){
        var tempArray=longString.split(shortString);
        var tempArray1=shortStringC.split(shortString);
        var count=0;
        var count1=0;

        for(i=0; tempArray.length>i; i++){
            if (tempArray[i]==""){
                count++;
            }
            else {
                break;
            }
        }
        for(i=0; tempArray1.length>i; i++){
            if (tempArray1[i]==""){
                count1++;
            }
            else{
                break;
            }
        }
        if (count==tempArray.length && count1==tempArray1.length){
            return shortString;
        }
        else if(shortString.length==0){
            return "";
        }

        shortString=shortString.slice(0, -1);
    }
};