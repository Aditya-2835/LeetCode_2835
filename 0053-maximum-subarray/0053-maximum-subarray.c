int maxSubArray(int* nums, int numsSize) {
    int best=nums[0];
    int ans=nums[0];

    for(int i=1;i<numsSize;i++){
        int v1=best+nums[i];
        int v2=nums[i];
        best=fmax(v1,v2);
        ans=fmax(ans,best);
    }

    return ans;
}