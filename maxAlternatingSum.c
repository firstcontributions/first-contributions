#include <stdlib.h>
#include <math.h>

int cmp(const void* a, const void* b) {
    long long x = llabs(*(int*)a), y = llabs(*(int*)b);
    return (x < y) ? 1 : (x > y ? -1 : 0);
}

long long maxAlternatingSum(int* numb, int map) {
    qsort(numb, map, sizeof(int), cmp);
    int k = (map + 1) / 2;
    long long q = 0;
    for (int i = 0; i < map; i++) {
        long long s = (long long)numb[i] * numb[i];
        q += (i < k) ? s : -s;
    }
    return q;
}
