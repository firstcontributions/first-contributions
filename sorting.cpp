#include <iostream>

using namespace std;

void sort(int A[], int n){
    for (int i = 0; i<n; i++){
        for (int j = 0; j < n; j++){
            int temp = A[i];
            if (A[j] > A[i]){
                temp = A[j];
                A[j] = A[i];
                A[i] = temp;
            }
        }
    }

    cout << "Araay Sorted!" << endl;

    for (int i =0; i<n; i++){
        cout << A[i] << " ";
    }
}

int main(){
    int A[] = {3,6,8,5,2,1,9,4};
    sort(A, 8);
}