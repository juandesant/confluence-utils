# Introduction
This package provides some Confluence utilities for managing several batch applications, for instance:
 * Adding or removing labels form a given page
 * Creating page content from a CVS file

This is very much work in progress, and for now this is based on my needs

# Dependencies
This package depends on `atlassian-python-api`.

It requires that a Personal Access Token is created in the relevant Confluence instance, and that that token is recorded either in a `~/.confluencePAT` file, or in a `[confluence]` section in an `~/.atlassianPAT` file. See installation for more details.


# Installation 

TBW 

## Local Prerequisites

One of two files need to exist for these tools to work:

1. A `.confluencePAT` file in the user's home directory, which contains a Personal Access Token for the only Confluence instance to be used with this tool. The format of this file is just a plain text file whose only content is the PAT.
2. An `.atlassianPAT` file in the user's home directory, which is a configuration file, readable by Python's [`ConfigParser`](https://docs.python.org/3/library/configparser.html "Python 3 Documentation: configparser — Configuration file parser"), and which can have sections for Confluence and Jira, and within each sections PATs for different instances. See an example of that file below.
 
   ```ini
   [DEFAULT]
   ; Nothing in default
   
   [confluence]
   confluence.example.com      = ConfluenceExample-fakePAT
   
   [jira]
   jira.example.com            = JiraExample-fakePAT
   ```

# License
As indicated in the LICENSE file, this project is licensed under a BSD 3-clause license.
