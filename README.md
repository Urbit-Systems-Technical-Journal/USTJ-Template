# Urbit Systems Technical Journal—Template Repo

Welcome, prospective USTJ author.  Please keep the following in mind:

1. USTJ is a technical journal.  We will generally consider any content related to solid state computing.  We do not wade into social or cultural commentary.  We welcome content that is not specifically about or on Urbit as well.
2. As an author, you shoud join the discussion group on Urbit at `~fabled-wander-lagrev-nocfep/urbit-system-technical-journal--planning-and-editors-`.  If you are not on Urbit yet, please DM us at `@UrbitSTJ` on Twitter/X.  If you are interested in participating as a reviewer or editor, please join the group as well.
3. We will review your article in a timely manner.  (Sometimes we will do this more than once.)  We will plan on which issue to release it based on the volume of content we are handling at any given time.
4. We accept submissions in LaTeX or Markdown.  Final article preparation is always done in LaTeX but we can convert it for you from Markdown.

---

This is the template repository for USTJ LaTeX submissions.  You may use this as a template repo; if you do not see this option, then you should *import* this repo, not *fork* it.

Line numbers should be kept on for submissions.

Authors should add their name, `@p`, and title to the manuscript, and should bring their own `bib` file.

The PDF can be built using `make`.

##  Style Guide

### General

1. We compile using XeTeX, but you should be careful about nonstandard characters.  Check your output log and PDF.

### Stylistic

1. In general, abbreviations or all-caps words that are three or more characters in length should be rendered as small caps using `{\sc this format}`.  There are exceptions, such as source code and partially minuscule terms.
2. Prefer to render code using `\lstinline[style=inlinecode]{}` to `\texttt{}` for source code.  (This does not require escaping `%`, `$`, `_`, etc.)
3. We make the following editorial policies:
  - `i.e.`, `e.g.`, `q.v.` → `i.\,e.\ `
  - lowercase “kelvin” everywhere it occurs (capitalize “4K”)
  - `IO` → `I/O`
  - scrys → scries


### Citations

1. Citations should be standardized:
    1. Cite a UIP as `\citet{UIP-0100}` → `UIP-0100`.
    2. Cite a PR as `\citet[UrbitPR6447}` → `#6447``.
    3. Cite a GitHub repo as `\citet{urbit/urbit}` → `urbit/urbit`.
    4. Cite a gist as a `@online` (generally) or `@techreport` (if from an organization like Urbit Foundation).
2. The standard `mss.bib` file provides common Urbit repos, UIPs, etc.  You may add to it locally or otherwise merge it into your preferred personal BibTeX file.  Contributions to the standard `mss.bib` are welcome.
3. We provide `\citepr{urbit/urbit_6891}` → `#6891` as an inline citation for PRs.
4. We compile using [BibLaTeX (`biber`)](https://mirrors.rit.edu/CTAN/macros/latex/contrib/biblatex/doc/biblatex.pdf) for more modern bibliographic entry options.

### Code

1. Arms are referred to with `++` or `+$`, not a simple `+` or `$`.
2. Vanes should be referred to by their primary name, e.g. “Ames” not `%ames`.
3. When referring to the source implementation of a particular piece of software, it may be appropriate to favor the syntax `/lib/agentio` or `/sys/hoon`.  File suffixes (marks) should not typically be included in these cases.
4. Code should be displayed with either `\lstinline[style=inlinecode]{.^}` or `\begin{lstlisting}[style=listingcode]` blocks.
    1. Other languages may be added as `\lstdefinestyle` in your copy of `ustj.sty`.
5. Nock opcodes are written numerically, e.g. “Nock 11”.
6. All references to runes should be of the form “`.^` dotket” including the pronunciation at each point.  This will make the text friendlier to outside readers and more searchable.  You may define a shorthand such as `\newcommand{\dotket}{\lstinline[style=inlinecode]{.^} dotket}`.  In this case, please make sure to use it with an explicit space afterwards:  “the \dotket~rune”.
7. Due to page size and typeface limitations, code is limited to **54 CHARACTERS WIDE**.  Make do, Hoon is flexible.
8. Refer to Clay files as “`/lib/test` on the `%base` desk“.  (I.e., omit the mark if it is not significant to the discussion.)

### Math Mode

1. Due to limitations of the LaTeX→HTML tool, we will replace all instances of `\mathtt{}` with `\texttt{}`.

### Other Resources

- [Hoffman, “How To Write a Scientific Paper and Format it Using LaTeX”](https://hoffman.physics.harvard.edu/Hoffman-example-paper.pdf)

