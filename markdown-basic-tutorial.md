# Markdown syntax guide

Markdown syntax
The page below contains examples of Markdown syntax. For a full list of all the Markdown syntax, consult the CommonMark help or specification.

Headings
# This is an H1
## This is an H2
###### This is an H6

This is also an H1
==================

This is also an H2
------------------
Paragraphs
Paragraphs are separated by empty lines. To create a new paragraph, press <return> twice.

Paragraph 1

Paragraph 2
Character styles
*Italic characters* 
_Italic characters_
**bold characters**
__bold characters__
~~strikethrough text~~
Unordered list
*  Item 1
*  Item 2
*  Item 3
    *  Item 3a
    *  Item 3b
    *  Item 3c
Ordered list
1.  Step 1
2.  Step 2
3.  Step 3
    1.  Step 3.1
    2.  Step 3.2
    3.  Step 3.3
List in list
1.  Step 1
2.  Step 2
3.  Step 3
    *  Item 3a
	*  Item 3b
	*  Item 3c
Quotes or citations
Introducing my quote:

> Neque porro quisquam est qui 
> dolorem ipsum quia dolor sit amet, 
> consectetur, adipisci velit...
Inline code characters
Use the backtick to refer to a `function()`.
 
There is a literal ``backtick (`)`` here.
Code blocks
Indent every line of the block by at least 4 spaces.

This is a normal paragraph:

    This is a code block.
    With multiple lines.

Alternatively, you can use 3 backtick quote marks before and after the block, like this:

```
This is a code block
```

To add syntax highlighting to a code block, add the name of the language immediately
after the backticks: 

```javascript
var oldUnload = window.onbeforeunload;
window.onbeforeunload = function() {
    saveCoverage();
    if (oldUnload) {
        return oldUnload.apply(this, arguments);
    }
};
```
Bitbucket Server uses CodeMirror to apply syntax highlighting to the rendered markdown in comments, READMEs and pull request descriptions. All the common coding languages are supported, including C, C++, Java, Scala, Python and JavaScript. See Configuring syntax highlighting for file extensions.

Within a code block, ampersands (&) and angle brackets (< and >) are automatically converted into HTML entities.

Links to external websites
This is [an example](http://www.example.com/) inline link.

[This link](http://example.com/ "Title") has a title attribute.

Links are also auto-detected in text: http://example.com/
Linking issue keys to JIRA applications
When you use Jira application issue keys (of the default format) in comments and pull request descriptions Bitbucket Server automatically links them to the Jira application instance.

The default Jira application issue key format is two or more uppercase letters ([A-Z][A-Z]+), followed by a hyphen and the issue number, for example TEST-123.


Linking to pull requests
Introduced with Bitbucket Server 4.9, you can reference pull requests from comments and descriptions in other pull requests. The syntax for linking to pull request looks like this: 

projectkey/repo-slug#pr_id
To link to a pull request in the same project and repository, you only need to include the pull request ID. 

#123
To link to a pull request in the same project but a different repository, include the repository slug before the pull request ID.

example-repo#123
To link to a pull request in a different project and repository, include the project key and the repository slug before the pull request ID.

PROJ/example-repo#123
Images
Inline image syntax looks like this:

![Alt text](/path/to/image.jpg)
![Alt text](/path/to/image.png "Optional title attribute")
![Alt text](/url/to/image.jpg)
For example:

...
![Mockup for feature A](http://monosnap.com/image/bOcxxxxLGF.png)
...
Reference image links look like this:

![Alt text][id]
where 'id' is the name of a previously defined image reference, using syntax similar to link references:

[id]: url/to/image.jpg "Optional title attribute"
For example:

...
<--Collected image definitions-->
[MockupA]: http://monosnap.com/image/bOcxxxxLGF.png "Screenshot of Feature A mockup" 
...
<!--Using an image reference-->
![Mockup for feature A][MockupA]
...
Tables
| Day     | Meal    | Price |
| --------|---------|-------|
| Monday  | pasta   | $6    |
| Tuesday | chicken | $8    |
Backslash escapes
Certain characters can be escaped with a preceding backslash to preserve the literal display of a character instead of its special Markdown meaning. This applies to the following characters:

\  backslash 
`  backtick 
*  asterisk 
_  underscore 
{} curly braces 
[] square brackets 
() parentheses 
#  hash mark 
>  greater than 
+  plus sign 
-  minus sign (hyphen) 
.  dot 
!  exclamation mark

README files
If your repository contains a README.md file at the root level, Bitbucket Server displays its contents on the repository's Source page if the file has the .md extension. The file can containMarkdown and a restricted set of HTML tags.

