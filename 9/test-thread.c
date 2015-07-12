#include <stdio.h>
#include <pthread.h>

int shared_resource = 0;
pthread_mutex_t mutex;

void *task2(void *arg){
  int i,j,tmp,loop;
  loop = (int)arg;
  for(i=0;i<loop;i++){
    pthread_mutex_lock(&mutex);
    for(j=0;j<10000;j++){
      tmp = shared_resource;
      tmp = tmp + 1;
      usleep(1);
      shared_resource = tmp;
    }
    pthread_mutex_unlock(&mutex);
    printf("Thread [%d]: count = %d / shared_resource = %d\n",loop,i,shared_resource);
  }
  arg = (void *)(shared_resource);
  pthread_exit((void *)arg);
}

void *task(void *arg){
  int i,j,tmp,loop;
  // pthread_mutex_lock(&mutex);
  loop = (int)arg;
  j = 0;
  for(i=0;i<loop;i++){
    j++;
    usleep(100000);
    printf("Thread [%d] : count = %d / j = %d\n",loop,i,j);
  }
  shared_resource = shared_resource + j;
  arg = (void *)(shared_resource);
  // pthread_mutex_unlock(&mutex);
}

int main(){
  pthread_t thread1,thread2;
  int loop1 = 10,loop2 = 20;
  pthread_mutex_init(&mutex,NULL);
  pthread_create(&thread1,NULL,task2,(void*)loop1);
  pthread_create(&thread2,NULL,task2,(void*)loop2);

  int ret1,ret2;
  pthread_join(thread1,(void **)&ret1);
  printf("Thread %x finished, return %d.\n",(int)thread1,ret1);
  pthread_join(thread2,(void **)&ret2);
  printf("Thread %x finished,return %d.\n",(int)thread2,ret2);
  return 0;
}
