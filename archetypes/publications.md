---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date.Format "2006-01-02" }}
draft: false
layout: "single"
type: "publications"
publication_type: "Journal Article"
authors:
  - "Jane Doe"
author_notes:
  - "Corresponding Author"
publication:
  name: "Journal of Science"
  volume: "1"
  issue: "1"
  pages: "1-10"
doi: ""
open_access: true
license: "CC BY 4.0"
url_code: ""
abstract: "Enter your short paper abstract overview summary description 
string directly inside this parameter block."
---

<!-- Not sure where this came from
  Your automated publications bundle is ready!
  1. Drop your manuscript file inside this folder and name it 'paper.pdf'
  2. Drop your BibTeX file inside this folder and name it 'cite.bib'
  3. RUN `hugo new publications/my-new-paper-title`

use this instead
1. conda activate academic (https://github.com/HugoBlox/academic-file-converter)
2. academic import cite.bib content/publications/  
-->

