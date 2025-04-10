class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented yet")
    
    def props_to_html(self):
        if self.props is None:
            return None
        text = ""
        for k in self.props:
            text += f' {k}="{self.props[k]}"'
        return text
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"