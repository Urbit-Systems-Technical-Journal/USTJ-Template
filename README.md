# USTJ Template

The template for USTJ LaTeX submissions.  You should *import* this repo, not *fork* it.

Line numbers should be kept on for submissions.

Authors should add their name, `@p`, and title to the manuscript, and should bring their own `bib` file.

The PDF can be built using `make`.

##  Style Guide

1. Arms are referred to with `++` or `+$`, not a simple `+` or `$`.
2. Either `fontspec` with `\string` or `verbatim` may be used to display the many Hoon and Nock ASCII characters that are meaningful in LaTeX.  (`[`, `]`, `~`, and so forth.)
3. All code should be in `listing` or `\texttt`.
4. Nock opcodes are written numerically, e.g. “Nock 11”.
5. We compile using XeTeX, but you should be careful about nonstandard characters.  Check your output log and PDF.
6. All references to runes should be of the form “`.^` dotket” including the pronunciation at each point.  This will make the text friendlier to outside readers and more searchable given regex.  You may define a shorthand such as `\newcommand{\dotket}{\texttt{\string.\string^~dotket}}`.  In this case, please make sure to use it with an explicit space afterwards:  “the \dotket~rune”.


