

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains a collection of files related to workflow automation. The `__init__.py` file provides functions for loading and collecting workflows from YAML files. The `api_git_history.yaml` file defines a workflow for making API calls, saving the response to a file, and pushing it to a Git repository. The `autogenerate_readmes.yaml` file contains workflows for summarizing files and folders and generating README summaries. The `insert_into_readme.yaml` file defines a task for inserting content into a file. The `summarize_pr.yaml` file defines a workflow for summarizing changes in a pull request.


### [`__init__.py`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/workflows/__init__.py/)

📋 This file contains a Python script that defines functions related to loading and collecting workflows from YAML files.
📁 It imports necessary modules and defines a logger.
🔍 The main functions are `_collect_workflows` and `_load_workflows_in_folder`, which recursively collect workflows from YAML files in a folder and its subfolders.
🔧 The `get_all_workflows` function is the entry point, which loads default workflows and custom workflows from specified paths.
📃 The script also includes a test to print all the loaded workflows.
🔄 The purpose of this file is to provide a way to load and gather workflow configurations for further processing.


### [`api_git_history.yaml`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/workflows/api_git_history.yaml/)

💡 This file defines a series of steps for making an API call, saving the response to a file, and committing and pushing the file to a Git repository.
💡 The file is structured using a YAML format.
💡 The file specifies the inputs required for the API call, such as the endpoint URL, headers, and file path.
💡 The API call is made using the "make_api_call" action, which performs a GET request.
💡 The response content is then saved to a file using the "write_into_file" action.
💡 The "commit_and_push" action is used to commit and push the file to a Git repository, with a customizable commit message.
💡 The file paths and other values can be provided as variables using the "var" keyword.
💡 The file can be used as a template for automating API calls and version control.
💡 The file can be customized by modifying the inputs, actions, and templates.
💡 If the file is empty, there are no defined steps or actions.


### [`autogenerate_readmes.yaml`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/workflows/autogenerate_readmes.yaml/)

📄 This file contains a set of workflows for summarizing files and folders and generating README summaries. 
📝 The workflows include steps for reading file contents, prompting for file summaries, and generating folder summaries. 
💻 The file also includes steps for reformatting the summary results and inserting them into a README file. 
📂 The workflows can handle both files and folders, and they ignore certain files like README.md. 
⚙️ The file also includes a workflow for generating multiple README summaries. 
🔑 The file relies on certain input parameters and outputs results like file summaries and URLs. 
🚀 The workflows are designed to be executed and the results can be committed and pushed to a repository. 
📝 The file provides default prompts and instructions for generating file and folder summaries. 
🔗 The file makes use of variables, lambda functions, and conditional statements to handle different scenarios. 
📑 The file ends with a workflow for committing and pushing the cache of README summaries.


### [`insert_into_readme.yaml`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/workflows/insert_into_readme.yaml/)

📝 The file defines a task called "insert_into_readme" for inserting content into a file.
📄 The task requires three inputs: filepath, tag, and content.
🔍 It reads the contents of the file specified by the filepath input.
✏️ The task then inserts the content between HTML-style comments using the tag as a delimiter.
📝 The modified content is stored in the "content" output.
💾 Finally, the modified content is written back into the file specified by the filepath input.
📝 The "append_at_the_end" input determines whether the content should be appended to the end of the file if no delimiter is found.
📝 The task does not currently have any outputs defined.
📝 The purpose of this file is to define the steps for inserting content into a file with optional tag-based delimiters.


### [`summarize_pr.yaml`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/workflows/summarize_pr.yaml/)

📋 This file defines a workflow called "summarize_pr" for summarizing changes in a pull request.
⌨️ It uses a bash action to get the diff of the changes in the pull request.
💬 Then it prompts the user to summarize the changes using markdown and emojis.
💡 The user is instructed to provide line items with emojis to highlight the contents of the changes.
💻 The resulting summary is stored in the "summary" variable.
💬 Finally, the summary is posted as a comment.


<!-- Living README Summary -->