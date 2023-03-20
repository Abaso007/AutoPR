from typing import List, ClassVar, Optional

import pydantic


class RailObject(pydantic.BaseModel):
    rail_spec: ClassVar[str] = ...


class InitialFileSelectResponse(RailObject):
    rail_spec = """<list name="filepaths">
    <string
        description="The path to the file in the repo."
        format="filepath"
        on-fail="noop"
    />
</list>"""

    filepaths: List[str]


class LookAtFilesResponse(RailObject):
    rail_spec = """<list name="filepaths_we_should_look_at">
    <string
        description="The paths to files we should look at next in the repo, out of the ones we haven't taken a look at yet. Empty list if we're done."
        format="filepath"
        on-fail="noop"
    />
</list>
<string 
    name="notes" 
    description="Notes about the files (including line numbers), relevant to the issue at hand, that will help us write code later." 
    length="1 1000"
    format="text" 
    on-fail="noop" 
/>"""

    filepaths_we_should_look_at: Optional[List[str]] = None
    notes: str


class Diff(RailObject):
    rail_spec = """<string
    name="diff"
    description="The diff of the commit, in unified format (unidiff), as output by `diff -u`."
    required="true"
    format="unidiff"
    on-fail-unidiff="fix"
/>"""

    text: str


class Commit(RailObject):
    rail_spec = f"""{Diff.rail_spec}
<string
    name="message"
    description="The commit message, describing the changes."
    required="true"
    format="length: 5 72"
    on-fail-length="noop"
/>"""

    diff: Diff
    message: str


class CommitPlan(RailObject):
    rail_spec = f"""<string
    description="The commit message, accurately describing the changes made."
    length="1 100"
    format="text"
    on-fail="noop"
/>
<list
    name="relevant_filepaths"
    description="The files we should be looking at while writing this commit."
>
    <string
        description="A file path, relative to the root of the repository."
        format="filepath"
        on-fail="fix"
    />
</list>
"""

    message: str
    relevant_filepaths: List[str]


class PullRequestDescription(RailObject):
    rail_spec = f"""<string 
    name="title" 
    description="The title of the pull request."
/>
<string 
    name="body" 
    description="The body of the pull request."
/>
<list 
    name="commits"
    on-fail="reask"
>
<object
    name="commit"
>
{CommitPlan.rail_spec}
</object>
</list>"""

    title: str
    body: str
    commits: list[CommitPlan]
