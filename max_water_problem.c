#include <stdio.h>


 
int returnArray(int arr[], int size){
    int left = 0;
    int right = size - 1;
    int result = 0;
    while (left != right){
        if (arr[left] < arr[right]){
            if (result < arr[left] * (right - left)){
                result = arr[left] * (right - left);
                
            }
            ++left;
        }
        else{
                if (result < arr[right] * (right - left)){
                    result = arr[right] * (right - left);
                    
                }
                --right;
            } 
            
        
    }
    return result;
}

int main(){
    printf("Hello World \n");
    int test[100] = {1, 8, 6, 2, 5, 4,8, 3, 7};
    int len = sizeof(test) / sizeof(test[0]);
    printf("%d", returnArray(test, len));
    return 0;


}