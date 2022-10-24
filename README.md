# Causal-Inference
Logistic optimization: Delivery drivers location optimization with Causal Inference

**Table of Contents**

- [Causal-Inference](#Causal-Inference)
  - [Overview](#overview)
  - [About](#about)
  - [Project Structure](#project-structure)
    - [.dvc](#.dvc)
    - [.github](#.github)
    - [data](#data)
    - [notebooks](#notebooks)
    - [scripts](#scripts)
    - [tests](#tests)
    - [root folder](#root-folder)

***

## Overview

This repository is used for week 9 challenge of 10Academy. The instructions for this project can be found in the challenge document.

Causal inference is the process of determining the independent, actual effect of a particular phenomenon that is a component of a larger system. The main difference between causal inference and inference of association is that causal inference analyzes the response of an effect variable when the cause of the effect variable is changed. The science of why things occur is called etiology. Causal inference is said to provide evidence of causality theorized by causal reasoning.

![Alt text](img2.png?raw=true "Causal Overview")

## About

The client for this week's challenge is Gokada, work on its data to help it
understand the primary causes of unfulfilled requests as well as come up with
solutions that recommend drivers locations that increase the fraction of
complete orders. Since drivers are paid based on the number of requests they
accept, your solution will help Gokada business grow both in terms of client
satisfaction and increased business.

![Alt text](img1.png?raw=true "Graph")

## Project Structure
The repository has a number of files including python scripts, jupyter notebooks, raw and cleaned data, and text files. Here is their structure with a brief explanation.


### .dvc
- Data Version Control configurations

### .github
- a configuration file for github actions and workflow
- `workflows/CML.yml` continous machine learning configuration

### data
- the folder where the raw, and cleaned datasets' csv files are stored

### notebooks
- `EDA.ipynb`: a jupyter notebook that Explanatory Data Analysis


### scripts
- Different python utility scripts that have different purposes.


### tests


### root folder
- `requirements.txt`: a text file lsiting the projet's dependancies
- `.gitignore`: a text file listing files and folders to be ignored
- `README.md`: Markdown text with a brief explanation of the project and the repository structure.


***

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]


[contributors-shield]: https://img.shields.io/github/contributors/natyrix/Causal-Inference.svg?style=for-the-badge
[contributors-url]: https://github.com/natyrix/Causal-Inference/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/natyrix/Causal-Inference.svg?style=for-the-badge
[forks-url]: https://github.com/natyrix/Causal-Inference/network/members
[stars-shield]: https://img.shields.io/github/stars/natyrix/Causal-Inference.svg?style=for-the-badge
[stars-url]: https://github.com/natyrix/Causal-Inference/stargazers
[issues-shield]: https://img.shields.io/github/issues/natyrix/Causal-Inference.svg?style=for-the-badge
[issues-url]: https://github.com/natyrix/Causal-Inference/issues
