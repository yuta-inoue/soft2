#include <stdio.h>
#include <immintrin.h>

int main(){
  float a[4] = {1.0,1.0,2.0,3.0};
  float b[4] = {8.0,13.0,21.0,34.0};
  __m128 u = {0};
  int i;
  for(i=0;i<1;i++){
    __m128 w = _mm_load_ps(&a[i]);
    __m128 x = _mm_load_ps(&b[i]);
    x = _mm_mul_ps(w,x);
    u = _mm_add_ps(u,x);
  }
  __attribute__((aligned(16))) float t[4] = {0};
  _mm_store_ps(t,u);

  printf("%f %f %f %f\n",t[0],t[1],t[2],t[3]);
  return 0;
}
