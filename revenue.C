#include <stdio.h>

int main() {
    int N, K, R;
    scanf("%d %d %d", &N, &K, &R);

    int remaining = N - K;
    int revenue = remaining * R;

    printf("%d", revenue);

    return 0;
}
