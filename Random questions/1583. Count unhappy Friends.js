/**
 * @param {number} n
 * @param {number[][]} preferences
 * @param {number[][]} pairs
 * @return {number}
 */
var unhappyFriends = function(n, preferences, pairs) {
    var count=0;

    for(i=0; i<pairs.length; i++){
        var prefI=pairs[i][0];
        var prefI1=pairs[i][1];
        if (preferences[prefI][0]!=pairs[i][1]){
            count++;
        }
        if(preferences[prefI1][0]!=pairs[i][0]){
            count++;
        }
    }
    return count;
};

//equal levels of depth