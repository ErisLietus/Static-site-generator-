from textnode import TextType, TextNode

def split_node_delimiter(old_nodes, delimiter, text_type):
    new_nodes = [] 

    for node in old_nodes: 
        if node.text_type is not TextType.TEXT: 
            new_nodes.append(node)
            continue
        if delimiter not in node.text:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise Exception("invalid markdown, unmatched delimiter") # if there is a single delimiter raise exception because it doesnt have a matching closing delimiter
        
        for i, part in enumerate(parts):
            if part == "": # these are just a normal string quotes ? 
                continue
            if i % 2 == 0: 
                new_nodes.append(TextNode(part, TextType.TEXT))
            else: 
                new_nodes.append(TextNode(part, text_type)) # sorry brain not worky on this part 

    return new_nodes