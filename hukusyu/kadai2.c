#include <stdio.h>
#include <string.h>

#define STR "TEST"

char str[2][50];

int main(){
  memset(str,'\0',sizeof(str));
  int i=0;
  char data[128];
  for(i=0;i<999;i++){
    memset(data,'\0',sizeof(data));
    strcpy(data,"abc");
    sprintf(str[i],"%s %s",data,STR);
    printf("%d,%s\n",i,str[i]);
  }
  return 0;
}
