#include<stdlib.h>
#include<string.h>
#ifdef _WIN32
    #include<io.h>
    #define sys_write _write
#elif defined(__linux__)||defined(__unix__)
    #include<unistd.h>
    #define sys_write write
#endif
typedef struct{
    size_t __n;
}n;
typedef struct{
    char *__buf;
    n *__n;
}printf;
static inline printf *print(printf *m,const long __fd){
    sys_write(__fd,m->__buf,m->__n->__n);
    return m;
}
int main(int argc, char **argv[]){
    printf *m = (printf*)malloc(sizeof(printf));
    m->__n = (n*)malloc(sizeof(n));
    m->__buf = "hello, world\n";
    m->__n->__n = strlen(m->__buf);
    const long __fd = 1;
    m = print(m,__fd);
    free(m->__n);
    free(m);
    return 0;
}