from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
            self, 
            tag: str | None, 
            value: str, 
            props: dict[str, str] | None = None) -> None:
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode has no value!")
        if self.tag is None:
            return self.value
        props_str = self.props_to_html()
        return f'<{self.tag}{props_str}>'\
                    f'{self.value}</{self.tag}>'
    
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

