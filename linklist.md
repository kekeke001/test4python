## 链表
### 单链表
单链表的定义
```c
//单链表节点类型的定义
typedef struct LNODE{
    int data;
    struct LNode *next;
}LNode,*LinkList;// LinkList表示指向struct LNode类型的指针

//typedef
typedef 数据类型 别名
typedef int *zhengshuzhizhen//给指向int类型的指针取别名zhengshuzhizhen
int *p <=> zhengshuzhizhen p;

//增加一个新节点，在内存中申请该节点所需要的空间，并用指针p指向这个节点
LNode *p=(LNode *)malloc(sizeof(struct LNode));
```
带头节点
```c
//初始化单链表
bool InitList(LinkList &L){
    L=(LNode *)malloc(sizeof(LNode));//分配一个头节点
    if (L==NULL)
        return false;//分配失败
    L->next=NULL;
    return true;
}

//单链表的建立--尾插法
LinkList List_TailInsert(LinkList &L){
    int x;
    L=(LinkList )malloc(sizeof(LNode));
    L->next=NULL;
    LNode *s,*r=L;//r为表尾指针
    scanf("%d",&x);
    while(x!=9999){//结束条件
        s=(LNode *)malloc(sizeof(LNode));
        s->data=x;
        s=r->next;
        r=s;//r重新指向表尾节点
        scanf("%d",&x);
    }
    r->next=NULL;
    return L;
}

//单链表的建立--头插法--输入元素的逆序--链表的逆置
LinkList List_headInsert(LinkList &L){
     L=(LinkList )malloc(sizeof(LNode));
     L->next=NULL;//初始化的时候，这句不能丢
     LNode *s
     int x;
     scanf("%d",&x);
     while(x!=9999){//结束条件
         s=(LNode *)malloc(sizeof(LNode));
         s->data=e;
         s->next=L->next;
         L->next=s;
         scanf("%d",&s);
     }
     return L
}

//按位插入
bool ListInsert(LinkList &L,int i,int e){
    if(i<1) return false;
    int j=0;//表示当前p指向的第几个节点
    LNode *p=L;//p指向头节点
    while(j<i-1 && p!=NULL){//循环找到第i-1个节点
        p=p->next;
        j++;
    }
    if(p==NULL)
        return false;//i的值不合法
    LNode *s=(LNode *)malloc(sizeof(LNode));
    s->data=x;
    s->next=p->next;
    p->next=s;
    return true;
}

//指定节点后插操作，在p节点之后插入元素e,p节点前节点未知，头指针未给出
bool InsertNextNode(LNode *p,int e){
    if(p==NULL) return false;
    LNode *s=(LNode *)malloc(sizeof(LNode));
    if (s==NULL) return false;//内存分配失败
    s->data=e;
    s->next=p->next;
    p->next=s;
    return true;
}

//指定节点后插操作，在p节点之前插入元素e,p节点前节点未知，头指针未给出
bool InsertPriorNode(LNode *p,int e){
    if(p==NULL) return false;
    LNode *s=(LNode *)malloc(sizeof(LNode));
    if (s==NULL) return false;//内存分配失败
    s->next=p->next;
    p->next=s;//新节点s连到p后
    s->data=p->data;//将p中的元素复制到s中
    p->data=e;//p中的元素覆盖成e
    return true;
}

//按位删除
bool ListDelete(LinkList &L,int i,int &e){
    if(i<1) return false;
    int j=0;
    LNode *p=L;
    while(j<i-1 && p!=NULL){//循环找到第i-1个节点
        p=p->next;
        j++;
    }
    if(p==NULL) return false;//i值不合法
    if(p->next==NULL) return false;//第i-1个节点后无其他节点
    q=p->next;
    e=q->data;
    p->next=q->next;
    free(q);
    return true;
}

//指定节点删除，删除节点p，节点p前未知，头指针未知
bool DeleteNode(LNode *p){
    if (p==NULL) return false;
    LNode *q=p->next;
    p->data=q->data;//若p是最后一个节点，有bug，因为指向null的指针没有数据域
    p->next=q->next;
    free(q);
    return true;
}

//按位查找并返回该节点
//要表示一个单链表，只需要声明一个头指针L，指向单链表中的第一个节点
LNode *GetElem(LinkList L,int i){
    j=1;
    LNode *p=L->next;//头节点的指针赋值给p
    if(i==0) return L;//若i等于0，则返回头节点
    if(i<1) return NULL;//i无效，返回null
    while(j<i && p!=NULL){//循环找到第i个节点
       p=p->next;
       j++;
    }
    return p;//返回第i个节点的指针，若i大于表长则返回null
}

//判空
bool Empty(LinkList L){
    if (L->next==NULL);
        return true;
    else 
        return false;
}

void main(){
    LinkList L1;//声明一个指向单链表的指针，内存中开辟一个空间，存放头指针L
    InitList (L1);//单链表初始化
}



```

不带头节点
```c
//初始化单链表
bool InitList(LinkList &L){
    L=NULL;//空表
    return true;
}

//判空
bool Empty(LinkList L){
    if (L==NULL);
        return true;
    else 
        return false;
}

//按位插入
bool ListInsert(LinkList &L,int i,int e){
    if(i<1) return false;
    int j=1;//表示当前p指向的第几个节点
    LNode *p=L;
    LNode *s=(LNode *)malloc(sizeof(LNode));
    if(i==1){
        s->data=e;
        s->next=p;
        L=s;//头指针指向新指针
        return true;
    }
    while(j<i-1 && p!=NULL){//循环找到第i-1个节点
        p=p->next;
        j++;
    }
    if(p==NULL)
        return false;//i的值不合法
    s->data=e;
    s->next=p->next;
    p->next=s;
    return true;
}

//按位删除
bool ListDelete(LinkList &L,int i,int &e){
    if(i<1) return false;
    int j=1;
    LNode *p=L;
    while(j<i-1 && p!=NULL){//循环找到第i-1个节点
        p=p->next;
        j++;
    }
    if(p==NULL) return false;//i值不合法
    if(i==1){
        e=p->data;
        L=p->next;
        free(p);
    }
    if(p->next==NULL) return false;//第i-1个节点后无其他节点
    q=p->next;
    e=q->data;
    p->next=q->next;
    free(q);
    return true;
}

void main(){
    LinkList L1;//声明一个指向单链表的指针，内存中开辟一个空间，存放头指针L
    InitList (L1);//单链表初始化
}
```

### 双链表
双链表的定义
```c
typedef struct DNode{
    int data;
    struct DNode *prior,*next;//前驱指针，后继指针
}DNode, *DLinkList;

```
带头节点
```c
//初始化
bool InitDLinkList(DLinkList &L){
    L=(DNode *)malloc(sizeof(DNode));//分配头节点，强调的是节点
    if(L==NULL) return false;//分配失败
    L->prior=NULL;
    L->next=NULL;
    return true;
}

//判空
bool Empty(DLinkList L){
    if(L->next==NULL)
        return true;
    else
        return false;
}

//后插--p前区域未知，在p节点后插入s
bool InsertNextDNode(DNode *p,DNode *s){
    if(p==NULL || s=NULL)  return fasle;
    s->next=p->next;
    if (p->next!=NULL)//如果p节点有后继节点
        p->next->prior=s;
    p->next=s;
    s->prior=p;
}

//删除--p前区域未知，删除p节点的后继节点q
bool DeletetNextDNode(DNode *p){
    if(p==NULL) return false;
    DNode *q=p->next;
    if(q==NULL) return false;
    p->next=q->next;
    if(q->next!=NULL)//q不是最后一个节点
        q->next->prior=p;
    free(q);
return true;    
}

//销毁双链表
void DestoryDLinkList(DLinkList &L){
    while(L->next!=NULL)//循环释放头节点之后的各个节点
        DeleteNextDNode(L);
    free(L);//释放头节点
    L=NULL;    //头指针指向NULL
}

//双链表的遍历
while(p!=NULL)//后向遍历
    p=p->next;

while(p!=NULL)//前向遍历，头节点没有前向指针
    p=p->prior;
while(p—>prior!=NULL)//前向遍历,不处理头节点，p->prior==null时,p指向的是头节点
    p=p->prior;
    
void main(){
   DLinkList L;//强调这是个链表
   InitDLinkList(L);
}

```

不带头节点
```c

```


### 循环链表
循环单链表
单链表：表尾指针的next指针指向NULL
循环单链表：表尾节点的next指针指向头节点
```c
typedef struct LNode{
    int data;
    struct LNode *next;
}LNode，*LinkList;

//初始化一个循环单链表
bool InitList(LinkList &L){
    L=(LNode *)malloc(sizeof(LNode));//分配头节点
    if (L==NULL)	//分配失败
        return false;
    L->next = L;//头节点的next指向头节点
    return true;
}

//判空
bool Empty(LinkList L){
    if (L->next==L)  
        return true;
    else
        return false;
}

//判断节点p释放为循环单链表的尾节点
bool isTail(LinkList L,LNode *p){
    if(p->next==L)
        return true;
    else
        return false;
}
    
```

循环双链表
双链表：表头节点的piror指针指向NULL；表尾节点的next指针指向NULL
循环双链表：表头节点的piror指向表尾节点；表尾节点的next指向头节点
```c
//初始化空的循环双链表
typedef struct DNode{
    int data;
    struct DNode *prior,*next;
}DNode,*DLinkList;

bool InitDLinkList(DLinkList &L){
    L=(DNode *)malloc(sizeof(DNode));//分配一个头节点
    if(L==NULL) 
        return false;
    L->prior=L;
    L->next=L;
    return true;
}

//判空
bool Empty(DLinkList L){
    if(L->next==L)
        return true;
    else
        return false;
}

//判断p节点是否为循环双链表的表尾节点
bool isTail(DLinkList L,DNode *p){
    if(p->next==L)
        return true;
    else 
        return false;
}

//插入
bool InsertNextNode(DNode *p,DNode *s){
    s->next=p->next;
    p->next->prior=s;
    s->prior=p;
    p->next=s;
}

//删除p的后继节点q
p->next=q->next;
q->next_>prior=p;
free (q);
```


### 静态链表
静态链表：分配一整片的连续空间，各个节点集中安置（数据元素，游标）
```c
//定义
#define MaxSize 10//静态链表的最大长度
struct Node {
    int data;//数据元素
    int next;//下一个元素的游标
};
or
//后续可用SLinkList定义一个长度为MaxSize的Node型数组
typedef struct Node SLinkList[MaxSize];
void SLinkList(){
    struct Node a[MaxSize];
}

//初始化
    把a[0]的next设置成-1//a[0]是头节点
    把其他空闲节点的next设置成-2
    
//在位序为i的地方插入节点
    找到一个空的节点，存入数据元素
    从头节点出发找到为序为i-1的节点
    修改新节点的next
    修改i-1号节点的next
    注：防止脏数据，应该将空闲节点的next设置成-2
```
###顺序表，链表比较
```
* 都是线性结构--逻辑结构
* 存储结构不同
* 创建操作：顺序表需要预分配大片的连续的空间；链表只需分配头节点，头指针；
* 销毁操作：链表--各个节点依次删除,free().  
          顺序表--length=0，静态分配：静态数组--系统自动回收空间；动态分配：动态数组(malloc,free)--需要手动free；malloc()和free()成对出现
* 插入删除：顺序表：元素后移/前移，O(n)--时间开销自于移动元素   链表：修改指针，          O(n)--时间开销来源于查找元素
* 查找：顺序表：随机存取，按位查找O(1)  按值查找O(n)
       链表：按位/按值查找O(n)
```













































































