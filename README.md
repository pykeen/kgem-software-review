# Awesome Knowledge Graph Embedding Model Software [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

This list contains awesome code for knowledge graph embedding models (KGEMs).
It doesn't contain single model research repositories nor more general graph
machine learning packages like PyTorch-Geometric.

## Contents

1. [PyKEEN](#pykeen)
2. [AmpliGraph](#ampligraph)
3. [Pykg2vec](#pykg2vec)
4. [StellarGraph](#stellargraph)
5. [PyTorch-BigGraph](#pytorch-biggraph)
6. [Deep Graph Library](#deep-graph-library)
7. [Paddle Graph Learning](#paddle-graph-learning)
8. [CogKGE](#cogkge)
9. [Marius](#marius)
10. [GraphVite](#graphvite)
11. [LibKGE](#libkge)
12. [OpenKE](#openke)
13. [μKG](#μkg)

## PyKEEN

[![GitHub](https://img.shields.io/badge/GitHub-pykeen/pykeen-black?logo=github)](https://github.com/pykeen/pykeen) [![Docs](https://img.shields.io/badge/Homepage-black?logo=HomeAdvisor)](https://pykeen.github.io) [![Docs](https://img.shields.io/badge/Docs-black?logo=gitbook)](https://pykeen.readthedocs.io)

PyKEEN is a PyTorch-based KGEM library for training and evaluation of knowledge graph embedding models. It is built with a modular architecture so the model, loss function, training loop, and other components can be used interchangably.

> [PyKEEN 1.0: A Python Library for Training and Evaluating Knowledge Graph Embeddings](https://jmlr.org/papers/v22/20-825.html)
> <br />Mehdi Ali, Max Berrendorf, Charles Tapley Hoyt, Laurent Vermue, Sahand Sharifzadeh, Volker Tresp, and Jens Lehmann
> <br />*JMLR*, 2021

Install with:

```shell
$ pip install pykeen
```

## AmpliGraph

[![GitHub](https://img.shields.io/badge/GitHub-Accenture/AmpliGraph-black?logo=github)](https://github.com/Accenture/AmpliGraph)  [![Docs](https://img.shields.io/badge/Docs-black?logo=gitbook)](https://docs.ampligraph.org)

AmpliGraph is a suite of neural machine learning models for relational Learning, a branch of machine learning that deals with supervised learning on knowledge graphs.


Install with:

```shell
$ pip install ampligraph
```

## Pykg2vec

[![GitHub](https://img.shields.io/badge/GitHub-SujitO/pykg2vec-black?logo=github)](https://github.com/Sujit-O/pykg2vec)  [![Docs](https://img.shields.io/badge/Docs-black?logo=gitbook)](https://pykg2vec.readthedocs.io)

Pykg2vec is a library for learning the representation of entities and relations in Knowledge Graphs built on top of PyTorch 1.5 (TF2 version is available in tf-master branch as well). It attempts to bring state-of-the-art knowledge graph embedding algorithms and the necessary building blocks in the pipeline of knowledge graph embedding task into a single library.

> [Pykg2vec: A Python Library for Knowledge Graph Embedding](https://jmlr.org/papers/v22/19-433.html)
> <br />Shih-Yuan Yu, Sujit Rokka Chhetri, Arquimedes Canedo, Palash Goyal, and Mohammad Abdullah Al Faruque
> <br />*JMLR*, 2021

Install with:

```shell
$ pip install pykg2vec
```

## StellarGraph

[![GitHub](https://img.shields.io/badge/GitHub-stellargraph/stellargraph-black?logo=github)](https://github.com/stellargraph/stellargraph)  [![Docs](https://img.shields.io/badge/Docs-black?logo=gitbook)](https://stellargraph.readthedocs.io)

The StellarGraph library offers state-of-the-art algorithms for graph machine learning, making it easy to discover patterns and answer questions about graph-structured data.


Install with:

```shell
$ pip install stellargraph
```

## PyTorch-BigGraph

[![GitHub](https://img.shields.io/badge/GitHub-facebookresearch/PyTorchBigGraph-black?logo=github)](https://github.com/facebookresearch/PyTorch-BigGraph)  [![Docs](https://img.shields.io/badge/Docs-black?logo=gitbook)](https://torchbiggraph.readthedocs.io)

PyTorch-BigGraph (PBG) is a distributed system for learning graph embeddings for large graphs, particularly big web interaction graphs with up to billions of entities and trillions of edges.

> [PyTorch-BigGraph: A Large-scale Graph Embedding Framework](https://mlsys.org/Conferences/2019/doc/2019/71.pdf)
> <br />Adam Lerer, Ledell Wu, Jiajun Shen, Timothee Lacroix, Luca Wehrstedt, Abhijit Bose, and Alex Peysakhovich
> <br />*Proceedings of the 2nd SysML Conference*, 2019

Install with:

```shell
$ pip install torchbiggraph
```

## Deep Graph Library

[![GitHub](https://img.shields.io/badge/GitHub-dmlc/dgl-black?logo=github)](https://github.com/dmlc/dgl) [![Docs](https://img.shields.io/badge/Homepage-black?logo=HomeAdvisor)](https://dgl.ai) [![Docs](https://img.shields.io/badge/Docs-black?logo=gitbook)](https://docs.dgl.ai)

DGL is an easy-to-use, high performance and scalable Python package for deep learning on graphs. DGL is framework agnostic, meaning if a deep graph model is a component of an end-to-end application, the rest of the logics can be implemented in any major frameworks, such as PyTorch, Apache MXNet or TensorFlow.

> [Deep Graph Library: A Graph-Centric, Highly-Performant Package for Graph Neural Networks](https://arxiv.org/abs/1909.01315)
> <br />Minjie Wang, Da Zheng, Zihao Ye, Quan Gan, Mufei Li, Xiang Song, Jinjing Zhou, Chao Ma, Lingfan Yu, Yu Gai, Tianjun Xiao, Tong He, George Karypis, Jinyang Li, and Zheng Zhang
> <br />*arXiv*, 2020

Install with:

```shell
$ pip install dgl
```

## Paddle Graph Learning

[![GitHub](https://img.shields.io/badge/GitHub-PaddlePaddle/PGL-black?logo=github)](https://github.com/PaddlePaddle/PGL)  [![Docs](https://img.shields.io/badge/Docs-black?logo=gitbook)](https://pgl.readthedocs.io)

Paddle Graph Learning (PGL) is an efficient and flexible graph learning framework based on PaddlePaddle.


Install with:

```shell
$ pip install pgl
```

## CogKGE

[![GitHub](https://img.shields.io/badge/GitHub-jinzhuoran/CogKGE-black?logo=github)](https://github.com/jinzhuoran/CogKGE) [![Docs](https://img.shields.io/badge/Homepage-black?logo=HomeAdvisor)](http://cognlp.com/cogkge) 

A Knowledge Graph Embedding Toolkit and Benckmark for Representing Multi-source and Heterogeneous Knowledge

> [CogKGE: A Knowledge Graph Embedding Toolkit and Benchmark for Representing Multi-source and Heterogeneous Knowledge](https://aclanthology.org/2022.acl-demo.16/)
> <br />Zhuoran Jin, Tianyi Men, Hongbang Yuan, Zhitao He, Dianbo Sui, Chenhao Wang, Zhipeng Xue, Yubo Chen, Jun Zhao
> <br />*ACL*, 2022

Install with:

```shell
$ pip install cogkge
```

## Marius

[![GitHub](https://img.shields.io/badge/GitHub-mariusteam/marius-black?logo=github)](https://github.com/marius-team/marius) [![Docs](https://img.shields.io/badge/Homepage-black?logo=HomeAdvisor)](https://marius-project.org) 

Marius is a system for large-scale graph learning that supports large-scale link prediction training, and preprocessing and training of datasets.

> [Marius: Learning Massive Graph Embeddings on a Single Machine](https://www.usenix.org/conference/osdi21/presentation/mohoney)
> <br />Jason Mohoney, Roger Waleffe, Henry Xu, Theodoros Rekatsinas, and Shivaram Venkataraman
> <br />*OSDI*, 2021


Marius can't currently be installed directly from PyPI *via* `pip`. See its [installation docs](https://github.com/marius-team/marius#build-and-install) instead.

## GraphVite

[![GitHub](https://img.shields.io/badge/GitHub-DeepGraphLearning/graphvite-black?logo=github)](https://github.com/DeepGraphLearning/graphvite) [![Docs](https://img.shields.io/badge/Homepage-black?logo=HomeAdvisor)](https://graphvite.io) 

GraphVite is a general and high-performance graph embedding system for various applications, designed for CPU-GPU hybrid architecture.

> [GraphVite: A High-Performance CPU-GPU Hybrid System for Node Embedding](https://arxiv.org/abs/1903.00757)
> <br />Zhaocheng Zhu, Shizhen Xu, Meng Qu, and Jian Tang
> <br />*arXiv*, 2019


GraphVite can't currently be installed directly from PyPI *via* `pip`. See its [installation docs](https://github.com/DeepGraphLearning/graphvite#installation) instead.

## LibKGE

[![GitHub](https://img.shields.io/badge/GitHub-umapi1/kge-black?logo=github)](https://github.com/uma-pi1/kge)  

LibKGE is a PyTorch-based library for efficient training, evaluation, and hyperparameter optimization of knowledge graph embeddings.

> [LibKGE - A knowledge graph embedding library for reproducible research](https://www.aclweb.org/anthology/2020.emnlp-demos.22)
> <br />Samuel Broscheit, Daniel Ruffinelli, Adrian Kochsiek, Patrick Betz, and Rainer Gemulla
> <br />*EMNLP*, 2020


LibKGE can't currently be installed directly from PyPI *via* `pip`. See its [installation docs](https://github.com/uma-pi1/kge#quick-start) instead.

## OpenKE

[![GitHub](https://img.shields.io/badge/GitHub-thunlp/OpenKE-black?logo=github)](https://github.com/thunlp/OpenKE) [![Docs](https://img.shields.io/badge/Homepage-black?logo=HomeAdvisor)](http://openke.thunlp.org) 

OpenKE is an open-source framework for knowledge embedding organized by THUNLP based on the TensorFlow toolkit.

> [OpenKE: An Open Toolkit for Knowledge Embedding](https://www.aclweb.org/anthology/D18-2024/)
> <br />Xu Han, Shulin Cao, Xin Lv, Yankai Lin, Zhiyuan Liu, Maosong Sun, and Juanzi Li
> <br />*EMNLP*, 2018


OpenKE can't currently be installed directly from PyPI *via* `pip`. See its [installation docs](https://github.com/thunlp/OpenKE#installation) instead.

## μKG

[![GitHub](https://img.shields.io/badge/GitHub-njuwebsoft/muKG-black?logo=github)](https://github.com/nju-websoft/muKG)  



> **Warning**
> <strong>This manuscript is not yet publicly available</strong>
> <br />μKG: A Library for Multi-source Knowledge Graph Embeddings and Applications
> <br />Xindi Luo, Zequn Sun, Wei Hu
> <br />*ISWC*, 2022


μKG can't currently be installed directly from PyPI *via* `pip`. See its [installation docs](https://github.com/nju-websoft/muKG#getting-started-) instead.


## Footnotes

The full list can be downloaded in YAML
[here](https://raw.githubusercontent.com/pykeen/kgem-software-review/main/_data/software.yml).
