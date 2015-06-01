/* fact.c */
#include<stdio.h>
#include<stdlib.h>

#define FALSE 0
#define TRUE 1

int Debug = FALSE;

int fact(int x){
  // xが0より大きい場合はx-1を引数にして再帰呼び出し
  if (x >0 ){
    if(Debug){
      printf("x = %d\n",x);
    }
    return (x * fact(x-1));
    
  // xが0以下の時は1を返す（ここに到達するまでの時間はO(n)）
  } else {
    if(Debug){
      printf("x = %d, return 1\n",x);
    }
    return 1;
  }
}

int main(int argc, char *argv[]){
  int x,ret;
  while((argc > 1) && (argv[1][0] == '-')){
    switch(argv[1][1]){
      case 'd' : Debug=TRUE;break;
      default : break;
    }
    argc--;argv++;
  }
  x = atoi(argv[1]);
  ret = fact(x);
  printf("ret = %d\n",ret);
  return 0;
}
