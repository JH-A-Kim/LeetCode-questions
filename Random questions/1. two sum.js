/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (i=0; i<nums.length; i++){
        for (j=i+1; j<nums.length; j++){
            sum=nums[i]+nums[j];
            if (sum==target){
                return [i, j];
            }
        }
    }
};

array=[2, 5, 5, 11];

console.log(twoSum(array, 10));