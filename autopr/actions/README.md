

<!-- Living README Summary -->
## 🌳 Living Summary

This folder contains a collection of Python files and a subfolder. The files define various actions and utilities for automation tasks. Each file represents a specific action, such as running a bash command, publishing a comment on a GitHub issue, committing and pushing changes to a remote repository, crawling and filtering the contents of a folder, inserting content into a string, generating prompts using the OpenAI API, reading the contents of a file, setting the title of an issue, and writing content into a file. The subfolder contains a file related to defining and transforming prompt contexts for auto PR generation. Overall, this folder provides a set of reusable components for automating different tasks.


### [`__init__.py`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/actions/__init__.py/)

📂 The file imports modules from the current directory.
🧩 It gathers all Python files in the directory and imports them.
📚 It also imports all modules from subdirectories.
📄 The imported modules are stored in the "__all__" variable.
🔍 The purpose of the file is to make all modules easily accessible.



### [`base.py`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/actions/base.py/)

📄 This file defines a base class for actions in an autonomous agent system. Actions are responsible for performing tasks, affecting the environment, and returning results.
🔍 The file also contains a metaclass for registering actions in a global registry.
📝 The base class has attributes for the ID, name, and description of an action.
🔀 The base class is generic and can take input and output types.
🏭 The base class has a run method that needs to be implemented by subclasses.
🔧 The base class has an initializer that takes various services and a logger.
🔢 The base class has methods for getting the input and output types.
🔍 The file includes a function that returns a dictionary of all registered actions.
🔀 The file imports various modules and types that are used throughout the code.


### [`bash.py`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/actions/bash.py/)

📝 This file contains a Python script for running a bash command and returning its output. 
🔧 It defines a class called "Bash" that extends a base class called "Action".
📥 The "Bash" class has a method called "run" which takes a command as input and executes it using asyncio.
📤 The output of the command is captured and returned as a string.
💡 The purpose of this file is to provide a reusable component for running bash commands in Python scripts.
🚀 The script can be run independently to manually test the "Bash" action with a predefined command.
🔧 The file imports necessary modules and defines input and output models for the "Bash" action.
🔬 The file also includes a conditional block that runs the "Bash" action with a sample command when the file is executed directly.
🧪 The file can be used as a starting point for building more complex automation tasks involving bash commands.


### [`comment.py`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/actions/comment.py/)

📄 This file defines a class called "Comment" which represents an action to publish a comment on a GitHub issue.
🔑 The class has an ID of "comment" and inherits from the "Action" class.
🔍 The class has an asynchronous method called "run" which takes an instance of "Inputs" as input and returns None.
📝 The "Inputs" class is a Pydantic BaseModel that defines the input parameters for the "Comment" action.
🗒️ The input parameters include a "comment" (str) and an optional "issue_number" (int).
⚙️ The "run" method calls the "publish_comment" method of the "publish_service" to publish the comment on the specified issue.
📚 The file imports necessary modules and packages like "typing" and "pydantic".
✅ The file is part of a larger codebase and serves the purpose of implementing a specific action in an automated process.



### [`commit_and_push.py`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/actions/commit_and_push.py/)

📄 This file defines a class called "CommitAndPush" that represents an action to commit and push changes to a remote repository.
🔐 The class extends a base class called "Action" and is generic with inputs of type "Inputs" and no output.
🔧 The "run" method within the class is async and takes an instance of "Inputs" as input.
📝 The "commit_message" attribute of "Inputs" is set to "AutoPR commit" by default.
📂 The "filepaths" attribute of "Inputs" is an optional list of strings.
📥 The "run" method calls the "commit" method of a "commit_service" object with the commit message, filepaths, and push flag.
📝 If the "filepaths" attribute is not provided, all changes are committed and pushed.
📝 The "commit_and_push" identifier is used to distinguish this action from others.
📄 The file uses the pydantic library for type validation and modeling of the "Inputs" class.


### [`crawl_folder.py`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/actions/crawl_folder.py/)

📄 This file defines a class called "CrawlFolder" that lists the files and subfolders in a given folder while excluding certain files and directories.
📂 The class takes inputs such as the folder path, a list of entries to ignore, and whether to ignore binary files.
🔍 It uses regular expressions to filter out non-informative files and directories.
💻 The class has a method to check if a file is binary.
🔗 It returns the list of file entries and the URL of the folder being crawled.
🚀 The file also contains a main function that manually runs the "CrawlFolder" action using the provided inputs.
💡 The purpose of the file is to provide a way to crawl and filter the contents of a folder.
📚 The file imports various modules and defines a couple of data models.
🔧 It utilizes the "autopr" and "pydantic" libraries for its functionality.
🔒 The file does not have any test cases included.


### [`insert_content_into_text.py`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/actions/insert_content_into_text.py/)

📄 This file contains a Python script for inserting content into a string at a specified delimiter.
🔍 The purpose of the script is to insert content into a string based on the occurrence of a delimiter.
🔧 It provides a class called "InsertContentIntoText" which has a method for inserting the content.
⚙️ The method checks the number of occurrences of the delimiter in the string.
✏️ If there are no or only one occurrence, the content is appended to the end with delimiters.
✏️ If there are two or more occurrences, the content is inserted between the last two delimiters.
📥 The script also defines input and output models for the action.
🔬 There are two examples provided to demonstrate the functionality of the script.
🧪 The script can be manually tested using the "run_action_manually" function from the test utils module.
📖 Overall, this script provides a convenient way to insert content into a string at a specific delimiter.


### [`prompt.py`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/actions/prompt.py/)

📝 This file contains a Python script that defines a class called "PromptString".
🧩 The purpose of the class is to generate a string using the OpenAI ChatCompletion API.
🔒 The class has a method called "run" that takes inputs, builds a prompt and instructions, invokes the API, and returns the result.
📄 The class also has helper methods for filtering nones, trimming the prompt context, and building the prompt and instructions.
⚙️ The class uses various external dependencies such as openai, tenacity, and pydantic.
📦 The class imports other modules and classes from the autopr package.
🧪 The file includes a test case that demonstrates the usage of the PromptString class.
🔍 The test case creates an instance of the Inputs class, sets some input values, and runs the PromptString class manually.
⚠️ The file should be executed as a standalone script when running the test case.
📥 The file can be used as a starting point for implementing a prompt generation functionality using the OpenAI API.


### [`read_file.py`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/actions/read_file.py/)

📝 The file contains a Python class called "ReadFile" that represents an action to read the contents of a file.
📄 It imports necessary modules and defines two Pydantic models for input and output data.
🔍 The "load_jupyter_notebook" method is used to read the contents of a Jupyter notebook file.
✅ The "ensure_file_exists" method ensures that a file exists at the given file path.
🔧 The "run" method is the main function that reads the contents of a file based on the input parameters.
🚀 It can handle both regular text files and Jupyter notebook files.
📑 The "contents" of the file, the "success" status, and the "url" of the file in the repository are returned as outputs.
❗️ If any unexpected error occurs during file reading, it will be logged and raised.
🔬 There is a test section at the end that demonstrates how to manually run the "ReadFile" action.


### [`set_issue_title.py`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/actions/set_issue_title.py/)

📝 This file defines a class named `SetIssueTitle` which represents an action to set the title of an issue. 
📋 The class is a subclass of `Action` and takes an input of type `Inputs` which has a single field `title` of type `str`. 
💻 The `run` method of the class is an asynchronous function that sets the title of an issue using the `publish_service` object. 
🔑 The class has a unique identifier `id` which is set to "set_issue_title".


### [`utils`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/actions/utils/)

This folder contains two files: "__init__.py" and "prompt_context.py". "__init__.py" is an empty file. "prompt_context.py" is a Python file that implements a prompt context model for auto PR (pull request) generation. It includes classes and functions related to defining and transforming prompt contexts, and also defines different types of declarations for prompt context in config. The file imports modules like `pydantic`, `tiktoken`, and `jinja2` for type checking, encoding, and template rendering.


### [`write_into_file.py`](https://github.com/raphael-francis/AutoPR-internal/tree/main/./autopr/actions/write_into_file.py/)

📝 This file defines a Python class called `WriteIntoFile` which is an action that writes content into a file.
📄 The `Inputs` class defines the required input parameters for the `WriteIntoFile` action.
📤 The `Outputs` class defines the output of the `WriteIntoFile` action, indicating whether the file was written to successfully.
🖊️ The `run` method of the `WriteIntoFile` class implements the logic to write the content into the specified file.
🔒 The file is opened in "append" mode if `append_at_the_end` is True, otherwise it is opened in "write" mode to replace the entire file content.
✅ The `run` method returns an instance of the `Outputs` class with the `success` field set to True if the file was written to successfully.
⚙️ The file also includes a test case that manually runs the `WriteIntoFile` action and removes the created test file afterwards.
🔧 The purpose of this file is to provide a reusable action for writing content into a file in a specified location.
📚 The `WriteIntoFile` action can be integrated into a larger system or workflow to automate file writing tasks.
📝 The file shows an example usage of the `WriteIntoFile` action to write the content "Hello world!" into a test file.

<!-- Living README Summary -->