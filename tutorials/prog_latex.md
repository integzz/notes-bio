# 搭建 LaTeX 轻量级写作环境

LaTeX 是一套强大的排版系统，在学术论文排版方面应用广泛，很多西方高效和期刊都会提供自己 LaTeX 模板方便论文提交。虽然 LaTeX 有不少相关的 IDE，如 TeXstudio，BaKoMa，LyX 等，但总给人一种笨重的感觉。如今，VS Code 为我们提供了另一种选择。

## 1. 安装 LaTeX

对于 LaTeX 的安装，有如下两种方法。

### 1.1. 手动安装

对于 LaTeX 的常见版本，个人推荐 [MiKTeX](https://miktex.org/download)，即最小安装版本，其 Windows 安装包约 200 多 MB，MacOS 安装包 50 多 MB。相比于很多人推荐的 TeXLive （3.7 G）和 MacTeX（4.0 G）轻便了一个量级。其官方下载地址如下。

### 1.2. 自动安装

即使用包管理器进行安装。

对 Windows 用户，有 Scoop

```powershell
scoop install latex
```

对 MacOS 用户，有 Homebrew

```bash
brew install basictex
```

## 2. 语法扩展

`LaTeX Workshop` 基本上没什么可说的，使用 VS Code 写 LaTeX 的都会使用这个扩展，可认为是必备。

![LaTeX](images/vscode/latex1.png)

安装完毕后，"ctrl"+", " 打开配置，并在搜索框中输入"json"，打开配置的 .json 文件。

![settings](images/vscode/settings.png)

对 MacOS 加入如下配置：

```json
{
  "latex-workshop.latex.recipes": [
    {
      "name": "xelatex -> bibtex -> xelatex*2",
      "tools": ["xelatex", "bibtex", "xelatex", "xelatex"]
    }
  ],
  "latex-workshop.latex.tools": [
    {
      "name": "xelatex",
      "command": "xelatex",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "%DOC%"
      ]
    },
    {
      "name": "latexmk",
      "command": "latexmk",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "%DOC%"
      ]
    },
    {
      "name": "pdflatex",
      "command": "pdflatex",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "%DOC%"
      ]
    },
    {
      "name": "bibtex",
      "command": "bibtex",
      "args": ["%DOCFILE%"]
    }
  ],
  "latex-workshop.view.pdf.viewer": "tab",
  "[latex]": {
    "editor.formatOnSave": false
  }
}
```

对于 Windows 加入如下配置：

```json
{
  "latex-workshop.latex.recipes": [
    {
      "name": "xelatex -> bibtex -> xelatex*2",
      "tools": ["xelatex", "bibtex", "xelatex", "xelatex"]
    }
  ],
  "latex-workshop.latex.tools": [
    {
      "name": "xelatex",
      "command": "xelatex",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "%DOC%"
      ]
    },
    {
      "name": "latexmk",
      "command": "latexmk",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "%DOC%"
      ]
    },
    {
      "name": "pdflatex",
      "command": "pdflatex",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "%DOC%"
      ]
    },
    {
      "name": "bibtex",
      "command": "bibtex",
      "args": ["%DOCFILE%"]
    }
  ],
  "latex-workshop.view.pdf.viewer": "tab"
}
```

## 3. 功能扩展

### 3.1. 拼写检查

LaTeX 的用户里，不少人均是使用它进行英文写作的，这时就不免会需要拼写检查，这里推荐多语言扩展 Spell Right，其配置如下：

```json
{
  "spellright.addToSystemDictionary": true,
  "spellright.documentTypes": ["markdown", "latex", "plaintext"],
  "spellright.language": ["en", "zh", "fr", "es", "it"],
  "spellright.groupDictionaries": true,
  "spellright.suggestionsInHints": true,
  "spellright.ignoreRegExpsByClass": {
    "markdown": ["/&amp;/g", "/&nbsp;/g"],
    "cpp": ["/#include\\s+\\\".+\\\"/g"],
    "html": ["/<script>[^]*?</script>/gm"],
    "latex": ["/\\\\begin{bmatrix}[^]*?\\\\end{bmatrix}/gm"]
  },
  "spellright.spellContextByClass": {
    "latex": "body",
    "cpp": "comments",
    "python": "strings"
  },
  "spellright.latexSpellParameters": [
    "author",
    "title",
    "date",
    "chapter",
    "section\\*?",
    "subsection\\*?",
    "subsubsection\\*?",
    "part",
    "paragraph",
    "subparagraph",
    "text(rm|sf|tt|md|bf|up|it|sl|sc|normal)",
    "underline",
    "emph",
    "item",
    "footnote(text)?",
    "caption(of)?",
    "multicolumn",
    "href",
    "hyperref",
    "begin\\{frame\\}"
  ],
  "spellright.notificationClass": "warning"
}
```

### 3.2. 格式转化

这里推荐文档格式领域的瑞士军刀 [Pandoc](https://pandoc.org/)。可去官网手动下载

也可使用包管理器自动下载。

对 Windows 用户，有 Scoop

```powershell
scoop install pandoc
```

对 MacOS 用户，有 Homebrew

```bash
brew install pandoc
brew install pandoc-citeproc
```

## 4. 宏包管理

### 4.1. 基本操作

对于 Windows 用户，不需要特别对包进行管理，当在文档中导入未安装的包时，LaTeX 会自动弹出窗口，询问是否安装。

对于 MacOS 用户，需要使用包管理器 tlmgr 对 LaTeX 包进行管理。

```bash
# 升级自身
sudo tlmgr update --self
# 升级所有包
sudo tlmgr update --all
# 列出已安装包
sudo tlmgr list --only-installed
```

### 4.2. 推荐

```bash
# chinese
sudo tlmgr install ctex latexmk
# chemistry & electronics
sudo tlmgr install mhchem chemfig circuitikz
# page
sudo tlmgr install multirow ifoddpage relsize titlesec
# graph & table
sudo tlmgr install epstopdf subfigure appendix
# text
sudo tlmgr install ulem xcolor environ letltxmacro enumitem stringenc trimspaces soul algorithm2e genmisc
```

| Column A |    Column B    | Column C |
| :------: | :------------: | :------: |
|   ulem   | 下划线、删除线 |    C1    |
|  xcolor  |    字体颜色    |    C2    |
|    A3    |       B3       |    C3    |
