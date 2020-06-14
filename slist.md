### 线性表---顺序表
#### 顺序表静态分配
```c
# define maxSize 100				//定义最大长度
typedef struct{
    ElemType data[Maxsize];		//用数组来存放数据
    int length;					//顺序表当前长度
}SqList;					//顺序表类型的定义

//初始化操作--初始化一个线性表
void InitList(SqList &L){
    for(i=0;i<MaxSize;i++)
        L.data[i]=0;			//将所有元素的数据设为0，防止脏数据；这步可省略
    int length=0;				//顺序表初始长度为0
    }
    
// 往线性表第i个位置上插入指定的元素e
bool Insert(SqList &L,int e,int i){
    if (i<1 || i>L.length + 1) //判断i的范围
        return false;
    if(L.length >= L.Maxsize)	//当前存储空间已满，不能插入
        return false;
     for(j=L.length;j>=i;j--)
        L.data[j]=L.data[j-1];
     L.data[i-1]=e;
     L.length ++;
     return true;
}

// 删除顺序表位置为i的元素
bool Delete (SqList &L,int &e,int i){
    if (i<1 || i>L.length ) 
        return false;
    e=L.data[i-1];
    for(j=i;j<L.length;j++)
        L.data[j-1]=L.data[j];
    L.length--;
    return true;
}

//按值查找
int LocationElem(int e,SqList L){
    for(i=0;i<L.length;i++)
        if (L.data[i]==e)
            return i;
    return 0;
}
    
int main(){
    //声明一个顺序表，并在内存中分配空间；MaxSize*sizeof(ElemType),length
    SqList L;
    InitList(L);				
    ...
    int e =-1；
    if (ListDelete(L,3,e))
        printf(....)
    return 0;
}
```

#### 顺序表动态分配存储空间
```c
#define InitSize 50			//顺序表初始长度
typedef struct{
    int *data;			//指示动态分配数组的指针,指向顺序表中第一个数据元素
    int length,MaxSize;
    }seqList;

bool InitSize(SeqList &L){
    //malloc():申请一整片连续的存储空间，并返回一个指向该存储空间起始地址的指针
    L.data =(int *) malloc(sizeof(int) * Initsize);
    if (!L.data) return 0;//存储空间分配失败
    int length=0;
    L.MaxSize=InitSize;
    return 1;
    }
    
//动态增加数组的长度
void IncreaseSize(SeqList &L,int len){
    int *p = L.data;
    L.data = (int *) malloc(sizeof(int) * (L.maxSize + len));
    for(i = 0;i < L.length;i++)
        L.data[i]=p[i];
    L.MaxSize = L.length + len;
    free (p); 
}



int main() {
    SeqList L;			//声明线性表，在内存中会开辟空间
    InitSize (L);
    IncreaseSize(L,5);
    return 0;
}   

```

## Exercise



1、从顺序表中删除具有最小值的元素（假设唯一）并由函数返回被删除元素的值。空出的位置由最后一个元素填补，若顺序表为空则显示出错误信息并退出运行

```c
    bool Del_Min(SqList &L,ElemType &e){
        if(L.length==0)  return false;
        e=L.data[0];
        int j=0;
        for(i=1;i<L.length;i++){
            if(L.data[i] < e)
                e=L.data[i];
                j=i;
        }
        L.data[j]=L.data[L.length-1];
        L.length--;
        return true;
        }     
    }//函数返回值只能返回一个值，而参数引用可以返回多个值
```

2、设计一个高效算法，将顺序表所有的元素逆置，要求算法的空间复杂度为O(1)
```c
    bool Reverse(SqList &L){
        if (L.length==0)  return false;//可以不要
        int temp;
        for(i=0;i<L.lenth/2:i++){
            temp=L.data[i];
            L.data[i]=L.data[L.length-i-1];
            L.data[L.length-i-1]=temp;
        }
        return true;
    }
    
3、对于长度为n的顺序表L，编写一个时间复杂度为O(n),空间复杂度为O(1)的算法，该算法删除线性表中所有值为x的数据元素
    void Del_x1 (SqList &L,int x){    //法1  O(n^2)
        for(int i=0;i<L.length-1;i++){
            if(L.data[i]==x){
                L.data[i]=L.data[i+1];
                L.length--;
            }
        }
    }
    
    void Del_x2 (SqList &L,int x){    //法2,k用于统计不等于x的个数
        int k=0;
        for(int i=0;i<L.length;i++ ){
            if(L.data[i]!=x){
                L.data[k]=L.data[i];
                k++;
                } 
        }
        L.length=k;
    }
    
    void Del_x3 (SqList &L,int x){    //法3，k用于统计等于x的个数
        int k=0;
        for(int i=0;i<L.length;i++ ){
            if(L.data[i]==k)    K++;
            else  L.data[i-k]=L.data[i]; 
        }
        L.length=L.length - k;
    }
```


4、从有序顺序表中删除其值在给定值s与t之间(要求s<t)的所有元素。如果s或t不合理或顺序表为空，则显示错误信息并退出
```c
    bool Del_s_t(SqList &L,int s,int t){
        if (L.length==0  || s>=t)    return false;
        for(int i=0;i<L.length && L.data[i]<s;i++);
        for (int j=0;j<L.length && L.data[j]<=t ;j++);
        for(;j<L.length;i++,j++)   
            L.data[i]=L.data[j];
        L.length=i;
        return true;   
    }
```


5、从顺序表中删除其值在给定值s与t之间(要求s<t)的所有元素。如果s或t不合理或顺序表为空，则显示错误信息并退出
```c
    bool Del_s_t(SqList &L,int s,int t){
        if (L.length==0  || s>=t)    return false;
        int k=0;
        for(i=0;i<L.length;i++){
            if(s<=L.data[i] && L.data[i]<=t)    k++;
            else   L.data[i-k]=L.data[i];
        }
        L.length=L.length-k;    
        return true;
        }
```

6、从有序顺序表中删除其值重复的元素，使表中的所有元素均不相同
```c
    void Del_Dupli(SqList &L){
        int k=0;
        a=L.data[0];
        for(int i=1;i<L.length;i++){
            if (L.data[i]!=a)  a=L.data[i];
            else{
                for(int j=i;j<L.length-1;j++)
                    L.data[j]=L.data[j+1];
                    L.length--;
            }
        }
    }
    
    bool Del_Same(SqList &L){            //法2
        if (L.length==0)    return false;
        for(int i=0,j=1;j<L.length;j++){
            if (L.data[i]!=L.data[j])
                L.data[++i]=L.data[j];
        }
        L.length=i+1;
        return true;
    }
```

7、将两个有序顺序表合并成一个新的有序顺序表，并由函数返回结果
```c
    bool merge(Sqlist A,Sqlist B,Sqlist &C){
        if(A.length+B.length>C.maxsize)
            return 0;
        int i=j=k=0;
        for(i=j=k=0;i<A.length,j<B.length;){
            if(A.data[i]<=B.data[j])
                c.data[k++]=A.data[i++];
            else c.data[k++]=B.data[j++];
        }
        while(i<A.length)
            c.data[k++]=A.data[i++];
        while(j<B.length)
            c.data[k++]=B.data[j++];
        C.length=k;
        return 1;
    }
```

8、已知在一维数组A[m+n]中依次存放两个线性表（a1，a2，a3，...,am）和（b1，b2，b3,...,bn)。试编写一个函数，将数组中两个顺序表位置互换，即将(b1,b2,b3,...,bn)放在（a1，a2，a3,...,am）的前面

```c
    void changepos(int A[],int &c[], m, n){//法一
        for (i=0;i<n;i++)
            c[i]=A[i+m];
        for(i=n;i<m+n;i++)
            c[i]=A[i-n];

    typedef int datatype;
    void Reverse(int A[],int left,int right,int arraysize){
        int mid=(left+right)/2;
        if (left >= right || right >=arraysize)
        for(int i=0;i<=mid -left;i++){
            int temp=a[left+i];
            a[left+i]=a[right-i];
            a[right-i]=temp;
        }
    }
    void Exchange(int A[],int m,int n,int arraysize){
        Reverse(A,0,m+n-1,arraysize);
        Reverse(A,0,n-1,arraysize);
        Reverse(A,n,m+n-1,arraysize);
    }
```

9、线性表(a1,a2,...,an)中的元素递增且有序，按顺序存储在计算机中。要求设计一个算法，完成用最少的时间在表中查找数值为x的元素，若找到将其与后继元素位置交换，若找不到则将其插入表中并使表中的元素递增且有序
```c
    void sqList(Sqlist &L，int x){
        for(i=0;i<L.length;i++){
            if (L.data[i]>=x)
                j=i;
                break;
        }
        if (L.data[j]==x){
            temp=L.data[j+1];
            L.data[j+1]=x;
            L.data[j]=temp;
            }
        else 
            for(int i=L.length;i>j;i--)
                L.data[i]=L.data[i-1];
            L.data[j]=x;
}

    void SearchExchangeInsert(){//折半查找，效率最高
        int low=0,high=n-1,mid;//low,high分别指向顺序表的下界和上界下标
        while(low<=high){
            mid=(low+high)/2;
            if(A.mid==x)  break;
            else if(A.mid<x) low=mid+1;
            else (A.mid>x) high=mid-1;
        }
        if(A[mid]==x && mid!=n-1){//若最后一个元素与x相等，则不存在交换的动作
            t=A[mid];
            A[mid]=A[mid+1];
            A[mid+1]=t;
        }
        if(low>high){//查找失败
            for(i=n-1;i>high,i--)
                A[i+1]=A[i];
            A[i+1]=x;
        }   
    }

```






