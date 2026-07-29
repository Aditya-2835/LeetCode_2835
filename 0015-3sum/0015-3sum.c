/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    qsort(nums, numsSize, sizeof(int), compare);

    int capacity = 100;
    int count = 0;
    int** res = (int**)malloc(sizeof(int*) * capacity);
    *returnColumnSizes = (int*)malloc(sizeof(int) * capacity);

    for (int i = 0; i < numsSize; i++) {
        if (i > 0 && nums[i] == nums[i - 1])
            continue;
        if (nums[i] > 0)
            break;

        int j = i + 1;
        int k = numsSize - 1;

        while (j < k) {
            int total = nums[i] + nums[j] + nums[k];

            if (total == 0) {
                if (count >= capacity) {
                    capacity *= 2;
                    res = (int**)realloc(res, sizeof(int*) * capacity);
                    *returnColumnSizes = (int*)realloc(*returnColumnSizes, sizeof(int) * capacity);
                }

                // Store triplet
                res[count] = (int*)malloc(sizeof(int) * 3);
                res[count][0] = nums[i];
                res[count][1] = nums[j];
                res[count][2] = nums[k];
                (*returnColumnSizes)[count] = 3;
                count++;

                j++;
                k--;

                while (j < k && nums[j] == nums[j - 1])
                    j++;
                while (j < k && nums[k] == nums[k + 1])
                    k--;
            } 
            else if (total < 0) {
                j++;
            } 
            else {
                k--;
            }
        }
    }

    *returnSize = count;
    return res;
}