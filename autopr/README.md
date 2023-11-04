

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains a collection of Python files and folders that implement various actions, services, and workflows for an autonomous agent system. The files define classes and functions for actions such as running commands, publishing comments, and committing changes. The folders contain code for managing triggers, executing workflows, and defining data models. Overall, this folder provides a range of reusable actions and services that can be used to automate processes or scripts.


### [`__init__.py`](https://github.com/raphael-francis/AutoPR-internal/blob/3bf8a4d34accd718d73d2e505656ba2ec3df1e98/./autopr/__init__.py)

This file is empty.  


### [`actions/`](https://github.com/raphael-francis/AutoPR-internal/blob/3bf8a4d34accd718d73d2e505656ba2ec3df1e98/./autopr/actions)

This folder contains a collection of Python files that implement various actions for an autonomous agent system. Each file represents a different action, such as running a bash command, generating choices, publishing comments on GitHub issues, committing and pushing changes to a remote repository, and more. The files define classes that encapsulate the logic for each action, and they often include input and output models for data validation. Additionally, there are utility files for managing prompt context, listing files and subfolders, and performing file operations like reading and writing. Overall, this folder provides a range of reusable actions that can be used in automated processes or scripts.  


### [`gh_actions_entrypoint.py`](https://github.com/raphael-francis/AutoPR-internal/blob/3bf8a4d34accd718d73d2e505656ba2ec3df1e98/./autopr/gh_actions_entrypoint.py)

📄 This file is the entry point for a GitHub Actions workflow.   
🔧 It contains the main logic for running the workflow.  
🔒 It retrieves settings and authentication tokens from environment variables.  
📥 It loads and parses the event data from a JSON file.  
🚀 It initializes and runs the main service for the GitHub Actions workflow.  
📝 It uses classes and methods from the "autopr" module to handle the workflow.  
⚙️ The purpose of this file is to orchestrate the execution of the workflow.  
🔗 It connects different services, such as the platform service and the publish service.  
🔄 It interacts with the GitHub API to perform actions on the repository.  
🔒 The GitHub token is used for authentication and authorization.  


### [`log_config.py`](https://github.com/raphael-francis/AutoPR-internal/blob/3bf8a4d34accd718d73d2e505656ba2ec3df1e98/./autopr/log_config.py)

📝 This file is used to configure logging settings and create loggers.   
🔧 It imports the necessary modules for logging and structlog.   
🔒 The logging level is set to DEBUG.   
🎨 If the "pretty" flag is True, additional processors are added for log level, exception info, and console rendering with colors.   
🔧 Otherwise, no processors are added.   
🔧 The structlog is configured with the chosen processors and the logger is cached on first use.   
📝 The file also includes a function to get a logger instance.   
🔧 The configure_logging function is called to configure logging on module import.  


### [`main.py`](https://github.com/raphael-francis/AutoPR-internal/blob/3bf8a4d34accd718d73d2e505656ba2ec3df1e98/./autopr/main.py)

📋 This file contains the implementation of the `MainService` class, which serves as the main entry point for the application.   
🔧 It initializes various services and handles the execution of triggers and workflows.  
📦 It also defines the `Settings` class for storing configuration settings.  
🔍 The `MainService` class retrieves repository information, creates necessary services, and runs triggers based on events.  
✨ Triggers are defined in the `triggers` module, and workflows are defined in the `workflows` module.  
🚀 The `run` method of the `MainService` class triggers the event and executes the associated workflows.  
🌐 The platform-specific functionality is encapsulated in the `PlatformService` class.  
💻 The `ActionService` class handles actions to be performed based on triggers.  
📝 The `CommitService` class manages commits to the repository.  
🔗 The `TriggerService` class handles the interaction between triggers, workflows, and the commit service.  


### [`models/`](https://github.com/raphael-francis/AutoPR-internal/blob/3bf8a4d34accd718d73d2e505656ba2ec3df1e98/./autopr/models)

This folder contains Python code and configuration files for building and executing workflows in the AutoPR system. It includes files for defining data models related to messages, threads, issues, and pull requests, as well as files for handling events, context variables, templates, and executables. The folder provides the framework and tools for defining, executing, and managing workflows with customizable actions and context variables.  


### [`services/`](https://github.com/raphael-francis/AutoPR-internal/blob/3bf8a4d34accd718d73d2e505656ba2ec3df1e98/./autopr/services)

This folder contains multiple Python files that implement various services and classes related to automating pull request workflows. These files provide functionality for managing and running actions, caching data, interacting with Git repositories, getting and applying diffs, making API calls to platforms like GitHub, publishing updates to pull request descriptions, handling triggers and executing workflows, and formatting and truncating data for publishing. The files are well-documented and include comments explaining the purpose and functionality of each class and method.  


### [`triggers.py`](https://github.com/raphael-francis/AutoPR-internal/blob/3bf8a4d34accd718d73d2e505656ba2ec3df1e98/./autopr/triggers.py)

📄 This file defines a function called `get_all_triggers`.  
📂 It imports necessary modules and classes.  
💡 The purpose of this function is to retrieve all trigger configurations from specified files.  
🗂️ It searches for trigger configurations in a given directory.  
🔍 The function looks for trigger configurations in both YAML and YML file formats.  
📝 It reads the contents of the trigger configuration files.  
🧪 The function validates and parses the trigger configurations using Pydantic.  
🔀 It extracts the triggers from the parsed configurations.  
🔄 The function returns a list of all triggers found in the trigger configuration files.  
📥 The function takes optional parameters for the configuration directory and repository path.  


### [`workflows/`](https://github.com/raphael-francis/AutoPR-internal/blob/3bf8a4d34accd718d73d2e505656ba2ec3df1e98/./autopr/workflows)

This folder contains a collection of Python scripts and YAML files that define various workflows. The scripts are responsible for loading and validating workflow configurations from YAML files, while the YAML files define different tasks and actions to be performed. These tasks include making API calls, summarizing files and folders, inserting content into files, managing TODO issues in code repositories, and summarizing changes in pull requests. The workflows can be customized and extended to fit specific needs, and the changes made by the workflows can be committed and pushed to a git repository.  

<!-- Living README Summary -->