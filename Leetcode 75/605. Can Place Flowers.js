/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    count=0;
    for(i=0; i<flowerbed.length; i++){
        if (flowerbed[i]==0 && flowerbed[i+1]!=1 && i==0){
            flowerbed[i]=1;
            count++;
        }
        else if(i==flowerbed.length-1 && flowerbed[i]==0 && flowerbed[i-1]!=1){
            flowerbed[i]=1;
            count++;
        }
        else if (flowerbed[i]==0 && flowerbed[i+1]==0 && flowerbed[i-1]==0){
            flowerbed[i]=1;
            count++;
        }
    }
    if (count>=n){
        console.log(count);
        return true;
    }
    else{
        console.log(count);
        return false;
    }
};