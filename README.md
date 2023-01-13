# Milestone 1: Data Ingestion System (Apache Kafka)
## Repository: 
[https://github.com/GeorgeDaoud3/SOFE4630U-MS1](https://github.com/GeorgeDaoud3/SOFE4630U-MS1)
## Objectives
1.	Understand the role of Data Ingestion System in Event Driven Architecture.
2.	Get familiar with Kafka and its terminologies. 
3.	Be able to create topics, producers, and consumers via GUI and code.
4.	Get familiar with Google Pub/sub.

## What’s Kafka?
1.	Watch the following video about [Event Driven Architecture (EDA)](https://www.youtube.com/watch?v=o2HJCGcYwoU)
2.	The core component of an EDA is the Data Ingestion System also known as Publisher/subscriber (pub/sup). 
Kafka is one of the most frequent used pub/sub. Watch the following video to get a good understanding of [Kafka and its terminologies](https://www.youtube.com/watch?v=Ch5VhJzaoaI).
3.	You can set up Kafka cluster on a set of locally connected computers, 
deploy it as a set of docker images over Kubernetes cluster, or use already exists cloud-native service. 
In this section, we will use Kafka confluent Cloud as a cloud-native service. It’s a tool that can integrate with any cloud platform 
like Google Cloud Platform (GCP) to create a Kafka cluster. Thus, we will start by creating a GCP account.  

## Creating GCP account
1.	It’s recommended to create a new Gmail account, but you can use an already existing account.
2.	Go to [GCP official site](https://cloud.google.com/gcp). Be sure that you are using the correct account. Then, click on **Get Started for free** button  

![a1](images/a1.jpg)  

3.	Fill the account information and accept the terms of services  

![a2](images/a2.jpg)  

4.	In the next step, you will fill in your personal information and a credit card information. That information is to ensure that you are a real person. This will create a free account for 90 days and give you 300+ $ free credits. **No charges are made unless you upgrade to a paid Cloud Billing account**. Please read [the GCP billing verification](https://cloud.google.com/free/docs/free-cloud-features#billing_verification) for more information.  

![a3](images/a3.jpg)  

5.	Fill in the final survey. Then, click **Done**. You can safely skip any given offers.  

![a4](images/a4.jpg)  

6.	Get yourself familiar with
* Dashboard: allows you to search and select available cloud services
* project(s): a project usually named **My First Project** will be created but we can create, edit, and delete projects.
* The console: By clicking the console icon, the console will be opened to you. The console is a Linux terminal that can be used to configure the cloud. Any commands that affect the console local OS will be temporary and lost whenever the session is closed while any change made to any cloud services will be permanent.  
 <img src="images/a5.jpg" alt="a5" width="750">

The console will be opened at the bottom of the page as shown in the following figure and from it we can exchange files and folders with your local computer by downloading or uploading them. You can also click **Open Editor** button to open the editor.  
<img src="images/a6.jpg" alt="a6" width="750">

* Editor: It’s a text editor that allows you to edit plain text file as shown in the following figure. You can switch back to the console by clicking **Open Terminal** button  

<img src="images/a7.jpg" alt="a7" width="750">

# Create a Confluent Kafka Cluster
1.	Open [the Confluent Cloud-native Service for Apache Kafka](https://www.confluent.io/confluent-cloud/). Then click **TRY FREE**.  

<img src="images/b1.jpg" alt="b1" width="750">  

2.	Sign in with the same Google account  

<img src="images/b2.jpg" alt="b2" width="750">  

3.	Enter your personal Information. Then, click **Submit**  

<img src="images/b3.jpg" alt="b3" width="350">  

4.	Finish the final survey and click **Continue**.  
5.	The first step in creating the Kafka cluster is to choose the free Basic configuration. Then, Choose Google Cloud as the service provider, Toronto as a **Region**, and the A single zone as the **Availability**. Then press **Continue**.   

<img src="images/b4.jpg" alt="b4" width="750">  

6.	Don’t enter the payment info.   

<img src="images/b5.jpg" alt="b5" width="750">  

7.	Finally, choose the cluster name and press **Launch cluster**  

<img src="images/b6.jpg" alt="b6" width="750">  

## Create a topic, producer and consumer using the GUI
1.	Go to [the Confluent Kafka home page](https://confluent.cloud/home).
2.	Click **View environments**.  

<img src="images/c0.jpg" alt="c1" width="750">  

3.	Select the default environment.  

<img src="images/c1.jpg" alt="c2" width="350">  

4.	Select the cluster according to its name.  

<img src="images/c2.jpg" alt="c3" width="750">  

5.	Create a topic by selecting **topics**. Then click on **Create topic**.  

<img src="images/c3.jpg" alt="c4" width="350">  

6.	Choose the topic name as **testTopic** and you can leave the number of partitions to the default value of 6. Also, by clicking on **Show advanced settings**. Thus, you can change the **Cleanup policy**, **Retention time**, **Retention size**, and **maximum message size**. For now, you clean leave them with the default values. Finally, click **create with defaults** to create the topic.  

<img src="images/c4.jpg" alt="c5" width="750">  

7.	In the **testTopic** page, create **messages** tap which allows you to produce and consume messages.  

<img src="images/c5.jpg" alt="c6" width="750">  

8.	Click on **+ Producer a new message to this topic** shown in the previous figure. A default value/key message will be generated for you. 
The value is in a JSON format, but we can change it to a plain string. The key also is a number, but it can also be a string.  
Change the **value** to **“Hello Kafka”** and the **key** to **1**. Then click **Produce**.  

<img src="images/c6.jpg" alt="c7" width="750">  

9.	It will be automatically consumed in the consumer region. The partition will be determined by hashing the key value.  

<img src="images/c7.jpg" alt="c8" width="750">  

10.	Produce more messages. The consumer part should look like  

<img src="images/c8.jpg" alt="c9" width="750">  

11.	If you refreshed the page, the consumption area will be empty because all messages were consumed before.  

## Create a Topic, Producer and Consumer Using Python Code
1.	To create a Kafka client, either a producer or a consumer using a language of your choice. Click **Dashboard**. Then, at the **Set up client** area, click **Get started**. Click **Set up a new client** to get a template of a given language.  

<img src="images/d1.jpg" alt="d1" width="750">  

2.	Inspired by the given template, this section will guide you to write a python script for a consumer and a producer. The first step is to get an API key for a credential that enables you to create to the Kafka cluster. Start by clicking **API keys**. Then, click **Create key**.  

<img src="images/d2.jpg" alt="d2" width="750">  

3.	To make your life easier, choose **Global access**. Then, click **next**.  

<img src="images/d3.jpg" alt="d3" width="350">  

4.	Click **Download and continue**. A text file will be downloaded containing the values of the **API key**, the **API secret**, and the address of the **Bootstrap server**.  
5.	Once created, **API keys** will show a list of already created keys to redownload.  
**Note**: The following steps should run on your local computer to act as a data source that is located outside the cloud. The following set of python codes will create a topic named “testTopic2” to produce and consume messages from  
6.	Install the python library  
``` python
pip install confluent-kafka[avro,json,protobuf]
```  
7.	Copy the file from folder **v1** from the GitHub repository to a certain folder in your computer.  
8.	Edit the cred.json and replace <**Bootstrap servers**>, <**CLUSTER_API_KEY**>, and  <**CLUSTER_API_SECRET**> by the values of the **Bootstrap server**, **API key**, and **API secret** you got in step 4 in this section. Save the file to be used as a credential for the other python scripts.  

<img src="images/d4.jpg" alt="d4" width="350">     

9.	**createTopic.py** is the script used to create a topic. Edit the file and change the topic name in line 8th from <"**topicname**"> to "**testTopic2**". You can change the default values of the number of partitions and the replication factor at lines 9 and 10. The credential is read from the **cred.json** file according to the python statement in line 7. The **cred.json** and **createTopic.py** should be in the same folder. In line 12, an admin client is created that has the privileged to create topics. The statement in lines 14 to 16 creates an array of new topics that contains only a single topic. The array is passed to a createTopics function to create the topics. The loop starting from line 18 goes through the results of createTopics and prints a summary of the creation results.  

<img src="images/d5.jpg" alt="d5" width="750">  

Save the file and run it, the output should look like  

<img src="images/d6.jpg" alt="d6" width="200">  

10.	**producer.py** is a python script that produces messages to a topic. Following the same technique change the topic name in line 8 to **“testTopic2”**. The second marked box in the following figure is a call back function that prints the output of each produce function that sends a message to the Kafka. The code in the third rectangle reads two strings and an integer that represents the key, value and the partition number from the user. Entering any integer less than -1 will stop the loop. The fourth box sends the message via produce function and invokes the call back function using the poll function. The last box flushes the producer internal buffer to ensure that all messages are already sent before ending the program. **Note:** a partition of value of -1 or when it's not included in the produce function, will make kafka decides automatically the paratition number accordinf to a built-in hashing function.  

<img src="images/d7.jpg" alt="d7" width="750">  

11.	The final script is **consumer.py**. As usual, change the topic name in line 6 to “testTopic2”. The group id is given in the 11th line. Consumers of the same group id will cooperate to read messages from the topic. The group id can be any string. The third rectangle marked in the following figure creates a consumer and subscribes it to the topic. Note, the consumer can subscribe to a set of topics. The poll function at the 23rd line reads messages from the topic. The fifth rectangle marks the code that prints the status and output of the consume function. The last box will end the consumer once **Ctrl-C** is pressed by the user that will trigger the **KeyboardInterrupt**.  

<img src="images/d8.jpg" alt="d8" width="500">  

## Simulating a Real Meter.
1.	Copy the files from **v2** folder from the GitHub repository.
2.	Edit **cred.json** as you did in the previous section.
3.	Edit **createTopic.py** to create a topic called **smartMeter** as you did in the previous section.
4.	Edit **consumer.py** to create a consumer that reads from **smartMeter** topic as you did in the previous section. Leave the file running such that you can consume the messages once they produced to the topic. The only difference in the message get decoded by the **json.loads()** function as the producer will send a JSON object instead of string.
5.	Edit **smartMeter.py** to create to produce smart meter measurements generated randomly. Update the topic name as before to **smartMeter**. The code looks like the same except the lines shown in the following figure. Lines from 12 to 18 have values that will be used to generate messages. Lines 33 till 54 are within a loop that will randomly generate messages that will be sent to the Kafka topic.  
<img src="images/e1.jpg" alt="e1" width="750">  

## Discussion
* What is EDA? What are its advantages and disadvantages?
* In Kafka, what’s meant by cluster, broker, topic, replica, partition, zookeeper, controller, leader, consumer, producer, and consumer group?

## Design
Google has an alternative ingestion tool called **Google Pub/sub**. Configure it and create a topic using Cloud interface. write a python code for a Google Pub/sub consumer and producer. The producer and the consumer should act as the smart meter shown before. **Note:** they needed a different library than that used for confluent kafka.

## Deliverables
1. A report that includes the discussion and the design parts. 
2. An audible video of about 3 minutes showing the smart meter using confluent cloud Kafka. 
3.  Another  audible  video  of about 5  minutes showing  the  design part. 
