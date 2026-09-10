

class HTMLNode():
    def __init__(self, 
                 tag: str | None = None, 
                 value: str | None = None, 
                 children: list["HTMLNode"] | None = None, 
                 props: dict[str, str] | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        output = ""
        if not self.props:
            return output
        for key in self.props:
            output += f' {key}="{self.props[key]}"'
        
        return output

    def __repr__(self):
        return (
                f"HTMLNode({self.tag}, {self.value}, "
                f"children: {self.children}, {self.props})"
        )



