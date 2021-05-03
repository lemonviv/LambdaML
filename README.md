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
* Abstract class Training - Implemented in GaSGD, MaSGD, ADMM **by 5/6**
  * Abstract class Communication - Implemented in SyncAllReduce, AsyncAllReduce, SyncScatterReduce, AsyncScatterReduce **by 4/30**
    * Abstract class Storage - Implemented in S3, Redis, Memcached **by 4/23**
      * Other AWS primitives that might be helpful (for example some code from `data_loader`)

### Goals
- It should be easy for anyone to add new implementations for each of the abstraction layers (Algorithm, Storage or Communication). For example, it would be ideal if you could add other cloud providers into any of the layers.
- For researchers: It should be possible to specify all of the parameters that might be interesting to other researchers (e.g. number of AWS Lambda instances, learning rate, convergence error range etc.)
- For other users: If you just want to get the best performance for your use case, it should not be many lines of code to use the library.
- At the end of the project, we should be able to run all of the experiments in the paper using the library APIs.
- Follow Liskov Substitution Principle and include type hinting to the exported functions
- Add integration tests, and check mypy in the integration test
- Add all of the nice checks into the readme, for example test coverage, following pep etc.
