# CKA Notes

Studying for the CKA exam, wanted to keep some notes I found helpful that I
might polish up later for others to enjoy. These include analogies,
visualizations, explanations, etc.

## Master / Control Plane (cp)

### Cluster Store

* Key/value store for cluster
* Stores current state
* Typically etcd

### Controller vs Controller Manager

* Controller - keeps asking the same question to its appropriate subordinate
resources. Think "mum?" gif from Family Guy. Controller runs in infinite
control loops.
* Controller Manager - keeps track of changes in responses received by
controllers and communicates changes to apiserver. Helps maintain desired
state.

### Scheduler

* Watches apiserver for new pods
* Assigns work to nodes based on availability
* Respects constraints

### API Server

* RESTful
* Single, central intermediary for all other cp services

## Nodes (Workers/Minions)

### kubelet

* Main k8s agent inside a node, must run as long as node runs
* Watches API server
* Instantiates pods
* Reports back to master
* Exposes endpoint on port 10255

### Container Engine

* Manages containers (pulling images, starting/stopping containers)
* Usually Docker, can be others

### kube-proxy



# If Kubernetes were a person (stage crew)

Cast
----

* K8s admin = stage director
* 


_Admin_: [finishes writing a letter] Done. [Hands letter to _API server_]

_API Server_: [reads letter, ]

_Controllers_: 



# Replication Controllers

Ensures specified number of pods are running

