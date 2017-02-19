#include <iostream>
#include <vector>
#include <algorithm>

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
    while (k-- > 0)
        result = (result << 1) + rand() % 2;
    return result;
}

int main()
{

	for(int i=5;i<23;i++){
		cout<<"str"<<endl;
		int *v = new int(i);
		cout<<"i "<<i<<endl;
	for(int j=0;j<i;j++){
		cout<<"j2 "<<j<<endl;
		v[j]=(random2(i));
		cout<<"j1 "<<v[j]<<endl;
	}
	cout<<"midd"<<endl;
	sort(v,v+i);
   
   int tar= random2(i);
   int j = Jessie(v,0,i-1,tar);
   int r = Riley(v,0,i-1,tar);

   cout<<"tar"<<tar<<endl;
   cout<<j<<endl;
   cout<<r<<endl;	
   cout<<countJ<<endl;
   cout<<countR<<endl;
   cout<<"end"<<endl;
   for(int k=0;k<i;k++){
   	delete v[k];
   }
   delete [] v;
	}
	

   return 0;
}

