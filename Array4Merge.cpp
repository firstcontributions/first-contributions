#include <iostream>
using namespace std;
class Array
{
    public:
    int *A,*B;
    int size;
    int length;
    void setdata()
    {
        int i,n;
        cout<<"Enter the size of array: ";
        cin>>size;
        A=new int[size];
        B=new int[size];
        cout<<"Enter the length:";
        cin>>n;
        cout<<"Enter the elements for A:"<<endl;
        for(i=0;i<n;i++)
        {
            cin>>A[i];
        }
        cout<<"Enter the elements for B:"<<endl;
        for(i=0;i<n;i++)
        {
            cin>>B[i];
        }
        length=n;
    }
    void display()
    {
        int i;
        cout<<"Elements of A are: "<<endl;
        for(i=0;i<length;i++)
        {
            cout<<A[i]<<" ";
        }
        cout<<endl;
        cout<<"Elements of B are: "<<endl;
        for(i=0;i<length;i++)
        {
            cout<<B[i]<<" ";
        }
        cout<<endl;
    }
    void Merge()
    {
        int *C;
        C=new int[size];
        int i=0,j=0,k=0;
        while(i<length && j<length)
        {
            if(A[i]<B[j])
            {
                C[k++]=A[i++];
            }
            else
            {
                C[k++]=B[j++];
            }
        }
        for(;i<length;i++)
        {
            C[k++]=A[i];
        }
        for(;j<length;j++)
        {
            C[k++]=B[j];
        }

        cout<<"Print elements of array C"<<endl;
        for(i=0;i<size;i++)
        {
            cout<<C[i]<<" ";
        }
    }
    void Union()
    {
        int *C;
        C=new int[size];
        int i=0,j=0,k=0;
        while(i<length && j<length)
        {
            if(A[i]<B[j])
            {
                C[k++]=A[i++];
            }
            else if(B[j]<A[i])
            {
                C[k++]=B[j++];
            }
            else
            {
                C[k++]=A[i++];
                j++;
            }
        }
        for(;i<length;i++)
        {
            C[k++]=A[i];
        }
        for(;j<length;j++)
        {
            C[k++]=B[j];
        }

        cout<<"Union of A and B is C: "<<endl;
        for(i=0;i<k;i++)
        {
            cout<<C[i]<<" ";
        }
        cout<<endl;
    }
    void intersection()
    {
        int i=0,j=0,k=0;
        int *C;
        C=new int[size];
        while(i<length && j<length)
        {
            if(A[i]<B[j])
            {
                i++;
            }
            else if(B[j]<A[i])
            {
                j++;
            }
            else
            {
                C[k++]=A[i++];
                j++;
            }
        }
        cout<<"Intersection of A and B is C: "<<endl;
        for(i=0;i<k;i++)
        {
            cout<<C[i]<<" ";
        }
        cout<<endl;
    }
    void difference()
    {
        int i=0,j=0,k=0;
        int *C;
        C=new int[size];
        while(i<length && j<length)
        {
            if(A[i]<B[j])
            {
                C[k++]=A[i++];
            }
            else if(B[j]<A[i])
            {
                C[k++]=A[i++];
                j++;
            }
            else 
            {
                i++;
                j++;
            }
        }
        cout<<"Difference of A and B is C: "<<endl;
        for(i=0;i<k;i++)
        {
            cout<<C[i]<<" ";
        }
        cout<<endl;
    }
};
int main()
{
    Array a;
    int ch;
    do{
        cout<<"  MENU  "<<endl;
        cout<<" 1)setdata "<<endl;
        cout<<" 2)Display "<<endl;
        cout<<" 3)Merge "<<endl;
        cout<<" 4)Union "<<endl;
        cout<<" 5)Intersection "<<endl;
        cout<<" 6)Difference "<<endl;
        cout<<" 7)EXIT "<<endl;

        cout<<"Enter your choice: ";
        cin>>ch;

        switch(ch)
        {
            case 1:cout<<"To set the data"<<endl;
            a.setdata();
            break;
            case 2:cout<<"To display the data"<<endl;
            a.display();
            break;
            case 3:cout<<"Merging Operaton"<<endl;
            a.Merge();
            break;
            case 4:cout<<"Union Operation"<<endl;
            a.Union();
            break;
            case 5:cout<<"Intersection Operation"<<endl;
            a.intersection();
            break;
            case 6:cout<<"Difference Operation"<<endl;
            a.difference();
            break;
        }

    }while(ch<7);
    //a.setdata();
    //a.display();
    //a.Merge();
    //a.Union();
    //a.intersection();
    //a.difference();
    return 0;
}