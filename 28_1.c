#include<stdio.h>
#include<string.h>
int main()
{
    char p[100];
    int len,i,j,k;
    while(scanf("%s",p)!=EOF)
    {
        j=0;
        k=0;
        len=strlen(p);
        for(i=0;i<len;i++)
            if(p[i]=='.')
            {j++;
        k=i+1;
        break;
        }
        for(;k<len;k++)
            if(p[k]-'0'!=0)
            {
                j++;
                break;
            }
            if(j==2)
                printf("No\n");
            else printf("Yes\n");
    }
    return 0;
}