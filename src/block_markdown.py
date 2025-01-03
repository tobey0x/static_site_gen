import re
from enum import Enum
from htmlnode import HTMLNode, ParentNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes

class BlockType(Enum):
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
# Splitting markdown into blocks
def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    blocks = []
    
    for line in raw_blocks:
        if line != "":
            blocks.append(line.strip())
            
    return blocks

# Converting markdown into HTML nodes
def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        
        node = convert_block_to_html_node(block, block_type)
        children.append(node)
        
    return ParentNode(tag="div", children=children)
  
    
# Determining the type of block    
def block_to_block_type(markdown_block):
    block = markdown_block
    """
    Determinne the type of MArkdown block.
    
    """
    
    # Check for headings
    if re.match(r'^(#{1,6})\s+(.)', block):
        return BlockType.HEADING
    
    # CHeck for code blocks
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Check for quote blocks
    if all(line.startswith(">") for line in block.splitlines()):
        return BlockType.QUOTE
    
    # Check for unordered list blocks
    if all(re.match(r'^[*-] ', line) for line in block.splitlines()):
        return BlockType.UNORDERED_LIST
    
    # Check for ordered list blocks
    lines = block.splitlines()
    if all(re.match(r'^\d+\. ', line) for line in lines):
        numbers = [int(re.match(r'^(\d+)\. ', line).group(1)) for line in lines]
        if numbers == list(range(1, len(numbers) + 1)):
            return BlockType.ORDERED_LIST
    
    # Default to paragraph
    return BlockType.PARAGRAPH


# Creating HTML tag for respective block types        
def convert_block_to_html_node(block: str, block_type: BlockType):        
    if block_type == BlockType.HEADING:
        level = len(block.split(" ")[0])
        content = block[level + 1:]
        children = text_to_html_node(content)
        return ParentNode(f"h{level}", children=children)
    
    if block_type == BlockType.PARAGRAPH:
        text = ""
        for line in block.split("\n"):
            text += " " + line
        children = text_to_html_node(text.strip())
        return ParentNode(tag="p", children=children)
    
    if block_type == BlockType.CODE:
        list_elements = []
        text = block.strip("```")
        children = text_to_html_node(text)
        list_elements.append(ParentNode(tag="pre", children=children))
        return ParentNode(tag="code", children=list_elements)
            
    if block_type == BlockType.QUOTE:
        lines = block.splitlines()
        text = " ".join(line.strip("> ") for line in lines)
            
        children = text_to_html_node(text.strip())
        return ParentNode(tag="blockquote", children=children)
                        
    if block_type == BlockType.UNORDERED_LIST:
        list_elements = []
        for line in block.splitlines():
            children = text_to_html_node(line[2:])
            list_elements.append(ParentNode(tag="li", children=children))
        return ParentNode(tag="ul", children=list_elements)
    
    if block_type == BlockType.ORDERED_LIST:
        list_elements = []
        for line in block.splitlines():
            children = text_to_html_node(line[3:])
            list_elements.append(ParentNode(tag="li", children=children))
        return ParentNode(tag="ol", children=list_elements)
    
    raise ValueError(f"invalid block type: {block_type}")
    
        
        
def text_to_html_node(text: str):
    text_nodes = text_to_textnodes(text)
    
    children = [text_node_to_html_node(node) for node in text_nodes]
    
    return children

# print(text_to_html_node("This is a **bold** text"))