/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    var result=[];

    for(i=0; i<candies.length; i++){
        var added=candies[i]+extraCandies;
        var max=Math.max(...candies);
        if(added>=max){
            result.push(true);
        }
        else {
            result.push(false);
        }
    }
    return result;
};