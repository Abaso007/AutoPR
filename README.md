<div align="center">

# 🌳 AutoPR 🌳

[![Discord](https://badgen.net/badge/icon/discord?icon=nope&label&color=purple)](https://discord.gg/ykk7Znt3K6)
[![Docs](https://badgen.net/badge/icon/docs?icon=docs&label&color=blue)](https://docs.autopr.com)

Breathe life into your codebase, configurably  

</div>

## 🌟 Features

🌳 Living summaries of your code in nested READMEs
📄 Summarize changes by adding a "summarize" label to a PR  


... more coming soon!

## 🚀 Getting Started

Please see the [installation guide](https://docs.autopr.com/installing/github).

---

Below is an example of AutoPR's Living README:

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains files and folders related to an automated pull request workflow. It includes a Dockerfile for building a Docker image, a Makefile for defining commands and dependencies, an action.yml file for configuring a GitHub action, a folder containing scripts and modules for automating pull requests, a shell script for setting up Git and running the workflow, and configuration files for the project. There are also JSON schema files for defining workflow models and trigger configurations. Overall, the files and folders in this directory provide reusable components for building an autonomous agent system that automates the process of creating and managing pull requests based on specified triggers and workflows.


### [`Dockerfile`](https://github.com/raphael-francis/AutoPR-internal/blob/e36635316560c218f91e02e1d071753bb4162785/./Dockerfile)

🔧 Install git from bullseye-backports    
📝 Set up entrypoint    
📥 Copy pyproject.toml and poetry.lock    
📥 Copy the entire project    
🔧 Install project dependencies using poetry    
🏃‍♀️ Run the app using entrypoint.sh as the command  


### [`LICENSE.md`](https://github.com/raphael-francis/AutoPR-internal/blob/e36635316560c218f91e02e1d071753bb4162785/./LICENSE.md)

📄 This file contains the MIT License for software developed by Raphael Francis Ltd.  
🔒 The license grants permission to use, copy, modify, merge, publish, distribute, sublicense, and sell the software.  
📝 The license requires that the copyright notice and permission notice be included in all copies or substantial portions of the software.  
🔧 The software is provided "as is" without warranty of any kind.  
📚 The license is designed to protect the rights of the authors and copyright holders.  


### [`Makefile`](https://github.com/raphael-francis/AutoPR-internal/blob/e36635316560c218f91e02e1d071753bb4162785/./Makefile)

📋 The file defines a set of commands and their dependencies.       
🔧 The `format` command runs the `black` code formatter on the project.       
📝 The `type` command runs the `pyright` static type checker on the project.       
🧪 The `test` command runs the `pytest` test suite for the `autopr` module.       
🔧 The `schema` command runs the `python` interpreter with the `autopr.models.config.entrypoints` module.       
🚀 The `all` command runs all the commands in the specified order.       


### [`action.yml`](https://github.com/raphael-francis/AutoPR-internal/blob/e36635316560c218f91e02e1d071753bb4162785/./action.yml)

📋 This file defines the configuration for an "Automatic Pull Request" action.   
🔧 It specifies the details of how the action should run, including using Docker and the Docker image to use.  
🎨 It also defines the branding for the action, including the icon and color to use.  
🔑 The file outlines the required inputs for the action, such as the GitHub token and base branch.  
🔄 It provides default values for optional inputs, such as the loading GIF URL and target branch name template.  
✍️ Additionally, it includes a flag to control whether to overwrite existing branches and pull requests.  


### [`autopr/`](https://github.com/raphael-francis/AutoPR-internal/blob/e36635316560c218f91e02e1d071753bb4162785/./autopr)

This folder contains a collection of files and folders that implement an automated pull request workflow. It includes scripts and modules for running various actions and utilities, defining triggers and workflows, managing services and classes, configuring logging, and defining models for automation and configuration management. The purpose of these files is to provide reusable components for building an autonomous agent system that automates the process of creating and managing pull requests based on specified triggers and workflows.  


### [`entrypoint.sh`](https://github.com/raphael-francis/AutoPR-internal/blob/e36635316560c218f91e02e1d071753bb4162785/./entrypoint.sh)

📝 This file is a shell script.  
🔧 It sets the global configuration for Git.  
📧 It sets the email address for the Git user.  
👤 It sets the name for the Git user.  
📁 It sets the safe directory for Git.  
🔌 It activates a virtual environment.  
🐍 It runs a Python module called autopr.gh_actions_entrypoint.  


### [`poetry.lock`](https://github.com/raphael-francis/AutoPR-internal/blob/e36635316560c218f91e02e1d071753bb4162785/./poetry.lock)

📄 This file is intended to serve as an executive summary.  
🔍 It provides a high-level overview of the contents of the document.  
📑 The purpose of this file is to give a concise understanding of the document's main points.  
🧐 It is designed for someone seeing the document for the first time.  
👀 It highlights the key objectives and outcomes.  
💡 It does not explain trivial details or imports.  
📝 It is brief, especially if the file is empty.  
💼 It helps the reader quickly grasp the document's purpose.  
📊 It provides a snapshot of the document's contents.  
📝 It serves as a guide for further exploration of the document.  


### [`pyproject.toml`](https://github.com/raphael-francis/AutoPR-internal/blob/e36635316560c218f91e02e1d071753bb4162785/./pyproject.toml)

📝 The file is a configuration file for the project "autopr"  
📦 It uses Poetry as the package manager for the project  
🔑 The project is licensed under the MIT license  
📚 The file specifies the dependencies required for the project, including Python, Pydantic, GitPython, and more  
🧪 There is a separate group for test dependencies, which includes Pytest and Aioresponses  
🛠️ There is a separate group for development dependencies, which includes Black  
🔧 The file also includes configuration settings for Pyright and Black  
🔒 The "build-system" section specifies the requirements for building the project  
🗒️ The "tool.black" section sets the line length and target version for the Black formatter  


### [`strict_workflow_schema.json`](https://github.com/raphael-francis/AutoPR-internal/blob/e36635316560c218f91e02e1d071753bb4162785/./strict_workflow_schema.json)

📋 The file contains a JSON schema definition for a workflow model.  
💡 It defines various types of actions that can be performed in a workflow.  
🔢 The actions include commenting, setting issue titles, crawling folders, making API calls, running bash commands, and more.  
📝 Each action has its own set of inputs and outputs.  
🌐 The schema also defines different types of declarations, such as templates, variables, constants, and lambdas.  
🔀 There are multiple types of workflow invocations and conditional statements.  
🗂️ The schema includes definitions for different types of workflows, including strict workflows and iterable workflows.  
📝 Workflows can have inputs, outputs, and a series of steps that can include actions, workflow invocations, and conditional statements.  
📚 The purpose of this file is to provide a structured definition for building and executing workflows.  


### [`trigger_schema.json`](https://github.com/raphael-francis/AutoPR-internal/blob/e36635316560c218f91e02e1d071753bb4162785/./trigger_schema.json)

📋 This file is a JSON schema that defines the structure and properties of a workflow trigger configuration.  
🔗 It contains definitions for various types of triggers, such as label, comment, push, and cron triggers.  
📝 Each trigger type has its own properties and requirements.  
💼 The purpose of this file is to provide a standardized format for defining triggers in a workflow configuration.  
🖥️ It can be used by workflow automation tools to validate and enforce the structure of trigger configurations.  
💡 The file also includes definitions for various action models, which can be used in conjunction with triggers to define workflow actions.  
❓ The file allows for flexibility in defining the inputs and outputs of each action.  
🧩 Overall, this file serves as a blueprint for creating and configuring triggers and actions in a workflow automation system.  


### [`workflow_schema.json`](https://github.com/raphael-francis/AutoPR-internal/blob/e36635316560c218f91e02e1d071753bb4162785/./workflow_schema.json)

📋 This file is a JSON schema that defines a workflow definition.  
🔢 It includes definitions for various types of actions that can be performed within the workflow.  
📝 Each action has its own model with properties such as name, description, and inputs.  
🔄 The workflow definition itself consists of a name, description, inputs, outputs, and a list of steps.  
💼 Steps can be strings, actions, workflow invocations, or conditional statements.  
🔀 Conditional statements can be based on a Python lambda expression.  
🔁 Workflows can be iterative, allowing for looping over a set of actions.  
🗃️ The file also includes definitions for various types of declarations used within the actions.  
📄 The purpose of this file is to provide a standardized structure for defining and executing workflows.  

<!-- Living README Summary -->