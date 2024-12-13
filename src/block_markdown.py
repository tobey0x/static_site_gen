def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    blocks = []
    
    for line in raw_blocks:
        if line.strip():
            blocks.append(line.strip())
            
    return blocks
    