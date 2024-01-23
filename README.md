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

1. Arms are referred to with `++` or `+$`, not a simple `+` or `$`.
2. Either `fontspec` with `\string` or `verbatim` may be used to display the many Hoon and Nock ASCII characters that are meaningful in LaTeX.  (`[`, `]`, `~`, and so forth.)
3. All code should be in `lstlisting` or `\texttt`.
    1. Inline code should be marked with `\texttt` or (preferably) `\lstinline[style=inlinecode]`.
    2. Listings should be marked with `\begin{lstlisting}[style=listingcode]`.  You may add C, Python, etc. as needed to the style file.
4. Nock opcodes are written numerically, e.g. “Nock 11”.
5. We compile using XeTeX, but you should be careful about nonstandard characters.  Check your output log and PDF.
6. All references to runes should be of the form “`.^` dotket” including the pronunciation at each point.  This will make the text friendlier to outside readers and more searchable.  You may define a shorthand such as `\newcommand{\dotket}{\lstinline[style=inlinecode]{.^} dotket}`.  In this case, please make sure to use it with an explicit space afterwards:  “the \dotket~rune”.
7. Citations should be standardized:
    1. Cite a UIP as `\citet{UIP-100}`.
    2. Cite a PR as `\citet[UrbitPR6447}` → `urbit/urbit` #6447.
    3. Cite a GitHub repo.
    4. Cite a gist.
