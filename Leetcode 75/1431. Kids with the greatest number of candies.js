/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    var result=[];
    var max=Math.max(...candies);

    for(i=0; i<candies.length; i++){
        var added=candies[i]+extraCandies;
        if(added>=max){
            result.push(true);
        }
        else {
            result.push(false);
        }
    }
    return result;
};