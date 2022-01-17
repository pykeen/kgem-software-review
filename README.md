# Awesome Knowledge Graph Embedding Model Software [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

This list contains awesome code for knowledge graph embedding models (KGEMs).
It doesn't contain single model research repositories nor more general graph
machine learning packages like PyTorch-Geometric.

## Contents

1. [PyKEEN](#pykeen)
1. [AmpliGraph](#ampligraph)
1. [Pykg2vec](#pykg2vec)
1. [StellarGraph](#stellargraph)
1. [PyTorch-BigGraph](#pytorch-biggraph)
1. [Deep Graph Library](#deep-graph-library)
1. [Paddle Graph Learning](#paddle-graph-learning)
1. [Marius](#marius)
1. [GraphVite](#graphvite)
1. [LibKGE](#libkge)
1. [OpenKE](#openke)

## <a href="https://pykeen.github.io">PyKEEN</a> [![GitHub](https://img.shields.io/badge/GitHub-pykeen/pykeen-black?logo=github)](https://github.com/pykeen/pykeen) ![License](https://img.shields.io/github/license/pykeen/pykeen) [![Docs](https://img.shields.io/badge/Docs-available-green?logo=gitbook)](https://pykeen.readthedocs.io) [![CI](https://img.shields.io/badge/CI-github-green?logo=github)](https://github.com/pykeen/pykeen/actions/workflows/tests.yml)

PyKEEN is a PyTorch-based KGEM library for training and evaluation of knowledge graph embedding models. It is built with a modular architecture so the model, loss function, training loop, and other components can be used interchangably.

Citation:

> [PyKEEN 1.0: A Python Library for Training and Evaluating Knowledge Graph Embeddings](https://jmlr.org/papers/v22/20-825.html)
> <br />Mehdi Ali, Max Berrendorf, Charles Tapley Hoyt, Laurent Vermue, Sahand Sharifzadeh, Volker Tresp, and Jens Lehmann
> <br />*JMLR*, 2021

Installation ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pykeen) ![PyPI - Software Version](https://img.shields.io/pypi/v/pykeen)

```shell
$ pip install pykeen
```

## <a href="https://github.com/Accenture/AmpliGraph">AmpliGraph</a> [![GitHub](https://img.shields.io/badge/GitHub-Accenture/AmpliGraph-black?logo=github)](https://github.com/Accenture/AmpliGraph) ![License](https://img.shields.io/github/license/Accenture/AmpliGraph) [![Docs](https://img.shields.io/badge/Docs-available-green?logo=gitbook)](https://docs.ampligraph.org) [![CI](https://img.shields.io/badge/CI-CircleCI-green?logo=CircleCI)](https://app.circleci.com/pipelines/github/Accenture/AmpliGraph)

AmpliGraph is a suite of neural machine learning models for relational Learning, a branch of machine learning that deals with supervised learning on knowledge graphs.


Installation ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ampligraph) ![PyPI - Software Version](https://img.shields.io/pypi/v/ampligraph)

```shell
$ pip install ampligraph
```

## <a href="https://github.com/Sujit-O/pykg2vec">Pykg2vec</a> [![GitHub](https://img.shields.io/badge/GitHub-SujitO/pykg2vec-black?logo=github)](https://github.com/Sujit-O/pykg2vec) ![License](https://img.shields.io/github/license/Sujit-O/pykg2vec) [![Docs](https://img.shields.io/badge/Docs-available-green?logo=gitbook)](https://pykg2vec.readthedocs.io) [![CI](https://img.shields.io/badge/CI-CircleCI-green?logo=CircleCI)](https://app.circleci.com/pipelines/github/Sujit-O/pykg2vec)

Pykg2vec is a library for learning the representation of entities and relations in Knowledge Graphs built on top of PyTorch 1.5 (TF2 version is available in tf-master branch as well). It attempts to bring state-of-the-art knowledge graph embedding algorithms and the necessary building blocks in the pipeline of knowledge graph embedding task into a single library.

Citation:

> [Pykg2vec: A Python Library for Knowledge Graph Embedding](https://jmlr.org/papers/v22/19-433.html)
> <br />Shih-Yuan Yu, Sujit Rokka Chhetri, Arquimedes Canedo, Palash Goyal, and Mohammad Abdullah Al Faruque
> <br />*JMLR*, 2021

Installation ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pykg2vec) ![PyPI - Software Version](https://img.shields.io/pypi/v/pykg2vec)

```shell
$ pip install pykg2vec
```

## <a href="https://github.com/stellargraph/stellargraph">StellarGraph</a> [![GitHub](https://img.shields.io/badge/GitHub-stellargraph/stellargraph-black?logo=github)](https://github.com/stellargraph/stellargraph) ![License](https://img.shields.io/github/license/stellargraph/stellargraph) [![Docs](https://img.shields.io/badge/Docs-available-green?logo=gitbook)](https://stellargraph.readthedocs.io) [![CI](https://img.shields.io/badge/CI-GitHub-green?logo=GitHub)](https://github.com/stellargraph/stellargraph/actions/workflows/ci.yml)

The StellarGraph library offers state-of-the-art algorithms for graph machine learning, making it easy to discover patterns and answer questions about graph-structured data.


Installation ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/stellargraph) ![PyPI - Software Version](https://img.shields.io/pypi/v/stellargraph)

```shell
$ pip install stellargraph
```

## <a href="https://github.com/facebookresearch/PyTorch-BigGraph">PyTorch-BigGraph</a> [![GitHub](https://img.shields.io/badge/GitHub-facebookresearch/PyTorchBigGraph-black?logo=github)](https://github.com/facebookresearch/PyTorch-BigGraph) ![License](https://img.shields.io/github/license/facebookresearch/PyTorch-BigGraph) [![Docs](https://img.shields.io/badge/Docs-available-green?logo=gitbook)](https://torchbiggraph.readthedocs.io) [![CI](https://img.shields.io/badge/CI-CircleCI-green?logo=CircleCI)](https://app.circleci.com/pipelines/github/facebookresearch/PyTorch-BigGraph)

PyTorch-BigGraph (PBG) is a distributed system for learning graph embeddings for large graphs, particularly big web interaction graphs with up to billions of entities and trillions of edges.

Citation:

> [PyTorch-BigGraph: A Large-scale Graph Embedding Framework](https://mlsys.org/Conferences/2019/doc/2019/71.pdf)
> <br />Adam Lerer, Ledell Wu, Jiajun Shen, Timothee Lacroix, Luca Wehrstedt, Abhijit Bose, and Alex Peysakhovich
> <br />*Proceedings of the 2nd SysML Conference*, 2019

Installation ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/torchbiggraph) ![PyPI - Software Version](https://img.shields.io/pypi/v/torchbiggraph)

```shell
$ pip install torchbiggraph
```

## <a href="https://dgl.ai">Deep Graph Library</a> [![GitHub](https://img.shields.io/badge/GitHub-dmlc/dgl-black?logo=github)](https://github.com/dmlc/dgl) ![License](https://img.shields.io/github/license/dmlc/dgl) [![Docs](https://img.shields.io/badge/Docs-available-green?logo=gitbook)](https://docs.dgl.ai) [![CI](https://img.shields.io/badge/CI-Jenkins-green?logo=Jenkins)](https://ci.dgl.ai/job/DGL/job/master)

DGL is an easy-to-use, high performance and scalable Python package for deep learning on graphs. DGL is framework agnostic, meaning if a deep graph model is a component of an end-to-end application, the rest of the logics can be implemented in any major frameworks, such as PyTorch, Apache MXNet or TensorFlow.

Citation:

> [Deep Graph Library: A Graph-Centric, Highly-Performant Package for Graph Neural Networks](https://arxiv.org/abs/1909.01315)
> <br />Minjie Wang, Da Zheng, Zihao Ye, Quan Gan, Mufei Li, Xiang Song, Jinjing Zhou, Chao Ma, Lingfan Yu, Yu Gai, Tianjun Xiao, Tong He, George Karypis, Jinyang Li, and Zheng Zhang
> <br />*arXiv*, 2020

Installation ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dgl) ![PyPI - Software Version](https://img.shields.io/pypi/v/dgl)

```shell
$ pip install dgl
```

## <a href="https://github.com/PaddlePaddle/PGL">Paddle Graph Learning</a> [![GitHub](https://img.shields.io/badge/GitHub-PaddlePaddle/PGL-black?logo=github)](https://github.com/PaddlePaddle/PGL) ![License](https://img.shields.io/github/license/PaddlePaddle/PGL) [![Docs](https://img.shields.io/badge/Docs-available-green?logo=gitbook)](https://pgl.readthedocs.io) ![CI](https://img.shields.io/badge/CI-missing-red)

Paddle Graph Learning (PGL) is an efficient and flexible graph learning framework based on PaddlePaddle.


Installation ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pgl) ![PyPI - Software Version](https://img.shields.io/pypi/v/pgl)

```shell
$ pip install pgl
```

## <a href="https://marius-project.org">Marius</a> [![GitHub](https://img.shields.io/badge/GitHub-mariusteam/marius-black?logo=github)](https://github.com/marius-team/marius) ![License](https://img.shields.io/github/license/marius-team/marius) ![Docs](https://img.shields.io/badge/Docs-missing-red?logo=gitbook) [![CI](https://img.shields.io/badge/CI-github-green?logo=github)](https://github.com/marius-team/marius/actions/workflows/build_and_test.yml)

Marius is a system for large-scale graph learning that supports large-scale link prediction training, and preprocessing and training of datasets.

Citation:

> [Marius: Learning Massive Graph Embeddings on a Single Machine](https://www.usenix.org/conference/osdi21/presentation/mohoney)
> <br />Jason Mohoney, Roger Waleffe, Henry Xu, Theodoros Rekatsinas, and Shivaram Venkataraman
> <br />*OSDI*, 2021


Marius can't currently be installed directly from PyPI *via* `pip`. See its [installation docs](https://github.com/marius-team/marius#installation-from-source-with-pip) instead.

## <a href="https://graphvite.io">GraphVite</a> [![GitHub](https://img.shields.io/badge/GitHub-DeepGraphLearning/graphvite-black?logo=github)](https://github.com/DeepGraphLearning/graphvite) ![License](https://img.shields.io/github/license/DeepGraphLearning/graphvite) ![Docs](https://img.shields.io/badge/Docs-missing-red?logo=gitbook) ![CI](https://img.shields.io/badge/CI-missing-red)

GraphVite is a general and high-performance graph embedding system for various applications, designed for CPU-GPU hybrid architecture.

Citation:

> [GraphVite: A High-Performance CPU-GPU Hybrid System for Node Embedding](https://arxiv.org/abs/1903.00757)
> <br />Zhaocheng Zhu, Shizhen Xu, Meng Qu, and Jian Tang
> <br />*arXiv*, 2019


GraphVite can't currently be installed directly from PyPI *via* `pip`. See its [installation docs](https://github.com/DeepGraphLearning/graphvite#installation) instead.

## <a href="https://github.com/uma-pi1/kge">LibKGE</a> [![GitHub](https://img.shields.io/badge/GitHub-umapi1/kge-black?logo=github)](https://github.com/uma-pi1/kge) ![License](https://img.shields.io/github/license/uma-pi1/kge) ![Docs](https://img.shields.io/badge/Docs-missing-red?logo=gitbook) ![CI](https://img.shields.io/badge/CI-missing-red)

LibKGE is a PyTorch-based library for efficient training, evaluation, and hyperparameter optimization of knowledge graph embeddings.

Citation:

> [LibKGE - A knowledge graph embedding library for reproducible research](https://www.aclweb.org/anthology/2020.emnlp-demos.22)
> <br />Samuel Broscheit, Daniel Ruffinelli, Adrian Kochsiek, Patrick Betz, and Rainer Gemulla
> <br />*EMNLP*, 2020


LibKGE can't currently be installed directly from PyPI *via* `pip`. See its [installation docs](https://github.com/uma-pi1/kge#quick-start) instead.

## <a href="http://openke.thunlp.org">OpenKE</a> [![GitHub](https://img.shields.io/badge/GitHub-thunlp/OpenKE-black?logo=github)](https://github.com/thunlp/OpenKE) ![License](https://img.shields.io/github/license/thunlp/OpenKE) ![Docs](https://img.shields.io/badge/Docs-missing-red?logo=gitbook) ![CI](https://img.shields.io/badge/CI-missing-red)

OpenKE is an open-source framework for knowledge embedding organized by THUNLP based on the TensorFlow toolkit.

Citation:

> [OpenKE: An Open Toolkit for Knowledge Embedding](https://www.aclweb.org/anthology/D18-2024/)
> <br />Xu Han, Shulin Cao, Xin Lv, Yankai Lin, Zhiyuan Liu, Maosong Sun, and Juanzi Li
> <br />*EMNLP*, 2018


OpenKE can't currently be installed directly from PyPI *via* `pip`. See its [installation docs](https://github.com/thunlp/OpenKE#installation) instead.


## Footnotes

The full list can be downloaded in YAML
[here](https://raw.githubusercontent.com/pykeen/kgem-software-review/main/_data/software.yml).
