#include<stdlib.h>
#include<math.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int threeSumClosest(int* nums, int numsSize, int target) {
    qsort(nums,numsSize,sizeof(int),compare);
    int clo_sum=nums[0]+nums[1]+nums[2];

    for(int i=0;i<numsSize-2;i++){
        int j=i+1;
        int k=numsSize-1;

        while(j<k){
            int total=nums[i]+nums[j]+nums[k];

            if (total==target)
                return total;
            
            if (abs(total-target)<abs(clo_sum-target))
                clo_sum=total;
            if (total<target)
                j++;
            else
                k--;
        }
    }
    return clo_sum;
}