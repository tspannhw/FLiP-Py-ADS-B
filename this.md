Ingesting ADS-B Data From Antenna to Pulsar
===========================================

[Automatic Dependent Surveillance–Broadcast (ADS-B)](https://en.wikipedia.org/wiki/Automatic_Dependent_Surveillance%E2%80%93Broadcast)

[New Format Courtesy Dev Advocate Super Star, Ricardo](https://github.com/riferrei/is-using-kop-a-good-idea)

Requirements
------------

- [Docker](https://www.docker.com/get-started) 4.11+
- [Java](https://openjdk.org/install/) 17+
- [Maven](https://maven.apache.org/download.cgi) 3.8.6+
- [Python](https://www.python.org/downloads/release/python-390/) 3.7+
- [Apache Pulsar](https://pulsar.apache.org/download) 2.10.1+

🏢 Apache Pulsar Infrastructure
--------------------------------------

Before jumping into any of the scenarios, you must start the shared infrastructure all of them will use. 
This includes one Zookeeper instance, two Bookkeepers, and two Pulsar brokers.

1️⃣ Start the persistence layer

```bash
sh start-persistence.sh
```

👀 You must wait until the containers `zookeeper`, `persistence-bookie-1`, and `persistence-bookie-2` are healthy to proceed with the next step.

2️⃣ Start the Pulsar brokers with KoP enabled

```bash
sh start-brokers.sh
```

👀 You must wait until the containers `kafka-1` and `kafka-2` are healthy to proceed with any next step.

✅ Scenario: Raspberry Pi Runs ADS-B Services
-------------------------------------------------

This scenario checks two things. First, if KoP provides a truly Kafka-compatible API where third-party frameworks such as [Spring Boot](https://spring.io/projects/spring-boot) can connect with without deployment problems. Second, to check whether KoP is capable of mimic the distributed protocol from Kafka. Kafka is not just a one-directional typical client-server protocol. Instead, it is a bi-directional protocol where messages are exchanged from both parties. A good example is when a producer connects to the Kafka cluster using one bootstrap server endpoint, and the cluster keeps periodically updating that list back to the producer with metadata about the new cluster formation. Same for the consumer, which after joining a group, may be eventually removed by the cluster for the absence of valid heartbeats.

To validate this scenario, two Apache Pulsar brokers with KoP enabled will be executed, and the microservice will use the endpoint of only one broker to bootstrap the cluster. When everything is up-and-running and working as expected, the broker being used by the microservice will be killed, and the assumption is that the microservice should fallback to the other available broker, and continue its execution. If that ever happens, it means that the bootstrap worked as expected, giving the specifications of how Kafka manages clusters and sends this information to its clients.

1️⃣ Run the Spring Boot microservice

```bash
sh microservice-with-kafka/run-microservice.sh
```

👀 You must wait until the microservice connects with the brokers and start producing and consuming messages like this:

```console
org.summit.pulsar.demo.FiveSecondsTom : Hi, I'm Tom 😄
```

2️⃣ Find out which broker is the leader of the partition

```bash
$PULSAR_HOME/bin/pulsar-admin --admin-url http://localhost:8081 topics lookup persistent://public/default/fiveSecondsTomTopic
```

👀 Take a note of which broker shows up in this lookup.

3️⃣ Forcing a fail-over situation by killing the leader

```bash
sh kill-broker.sh <BROKER_CONTAINER_NAME_FROM_STEP_TWO>
```

👀 Observe the microservice for a couple minutes. It must continue its processing.

#️⃣ stop all containers if you're done for the day.

```bash
sh stop-everything.sh
```

Alternatively, you can also stop all containers if you're done for the day.

```bash
cd ..
sh stop-everything.sh
```

# License

This project is licensed under the [Apache 2.0 License](./LICENSE).
