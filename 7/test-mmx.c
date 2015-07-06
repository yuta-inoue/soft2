#include <stdio.h>

int main(int argc,char *argv[]){
  short a[4] = {1,2,3,4};
  short b[4] = {-4,-3,-2,-1};
  int c[2];
  int i;

#if 0
  asm ( assembler template
      : output operands
      : input operands
      : list of clobbered registers
    );
#endif
  asm volatile ("movq %0,%%mm0": :"m"(a[0]));
  asm volatile ("movq %0,%%mm1": :"m"(b[0]));
  asm volatile ("pmaddwd %%mm1,%%mm0"::);
  asm volatile ("movq %%mm0,%0":"=m"(c[0]));
  asm volatile ("emms");

  for(i=0;i<4;i++)printf(" %3d",a[i]);printf("\n");
  for(i=0;i<4;i++)printf(" %3d",b[i]);printf("\n");
  for(i=0;i<2;i++)printf(" %3d",c[i]);printf("\n");
  return 0;
}
