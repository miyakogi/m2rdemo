# -*- coding: utf-8 -*-

from typing import Dict

from docutils.core import publish_parts
import m2r

from wdom import options, server
from wdom.document import get_document, set_app
from wdom.event import Event
from wdom.parser import parse_html

options.config.theme = 'skyblue'  # Fake command line option
from wdom.themes import default  # noqa
from wdom.themes.default import Div, Textarea, Col6, Col12, Row, H1, Hr  # noqa
from wdom.themes.default import Option, Pre, Select, Span  # noqa

converter = m2r.M2R()
src = '''
# M2R Preview

This is a m2r demo editor.

You can **directly** write `Markdown`, :code:`reStructuredText`, and
<span style="color: #b33;">Raw HTML</span>.

## Source Code Example

Markdown style:

```py
print('Hello, M2R!')
```

### reStructuredText Directives

.. code:: python

   print('Hello, WDOM!')

.. note::

   reST directives are also OK!

'''


def parse2rst(text: str) -> str:
    rst = converter(text)
    return rst


def parse(text: str) -> Dict[str, str]:
    rst = parse2rst(text)
    output = publish_parts(source=rst, writer_name='html5')
    return output


class Selector(Select):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.opt1 = Option(parent=self, value='html')
        self.opt1.textContent = 'HTML'
        self.opt2 = Option(parent=self, value='raw_html')
        self.opt2.textContent = 'Raw HTML'
        self.opt3 = Option(parent=self, value='rst')
        self.opt3.textContent = 'RST'


class App(Row):
    def __init__(self) -> None:
        super().__init__()
        self.doc = get_document()
        self.style = 'height: 80vh;'
        editor_col = Col6(parent=self)
        self.editor = Textarea(parent=editor_col)
        self.editor.style = 'font-family: monospace; height: 80vh; width: 95%;'

        viewer_col = Col6(parent=self)

        self.selector_row = Row()
        self.selector_row.appendChild(Col6(
            Span('Output Format: '),
            style='text-align: right;',
        ))

        self.selector_col = Col6(parent=self.selector_row)
        self.selector = Selector(parent=self.selector_col)
        self.selector.addEventListener('change', self.preview)

        self.viewer_row = Row()
        self.viewer = Col12(parent=self.viewer_row)
        self.viewer.style = '''
            height: 100%;
            margin-top: 1rem;
            padding: 1rem 2rem;
            border: 1px solid #ddd;
            border-radius: 3px;
        '''

        viewer_col.appendChild(self.selector_row)
        viewer_col.appendChild(self.viewer_row)

        self.editor.addEventListener('input', self.preview)
        self.editor.textContent = src
        output = parse(src)
        _style = parse_html(output['stylesheet'])
        self.doc.head.appendChild(_style)
        self.viewer.innerHTML = output['html_body']

    def update(self, text: str) -> None:
        if self.selector.value == self.selector.opt3.value:
            self.viewer.replaceChild(
                Pre(parse2rst(text)),
                self.viewer.firstChild
            )
        else:
            html = parse(text)['html_body']
            if self.selector.value == self.selector.opt2.value:
                self.viewer.replaceChild(
                    Pre(html),
                    self.viewer.firstChild
                )
            else:
                self.viewer.innerHTML = html

    def preview(self, event: Event) -> None:
        content = self.editor.textContent
        self.update(content)


def sample_page() -> Div:
    doc = get_document()
    doc.register_theme(default)
    doc.title = 'M2R DEMO'
    app = Div(style='width: 90vw; margin: auto')
    title = H1('M2R DEMO Editor (powered by WDOM)',
               style='text-align: center;')
    app.appendChild(title)
    app.appendChild(Hr())
    app.appendChild(App())
    return app


def main() -> None:
    set_app(sample_page())
    server.start()
