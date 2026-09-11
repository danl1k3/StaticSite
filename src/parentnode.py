from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list["HTMLNode"],
        props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag=tag, children=children, value=None,props=props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Tag has no value!")
        if self.children is None:
            raise ValueError("Children is missing.")

        output = f"<{self.tag}>"
        for child in self.children:
            output += child.to_html()
        output += f"</{self.tag}>"

        return output
