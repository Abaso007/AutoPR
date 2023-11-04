

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains Python scripts and YAML configuration files that are used for various workflow-related tasks. The scripts are designed to collect and load workflow configurations from YAML files, handle exceptions and log errors, and provide functions for interacting with APIs, generating README summaries, inserting content into files, managing TODO issues, and summarizing changes in pull requests. The YAML configuration files define the inputs, outputs, and steps for each workflow, and can be extended or modified to fit specific workflow configuration needs.


### [`__init__.py`](https://github.com/raphael-francis/AutoPR-internal/blob/2f0b06f314ecec7d8eddf44bf3ce5967d4ba90e1/./autopr/workflows/__init__.py)

📝 This file contains a Python script.  
🛠️ The purpose of the script is to collect and load workflow configurations from YAML files.  
📂 It recursively searches for YAML files in a specified folder and its subfolders.  
📝 The collected workflows are stored in a `TopLevelWorkflowConfig` object.  
⚠️ It handles exceptions and logs errors if there are any issues with loading or validating the workflows.  
🔄 It can also load additional test workflows if provided.  
📥 The loaded workflows are returned as the result of the `get_all_workflows()` function.  
📥 The script can be run as a standalone program to print the loaded workflows.  
📂 The script relies on other modules and classes imported at the beginning of the file.  
🚀 The script can be extended or modified to fit specific workflow configuration needs.  


### [`api_git_history.yaml`](https://github.com/raphael-francis/AutoPR-internal/blob/2f0b06f314ecec7d8eddf44bf3ce5967d4ba90e1/./autopr/workflows/api_git_history.yaml)

📝 This file defines a set of steps for making an API call, saving the response to a file, and committing and pushing the file to a git repository.  
🔗 The API call endpoint URL, headers, and filepath are defined as inputs.  
🔀 The file uses a "make_api_call" action to make a GET request to the specified endpoint URL, using the provided headers.  
📄 The response content is then saved into a file specified by the filepath input, overwriting any existing content in the file.  
📦 Finally, the file is committed and pushed to a git repository, with a commit message template that includes the endpoint URL and filepath.  


### [`autogenerate_readmes.yaml`](https://github.com/raphael-francis/AutoPR-internal/blob/2f0b06f314ecec7d8eddf44bf3ce5967d4ba90e1/./autopr/workflows/autogenerate_readmes.yaml)

📝 This file contains a YAML configuration for generating living summaries of files and folders.   
🔍 It includes workflows for summarizing individual files and folders, as well as a main workflow for generating README summaries.   
⚙️ The file defines various inputs, outputs, and steps for each workflow.   
📂 The `summarize_file` workflow reads a file, prompts for a summary, and outputs the summary and file URL.   
📁 The `summarize_folder` workflow summarizes all files and subfolders in a given folder, and prompts for a folder summary.   
✏️ The `reformat_results` workflow formats the summary outputs for inclusion in a README.   
📄 The `insert_into_readme` workflow inserts the formatted summary into the README file.   
🗂️ The `generate_summary` workflow is the entry point for summarizing both files and folders.   
📄 The `generate_readme_summaries` workflow executes the `generate_summary` workflow for the current directory.  


### [`insert_into_readme.yaml`](https://github.com/raphael-francis/AutoPR-internal/blob/2f0b06f314ecec7d8eddf44bf3ce5967d4ba90e1/./autopr/workflows/insert_into_readme.yaml)

📝 This file defines a task called "insert_into_readme" that inserts content into a file between two HTML-style comments.  
📂 The file path, tag name, and content to insert are specified as inputs.  
💾 The task reads the file, inserts the content between the specified comments, and then writes the modified content back into the file.  
📥 If the file does not exist, it will be created.  
📑 If only one comment is found, the content will be appended to the end of the file.  
🖋️ The task uses three actions: "read_file" to read the file, "insert_content_into_text" to insert the content, and "write_into_file" to write the modified content.  
📄 The output of the task is the content of the file after the insertion.  
✅ The task returns a success flag indicating whether the write operation was successful.  


### [`list_and_publish_todos.yaml`](https://github.com/raphael-francis/AutoPR-internal/blob/2f0b06f314ecec7d8eddf44bf3ce5967d4ba90e1/./autopr/workflows/list_and_publish_todos.yaml)

💡 The file defines a workflow for managing TODO issues in code repositories.  
💡 It includes steps for finding TODOs, prompting for task difficulty and suggestions, and publishing issues.  
💡 The workflow can be triggered with inputs for language and todo keywords.  
💡 It uses a set of predefined choices for task difficulty labels.  
💡 The issue title and body are generated based on the TODO information and prompt suggestions.  
💡 The workflow supports iterating over multiple TODOs and building and publishing issues for each.  
💡 TODOs without any suggestions are skipped and not published.  
💡 The workflow can be executed to update existing TODO issues and retrieve a list of issue numbers.  
💡 The file includes a "publish_todo_issues" workflow that triggers the "list_todos" workflow and retrieves the issue numbers.  
💡 The file is written in a specific format, likely for use with a workflow management system.  


### [`summarize_pr.yaml`](https://github.com/raphael-francis/AutoPR-internal/blob/2f0b06f314ecec7d8eddf44bf3ce5967d4ba90e1/./autopr/workflows/summarize_pr.yaml)

📝 This file defines a workflow called `summarize_pr` that summarizes the changes in a pull request.  
🔍 It uses the `git diff` command to get the difference between the base commit and the pull request.  
💬 It prompts the user to summarize the changes using markdown and emojis to highlight the contents of the changes.  
💡 The user's input is stored in the `summary` variable.  
💬 The summarized changes are then posted as a comment.  

<!-- Living README Summary -->