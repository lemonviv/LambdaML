# LambdaML
Python library for doing serverless machine learning training (currently only on AWS).

## Project overview (deadline May 17th)
Design space:
* Distributed optimization algorithm
  * Gradient averaging in stochastic gradient descent (GA-SGD)
  * Model averaging in stochastic gradient descent (MA-SGD)
  * Alternating direction method of multipliers (ADMM)
* Communication channel (on AWS)
  * S3
  * Redis
  * Memcached
* Communication pattern
  * AllReduce
  * ScatterReduce
* Synchronization protocol
  * Synchronous
  * Asynchronous

## Design
Based on the results presented in the LambdaML paper, we select the default for the top level classes. However, the user of the library should be allowed to change these in order to perform the experiments themselves.
NOTE: Implementing the structures bottom -> top.
Class hierarchy (top to bottom):
* Abstract class Training - Implemented in GaSGD, MaSGD, ADMM
  * Abstract class Communication - Implemented in SyncAllReduce, AsyncAllReduce, SyncScatterReduce, AsyncScatterReduce
    * Abstract class Storage - Implemented in S3, Redis, Memcached
      * Other AWS primitives that might be helpful (for example some code from `data_loader`)
