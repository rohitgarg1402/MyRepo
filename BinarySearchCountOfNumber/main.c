//
//  main.c
//  BinarySearchCountOfNumber
//
//  Created by Rohit Garg on 10/24/16.
//  Copyright © 2016 Rohit Garg. All rights reserved.
//

#include <stdio.h>

int countarr(int *a,int len, int x);
int lowest(int *a, int len, int x);
int highest(int *a, int len, int x);

int countarr(int *a,int len, int x)
{
    int index1, index2,val;
    index1 = lowest(a,len,x);
    index2 = highest(a,len,x);
    val = (index2-index1) + 1;
    return val;
}
int lowest(int *a, int len, int x)
{
    int low,high,mid,index = -1;
    low = 0;
    high = len-1;
    while(low<=high)
    {
        mid = (low+high)/2;
        if(a[mid] == x)
        {
            index = mid;
            high = mid-1;
        }
        else if(a[mid] > x)
        {
            high = mid-1;
        }
        else
        {
            low = mid + 1;
        }
    }
    return index;
}
int highest(int *a, int len, int x)
{
    int low,high,mid,index = -1;
    low = 0;
    high = len-1;
    while(low<=high)
    {
        mid = (low+high)/2;
        if(a[mid] == x)
        {
            index = mid;
            low = mid + 1;
        }
        else if(a[mid] > x)
        {
            high = mid-1;
        }
        else
        {
            low = mid + 1;
        }
    }
    return index;
}

int main()
{
    int a[] = {1,2,2,3,3,4,4,4,4,5,5,5,5,5,5,5,5,6,6,6,6};
    int len,ret;
    len = sizeof(a)/sizeof(a[0]);
    ret = countarr(a,len,5);
    printf("%d ",ret);
}
