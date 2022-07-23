# Lesson 1: Big Data:

## 2. Data Sources:

IBM estimates that 90% of world's data was created in the last 2 years alone.

<img src="/home/mosaab/.config/Typora/typora-user-images/image-20191117135638829.png" alt="image-20191117135638829" style="zoom:50%;" />

There are a lot of sources that cause a huge amount of data like:

- Phone Data.

- Online Stores.

- Medicine (X-rays).

- Research.


But here's the problem, **How can we store that amount of data** and **process it too**?

## Definition of Big Data:

There's no one definition for big data, it's a very subjective term.

A reasonable definition of big data might be, it's **data that's too big to be processed on a single machine**.

## Challenges with Big Data:

- Data is created fast.
- Data from different sources in various formats.

## The 3 Vs:

When you read or talk about big data, you often hear people say the 3 Vs.

1. **Volume**: refers to the size of the data you're dealing with.
2. **Variety**: refers to the fact that the data is often coming from a lot of different sources and different formats.
3. **Velocity**: refers to the speed at which it's being generated, and the speed at which it needs to be made available for processing. 

1. **Volume**: to actually store the data reliably. You're going to end up paying more than that.

   That's the case with more traditional storage devices such as _Storage Area Network_  **SAN**, which can be extremely expensive.

   The high cost of reliable storage puts a cap on the amount of data companies can practically store.

   Storing the data is not the only problem, but streaming the data from the SAN across the network can take a long time and processing can be extremely slow.

2. **Variety**: The data has to be able to fit in pre-defined tables, and a lot of the data that we deal with these days, tends to be what we call **unstructured** or **semi-structured** data.

   By **unstructured**, we mean data arrived in lots of different formats. For example, a bank might have a list of your credit card and account transactions.

   All these data, in a variety of different formats can be hard to store and reconcile in a traditional system.

   The nice thing about **Hadoop** is that it doesn't care what format your data comes in. Unlike a traditional database, you can store the data in its raw format and manipulate it and reformat it later.

3. **Velocity**: is about the speed at which the data arrives, ready to be processed.

## Core Hadoop:

The core hadoop project consists of a way to store data, known as the  **Hadoop Distributed File System**, or **HDFS** and a way to process data with **MapReduce**.

![image-20191117153254974](/home/mosaab/.config/Typora/typora-user-images/image-20191117153254974.png)The key concept is that we _split_ the data up and store it across the collection of machines known as a **cluster**. Then when we want to process the data, we process it where it's actually stored.

Rather than retrieving the data from a central server, the data's already on the cluster, so we can process it in place.

You can add more machines to the cluster,  as the amount of data you're storing grows.

The machines in your cluster don't need to be anything particularly high end. Although most clusters are built using rack-mounted servers, they are typically mid-range servers, rather than top of the range equipment.

## Hadoop Ecosystem:

 Since the Hadoop project was first started, a lot of other software has grown up around it. And that's what we call the **Hadoop Ecosystem**. Some of the software is intended to make it easier to load data into the Hadoop cluster.

Writing **MapReduce** Code isn't completely simple. You need to know a programming language such as Java, Python, Ruby or Perl. But there are lots of folks out there who  aren't programmers, but can write SQL queries to access data in a traditional relational database system, like SQL Server.

For that reason, other open source projects have been created to make it easier for people to query their data without knowing how to code.

Two key ones are **Hive** and **Pig**. Instead of having to write **MapReduce**, in **Hive** you can write statements like standard SQL. The **Hive** interpreter turns the SQL into **MapReduce** code, which then runs on the cluster.

And alternative is **Pig**, which allows you to write code to analyse your data in a fairly simple scripting language, rather than **MapReduce**, and again the code will turn into **MapReduced** code and run on a cluster.

**NOTE**: **Hive** and **Pig** are great, but they're still running map reduce jobs, which as you'll see can take a reasonable around of time to run, especially over large amount of data.

Another open source project, is called **Impala**, which was developed as a way to query your data with SQL, but which directly accesses the data in **HDFS**, rather than needing map reduce.

**Impala** is optimized for low latency queries. In other words, **Impala** queries run very quickly, many times faster than **Hive**, while **Hive** is optimized for running long batch processing jobs.

Another project is called **Sqoop**, which takes data from a traditional relational database, such as **Microsoft SQL Server**, and puts it in **HDFS**, as the delimited files. So it can be processed along with other data on the cluster.

Then, there's **Flume**, which injests data as it's generated by external systems, and again puts it into the cluster.

**HBase** is a real-time database, built on top of **HDFS**.

**Hue** is a graphical front-end to the cluster. **Oozie** is a workflow management tool. **Mahout** is a machine learning library.

In fact, there are so many ecosystem projects that making them all talk to one another, and work well can be tricky.

**Cloudera** the company, has put together a distribution of **Hadoop** called **CDH**. (Cloudera Distribution including apache Hadoop) takes all the key ecosystem projects, along with **Hadoop** itself, and packages them together so that installation is a really easy process.

![image-20191117160328562](/home/mosaab/.config/Typora/typora-user-images/image-20191117160328562.png)