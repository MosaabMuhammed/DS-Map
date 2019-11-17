# Lesson 2: HDFS and MapReduce

## 1. HDFS:

Let's see how a file is stored as HDFS.

Imagine we're going to store a file called *mydata.txt* in **HDFS**, this file is a 150 megabytes. When a file is loaded into HDFS, it's split into chunks which we call **blocks**.

Each **block** is pretty big. The default is **64 megabytes**. Each block is given a unique name, which is **blk_num** 

<img src="/home/mosaab/.config/Typora/typora-user-images/image-20191117175450079.png" alt="image-20191117175450079" style="zoom:50%;" />

You can see the last **block** has the remaining megabytes and not necessarily 64 megabytes. 

As the file is uploaded to **HDFS**, each block will get stored on one node in the cluster.

There's a **Damon**, or piece of software, running on each of the machines in the cluster, called the **DataNode**.

Now clearly we need to know which blocks make up the original file. And that's handled by a separate machine, running the **Damon** called the **NameNode**.

The information stored on the **NameNode** is known as the **Metadata**. 

<img src="/home/mosaab/.config/Typora/typora-user-images/image-20191117180434652.png" alt="image-20191117180434652" style="zoom:67%;" />

Problems can exist in HDFS, if:

1. There a failure in the network.
2. There is a disk failure on DataNode.
3. Disk Failure on NameNode.

## 2. Data Redundancy:

The problem with things right now, is that if one of our nodes fails, we're left with missing data for the file. If the node goes away for example, we've got a 64 megabytes hole in the middle of mydata.txt.

To solve this problem, **Hadoop** replicates each block **3 times**, as it's stored in HDFS.

<img src="/home/mosaab/.config/Typora/typora-user-images/image-20191117181234504.png" alt="image-20191117181234504" style="zoom:40%;" />

**Hadoop** just picks 2 nodes at random and puts one copy of the block on each of the three. Well, it's not totally random, but that's close enough for us right now.

So now, if a single node fails, it's not a problem, because we have 2 other copies of the block on other node.

And the **NameNode** is smart enough to see that these blocks are now under-replicated and it will arrange to have those block re-replicated on the cluster.

Then, What happens if the **NameNode** has a hardware problem? 

- The data will be temporarily inaccessible.
- The data on HDFS could be lost forever.

So, to avoid the problem, people would configure the **NameNode** to store **MetaData**, not only on it's own hard drive but also somewhere on a network file system **NFS**.

**NFS** is a method of mounting a remote disk. that way even if the **NameNode** bursts into flames, there would be a copy of the metadata elsewhere on the network.

The **NameNode** is not a single point of failure in most production clusters, because they've configured 2 **NameNodes**. 

The **Active NameNode** works as before, but the standby can be configured to take over if the active one fails. That way the cluster will keep running if any of the nodes, even one of the Name Nodes, fails.

<img src="/home/mosaab/.config/Typora/typora-user-images/image-20191117182302997.png" alt="image-20191117182302997" style="zoom:67%;" />