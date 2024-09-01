# lucide-fasthtml

*Any use of the code retrieved from lucide.dev is subject to the terms of the Lucide license, found [here](https://lucide.dev/license).*

[![PyPI - Version](https://img.shields.io/pypi/v/lucide-fasthtml.svg)](https://pypi.org/project/lucide-fasthtml)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lucide-fasthtml.svg)](https://pypi.org/project/lucide-fasthtml)

A small package for FastHTML that allows you to use Lucide icons efficiently with fasthtml projects, avoiding cdn's and downloading entire static bundles. Features include:

- Full tree-shaking support
- Client-side `script` retrieval on cache-miss
- Streamlined attribute handling for full customization (mimics [lucide-react](https://github.com/lucide-icons/lucide-react))
- Immediate icon retrieval on cache-hit, no additional network requests
-----

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [License](#license)

## Installation

```console
pip install lucide-fasthtml
```

## Usage

```python
from lucide_fasthtml import Lucide

Lucide("sun") # or Lucide(icon="sun")
```

>[!RESULT]
><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-sun"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="m2 12h2"/><path d="m20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>

## Customization

Supports all standard svg attributes. Defaults are set to the standard defaults found at [lucide.dev](https://lucide.dev). For ease of use, streamlined attributes used by `lucide-react` are also supported in a FastHTML-compatible format.

| lucide-react | lucide-fasthtml | notes |
| ------------- | --------------- | ----- |
| `color="red"` | `color="red"` | Can be used instead of `stroke`. Sets the color of the icon stroke. |
| `strokeWidth="2"` | `stroke_width="2"` | Sets the stroke width of the icon. |
| `absoluteStrokeWidth=True` | `absolute_sw=True` | Calculates the stroke width based on the icon's size, to standardize the stroke width across different icon sizes. |
| `size=16` | `size=16` | Can be used instead of `width` and `height` properties. Sets the size (width and height) of the icon to the specified value. |

```python
Lucide("sun", color="red", stroke_width="1.5", absolute_sw=True, size=16)
```

>[!RESULT]
><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="red" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="m2 12h2"/><path d="m20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>



## License

`lucide-fasthtml` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
