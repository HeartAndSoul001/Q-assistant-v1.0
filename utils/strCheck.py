def is_valid_txtFilename(filename) -> bool:
    # 检查长度
    if len(filename) > 255:
        return False
    
    # 检查扩展名
    if not filename.lower().endswith('.txt'):
        return False

    # 分离文件名和扩展名
    base_name = filename[:-4]  # 假设.txt扩展名长度为4

    # 检查非法字符
    invalid_chars = '<>:"/\\|?*'
    if any(char in invalid_chars for char in base_name):
        return False

    # 检查文件名是否以点或空格开始或结束
    if base_name.startswith('.') or base_name.endswith('.') or base_name.startswith(' ') or base_name.endswith(' '):
        return False

    # 检查文件名是否只包含合法字符
    if not all(c.isalnum() or c in ' .,;=+[]{}()_-' for c in base_name):
        return False

    # 如果所有检查都通过，文件名是有效的
    return True