#include <iostream>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <time.h> 

using namespace std;
int countJ=0;
int countR=0;
int Jessie(int nums[], int first, int last, int target) {
	countJ++;
	if (first == last) 
		return nums[first] == target ? first : -1;
	
	int mid = (first + last) / 2;
	if (target <= nums[mid]) 
		return Jessie(nums, first, mid, target);
	else
		return Jessie(nums, mid+1, last, target);
}

int Riley(int nums[], int first, int last, int target) {
	countR++;
	if (first >= last) 
		return (first > last || nums[first] != target) ? -1 : first;
	
	int mid = (first + last) / 2;
	if (target == nums[mid])  
		return mid;
	if (target < nums[mid]) 
		return Riley(nums, first, mid-1, target);
	return Riley(nums, mid+1, last, target);
}

int random2(int k) {
    if (k > 31)  k = 31;
    int result = 0;
    int bit;
    while (k-- > 0) {
        int r = rand() % 17;
        result = (result << 1) + (r == 0 ? rand() % 2 : r > 8 ? 1 : 0);
    }   
    return result;
}


int main()
{
	int con = 5;

	for(int i=pow(2,con);con<24;con++,i++){
		srand(unsigned int(time(0)));
		countJ = 0;
		countR = 0;
		int Jc=0;
		int  Rc=0;
		int *v = new int[i];
	for(int j=0;j<i;j++){
		v[j]=(rand()%(i));
	}
	sort(v,v+i);
   for(int k=0;k<1000;k++){
   	int tar= rand()%(i);
   //int j = Jessie(v,0,i-1,tar);
   int r = Riley(v,0,i-1,tar);
   Jc += countJ;
   
   Rc += countR;
  //cout<<"R"<<countR<<endl;
   }
   //cout<<Jc<<endl;
   cout<<Rc/1000<<endl;
   
   delete v;
	}
	
	/*int v[100];
	int Jc = 0;
	int Rc = 0;
	for(int i=0;i<100;i++){
		v[i] = i;
	}
	int j = Jessie(v,0,100,1);
	int r = Riley(v,0,100,1);
	Jc = countJ;
	Rc = countR;
	cout<<Jc<<endl;
	cout<<Rc<<endl;
	*/

   return 0;
}

