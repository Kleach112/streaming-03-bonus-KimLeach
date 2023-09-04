# streaming-03-bonus-KimLeach

**Date:** September 4, 2023

## Introduction

This repository contains a custom streaming project that demonstrates the use of producers and consumers to process data in real-time. The project is named "streaming-03-bonus-KimLeach"

## Original Data

The original data used in this project can be found [here]([link-to-original-data](https://data.world/carmichael/mavenmagicchallenge/workspace/file?filename=Characters.xlsx)).

## Project Overview

In this project, I created two main components:

### Producer

- The producer reads data from an original CSV file.
- It generates messages from the CSV data and sends them to a RabbitMQ queue.
- Messages are generated and sent every 1-3 seconds to simulate real-time data transmission.

### Consumer

- The consumer continuously listens to the RabbitMQ queue for incoming messages.
- As messages arrive, the consumer writes them to a new file in real-time.
