#include<stdio.h>

int main()
{
    unsigned char buf[512];
    int *ptr;
    ptr=&ptr;
  //  *ptr=(0x0000000FF & *ptr )

    *ptr= 0x244;


    printf("%p\n",ptr);

    return 0;
}