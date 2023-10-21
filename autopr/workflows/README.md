

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains a collection of files related to workflow configuration and execution. The main file, `__init__.py`, defines functions for collecting and loading workflows from YAML files in a specified folder and its subfolders. The other files contain specific workflow configurations, such as making API calls, generating README summaries, inserting content into files, and summarizing changes in pull requests. Each file serves a specific purpose and can be customized to automate various tasks.


### [`__init__.py`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/workflows/__init__.py/)

📝 This file is a Python script that defines functions for collecting and loading workflows from YAML files in a specified folder and its subfolders.
📂 It imports various modules and defines a class and functions related to workflow configuration and execution.
📄 The main function, `get_all_workflows()`, loads default workflows from a specified folder and also allows for the loading of test workflows.
📥 The workflow configurations are parsed from YAML files using the `pydantic` library.
🌐 The loaded workflows are stored in a `TopLevelWorkflowConfig` object, which is a data model defined in another module.
🔁 The `_collect_workflows()` function is used to collect and validate individual workflow configurations.
📁 The `_load_workflows_in_folder()` function recursively loads workflows from YAML files in a specified folder and its subfolders.
⚠️ Error handling is included for invalid workflow configurations and duplicate workflow IDs.
🖨️ When executed as a standalone script, the `get_all_workflows()` function is called and the loaded workflows are printed.


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

📝 This file contains a set of workflows and actions for generating and formatting summaries for files and folders, and updating a README with the summaries. It includes workflows for summarizing individual files, summarizing folders, reformatting the results, and inserting the formatted summaries into the README. The file also includes an execution workflow for generating README summaries for all folders in the current directory.


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