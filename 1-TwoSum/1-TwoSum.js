// Last updated: 8/2/2025, 4:54:24 PM
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++){
        const comp = target - nums[i];
        if(i == nums.length - 1) {
            break
        }
        for (let j = i+1; j < nums.length; j++){
            if(nums[j] == comp){
                return[i, j];
            }          
        }
    }
    return -1;
};