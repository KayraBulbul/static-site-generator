class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        return f' href="{self.props["href"]}" target="{self.props["target"]}"'

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children=[{self.children}], props=[{self.props}])"


class LeafNode(HTMLNode):
    def __init__(
        self, tag: str | None, value: str, props: dict[str, str] | None = None
    ):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError

        if not self.tag:
            return self.value

        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, props=[{self.props}])"


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: list["HTMLNode"], props: dict[str, str] | None = None
    ):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode needs a tag")

        if not self.children:
            raise ValueError("ParentNode needs children")

        string = []
        for child in self.children:
            string.append(child.to_html())

        return f"<{self.tag}>{''.join(string)}</{self.tag}>"
