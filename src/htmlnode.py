class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join([f' {key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
        

class LeafNode(HTMLNode):
    def __init__(self, value, tag, props=None):
        super().__init__(tag, value, None, props)

        
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return f'{self.value}'
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is important to have here")
        if self.children is None:
            raise ValueError("you are forgetting the children!")

        body = ""        
        for child in self.children:
            body += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{body}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
            
