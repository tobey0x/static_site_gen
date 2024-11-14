from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # If node is not TEXT type, add it as is
            new_nodes.append(node)
            continue

        # Split by the delimiter
        parts = node.text.split(delimiter)
        
        # Ensure delimiters are matched
        if len(parts) % 2 == 0:
            raise ValueError("Unmatched delimiter found")

        i = 0
        while i < len(parts):
            # Text outside delimiters
            if i % 2 == 0:
                if parts[i]:
                    new_nodes.append(TextNode(parts[i], TextType.TEXT))
            # Text inside delimiters
            else:
                new_nodes.append(TextNode(parts[i], text_type))
            i += 1

    return new_nodes
