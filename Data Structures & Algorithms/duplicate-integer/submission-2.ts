class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const arr = [];
        for(let i = 0; i < nums.length; i++) {
            const filtered = nums.filter(n => n === nums[i]);
            if(filtered.length > 1) {
                arr.push(filtered);
            }
        }

        return arr.length > 0;
    }
}
