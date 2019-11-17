# Lesson 2: HDFS and MapReduce

## 1. HDFS:

Let's see how a file is stored as HDFS.

Imagine we're going to store a file called *mydata.txt* in **HDFS**, this file is a 150 megabytes. When a file is loaded into **HDFS**, it's split into chunks which we call **blocks**.

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

<hr>

## 2. Data Redundancy:

The problem with things right now, is that if one of our nodes fails, we're left with missing data for the file. If the node goes away for example, we've got a 64 megabytes hole in the middle of _mydata.txt_.

To solve this problem, **Hadoop** replicates each block **3 times**, as it's stored in **HDFS**.

<img src="/home/mosaab/.config/Typora/typora-user-images/image-20191117181234504.png" alt="image-20191117181234504" style="zoom:40%;" />

**Hadoop** just picks 2 nodes at random and puts one copy of the block on each of the three. Well, it's not totally random, but that's close enough for us right now.

So now, if a single node fails, it's not a problem, because we have 2 other copies of the block on other node.

And the **NameNode** is smart enough to see that these blocks are now under-replicated and it will arrange to have those block re-replicated on the cluster.

Then, What happens if the **NameNode** has a hardware problem? 

- The data will be temporarily inaccessible.
- The data on **HDFS** could be lost forever.

So, to avoid the problem, people would configure the **NameNode** to store **MetaData**, not only on it's own hard drive but also somewhere on a network file system **NFS**.

**NFS** is a method of mounting a remote disk. that way even if the **NameNode** bursts into flames, there would be a copy of the **metadata** elsewhere on the network.

The **NameNode** is not a single point of failure in most production clusters, because they've configured 2 **NameNodes**. 

The **Active NameNode** works as before, but the standby can be configured to take over if the active one fails. That way the cluster will keep running if any of the nodes, even one of the Name Nodes, fails.

<img src="/home/mosaab/.config/Typora/typora-user-images/image-20191117182302997.png" alt="image-20191117182302997" style="zoom:67%;" />

<hr>

## 3. MapReduce:

Now, after we've seen how data is stored in **HDFS**, let's discuss how that data is processed with **MapReduce**.

Say, I have a large file. Processing that serially from the top to the bottom could take a long time.

<img src="/home/mosaab/.config/Typora/typora-user-images/image-20191117191955792.png" alt="image-20191117191955792" style="zoom:67%;" />Instead, **MapReduce** is designed to process data in **Parallel**. So your file was broken into chunks, and then processed in parallel.

<hr>

## 4. Distributed Work:

Rather than one person reading the entire ledger, say we had more people to help, we'll split them into 2 groups, called the **Mappers** and **Reducers**.

Then we'll take the ledger, break it into **chunks**, give each chunk to one of the **mappers**.

That way all the **mappers** can work at the same time, each over a **small** fraction of the data.

Let's see what a **mapper** would do. They will take the first record in their ledger, and on an index card write the name of the store, for example, and the amount of a sale.

Then they'll take the next record, and repeat. As they've writing the index cards, they'll pile them up so that cards for the same store go in the same pile.

By the end, each **mapper** will have a pile of card per store. Once the **mappers** have finished, the **reducers** can collect their sets of cards.

We'll tell each **reducer**, which store they're responsible for. The **reducers** go to the **mappers** and retrieve the pile of cards for their stores.

It's fast for them to do because the **mappers** have already separated the cards into a pile per store. Once the **reducers** have retrieved all their data, they collect all the small  piles and create a larger pile. Then they start going through the piles one at a time.

All they have to do, is add up all the amounts from all the cards in in the pile. That gives them a total sale for that store.

![image-20191117193600086](/home/mosaab/.config/Typora/typora-user-images/image-20191117193600086.png)

### Summary

The **Mappers** are just little programs that each deal with a relatively small amount of data, and work in parallel.

We call that output the **Intermediate Records**. That's what we were writing on our index cards. 

**Hadoop** deals with all data in the form of **key** and **value**. In our example, the key was the store name and the value was the sale total for each particular piece of input.

Once the **Mappers** have finished, a phase of **MapReduce** called the **Shuffle** and **Sort** takes place. 

- The **Shuffle** is the movement of the **intermediate records** from the **Mappers** to the **Reducers**. 
- The **Sort** is the fact that the **Reducers** will organize these sets or records, in our case these piles of index cards, into sorted order.

Finally, each **Reducer** works on one set of records at a time, or one pile of cards. It gets the key and then a list of all the values.

It process these values in some way. In our case, we were adding up the sales. Then it writes out the final results.

<img src="/home/mosaab/.config/Typora/typora-user-images/image-20191117194605684.png" alt="image-20191117194605684" style="zoom:50%;" />

<hr>

## 5. Daemons on MapReduce:

![image-20191117211636120](/home/mosaab/.config/Typora/typora-user-images/image-20191117211636120.png) There are a set of **daemons**, which is just a piece of code, running all the time, running on each of these machines. There were the **DataNodes** and the **NameNodes**. 

When you run a **MapReduce** job, you submit the job to what's called the **Job Tracker**. That splits the work into **mappers** and **reducers**.

Those **mappers** and **reducers** will run on the other cluster nodes. Running the actual map and reduce tasks is handled by a **daemon** called the **Task Tracker**. 

The **Task Tracker** software will run on each of these nodes. Note that since the **Task Tracker** runs on the same machine as the **data nodes**, the **Hadoop** framework will be able to have the map tasks work directly on the pieces of data that are stored on that machine. This will save a lot of network traffic.

As we saw, each **mapper** processes a portion of the input data, that's known as the **input split**. And by default, **Hadoop** use an **HDFS** block as the input split for each **Mapper**.

It will try to make sure that a **Mapper** works on data on the same machine. So the **mappers** will read their input data. They'll produce **intermediate data**, which the **Hadoop** framework will pass to the **reducers**, remember that's the **Shuffle** and **Sort**.

Then the **reducers** process that data and write their final output back to **HDFS**.

 