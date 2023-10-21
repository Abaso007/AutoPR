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

This folder contains various files and directories related to a Python project. It includes a Dockerfile for setting up the project environment, a license file specifying permissions and terms of use, a Makefile for running different tasks, an action configuration file for GitHub Actions, a folder with diverse automation functionalities, a shell script for configuring Git, lock and configuration files for project dependencies, JSON schemas for defining workflows and triggers, and other supporting files. These files and directories are essential for building, testing, automating, and managing the project.


### [`Dockerfile`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./Dockerfile/)

🔧 Install git from bullseye-backports  
📝 Set up entrypoint  
📥 Copy pyproject.toml and poetry.lock  
📥 Copy the entire project  
🔧 Install project dependencies using poetry  
🏃‍♀️ Run the app using entrypoint.sh as the command


### [`LICENSE.md`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./LICENSE.md/)

📄 This file contains the MIT License for software developed by Raphael Francis Ltd.
🔒 The license grants permission to use, copy, modify, merge, publish, distribute, sublicense, and sell the software.
📝 The license requires that the copyright notice and permission notice be included in all copies or substantial portions of the software.
🔧 The software is provided "as is" without warranty of any kind.
📚 The license is designed to protect the rights of the authors and copyright holders.



### [`Makefile`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./Makefile/)

📝 This file defines several targets for a Python project    
🎯 `type` target runs static type checking using Pyright    
🧪 `test` target runs unit tests using pytest    
📋 `schema` target runs a command to generate schema for the project    
🔀 `all` target combines type, test, and schema targets    
🔧 The purpose of this file is to provide a convenient way to run different tasks in the project    
🐍 The file may be used as a Makefile or a task runner for the project    
💡 It is recommended to read the documentation or comments in the file for more details    
✅ The file is easy to understand and modify    
💻 This file is an important part of the project's build and development process


### [`action.yml`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./action.yml/)

📋 This file defines the configuration for an "Automatic Pull Request" action. 
🔧 It specifies the details of how the action should run, including using Docker and the Docker image to use.
🎨 It also defines the branding for the action, including the icon and color to use.
🔑 The file outlines the required inputs for the action, such as the GitHub token and base branch.
🔄 It provides default values for optional inputs, such as the loading GIF URL and target branch name template.
✍️ Additionally, it includes a flag to control whether to overwrite existing branches and pull requests.



### [`autopr/`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/)

This folder contains a diverse set of functionalities and actions that can be used in various automation tasks. It includes Python files for managing autonomous agent systems, performing tasks, making API calls, running bash commands, generating prompts, reading and writing files, and searching directories. There are also files for configuring and running GitHub Actions workflows, handling logging, and defining services and classes for managing actions, caching, commits, diffs, platforms, publishing, triggers, utilities, and workflows. Additionally, there are files for defining data models, event classes, and executable actions for an AutoPR system. Overall, this folder provides a range of tools and components for building and automating processes.


### [`entrypoint.sh`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./entrypoint.sh/)

📝 This file is a shell script.
🔧 It sets the global configuration for Git.
📧 It sets the email address for the Git user.
👤 It sets the name for the Git user.
📁 It sets the safe directory for Git.
🔌 It activates a virtual environment.
🐍 It runs a Python module called autopr.gh_actions_entrypoint.


### [`poetry.lock`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./poetry.lock/)

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


### [`pyproject.toml`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./pyproject.toml/)

📋 This file is a configuration file for a Python project using Poetry as a dependency management tool. 
📦 It specifies the project name, version, authors, license, and packages to include.
🔧 It defines the dependencies required for the project, including Python version and various libraries.
🔬 There is a separate section for test dependencies.
🛠️ The file also includes configuration for the build system and Pyright, a static type checker for Python.



### [`strict_workflow_schema.json`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./strict_workflow_schema.json/)

📋 This file is a JSON schema that defines the structure and properties of a workflow definition.
🔢 It includes various action models that can be used in the workflow, such as commenting, crawling folders, making API calls, running bash commands, and more.
🧩 The workflow definition consists of a series of steps, each containing one or more actions or sub-workflows.
🔀 Conditional logic can be added using If statements based on Python lambda expressions.
📥 The definition can have inputs and outputs, which are arrays of strings representing the variables used in the workflow.
📝 Each action model has specific properties and inputs required for its execution.
🔗 References to other definitions are used to reuse common properties and structures.
📄 The file also includes definitions for templates, variables, constants, and lambda expressions used within the actions.
📖 This JSON schema serves as a blueprint for creating and validating workflows in a specific format.


### [`trigger_schema.json`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./trigger_schema.json/)

📝 This file is a JSON schema definition.
📝 It defines a data structure for a trigger configuration.
📝 The trigger configuration includes various types of triggers such as label, comment, push, and cron triggers.
📝 Each trigger type is defined with its own properties and actions.
📝 Actions include various tasks such as commenting, setting issue title, crawling folders, making API calls, running bash commands, and more.
📝 The file also defines different models for each action type, specifying their properties and required inputs.
📝 The trigger configuration can have multiple triggers, each with its own set of actions.
📝 The file also includes definitions for various parameter types such as templates, variables, constants, and lambda expressions.
📝 The purpose of this file is to provide a standardized schema for defining trigger configurations in a workflow automation system.
📝 The schema can be used to validate and enforce the structure of trigger configurations in order to ensure consistency and correctness.


### [`workflow_schema.json`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./workflow_schema.json/)

📄 The file contains a JSON schema for defining workflows.
🔢 It includes various definitions for different types of actions that can be performed in a workflow.
📝 Each action has its own set of properties and can be used to perform specific tasks.
🔄 The workflow definition includes a list of steps, which can be a combination of actions, workflow invocations, and conditional statements.
🔀 Conditional statements can be used to control the flow of the workflow based on certain conditions.
🔢 Inputs and outputs can be defined for the overall workflow and individual actions.
🔍 The purpose of this file is to provide a standardized way to define and execute workflows.
💻 It can be used in automation or orchestration systems to automate complex tasks or processes.
📚 The file also includes descriptions and additional properties for each definition, providing more context and guidance for users.
📝 The schema can be used to validate and enforce the structure and properties of workflow definitions.

<!-- Living README Summary -->